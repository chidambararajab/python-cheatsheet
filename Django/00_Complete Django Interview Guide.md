# Complete Django Interview Guide
**For Mid to Senior Backend Engineers | REST API & Production Roles**

---

## Table of Contents
1. [Django Core (Interview Depth)](#django-core)
2. [Django REST Framework (Critical)](#django-rest-framework)
3. [Real-Time & Async Django](#real-time-async)
4. [Performance Optimization](#performance-optimization)
5. [Production Bugs & Fixes](#production-bugs)
6. [System Design & Architecture](#system-design)
7. [Interview Q&A Section](#interview-qa)

---

## 1. Django Core (Interview Depth) {#django-core}

### 1.1 Django Request/Response Lifecycle

**What Happens When a Request Hits Your Django App?**

1. **WSGI/ASGI Server** receives HTTP request
2. **Middleware (Request Phase)** - runs in order defined in `MIDDLEWARE` setting
3. **URL Resolver** - matches URL pattern, extracts kwargs
4. **View Function/Class** - executes business logic
5. **Middleware (Response Phase)** - runs in reverse order
6. **HTTP Response** - sent back to client

**Interview Question: "What's the order of middleware execution?"**

- **Request phase**: Top to bottom (as defined in settings)
- **Response phase**: Bottom to top (reverse)
- **Exception phase**: Bottom to top (only for middleware with `process_exception`)

**Why This Matters in Production:**
- Middleware order affects authentication, CORS, logging
- Common bug: CORS middleware placed after authentication → OPTIONS preflight fails
- Fix: Always put CORS middleware near the top

---

### 1.2 ORM Internals & Query Optimization

**How Django ORM Works (Interview Answer):**

Django ORM is lazy:
- Queryset creation doesn't hit the database
- Database query executes when you:
  - Iterate over queryset (`for obj in queryset`)
  - Call `list()`, `len()`, `bool()`
  - Slice with step (`queryset[0:10:2]`)
  - Call evaluation methods (`.count()`, `.exists()`, `.first()`)

**Queryset Caching:**
```python
# BAD: Hits database twice
users = User.objects.all()
print(users.count())  # Query 1
for user in users:    # Query 2
    print(user.name)

# GOOD: Hits database once
users = list(User.objects.all())  # Query 1, cached
print(len(users))                  # Uses cache
for user in users:                 # Uses cache
    print(user.name)
```

**Interview Trap Question: "When does this hit the database?"**
```python
qs = Book.objects.filter(published=True)  # No query
first_book = qs[0]                        # Query executed
second_book = qs[1]                       # NEW query (slicing doesn't cache)
```

**Why:** Single index slicing doesn't cache. Use `list(qs)` or iterate once.

**Production Bug:**
- Symptom: API response takes 10+ seconds
- Cause: Queryset evaluated multiple times in template
- Fix: Evaluate once in view, pass list to template

---

### 1.3 Middleware (Custom + Built-in)

**When to Write Custom Middleware:**

1. **Request/Response modification** (add headers, modify data)
2. **Cross-cutting concerns** (logging, metrics, tracing)
3. **Authentication/Authorization** (custom JWT validation)
4. **Rate limiting** (before it reaches view)

**Custom Middleware Template:**
```python
class RequestTimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        start_time = time.time()
        
        # Before view
        request.start_time = start_time
        
        response = self.get_response(request)
        
        # After view
        duration = time.time() - start_time
        response['X-Request-Duration'] = str(duration)
        
        return response
    
    def process_exception(self, request, exception):
        # Handle exceptions
        logger.error(f"Exception: {exception}")
        return None  # Let Django handle it
```

**Interview Question: "Why not use decorators instead of middleware?"**

**Answer:**
- **Middleware**: Runs for ALL requests (global), can modify request before URL resolution
- **Decorators**: Runs only for specific views, applied after URL resolution
- Use middleware for cross-cutting concerns, decorators for view-specific logic

**Production Example:**
- Built custom middleware to inject `request_id` for distributed tracing
- Added `X-Request-ID` header to all responses
- Logged request_id in all log statements for debugging

---

### 1.4 Signals (When to Use / Avoid)

**What Are Signals?**
- Decoupled way to perform actions when certain events occur
- Common signals: `pre_save`, `post_save`, `pre_delete`, `post_delete`, `m2m_changed`

**When to Use:**
1. **Cross-app communication** (avoid circular imports)
2. **Audit logging** (track model changes)
3. **Cache invalidation** (clear cache when model updates)
4. **Third-party integration** (send webhook when object created)

**When to AVOID (Interview Critical):**

**❌ Don't Use Signals For:**
1. **Business logic** - belongs in model methods or services
2. **Tight coupling** - sender and receiver are in same app
3. **Complex workflows** - hard to debug, prefer explicit calls
4. **Performance-critical paths** - signals add overhead

**Production Bug:**
```python
# BAD: Signal causes infinite loop
@receiver(post_save, sender=Order)
def update_inventory(sender, instance, **kwargs):
    if instance.status == 'completed':
        instance.inventory_updated = True
        instance.save()  # Triggers post_save again!
```

**Fix:**
```python
@receiver(post_save, sender=Order)
def update_inventory(sender, instance, created, **kwargs):
    if not created and instance.status == 'completed':
        # Use update to avoid triggering signal
        Order.objects.filter(pk=instance.pk).update(inventory_updated=True)
```

**Interview Answer: "Why avoid signals in business logic?"**
- Hard to trace execution flow (implicit)
- Transaction atomicity issues (signal might commit before view)
- Testing becomes harder (need to mock signals)
- Prefer explicit service layer calls

---

### 1.5 Authentication vs Authorization

**Authentication:** "Who are you?" (Identity verification)
**Authorization:** "What can you do?" (Permission checking)

**Django's Authentication System:**

1. **Authentication Backends:**
   - `ModelBackend` (default, checks username/password)
   - Custom backends (LDAP, OAuth, JWT)

2. **Middleware:**
   - `AuthenticationMiddleware` - attaches `request.user`
   - `SessionMiddleware` - manages session (required for auth)

3. **User Model:**
   - Default: `django.contrib.auth.User`
   - Custom: Extend `AbstractUser` or `AbstractBaseUser`

**Authorization (Permissions):**

```python
# Model-level permissions (auto-created)
user.has_perm('app.add_book')
user.has_perm('app.change_book')
user.has_perm('app.delete_book')

# Custom permissions
class Book(models.Model):
    class Meta:
        permissions = [
            ("can_publish", "Can publish book"),
        ]

# Check in view
if request.user.has_perm('app.can_publish'):
    book.publish()
```

**Interview Question: "How do you implement row-level permissions?"**

**Answer:**
```python
# BAD: Checking in view is repetitive
def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    if book.author != request.user:
        raise PermissionDenied
    return render(request, 'book.html', {'book': book})

# GOOD: Custom permission class (DRF) or mixin
class IsAuthorPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

# BETTER: Filter queryset in manager
class BookManager(models.Manager):
    def for_user(self, user):
        if user.is_staff:
            return self.all()
        return self.filter(author=user)

# Usage
books = Book.objects.for_user(request.user)
```

**Production Lesson:**
- Started with view-level checks
- Moved to DRF permissions (reusable)
- Finally implemented manager methods (can't accidentally bypass)

---

### 1.6 Security Best Practices

**CSRF (Cross-Site Request Forgery):**

**How Django Protects:**
1. Middleware generates CSRF token, stores in cookie
2. Form includes hidden `{% csrf_token %}` field
3. On POST, Django verifies token matches

**Interview Question: "When do you need to disable CSRF?"**

**Answer:**
- **API endpoints** (using token authentication, not session)
- **Webhooks** (external services can't have CSRF token)
- Use `@csrf_exempt` carefully, ensure other auth is in place

```python
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Only for API with token auth
def webhook_handler(request):
    # Verify webhook signature instead
    if not verify_signature(request):
        return HttpResponse(status=403)
    # Process webhook
```

**Production Bug:**
- Symptom: API calls from mobile app returning 403 Forbidden
- Cause: CSRF enabled for DRF views using token auth
- Fix: Set `'rest_framework.authentication.SessionAuthentication'` to use `CsrfExemptSessionAuthentication` for APIs

---

**XSS (Cross-Site Scripting):**

**Django's Auto-Escaping:**
```django
{# Template auto-escapes by default #}
{{ user_input }}  <!-- Safe: <script> becomes &lt;script&gt; -->

{# Mark safe ONLY for trusted content #}
{{ trusted_html|safe }}
```

**Interview Question: "When would auto-escaping cause problems?"**

**Answer:** JSON in `<script>` tags
```django
{# BAD: JSON breaks with escaped quotes #}
<script>
    var data = {{ json_data }};  // Breaks with &quot;
</script>

{# GOOD: Use json_script #}
{{ json_data|json_script:"data-id" }}
<script>
    var data = JSON.parse(document.getElementById('data-id').textContent);
</script>
```

---

**SQL Injection:**

**Django ORM Protects Automatically:**
```python
# SAFE: ORM uses parameterized queries
User.objects.filter(username=user_input)

# DANGEROUS: Raw SQL with string formatting
User.objects.raw(f"SELECT * FROM users WHERE username = '{user_input}'")

# SAFE: Raw SQL with parameters
User.objects.raw("SELECT * FROM users WHERE username = %s", [user_input])
```

**Interview Question: "Can you get SQL injection with Django ORM?"**

**Answer:** Yes, in these cases:
1. Raw queries with string formatting
2. `.extra()` with unsafe params
3. Custom SQL in migrations

**Always use parameterized queries.**

---

### 1.7 Settings Separation (Dev/Stage/Prod)

**Why Separate Settings?**
- Different databases per environment
- Debug mode only in dev
- Different secret keys
- Environment-specific middleware/apps

**Common Approaches:**

**Approach 1: Environment-based import**
```python
# settings/__init__.py
import os
env = os.environ.get('DJANGO_ENV', 'dev')

if env == 'production':
    from .production import *
elif env == 'staging':
    from .staging import *
else:
    from .development import *
```

**Approach 2: Base + override (Better)**
```python
# settings/base.py - Common settings
INSTALLED_APPS = [...]

# settings/dev.py
from .base import *
DEBUG = True
DATABASES = {'default': {...}}

# settings/prod.py
from .base import *
DEBUG = False
ALLOWED_HOSTS = ['api.example.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'],
        'HOST': os.environ['DB_HOST'],
    }
}
```

**Production Best Practices:**
1. **Never commit secrets** - use environment variables
2. **Use django-environ** or **python-decouple** for env vars
3. **Separate `SECRET_KEY`** per environment
4. **Different error reporting** (Sentry in prod, console in dev)

**Interview Question: "How do you handle secrets in Django?"**

**Answer:**
```python
import os
from pathlib import Path

# Read from environment
SECRET_KEY = os.environ.get('SECRET_KEY')
if not SECRET_KEY:
    raise ValueError("SECRET_KEY not set")

# Or use django-environ
import environ
env = environ.Env()
environ.Env.read_env()  # Reads .env file

SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG', default=False)
DATABASE_URL = env('DATABASE_URL')
```

---

## 2. Django REST Framework (Critical) {#django-rest-framework}

### 2.1 DRF Architecture (APIView vs ViewSet vs GenericView)

**APIView (Low-Level):**
```python
from rest_framework.views import APIView
from rest_framework.response import Response

class BookListView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
```

**When to use:** Full control, custom logic, non-standard endpoints.

---

**GenericAPIView + Mixins (Mid-Level):**
```python
from rest_framework.generics import ListCreateAPIView

class BookListView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
```

**When to use:** Standard CRUD, less boilerplate.

---

**ViewSet (High-Level):**
```python
from rest_framework.viewsets import ModelViewSet

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # Custom action
    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        book = self.get_object()
        book.published = True
        book.save()
        return Response({'status': 'published'})
```

**When to use:** Full REST API for a model, custom actions.

---

**Interview Question: "When would you use APIView over ViewSet?"**

**Answer:**
- **APIView:** Non-CRUD endpoints (analytics, search, complex aggregations)
- **GenericView:** Simple CRUD with tweaks
- **ViewSet:** Full REST API, custom actions, routable

**Production Example:**
- Used `ViewSet` for standard resources (User, Product, Order)
- Used `APIView` for dashboard analytics endpoint (not resource-based)
- Used `GenericAPIView` for one-off filtered lists

---

### 2.2 Serializers (ModelSerializer vs Serializer)

**ModelSerializer (90% of cases):**
```python
class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name', read_only=True)
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'author_name', 'published_date']
        read_only_fields = ['id', 'published_date']
```

**When to use:** Tied to a model, standard CRUD.

---

**Serializer (Custom):**
```python
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        data['user'] = user
        return data
```

**When to use:** No model backing, custom validation, complex input.

---

**Nested Serializers (Interview Focus):**

**Read-Only Nested:**
```python
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)  # Nested for GET
    author_id = serializers.IntegerField(write_only=True)  # ID for POST
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'author_id']
```

**Writable Nested (Complex):**
```python
class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    
    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author = Author.objects.create(**author_data)
        book = Book.objects.create(author=author, **validated_data)
        return book
    
    def update(self, instance, validated_data):
        author_data = validated_data.pop('author', None)
        if author_data:
            for key, value in author_data.items():
                setattr(instance.author, key, value)
            instance.author.save()
        
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
```

**Interview Question: "What's wrong with this?"**
```python
class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Book
        fields = ['id', 'title', 'author']
```

**Answer:**
- No `create()` or `update()` method defined
- DRF will fail when trying to create/update with nested data
- Must handle nested writes manually

**Production Bug:**
- Symptom: 500 error when updating book with author data
- Cause: Nested serializer without custom `update()` method
- Fix: Implement custom `update()` or use separate endpoints

---

### 2.3 Validation Strategies

**Field-Level Validation:**
```python
class BookSerializer(serializers.ModelSerializer):
    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title too short")
        return value
```

**Object-Level Validation:**
```python
def validate(self, data):
    if data['start_date'] > data['end_date']:
        raise serializers.ValidationError("End date must be after start date")
    return data
```

**Custom Validators:**
```python
def validate_isbn(value):
    if len(value) != 13:
        raise serializers.ValidationError("ISBN must be 13 digits")

class BookSerializer(serializers.ModelSerializer):
    isbn = serializers.CharField(validators=[validate_isbn])
```

**Interview Question: "Where should business logic validation go?"**

**Answer (Production Perspective):**

1. **Serializer:** API input validation (format, required fields)
2. **Model:** Data integrity (unique constraints, FK relationships)
3. **Service Layer:** Business rules (pricing, inventory, workflows)

**Example:**
```python
# Serializer: Input validation
def validate_quantity(self, value):
    if value <= 0:
        raise ValidationError("Quantity must be positive")
    return value

# Model: Data integrity
class Order(models.Model):
    quantity = models.IntegerField()
    
    def clean(self):
        if self.quantity <= 0:
            raise ValidationError("Invalid quantity")

# Service: Business logic
def create_order(user, product, quantity):
    if product.stock < quantity:
        raise InsufficientStockError()
    if user.credit < product.price * quantity:
        raise InsufficientCreditError()
    # Create order
```

---

### 2.4 Pagination, Filtering, Ordering

**Pagination:**

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20
}

# Custom pagination
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = LargeResultsSetPagination
```

**Interview Question: "Why is pagination critical in production?"**

**Answer:**
1. **Memory:** Loading 100K records crashes server
2. **Database:** Large queries timeout
3. **Network:** Huge JSON responses timeout client
4. **UX:** Users can't consume 100K items at once

**Production Bug:**
- Symptom: API works in dev, crashes in prod
- Cause: No pagination, dev has 100 records, prod has 1M
- Fix: Always paginate, set reasonable limits

---

**Filtering:**

```python
# Use django-filter
from django_filters.rest_framework import DjangoFilterBackend

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['author', 'published_date', 'genre']
    ordering_fields = ['title', 'published_date']
    ordering = ['-published_date']  # Default ordering

# GET /api/books/?author=5&genre=fiction&ordering=-published_date
```

**Custom Filtering:**
```python
def get_queryset(self):
    queryset = Book.objects.all()
    author_name = self.request.query_params.get('author_name')
    if author_name:
        queryset = queryset.filter(author__name__icontains=author_name)
    return queryset
```

---

### 2.5 Permissions & Authentication

**Authentication (Who are you?):**

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',  # Web
        'rest_framework.authentication.TokenAuthentication',    # Mobile
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # JWT
    ],
}
```

**Session Auth:** Browser-based, uses cookies, requires CSRF
**Token Auth:** Mobile/API, send `Authorization: Token <token>` header
**JWT Auth:** Stateless, contains user info + expiry, no DB lookup

---

**Permissions (What can you do?):**

```python
from rest_framework.permissions import BasePermission

# Built-in
IsAuthenticated  # Must be logged in
IsAdminUser      # Must be staff
AllowAny         # No restriction

# Custom permission
class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions for all
        if request.method in SAFE_METHODS:
            return True
        # Write permissions only for author
        return obj.author == request.user

class BookViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
```

**Interview Question: "Session vs Token vs JWT - when to use which?"**

| Auth Type | Use Case | Pros | Cons |
|-----------|----------|------|------|
| **Session** | Web app (same domain) | Simple, server-controlled logout | Requires cookies, CSRF protection, not scalable (stateful) |
| **Token** | Mobile app, simple API | Stateless, simple | Token stored in DB, no auto-expiry |
| **JWT** | Microservices, mobile | Fully stateless, contains claims, auto-expiry | Can't revoke (till expiry), larger token size |

**Production Decision:**
- Used JWT for mobile apps (stateless, scalable)
- Used sessions for admin dashboard (same domain, better UX)
- Hybrid: JWT with short expiry + refresh tokens

---

### 2.6 Throttling & Rate Limiting

**Why Rate Limit?**
1. Prevent abuse (DDoS, scraping)
2. Fair usage (one user doesn't hog resources)
3. Cost control (API costs per request)

```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day'
    }
}

# Custom throttle
class BurstRateThrottle(UserRateThrottle):
    rate = '10/min'  # Burst protection

class BookViewSet(ModelViewSet):
    throttle_classes = [BurstRateThrottle]
```

**Interview Question: "How would you implement rate limiting in production?"**

**Answer (Multi-Layer):**
1. **API Gateway:** Nginx/Cloudflare rate limiting (before Django)
2. **DRF Throttle:** Application-level (per user/endpoint)
3. **Redis:** Custom rate limiting (sliding window)

**Production Example:**
```python
import redis
from django.core.cache import cache

def rate_limit(user_id, limit=100, window=3600):
    key = f"rate_limit:{user_id}"
    current = cache.get(key, 0)
    if current >= limit:
        raise ThrottledException()
    cache.set(key, current + 1, timeout=window)
```

---

### 2.7 Versioning Strategies

**Why Version APIs?**
- Breaking changes without breaking clients
- Gradual migration
- Sunset old versions

**Versioning Methods:**

**1. URL Path (Most Common):**
```python
# urls.py
urlpatterns = [
    path('api/v1/', include('api.v1.urls')),
    path('api/v2/', include('api.v2.urls')),
]
```

**Pros:** Clear, easy to route, easy to deprecate
**Cons:** Code duplication

**2. Accept Header:**
```python
REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.AcceptHeaderVersioning',
}
# Client sends: Accept: application/json; version=1.0
```

**Pros:** Clean URLs
**Cons:** Harder to test, not browser-friendly

**3. Query Parameter:**
```
GET /api/books/?version=1
```

**Pros:** Simple
**Cons:** Pollutes query params

**Interview Question: "How do you handle breaking changes in production?"**

**Answer (Real Process):**
1. **Introduce v2** with new structure
2. **Deprecation notice** in v1 responses (`Deprecated: true` header)
3. **Migration guide** for clients
4. **Support both** for 6-12 months
5. **Monitor v1 usage** (track via headers)
6. **Sunset v1** after migration complete

---

### 2.8 Error Handling & Standard API Responses

**Consistent Error Format:**

```python
# exceptions.py
from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    
    if response is not None:
        custom_response = {
            'error': {
                'code': response.status_code,
                'message': str(exc),
                'details': response.data
            }
        }
        response.data = custom_response
    
    return response

# settings.py
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'app.exceptions.custom_exception_handler',
}
```

**Production Standard Response Format:**
```json
{
  "success": true,
  "data": {...},
  "meta": {
    "timestamp": "2026-01-21T10:30:00Z",
    "version": "v1"
  }
}

// Error response
{
  "success": false,
  "error": {
    "code": 400,
    "message": "Validation failed",
    "details": {
      "email": ["This field is required"],
      "password": ["Password too short"]
    }
  },
  "meta": {
    "timestamp": "2026-01-21T10:30:00Z",
    "request_id": "abc123"
  }
}
```

**Interview Question: "How do you handle unexpected errors in production?"**

**Answer:**
1. **Catch at view level** (generic exception handler)
2. **Log with context** (user, request_id, stack trace)
3. **Return safe error** (don't expose internals)
4. **Alert on-call** (Sentry, PagerDuty)
5. **Track metrics** (error rate, status code distribution)

---

### 2.9 API Testing Strategies

**APIClient for Testing:**

```python
from rest_framework.test import APITestCase, APIClient

class BookAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user('test', 'test@example.com', 'pass')
        self.client.force_authenticate(user=self.user)
    
    def test_create_book(self):
        data = {'title': 'Test Book', 'author_id': 1}
        response = self.client.post('/api/books/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Book.objects.count(), 1)
    
    def test_list_books_requires_auth(self):
        self.client.force_authenticate(user=None)
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, 401)
```

**What to Test (Interview Answer):**
1. **Happy path** (valid input → success)
2. **Validation** (invalid input → 400)
3. **Authentication** (no auth → 401)
4. **Authorization** (wrong user → 403)
5. **Edge cases** (empty list, pagination, filtering)

**Production Testing Strategy:**
- **Unit tests:** Serializer validation, business logic
- **Integration tests:** Full API endpoint tests
- **Load tests:** Performance under load (Locust, k6)
- **Contract tests:** API contract doesn't break clients

---

## 3. Real-Time & Async Django {#real-time-async}

### 3.1 Django + WebSockets (Channels)

**When You Need WebSockets:**
- Real-time chat
- Live notifications
- Collaborative editing
- Live dashboards

**Django Channels Architecture:**
1. **ASGI** (not WSGI) - async protocol
2. **Channel Layer** (Redis) - message passing between workers
3. **Consumers** (like views) - handle WebSocket connections

**Simple Consumer:**
```python
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
    
    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )
    
    async def chat_message(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': event['message']
        }))
```

**Interview Question: "How do you scale WebSocket connections?"**

**Answer:**
1. **Multiple workers** (Channels workers connect to Redis)
2. **Redis Cluster** (channel layer backed by Redis cluster)
3. **Horizontal scaling** (multiple servers, shared Redis)
4. **Connection limits** (per worker, graceful degradation)

**Production Challenges:**
- **Stale connections** → Implement heartbeat/ping-pong
- **Memory leaks** → Monitor open connections, set timeouts
- **Authentication** → Verify user in `connect()` method

---

### 3.2 Celery (Tasks, Retries, Idempotency)

**What is Celery?**
- Distributed task queue
- Executes tasks asynchronously
- Backed by message broker (Redis, RabbitMQ)

**When to Use Celery:**
1. **Long-running tasks** (video processing, report generation)
2. **Scheduled tasks** (daily email, cleanup)
3. **Background work** (send email, update cache)
4. **Offload from request cycle** (keep API fast)

**Basic Task:**
```python
from celery import shared_task

@shared_task
def send_welcome_email(user_id):
    user = User.objects.get(id=user_id)
    send_email(
        subject='Welcome',
        to=user.email,
        template='welcome.html'
    )

# In view
def register(request):
    user = User.objects.create(...)
    send_welcome_email.delay(user.id)  # Async
    return Response({'status': 'created'})
```

**Retries (Critical for Production):**
```python
@shared_task(bind=True, max_retries=3, default_retry_delay=60)
def charge_payment(self, order_id):
    try:
        order = Order.objects.get(id=order_id)
        payment_gateway.charge(order.amount)
    except PaymentGatewayError as exc:
        # Retry with exponential backoff
        raise self.retry(exc=exc, countdown=2 ** self.request.retries)
```

**Idempotency (Interview Critical):**

**Problem:** Task might be executed multiple times (worker crash, retry)

**Solution:** Make tasks idempotent (safe to run multiple times)

```python
# BAD: Not idempotent
@shared_task
def increment_view_count(post_id):
    post = Post.objects.get(id=post_id)
    post.view_count += 1
    post.save()  # Runs 3 times = +3 instead of +1

# GOOD: Idempotent with lock
from django.core.cache import cache

@shared_task
def increment_view_count(post_id):
    lock_id = f'lock:view_count:{post_id}'
    if cache.add(lock_id, 'true', timeout=60):  # Acquire lock
        try:
            post = Post.objects.get(id=post_id)
            post.view_count += 1
            post.save()
        finally:
            cache.delete(lock_id)  # Release lock
    else:
        # Task already running, skip
        pass
```

**Production Bug:**
- Symptom: Users charged multiple times
- Cause: Payment task retried after timeout (but first attempt succeeded)
- Fix: Check if payment already processed before charging (idempotency key)

---

### 3.3 Redis Use Cases

**Why Redis in Django?**
1. **Caching** (fast key-value store)
2. **Session storage** (instead of DB)
3. **Task queue** (Celery broker)
4. **Rate limiting** (fast counters)
5. **Real-time data** (leaderboards, counters)
6. **Pub/Sub** (Channels channel layer)

**Caching with Redis:**
```python
# settings.py
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://localhost:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# Usage
from django.core.cache import cache

# Set cache
cache.set('user:123:profile', user_data, timeout=3600)

# Get cache
user_data = cache.get('user:123:profile')
if not user_data:
    user_data = fetch_from_db()
    cache.set('user:123:profile', user_data, timeout=3600)
```

**Interview Question: "When should you use Redis vs database?"**

| Redis | Database |
|-------|----------|
| Temporary data (cache, sessions) | Permanent data |
| High read/write throughput | Complex queries, joins |
| Simple data structures (key-value) | Relational data |
| Tolerate data loss (cache miss) | ACID guarantees required |

---

### 3.4 Async Views (ASGI)

**When to Use Async Views:**
- External API calls (don't block worker)
- I/O-bound operations (database, file reads)
- Long-polling endpoints

**Async View:**
```python
import httpx
from django.http import JsonResponse

async def fetch_external_data(request):
    async with httpx.AsyncClient() as client:
        response = await client.get('https://api.example.com/data')
    return JsonResponse(response.json())
```

**Interview Question: "Async views vs Celery - when to use which?"**

| Async View | Celery Task |
|------------|-------------|
| Client waits for response | Fire-and-forget |
| < 30 seconds | Can run for hours |
| Must return result to client | Result optional |
| External API calls | Background jobs, scheduled tasks |

**Production Decision:**
- **Async view:** Fetch user's order status from external API (client needs result)
- **Celery:** Send daily email digest (don't wait for result)

---

## 4. Performance Optimization {#performance-optimization}

### 4.1 N+1 Query Problem (Critical Interview Topic)

**What is N+1?**
- 1 query to fetch N objects
- N queries to fetch related objects
- Total: N+1 queries (instead of 1-2)

**Example:**
```python
# BAD: N+1 queries
books = Book.objects.all()  # 1 query
for book in books:
    print(book.author.name)  # N queries (1 per book)

# Total: 1 + 100 = 101 queries for 100 books
```

**Fix with select_related (ForeignKey, OneToOne):**
```python
# GOOD: 1 query with JOIN
books = Book.objects.select_related('author').all()
for book in books:
    print(book.author.name)  # No additional query

# SQL: SELECT * FROM book JOIN author ON book.author_id = author.id
```

**Fix with prefetch_related (ManyToMany, Reverse FK):**
```python
# BAD: N+1
authors = Author.objects.all()
for author in authors:
    print(author.books.count())  # N queries

# GOOD: 2 queries (1 for authors, 1 for all related books)
authors = Author.objects.prefetch_related('books').all()
for author in authors:
    print(author.books.count())  # No additional query
```

**Interview Question: "select_related vs prefetch_related - when to use which?"**

| `select_related` | `prefetch_related` |
|------------------|---------------------|
| **ForeignKey**, **OneToOne** | **ManyToMany**, **Reverse FK** |
| **SQL JOIN** (single query) | **Separate query + Python join** |
| Returns queryset | Returns list |
| Can chain filters | Can't chain filters after prefetch |

**Production Bug:**
- Symptom: API endpoint times out with 1000 books
- Cause: N+1 query in DRF serializer
- Debug: `django-debug-toolbar` showed 1001 queries
- Fix: Add `select_related('author')` in viewset's `get_queryset()`

---

### 4.2 Query Optimization Techniques

**Only fetch needed fields:**
```python
# BAD: Fetches all fields
books = Book.objects.all()

# GOOD: Only fetch needed fields
books = Book.objects.only('id', 'title')  # Other fields deferred

# GOOD: Exclude large fields
books = Book.objects.defer('description', 'content')  # Lazy load
```

**Aggregate in database, not Python:**
```python
# BAD: Fetch all, count in Python
books = Book.objects.filter(published=True)
count = len(list(books))  # Fetches all records

# GOOD: Count in database
count = Book.objects.filter(published=True).count()  # SELECT COUNT(*)
```

**Bulk operations:**
```python
# BAD: N queries
for i in range(1000):
    Book.objects.create(title=f'Book {i}')

# GOOD: 1 query
Book.objects.bulk_create([
    Book(title=f'Book {i}') for i in range(1000)
])

# BAD: N update queries
for book in books:
    book.published = True
    book.save()

# GOOD: 1 update query
books.update(published=True)
```

**Use `iterator()` for large querysets:**
```python
# BAD: Loads all 1M records into memory
for book in Book.objects.all():
    process(book)

# GOOD: Streams results, low memory
for book in Book.objects.iterator(chunk_size=1000):
    process(book)
```

**Interview Question: "How do you optimize a slow API endpoint?"**

**Answer (Step-by-Step):**
1. **Profile:** Use `django-debug-toolbar` or `django-silk`
2. **Identify bottleneck:** Check query count, slow queries
3. **Fix N+1:** Add `select_related` / `prefetch_related`
4. **Add indexes:** For filtered/ordered fields
5. **Cache:** Frequently accessed, rarely changing data
6. **Paginate:** Don't return 10K records
7. **Optimize serializer:** Remove unnecessary nested fields

---

### 4.3 Database Indexing Strategies

**When to Add Index:**
1. Fields in `WHERE` clause (filtering)
2. Fields in `ORDER BY` (sorting)
3. Foreign keys (auto-indexed in Django)
4. Fields in `JOIN` conditions

**How to Add Index:**
```python
class Book(models.Model):
    title = models.CharField(max_length=200, db_index=True)  # Simple index
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # Auto-indexed
    published_date = models.DateField()
    
    class Meta:
        indexes = [
            models.Index(fields=['published_date']),  # Single field
            models.Index(fields=['author', 'published_date']),  # Composite
            models.Index(fields=['-published_date']),  # Descending
        ]
```

**Interview Question: "What's the downside of too many indexes?"**

**Answer:**
- **Slower writes:** Every INSERT/UPDATE must update all indexes
- **More storage:** Indexes take disk space
- **Maintenance overhead:** Index rebuilds during migrations

**Rule of Thumb:**
- Index fields you filter/order by frequently
- Don't index rarely used fields
- Composite index for common filter combinations

**Production Example:**
```python
# Query: Book.objects.filter(author=5, published_date__gte='2025-01-01').order_by('-published_date')
# Index: (author, published_date)  # Composite index matches this query
```

---

### 4.4 Caching (Per-View, Low-Level, Redis)

**Caching Levels:**

**1. Per-View Caching:**
```python
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)  # Cache for 15 minutes
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})
```

**2. Template Fragment Caching:**
```django
{% load cache %}
{% cache 600 sidebar %}
  ... expensive sidebar rendering ...
{% endcache %}
```

**3. Low-Level Caching:**
```python
from django.core.cache import cache

def get_popular_books():
    books = cache.get('popular_books')
    if books is None:
        books = Book.objects.filter(views__gt=1000).order_by('-views')[:10]
        cache.set('popular_books', books, timeout=3600)
    return books
```

**4. ORM Query Caching (cachalot):**
```python
# django-cachalot automatically caches ORM queries
books = Book.objects.filter(published=True)  # Cached automatically
```

**Interview Question: "How do you invalidate cache when data changes?"**

**Answer (Strategies):**

1. **Time-based expiry** (simple, but stale data possible)
2. **Manual invalidation** (on save/delete)
   ```python
   def save(self, *args, **kwargs):
       super().save(*args, **kwargs)
       cache.delete('popular_books')
   ```
3. **Cache versioning** (increment version on change)
4. **Event-driven** (Signal triggers cache clear)

**Production Bug:**
- Symptom: Users see old data for 1 hour
- Cause: View cached, but data updated every 5 minutes
- Fix: Reduced cache timeout to 5 minutes, added manual invalidation

---

### 4.5 Handling High Traffic & Load Spikes

**Horizontal Scaling:**
- Multiple Django workers (gunicorn with 4-8 workers)
- Load balancer (Nginx, HAProxy) distributes requests
- Stateless app (session in Redis/DB, not in-memory)

**Database Optimization:**
- **Read replicas:** Read from replica, write to primary
- **Connection pooling:** Reuse DB connections (pgbouncer)
- **Query optimization:** As discussed above

**Async Task Processing:**
- Offload heavy tasks to Celery
- Use Redis for fast operations
- Return `202 Accepted` immediately, process async

**CDN & Static Files:**
- Serve static files from CDN (CloudFront, Cloudflare)
- Django serves only API responses
- Reduce Django server load

**Interview Question: "Your API is slow during peak hours. How do you debug?"**

**Answer (Systematic Approach):**

1. **Monitor:** Check metrics (CPU, memory, DB connections, response time)
2. **Identify bottleneck:**
   - High CPU → Application logic issue
   - High DB connections → Query optimization needed
   - High memory → Memory leak or large objects
   - High response time → Slow queries or external API calls
3. **Profile:** Use APM tools (New Relic, Datadog) to find slow endpoints
4. **Fix:**
   - Add caching for frequently accessed data
   - Optimize slow queries (indexes, N+1 fixes)
   - Add rate limiting to prevent abuse
   - Scale horizontally (more workers)
5. **Test:** Load test to verify fix (Locust, k6)

**Production Example:**
- **Issue:** API slow during Black Friday sale
- **Cause:** Product inventory check hitting DB on every request
- **Fix:** Cached inventory in Redis (TTL 10 seconds), reduced DB load by 90%

---

## 5. Production Bugs & Fixes {#production-bugs}

### 5.1 Memory Leaks

**Symptom:**
- Worker memory grows over time
- Eventually crashes or gets killed by OS (OOM)

**Common Causes:**

**1. Holding references to large objects:**
```python
# BAD: Global list keeps growing
all_requests = []

def my_view(request):
    all_requests.append(request)  # Memory leak!
    ...

# FIX: Don't store requests globally, or limit size
from collections import deque
recent_requests = deque(maxlen=100)  # Only keep last 100
```

**2. QuerySet not garbage collected:**
```python
# BAD: Large queryset held in closure
def get_processor():
    all_books = Book.objects.all()  # Fetches all books
    def process():
        return all_books.count()
    return process

# FIX: Fetch inside function or use iterator
def get_processor():
    def process():
        return Book.objects.count()  # No queryset held
    return process
```

**3. Celery task keeps references:**
```python
# BAD: Task holds large data
@shared_task
def process_data():
    data = fetch_large_dataset()  # 1GB data
    process(data)
    # data not released until task completes

# FIX: Explicitly delete or use generator
@shared_task
def process_data():
    for chunk in fetch_data_generator():
        process(chunk)
        # chunk garbage collected after each iteration
```

**How to Debug:**
- Use `memory_profiler` to track memory usage
- Check worker memory over time (monitoring)
- Enable garbage collection logs

---

### 5.2 Slow APIs

**Symptom:**
- API response time > 2 seconds
- Timeouts under load

**Debugging Steps:**

1. **Check query count:**
```python
from django.db import connection
from django.test.utils import override_settings

@override_settings(DEBUG=True)
def my_view(request):
    # Your view logic
    print(len(connection.queries))  # Number of queries
    print(connection.queries)        # Full query log
```

2. **Profile with django-silk:**
```bash
pip install django-silk
# Visit /silk/ to see slow queries, requests
```

3. **Common Fixes:**
   - N+1 query: Add `select_related` / `prefetch_related`
   - Missing index: Add `db_index=True`
   - Large dataset: Add pagination
   - Heavy computation: Move to Celery
   - External API: Add caching or timeout

**Production Example:**
- **Issue:** `/api/users/` taking 8 seconds
- **Debug:** django-debug-toolbar showed 2000+ queries
- **Cause:** Serializer included nested comments → N+1 on comments and comment authors
- **Fix:** 
  - Added `prefetch_related('comments__author')` in viewset
  - Response time: 8s → 200ms

---

### 5.3 Celery Task Failures

**Symptom:**
- Tasks stuck in PENDING state
- Tasks fail silently
- Tasks run multiple times

**Common Causes:**

**1. Worker not running:**
```bash
# Check if worker is running
celery -A myapp inspect active
```

**2. Task not imported:**
```python
# celery.py - Must import tasks
from celery import Celery
app = Celery('myapp')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()  # Auto-discover tasks.py in each app
```

**3. Broker (Redis) connection lost:**
```python
# settings.py - Add retry logic
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
```

**4. Task timeout:**
```python
@shared_task(time_limit=300, soft_time_limit=270)
def long_task():
    # Will be killed after 300 seconds
    # Receives SIGTERM after 270 seconds (soft limit)
    pass
```

**5. Not idempotent (runs multiple times):**
- See idempotency section above
- Always check if work already done

**Production Bug:**
- **Issue:** Payment email sent 3 times to customer
- **Cause:** Task retried after timeout, but first attempt succeeded
- **Fix:** Check if email already sent before sending (idempotency)
```python
@shared_task
def send_payment_email(order_id):
    order = Order.objects.get(id=order_id)
    if order.email_sent:  # Idempotency check
        return
    send_email(order)
    order.email_sent = True
    order.save()
```

---

### 5.4 Deadlocks

**Symptom:**
- Requests hang indefinitely
- Database deadlock errors

**Common Causes:**

**1. Conflicting transaction order:**
```python
# Transaction 1
with transaction.atomic():
    order = Order.objects.select_for_update().get(id=1)
    product = Product.objects.select_for_update().get(id=1)
    # Update both

# Transaction 2 (at same time)
with transaction.atomic():
    product = Product.objects.select_for_update().get(id=1)  # Locked by Txn1
    order = Order.objects.select_for_update().get(id=1)      # Locked by Txn2
    # DEADLOCK!
```

**Fix:** Always acquire locks in same order
```python
# Both transactions lock in same order: order first, then product
with transaction.atomic():
    order = Order.objects.select_for_update().get(id=1)
    product = Product.objects.select_for_update().get(id=2)
```

**2. Long-running transactions:**
```python
# BAD: Hold lock during external API call
with transaction.atomic():
    order = Order.objects.select_for_update().get(id=1)
    payment_result = call_payment_api()  # Takes 5 seconds, holds lock!
    order.status = 'paid'
    order.save()

# GOOD: Release lock before external call
order = Order.objects.select_for_update().get(id=1)
order.status = 'processing'
order.save()
# transaction.commit()  # Lock released

payment_result = call_payment_api()  # No lock held

order.refresh_from_db()
order.status = 'paid'
order.save()
```

**Production Example:**
- **Issue:** Random deadlocks during checkout
- **Cause:** Updating user wallet and order in different order across views
- **Fix:** Created service function that always locks user → order → product (consistent order)

---

### 5.5 Race Conditions

**Symptom:**
- Incorrect data (double booking, overselling)
- Inconsistent state

**Example: Overselling Products**
```python
# BAD: Race condition
def checkout(request):
    product = Product.objects.get(id=1)
    if product.stock > 0:
        product.stock -= 1  # Not atomic!
        product.save()
        create_order(product)
    else:
        return HttpResponse("Out of stock")

# Two requests at same time:
# Request 1: Reads stock=1
# Request 2: Reads stock=1
# Request 1: Writes stock=0, creates order
# Request 2: Writes stock=0, creates order  ← OVERSOLD!
```

**Fix 1: Database-level atomic update:**
```python
from django.db.models import F

def checkout(request):
    # Atomic decrement
    updated = Product.objects.filter(id=1, stock__gt=0).update(stock=F('stock') - 1)
    if updated:
        create_order(product_id=1)
        return HttpResponse("Success")
    else:
        return HttpResponse("Out of stock")
```

**Fix 2: Select for update (pessimistic lock):**
```python
from django.db import transaction

def checkout(request):
    with transaction.atomic():
        product = Product.objects.select_for_update().get(id=1)
        if product.stock > 0:
            product.stock -= 1
            product.save()
            create_order(product)
        else:
            return HttpResponse("Out of stock")
```

**Fix 3: Optimistic locking (version field):**
```python
class Product(models.Model):
    stock = models.IntegerField()
    version = models.IntegerField(default=0)

def checkout(request):
    while True:
        product = Product.objects.get(id=1)
        if product.stock > 0:
            updated = Product.objects.filter(
                id=1,
                version=product.version,  # Only update if version matches
                stock__gt=0
            ).update(
                stock=F('stock') - 1,
                version=F('version') + 1
            )
            if updated:
                create_order(product_id=1)
                return HttpResponse("Success")
            # Version changed, retry
        else:
            return HttpResponse("Out of stock")
```

**Interview Question: "Optimistic vs Pessimistic locking?"**

| Optimistic | Pessimistic |
|------------|-------------|
| No lock, check version on update | Lock row immediately |
| Better performance (no blocking) | Guaranteed consistency |
| Retry on conflict | No retries needed |
| Use when conflicts are rare | Use when conflicts are common |

---

### 5.6 Broken Migrations

**Symptom:**
- Migration fails midway
- Database in inconsistent state
- Can't roll back

**Common Causes:**

**1. Data migration depends on model:**
```python
# BAD: Model might change
def migrate_data(apps, schema_editor):
    from myapp.models import Book  # Direct import
    for book in Book.objects.all():
        book.status = 'published'
        book.save()

# GOOD: Use historical model
def migrate_data(apps, schema_editor):
    Book = apps.get_model('myapp', 'Book')
    for book in Book.objects.all():
        book.status = 'published'
        book.save()
```

**2. Non-atomic operation:**
```python
# BAD: No atomic block
def migrate_data(apps, schema_editor):
    Book = apps.get_model('myapp', 'Book')
    for book in Book.objects.all():
        book.save()  # Fails halfway → partial update

# GOOD: Atomic
from django.db import transaction

@transaction.atomic
def migrate_data(apps, schema_editor):
    Book = apps.get_model('myapp', 'Book')
    for book in Book.objects.all():
        book.save()  # All or nothing
```

**3. Irreversible migration:**
```python
# BAD: Can't roll back
class Migration(migrations.Migration):
    operations = [
        migrations.RunPython(add_data),
    ]

# GOOD: Add reverse operation
class Migration(migrations.Migration):
    operations = [
        migrations.RunPython(add_data, reverse_code=remove_data),
    ]
```

**Production Bug:**
- **Issue:** Migration failed on production, database in bad state
- **Cause:** Data migration tried to populate field but hit validation error on some rows
- **Fix:** 
  - Manually fixed bad rows in database
  - Re-ran migration
  - Changed migration to skip invalid rows and log them

**Best Practices:**
1. **Test migrations on prod-like data** (copy of prod DB)
2. **Keep migrations small** (easier to debug)
3. **Separate schema and data migrations**
4. **Add rollback logic**
5. **Backup before running migrations**

---

### 5.7 Incorrect Queryset Usage

**Symptom:**
- Wrong results returned
- Unexpected behavior

**Example 1: Queryset is lazy**
```python
# BAD: Queryset evaluated after delete
books = Book.objects.filter(published=True)
Book.objects.all().delete()
for book in books:  # Empty! Queryset evaluated after delete
    print(book)

# FIX: Evaluate before delete
books = list(Book.objects.filter(published=True))
Book.objects.all().delete()
for book in books:  # Works, already in memory
    print(book)
```

**Example 2: Modifying queryset in loop**
```python
# BAD: Infinite loop
books = Book.objects.filter(published=False)
for book in books:
    book.published = True
    book.save()  # Queryset re-evaluated, same books returned!

# FIX: Evaluate once
books = list(Book.objects.filter(published=False))
for book in books:
    book.published = True
    book.save()

# BETTER: Bulk update
Book.objects.filter(published=False).update(published=True)
```

**Example 3: Chaining filters wrong**
```python
# Confusing: Q objects for OR
books = Book.objects.filter(published=True).filter(genre='fiction')  # AND
books = Book.objects.filter(published=True, genre='fiction')         # AND
books = Book.objects.filter(Q(published=True) | Q(genre='fiction'))  # OR
```

---

## 6. System Design & Architecture {#system-design}

### 6.1 Monolith vs Microservices (Django Context)

**Monolith (Single Django App):**

**Pros:**
- Simple to develop and deploy
- No network overhead
- Easy debugging (single codebase)
- Transactions across modules

**Cons:**
- Hard to scale independently
- Large codebase (harder to navigate)
- Tight coupling (changes ripple)
- All or nothing deployment

**When to Use:**
- Small to medium apps
- Team < 10 people
- Rapid prototyping
- Internal tools

---

**Microservices (Multiple Django Apps):**

**Pros:**
- Independent scaling (scale payment service separately)
- Technology diversity (Python for API, Go for real-time)
- Fault isolation (payment down ≠ whole app down)
- Team autonomy (each team owns service)

**Cons:**
- Complex deployment (orchestration needed)
- Network overhead (latency, failures)
- Distributed transactions (hard to maintain consistency)
- Debugging is harder (distributed tracing needed)

**When to Use:**
- Large apps (> 100K lines)
- Multiple teams
- Different scaling needs (e.g., chat vs checkout)
- Need technology flexibility

---

**Interview Question: "When would you split a Django monolith?"**

**Answer (Decision Criteria):**

1. **Independent scaling needed** (e.g., read-heavy vs write-heavy)
2. **Team boundaries** (separate teams work on separate features)
3. **Technology constraints** (need Go for real-time, Python for API)
4. **Deployment independence** (deploy payment without affecting orders)

**Don't split too early:**
- Premature optimization
- Adds complexity without benefit
- Hard to change boundaries later

**Production Story:**
- Started as monolith (faster to build)
- Split after 2 years when team grew to 20 people
- Separated: Auth, Catalog, Orders, Payments, Notifications
- Used API gateway for routing

---

### 6.2 API-First Architecture

**What is API-First?**
- Design API contract before implementation
- API is the primary interface (not templates)
- Frontend (web/mobile) consumes API

**Benefits:**
1. **Decoupled frontend/backend** (can evolve independently)
2. **Multiple clients** (web, mobile, partner integrations) use same API
3. **Easier testing** (test API without frontend)
4. **Clear contracts** (API documentation as source of truth)

**How to Implement in Django:**

1. **Use DRF for all endpoints**
2. **Document API** (OpenAPI, Swagger)
3. **Version API** (plan for changes)
4. **Separate frontend** (React/Next.js, not Django templates)

```python
# API-first: Return JSON
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# vs Template-based: Return HTML
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})
```

**Production Setup:**
- **Backend:** Django + DRF (API only)
- **Frontend:** Next.js (consumes API)
- **Mobile:** React Native (consumes same API)
- **Benefits:** Built mobile app without changing backend

---

### 6.3 Database Design Best Practices

**1. Normalization (Avoid Redundancy):**

```python
# BAD: Denormalized
class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    # If customer changes email, must update all orders!

# GOOD: Normalized
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
```

**Exception: Denormalize for performance**
```python
# Acceptable denormalization
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    customer_name_snapshot = models.CharField(max_length=100)  # For historical record
    total_amount = models.DecimalField()  # Cached, not re-calculated
```

---

**2. Use Appropriate Field Types:**

```python
# BAD: Wrong types
class Product(models.Model):
    price = models.FloatField()  # Float has precision issues
    quantity = models.CharField(max_length=10)  # Quantity is a number

# GOOD: Correct types
class Product(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
```

---

**3. Add Constraints:**

```python
class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)  # No duplicate names
    stock = models.IntegerField()
    
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(stock__gte=0),
                name='stock_non_negative'
            )
        ]
```

---

**4. Soft Delete vs Hard Delete:**

```python
# Hard delete (data lost forever)
book.delete()

# Soft delete (mark as deleted)
class Book(models.Model):
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()
    
    objects = BookManager()  # Custom manager to exclude deleted

class BookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)
```

**Interview Question: "When to use soft delete?"**

**Answer:**
- **Soft delete:** Audit trail needed, might restore, regulatory compliance
- **Hard delete:** Sensitive data (GDPR), storage constraints, no recovery needed

---

### 6.4 Service Boundaries

**What are Service Boundaries?**
- Clear separation of responsibilities
- Each service has single responsibility
- Loose coupling between services

**Example: E-commerce**

```
Auth Service       → User management, login, JWT
Catalog Service    → Products, categories, search
Cart Service       → Shopping cart operations
Order Service      → Order creation, status
Payment Service    → Payment processing
Notification Service → Email, SMS, push notifications
```

**How Services Communicate:**

1. **Synchronous (REST API):**
```python
# Order service calls Payment service
import requests
payment_response = requests.post(
    'https://payment-service/api/charge',
    json={'amount': 100, 'order_id': order.id}
)
```

2. **Asynchronous (Message Queue):**
```python
# Order service publishes event
from myapp.events import publish_event
publish_event('order.created', {'order_id': order.id})

# Notification service subscribes
@subscribe('order.created')
def send_order_email(event):
    order_id = event['order_id']
    send_email(order_id)
```

**Interview Question: "How do you maintain data consistency across services?"**

**Answer (Distributed Transactions):**

1. **Saga Pattern:** Each service completes its transaction, compensates on failure
```
Order Service: Create order
↓
Payment Service: Charge payment
↓ (Success)
Inventory Service: Reduce stock
↓ (Failure)
Payment Service: Refund payment (compensation)
Order Service: Cancel order (compensation)
```

2. **Event Sourcing:** Store events, rebuild state from events

3. **Two-Phase Commit:** All services agree before committing (rarely used, complex)

**Production Choice:**
- Use Saga pattern for critical flows (order, payment)
- Use eventual consistency for non-critical (email, analytics)

---

### 6.5 Django with Frontend (React / Next.js)

**Architecture Options:**

**Option 1: Separate Deployment (API-First)**
```
Django (API)     →  Port 8000
Next.js (Frontend)  →  Port 3000
Nginx (Reverse Proxy) → Routes /api/* to Django, /* to Next.js
```

**Pros:**
- Independent scaling
- Clear separation
- Deploy frontend without backend

**Cons:**
- CORS configuration needed
- More complex deployment

---

**Option 2: Django Serves Frontend (SPA)**
```
Django serves Next.js build output
GET /         → index.html
GET /static/* → JS/CSS
POST /api/*   → Django API
```

**Pros:**
- Single deployment
- No CORS issues

**Cons:**
- Coupled deployment
- Django serves static files (not ideal for scale)

---

**Production Setup:**
```
CloudFront (CDN)
    ↓
    ├── /api/*     → Django (API Gateway → ECS)
    └── /*         → S3 (Next.js static build)
```

**Benefits:**
- Static files on CDN (fast, cheap)
- API on Django (scalable)
- Frontend deploy independent (just update S3)

---

### 6.6 Logging & Monitoring

**What to Log:**
1. **Request/Response** (API calls, status codes)
2. **Errors/Exceptions** (stack traces, context)
3. **Performance** (slow queries, response time)
4. **Business events** (order created, payment processed)

**Logging Setup:**
```python
# settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'django.log',
            'maxBytes': 1024 * 1024 * 10,  # 10MB
            'backupCount': 5,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
        'myapp': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
    },
}

# Usage
import logging
logger = logging.getLogger(__name__)

def my_view(request):
    logger.info(f"User {request.user} accessed view")
    try:
        result = expensive_operation()
        logger.debug(f"Operation result: {result}")
    except Exception as e:
        logger.error(f"Operation failed: {e}", exc_info=True)
```

**Production Monitoring (Concepts):**

1. **Sentry:** Error tracking, stack traces, alerts
2. **Prometheus + Grafana:** Metrics (request rate, response time, CPU)
3. **ELK Stack:** Log aggregation (Elasticsearch, Logstash, Kibana)
4. **APM Tools:** New Relic, Datadog (full request tracing)

**What to Monitor:**
- **Response time:** P50, P95, P99 latency
- **Error rate:** 4xx, 5xx errors per minute
- **Throughput:** Requests per second
- **Database:** Query time, connection pool
- **Celery:** Task success rate, queue length

**Interview Question: "How do you debug a production issue?"**

**Answer (Process):**
1. **Check monitoring** (is it slow? erroring? high load?)
2. **Check logs** (error messages, stack traces)
3. **Reproduce locally** (if possible)
4. **Add more logging** (if needed)
5. **Deploy fix**
6. **Verify fix** (monitor metrics)

---

## 7. Interview Q&A Section {#interview-qa}

### 7.1 Common Django Interview Questions

**Q: Explain Django's MTV architecture.**

**A:** 
- **Model:** Data layer (ORM, database schema)
- **Template:** Presentation layer (HTML rendering)
- **View:** Business logic (request handling, response)

Unlike MVC (Model-View-Controller), Django's "View" is the controller, and "Template" is the view.

---

**Q: What's the difference between `null=True` and `blank=True`?**

**A:**
- **`null=True`:** Database allows NULL values (DB level)
- **`blank=True`:** Form validation allows empty values (Django level)

```python
# Can be empty in form, but stores empty string (not NULL) in DB
field = models.CharField(max_length=100, blank=True)

# Can be NULL in DB, but form requires value
field = models.CharField(max_length=100, null=True)

# Can be empty in form AND NULL in DB
field = models.CharField(max_length=100, null=True, blank=True)
```

**Interview Tip:** For `CharField`, use `blank=True` only (Django stores empty string, not NULL). For `IntegerField`, `DateField`, use both.

---

**Q: What are Django signals and when would you use them?**

**A:** (Covered in detail above)
- Decoupled event handling
- Use for cross-app communication, audit logs
- Avoid for business logic (hard to debug)

---

**Q: Explain the difference between `select_related` and `prefetch_related`.**

**A:** (Covered in detail above)
- `select_related`: ForeignKey/OneToOne, SQL JOIN
- `prefetch_related`: ManyToMany/Reverse FK, separate query

---

**Q: How do you handle database transactions in Django?**

**A:**
```python
from django.db import transaction

# Automatic transaction (all or nothing)
with transaction.atomic():
    user.balance -= 100
    user.save()
    order.create()
    # If any fails, all rolled back

# Manual rollback
with transaction.atomic():
    try:
        risky_operation()
    except Exception