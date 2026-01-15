"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 DJANGO REST DEBUGGING - ELIMINATION INTERVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Interviewer: Senior Backend Engineer | Production Firefighter
Target: 3-7 YOE Backend Engineers
Focus: Real Failures, Debugging, Performance, N+1 Queries
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ELIMINATION CRITERIA:
─────────────────────
• Can't debug N+1 query problem → REJECT
• Doesn't understand serializer validation flow → REJECT
• Can't explain why request.data is empty → REJECT
• Doesn't know select_related vs prefetch_related → REJECT
• Can't identify performance bottlenecks → REJECT

This is where theory meets reality. Can you fix production fires?
"""

# ═══════════════════════════════════════════════════════════════════════
# PART 4: DEBUGGING & FAILURE SCENARIOS
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4.1 SERIALIZER ALWAYS RETURNS 400 - WHY?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEW QUESTION:
"Your endpoint always returns 400 Bad Request, even with valid data. Debug this."

BROKEN CODE:
"""

from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


# ❌ BROKEN SERIALIZER
class BrokenProductSerializer(serializers.ModelSerializer):
    """
    ❌ MULTIPLE BUGS - Can you spot them all?
    """
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'owner']
        # ❌ BUG #1: owner is required but not provided


class BrokenProductViewSet(viewsets.ModelViewSet):
    """
    ❌ BROKEN: Always 400
    """
    queryset = Product.objects.all()
    serializer_class = BrokenProductSerializer
    
    # ❌ BUG #2: Not setting owner automatically


"""
SYMPTOMS:
─────────
POST /api/products/
{
    "name": "Widget",
    "price": "19.99"
}

Response: 400 Bad Request
{
    "owner": ["This field is required."]
}

CLIENT COMPLAINT: "I'm sending all required data but getting 400!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ROOT CAUSE ANALYSIS:
────────────────────

1. Serializer declares 'owner' in fields
2. ModelSerializer makes it required by default (ForeignKey is not null)
3. Client can't/shouldn't send owner ID
4. View doesn't set owner automatically
5. Validation fails: "owner is required"

🎤 DEBUGGING PROCESS:
─────────────────────

"When I get 400, first thing: check the error response. It says 'owner required'.
Looking at the serializer, owner is in fields but not marked read_only. This means
DRF expects the client to provide it.

But the client shouldn't be choosing the owner - that's a security issue. The view
should set it based on request.user.

There are two fixes:
1. Make owner read_only in serializer
2. Set owner in perform_create()

I'd do both for defense in depth."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ FIXED VERSION:
"""

class FixedProductSerializer(serializers.ModelSerializer):
    """
    ✅ FIXED: owner is read-only
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'owner']
        # owner will be shown in response but not accepted in request


from rest_framework.permissions import IsAuthenticated

class FixedProductViewSet(viewsets.ModelViewSet):
    """
    ✅ FIXED: Sets owner automatically
    """
    queryset = Product.objects.all()
    serializer_class = FixedProductSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        """✅ CRITICAL: Set owner from authenticated user"""
        serializer.save(owner=self.request.user)


"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4.2 request.data IS EMPTY - WHY?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEW QUESTION:
"Client sends JSON but request.data is empty. What's wrong?"

SYMPTOMS:
"""

from rest_framework.views import APIView

class DebugView(APIView):
    def post(self, request):
        print(f"request.data: {request.data}")  # Prints: {}
        print(f"request.body: {request.body}")  # Prints: b'{"name":"test"}'
        return Response({'received': request.data})

"""
Client sends:
POST /api/debug/
Content-Type: application/json
Body: {"name": "test"}

request.data is EMPTY but request.body has data!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ROOT CAUSES (Multiple Possibilities):
──────────────────────────────────────

CAUSE #1: Content-Type Header Missing or Wrong
"""

# Client mistake:
"""
# ❌ WRONG: No Content-Type header
POST /api/debug/
{"name": "test"}

# DRF doesn't know it's JSON, won't parse

# ✅ CORRECT: Explicit Content-Type
POST /api/debug/
Content-Type: application/json
{"name": "test"}
"""

"""
CAUSE #2: Parser Not Configured
"""

# settings.py
# ❌ WRONG: Removed JSON parser
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': [
        # Missing: 'rest_framework.parsers.JSONParser',
    ]
}

# ✅ CORRECT: Include parsers
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',  # ✅ For JSON
        'rest_framework.parsers.FormParser',  # For form data
        'rest_framework.parsers.MultiPartParser',  # For file uploads
    ]
}

"""
CAUSE #3: CSRF Middleware Blocking Request
"""

# If using SessionAuthentication + POST without CSRF token
# Middleware blocks request BEFORE view runs
# request.data never gets parsed

# Solution: Use Token/JWT auth, or send CSRF token

"""
CAUSE #4: request.body Already Read
"""

# ❌ WRONG: Reading body before DRF parses
class BrokenView(APIView):
    def post(self, request):
        body = request.body.decode('utf-8')  # ❌ Consumes stream!
        # Now request.data can't read it - stream exhausted
        print(request.data)  # Empty!

"""
🎤 DEBUGGING APPROACH:
──────────────────────

"First, I'd check if request.body has data. If yes, but request.data is empty,
it's a parsing issue, not a network issue.

Next, I'd verify:
1. Content-Type header in request (use curl -v or browser DevTools)
2. DEFAULT_PARSER_CLASSES in settings
3. Any middleware blocking the request
4. Nothing reading request.body before the view

Most common cause: Frontend not setting Content-Type: application/json."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4.3 N+1 QUERY PROBLEM (CRITICAL PERFORMANCE BUG)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEW QUESTION:
"Your API is slow under load. Show me how you debug and fix N+1 queries."

THIS IS THE #1 DRF PERFORMANCE KILLER
"""

# Models
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    published_date = models.DateField()


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField()


# ❌ BROKEN: Causes N+1 queries
class BrokenBookSerializer(serializers.ModelSerializer):
    """
    ❌ DISASTER: Triggers database query for EACH book's author
    """
    author_name = serializers.CharField(source='author.name')  # ❌ N+1!
    review_count = serializers.SerializerMethodField()  # ❌ N+1!
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'author_name', 'review_count', 'published_date']
    
    def get_review_count(self, obj):
        return obj.reviews.count()  # ❌ Query for EACH book!


class BrokenBookViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ❌ BROKEN: No query optimization
    """
    queryset = Book.objects.all()  # ❌ Only fetches books!
    serializer_class = BrokenBookSerializer


"""
SYMPTOM:
────────
GET /api/books/ (100 books in database)

QUERIES EXECUTED:
1. SELECT * FROM books                    (1 query - gets 100 books)
2. SELECT * FROM authors WHERE id=1       (1 query - book 1's author)
3. SELECT * FROM authors WHERE id=2       (1 query - book 2's author)
4. SELECT * FROM authors WHERE id=3       (1 query - book 3's author)
... (98 more author queries)
101. SELECT COUNT(*) FROM reviews WHERE book_id=1    (book 1's review count)
102. SELECT COUNT(*) FROM reviews WHERE book_id=2    (book 2's review count)
... (98 more review count queries)

TOTAL: 1 + 100 + 100 = 201 queries! 🔥🔥🔥

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎤 HOW TO DETECT:
─────────────────

# Method 1: Django Debug Toolbar (development)
pip install django-debug-toolbar
# Shows query count and duplicate queries

# Method 2: django.db.connection.queries (code)
from django.db import connection

# Make request
with self.assertNumQueries(3):  # Expect 3 queries max
    response = client.get('/api/books/')

print(len(connection.queries))  # Shows actual count

# Method 3: Logging (settings.py)
LOGGING = {
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',  # Logs all SQL queries
        }
    }
}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ FIXED: select_related + prefetch_related + annotate
"""

from django.db.models import Count

class FixedBookSerializer(serializers.ModelSerializer):
    """
    ✅ FIXED: Same fields, optimized queries
    """
    author_name = serializers.CharField(source='author.name', read_only=True)
    review_count = serializers.IntegerField(read_only=True)  # ✅ From annotation
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'author_name', 'review_count', 'published_date']


class FixedBookViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ✅ FIXED: Query optimization
    
    QUERIES NOW:
    1. SELECT * FROM books 
       LEFT JOIN authors ON books.author_id = authors.id
       (1 query - gets books + authors via JOIN)
    
    2. SELECT book_id, COUNT(*) FROM reviews GROUP BY book_id
       (1 query - gets all review counts at once)
    
    TOTAL: 2 queries instead of 201! ⚡
    """
    serializer_class = FixedBookSerializer
    
    def get_queryset(self):
        """
        ✅ CRITICAL: Optimize queries
        
        select_related: For ForeignKey and OneToOne (uses JOIN)
        prefetch_related: For ManyToMany and reverse ForeignKey (uses separate query + Python join)
        annotate: For aggregations (COUNT, SUM, etc.)
        """
        return Book.objects.select_related(
            'author'  # ✅ JOINs author table - 1 query
        ).annotate(
            review_count=Count('reviews')  # ✅ Aggregates counts - no extra queries
        )


"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DECISION TREE: select_related vs prefetch_related
──────────────────────────────────────────────────

USE select_related() WHEN:
- Accessing ForeignKey (Book → Author)
- Accessing OneToOneField
- Want SQL JOIN
- Related object is always needed
- Example: book.author.name

USE prefetch_related() WHEN:
- Accessing reverse ForeignKey (Author → Books)
- Accessing ManyToManyField
- Want separate query + Python join
- May not need all related objects
- Example: author.books.all()

USE annotate() WHEN:
- Need COUNT, SUM, AVG, etc.
- Aggregating related data
- Example: author.books.count()

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎤 EXPLANATION IN INTERVIEW:
────────────────────────────

"N+1 is when you fetch a list of objects (1 query), then access a related field
on each object in a loop (N queries). Classic example: serializer accesses
obj.author.name for each book.

I detect it using Django Debug Toolbar in dev or logging queries in test. If I
see the same query with different IDs, that's N+1.

Fix depends on relationship:
- ForeignKey: select_related() for JOIN
- Reverse FK or M2M: prefetch_related()
- Aggregations: annotate()

In this case, author is ForeignKey so select_related(). Review count is aggregation
so annotate(Count('reviews')). This reduces 201 queries to 2."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4.4 MIGRATIONS FAIL AFTER ADDING FIELD - WHY?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEW QUESTION:
"You add a required field to User model. makemigrations works, but migrate
fails in production with existing users. Fix it."

SCENARIO:
"""

# You add this to User model:
class User(models.Model):
    # ... existing fields ...
    phone_number = models.CharField(max_length=15)  # ❌ Required, no default!

# makemigrations
# → Creates migration

# migrate
# → ERROR: "column phone_number cannot be null"

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ROOT CAUSE:
───────────
Production has 10,000 existing users. New field is required (NOT NULL).
Django tries to add column but can't determine what value to use for existing rows.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ SOLUTION 1: Make field nullable
"""

class User(models.Model):
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    # ✅ Existing users get NULL, new users can be required via serializer

"""
✅ SOLUTION 2: Provide default value
"""

class User(models.Model):
    phone_number = models.CharField(max_length=15, default='')
    # ✅ Existing users get empty string

"""
✅ SOLUTION 3: Two-step migration (SAFEST for production)
"""

# Step 1: Add field as nullable
phone_number = models.CharField(max_length=15, null=True, blank=True)
# → makemigrations, migrate

# Step 2: Data migration to populate values
# → Write custom migration to set defaults

# Step 3: Make field required
phone_number = models.CharField(max_length=15)  # Remove null=True
# → makemigrations, migrate

"""
🎤 INTERVIEW EXPLANATION:
─────────────────────────

"When adding a required field to a model with existing data, Django needs a value
for existing rows. Three options:

1. Make field nullable - safest, but field not truly required at DB level
2. Provide default - works but all existing rows get same value
3. Three-step migration - nullable, populate data, then make required

For production, I'd use option 3 with a data migration. This ensures existing
users get meaningful values, not just NULL or empty string."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4.5 AUTH WORKS LOCALLY, FAILS IN PRODUCTION - WHY?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

COMMON CAUSES:
"""

# CAUSE #1: CORS not configured
"""
Local: Frontend and backend on same domain (localhost)
Production: Frontend on app.com, backend on api.app.com
→ CORS blocks requests

Fix: Install django-cors-headers

pip install django-cors-headers

settings.py:
INSTALLED_APPS = [
    'corsheaders',
    ...
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # ✅ Before CommonMiddleware
    'django.middleware.common.CommonMiddleware',
    ...
]

CORS_ALLOWED_ORIGINS = [
    'https://app.com',
]

# Or for development (INSECURE):
CORS_ALLOW_ALL_ORIGINS = True  # ❌ Don't use in production
"""

# CAUSE #2: HTTPS vs HTTP
"""
Local: http://localhost:8000
Production: https://api.app.com
→ Browser blocks mixed content

Fix: Ensure frontend uses HTTPS if backend does
"""

# CAUSE #3: Cookie settings
"""
If using SessionAuthentication:

settings.py:
SESSION_COOKIE_SECURE = True  # ✅ Only send over HTTPS
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'None'  # ✅ For cross-domain
CSRF_COOKIE_SAMESITE = 'None'

# ⚠️ SAMESITE='None' requires SECURE=True
"""

# CAUSE #4: Allowed Hosts
"""
settings.py:
ALLOWED_HOSTS = []  # ❌ Blocks all requests in production!

# ✅ Fix:
ALLOWED_HOSTS = ['api.app.com', '.app.com']  # ✅ Allow domain
"""


"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4.6 SERIALIZER VALIDATION ORDER (CRITICAL TO UNDERSTAND)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEW QUESTION:
"Explain the order in which serializer validations run."
"""

class ExampleSerializer(serializers.Serializer):
    email = serializers.EmailField()
    age = serializers.IntegerField()
    password = serializers.CharField()
    
    def validate_age(self, value):
        """Step 2: Field-level validation for 'age'"""
        if value < 18:
            raise serializers.ValidationError("Must be 18+")
        return value
    
    def validate_email(self, value):
        """Step 2: Field-level validation for 'email'"""
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value
    
    def validate(self, attrs):
        """Step 3: Object-level validation (all fields together)"""
        if attrs['age'] < 21 and len(attrs['password']) < 12:
            raise serializers.ValidationError(
                "Users under 21 must have 12+ character password"
            )
        return attrs


"""
VALIDATION ORDER:
─────────────────

1. FIELD TYPE VALIDATION (automatic)
   - EmailField checks valid email format
   - IntegerField checks it's a number
   - Required fields check presence
   
2. FIELD-LEVEL VALIDATORS (validate_<field>)
   - validate_age() runs for age
   - validate_email() runs for email
   - Runs for EACH field independently
   
3. OBJECT-LEVEL VALIDATION (validate())
   - Runs with ALL fields
   - Can validate relationships between fields
   - Runs AFTER all field validations pass

4. UNIQUE CONSTRAINTS (if using ModelSerializer)
   - Checks database uniqueness
   - Runs LAST

serializer.is_valid() returns False if ANY step fails.
serializer.errors contains all validation errors.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ═══════════════════════════════════════════════════════════════════════
# RAPID-FIRE DEBUGGING QUESTIONS
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RAPID-FIRE (45 seconds per question)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q1: "API returns 400, error says 'owner required'. Fix?"
EXPECTED: "Make owner read_only in serializer, set in perform_create()"
REJECT IF: "Tell client to send owner"

Q2: "request.data is empty but request.body has data. Cause?"
EXPECTED: "Missing Content-Type header or parser not configured"
REJECT IF: Doesn't know

Q3: "100 books, 201 database queries. Problem?"
EXPECTED: "N+1 query problem - use select_related()"
INSTANT REJECT IF: "That's normal"

Q4: "select_related vs prefetch_related - when to use each?"
EXPECTED: "select_related for FK (JOIN), prefetch_related for reverse FK/M2M"
REJECT IF: Confuses them

Q5: "Migration fails: 'column cannot be null'. Fix?"
EXPECTED: "Add null=True, blank=True or default value"
REJECT IF: "Just drop the database"

Q6: "Auth works locally, fails in production. First thing to check?"
EXPECTED: "CORS configuration and ALLOWED_HOSTS"
REJECT IF: Doesn't mention CORS

Q7: "Serializer validation order?"
EXPECTED: "Field type → field validators → object validator → unique constraints"
REJECT IF: Doesn't know order

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ═══════════════════════════════════════════════════════════════════════
# SELF-ASSESSMENT
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CRITICAL (Must answer YES to ALL):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

□ Can debug N+1 query problems
□ Know select_related vs prefetch_related
□ Understand serializer validation order
□ Can fix "field required" serializer errors
□ Know why request.data can be empty
□ Can handle migrations with existing data
□ Understand CORS and production auth issues

SCORING:
< 7/7: FAIL - Cannot debug production issues
7/7: PASS - Can handle production fires

INTERVIEWER CONCLUSION:

IF FAIL:
"Candidate cannot debug real-world problems. Would struggle in production
incidents. N+1 queries would kill performance. Cannot migrate data safely. REJECT."

IF PASS:
"Can diagnose and fix production issues. Understands performance optimization.
Knows Django/DRF debugging tools. Can handle incidents. PROCEED."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BOTTOM LINE:
Theory is useless if you can't debug production fires. N+1 queries are the
#1 performance killer in DRF - if you don't know select_related(), you'll
build slow APIs.

400 errors are usually serializer validation - learn to read error messages.
request.data empty is usually Content-Type header - check network tab.
Auth fails in prod is usually CORS - check browser console.

If you can't debug these, you're not production-ready.
"""
