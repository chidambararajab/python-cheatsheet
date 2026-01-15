"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 DJANGO REST FRAMEWORK CORE - ELIMINATION INTERVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Interviewer: Senior Backend Engineer | Django Expert | Hiring Bar-Raiser
Target: 3-7 YOE | Backend Engineers
Focus: Django vs DRF Responsibility + Core API Design
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ELIMINATION CRITERIA:
─────────────────────
• Can't explain Django request vs DRF Request → REJECT
• Confuses middleware with authentication classes → REJECT
• Doesn't know serializer validation order → REJECT
• Can't explain when to use APIView vs ViewSet → REJECT
• Writes insecure or N+1 query code → REJECT

This file covers FUNDAMENTAL DRF knowledge.
If you fail these questions, you don't understand DRF at a production level.
"""

# ═══════════════════════════════════════════════════════════════════════
# PART 1: DJANGO vs DRF RESPONSIBILITY
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1.1 DJANGO REQUEST vs DRF REQUEST (CRITICAL)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEW QUESTION:
"Explain the difference between Django's HttpRequest and DRF's Request.
Why does DRF wrap it?"

WHAT INTERVIEWER IS TESTING:
• Do you understand the request parsing layer?
• Do you know how DRF handles content negotiation?
• Can you explain request.data vs request.POST?
"""

# ─────────────────────────────────────────────────────────────────────
# DJANGO WAY (Standard View)
# ─────────────────────────────────────────────────────────────────────

from django.http import JsonResponse
from django.views import View
import json

class DjangoOrderView(View):
    """
    ❌ DJANGO VANILLA VIEW - Manual parsing required
    """
    def post(self, request):
        # ⚠️ Problem 1: request.POST only works for form data!
        # If client sends JSON, request.POST is empty
        
        # Manual parsing required:
        try:
            data = json.loads(request.body)  # You must do this manually
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
        product_id = data.get('product_id')
        quantity = data.get('quantity')
        
        # ⚠️ Problem 2: No automatic validation
        # ⚠️ Problem 3: request.body can only be read once!
        # ⚠️ Problem 4: Content-Type handling is manual
        
        return JsonResponse({'status': 'created'})


# ─────────────────────────────────────────────────────────────────────
# DRF WAY (API View)
# ─────────────────────────────────────────────────────────────────────

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class DRFOrderView(APIView):
    """
    ✅ DRF API VIEW - Automatic parsing and content negotiation
    """
    def post(self, request):
        # ✅ request.data works for JSON, form data, multipart, etc.
        # DRF automatically parses based on Content-Type header
        
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity')
        
        # ✅ request.data is cached, can be accessed multiple times
        # ✅ Content negotiation handled automatically
        # ✅ Supports multiple parsers (JSON, XML, YAML, etc.)
        
        return Response({'status': 'created'}, status=status.HTTP_201_CREATED)


"""
🎤 IDEAL THINK-ALOUD EXPLANATION:
──────────────────────────────────

"DRF's Request class wraps Django's HttpRequest to provide a unified interface
for accessing parsed data. In Django, request.POST only contains form data - if
the client sends JSON, request.POST is empty and you must manually parse request.body.

DRF's request.data provides a single interface that works with any content type.
DRF uses parsers to automatically deserialize the request body based on Content-Type.
It's also cached, so you can access request.data multiple times without re-parsing.

Additionally, request.body can only be read once in Django - it's a stream. DRF
handles this internally."

🚫 COMMON WRONG ANSWER:
"They're basically the same, DRF just adds some convenience methods."
→ REJECT: Doesn't understand content negotiation or parsing

❌ PRODUCTION FAILURE:
If you use request.POST with JSON requests, your API silently ignores the payload.
Client sends data, you process nothing, return success - data corruption.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1.2 MIDDLEWARE vs DRF AUTHENTICATION CLASSES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEW QUESTION:
"Should authentication logic go in middleware or DRF authentication classes?
What breaks if you put it in the wrong place?"

WHAT INTERVIEWER IS TESTING:
• Do you understand the Django request lifecycle?
• Do you know when middleware runs vs when auth classes run?
• Can you explain the order of operations?
"""

# ─────────────────────────────────────────────────────────────────────
# ❌ WRONG: Putting API auth in middleware
# ─────────────────────────────────────────────────────────────────────

class WrongTokenAuthMiddleware:
    """
    ❌ ANTI-PATTERN: API authentication in middleware
    
    Why this is WRONG:
    1. Runs for ALL requests (static files, admin, health checks)
    2. Can't return DRF Response with proper error format
    3. Runs before DRF request wrapping
    4. No access to DRF's authentication/permission framework
    5. Performance impact on non-API requests
    """
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # ⚠️ This runs for EVERY request, even static files!
        token = request.META.get('HTTP_AUTHORIZATION')
        
        if token:
            # ⚠️ Must manually parse and validate
            # ⚠️ Can't use DRF's token model easily
            # ⚠️ Error handling is awkward
            pass
        
        response = self.get_response(request)
        return response


# ─────────────────────────────────────────────────────────────────────
# ✅ CORRECT: DRF Authentication Class
# ─────────────────────────────────────────────────────────────────────

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import get_user_model

User = get_user_model()

class TokenAuthentication(BaseAuthentication):
    """
    ✅ CORRECT: Authentication as DRF authentication class
    
    Why this is CORRECT:
    1. Only runs for DRF views
    2. Returns (user, auth) tuple - DRF standard
    3. Can raise AuthenticationFailed with proper DRF error format
    4. Integrates with DRF permission system
    5. Runs after request wrapping, has access to request.data
    """
    
    def authenticate(self, request):
        # Only called for API views with this auth class
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        
        if not auth_header:
            return None  # Let other auth classes try
        
        try:
            token = auth_header.split(' ')[1]  # "Bearer <token>"
        except IndexError:
            raise AuthenticationFailed('Invalid token format')
        
        # Validate token (pseudo-code)
        try:
            # user = validate_token(token)
            user = User.objects.get(auth_token=token)
        except User.DoesNotExist:
            raise AuthenticationFailed('Invalid token')
        
        return (user, token)  # DRF standard return


# Usage in view:
from rest_framework.permissions import IsAuthenticated

class ProtectedView(APIView):
    """
    Combines authentication + permissions correctly
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        # request.user is set by authentication class
        return Response({'user': request.user.username})


"""
🎤 IDEAL THINK-ALOUD EXPLANATION:
──────────────────────────────────

"Middleware runs for EVERY request in Django - static files, admin, API, everything.
It runs early in the request lifecycle, before Django even determines which view
to call. Middleware is for cross-cutting concerns like CORS, logging, or session
management.

DRF authentication classes run ONLY for DRF views, after the request is wrapped
in DRF's Request object. They're designed to integrate with DRF's permission and
throttling system. They return a (user, auth) tuple that DRF uses to populate
request.user and request.auth.

If you put API auth in middleware, you'll authenticate requests to static files,
waste CPU, can't return proper DRF error responses, and bypass DRF's permission
system entirely."

🚫 COMMON WRONG ANSWER:
"Middleware is for Django views, auth classes are for API views."
→ INCOMPLETE: Doesn't explain the lifecycle or integration issues

❌ PRODUCTION FAILURE:
Middleware-based API auth runs on health check endpoints, causing performance
issues. During incident response, health checks time out, leading to cascading
failures and incorrect auto-scaling decisions.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1.3 DJANGO VIEWS vs APIView vs ViewSet
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEW QUESTION:
"When would you use APIView vs ViewSet? Give a real-world example where
using the wrong one causes problems."

WHAT INTERVIEWER IS TESTING:
• Do you understand ViewSet is for CRUD?
• Do you know when custom logic needs APIView?
• Can you explain router auto-generation?
"""

from rest_framework import viewsets, serializers
from rest_framework.decorators import action
from django.db import models

# ─────────────────────────────────────────────────────────────────────
# MODELS (for examples)
# ─────────────────────────────────────────────────────────────────────

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'stock', 'created_at']


# ─────────────────────────────────────────────────────────────────────
# SCENARIO 1: CRUD Operations → Use ViewSet
# ─────────────────────────────────────────────────────────────────────

class ProductViewSet(viewsets.ModelViewSet):
    """
    ✅ CORRECT: ViewSet for standard CRUD
    
    Auto-generates:
    - GET /products/ (list)
    - POST /products/ (create)
    - GET /products/{id}/ (retrieve)
    - PUT /products/{id}/ (update)
    - PATCH /products/{id}/ (partial_update)
    - DELETE /products/{id}/ (destroy)
    
    Router auto-wires URLs.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    # Can add custom actions:
    @action(detail=True, methods=['post'])
    def restock(self, request, pk=None):
        """
        POST /products/{id}/restock/
        Custom action within resource context
        """
        product = self.get_object()
        amount = request.data.get('amount', 0)
        product.stock += amount
        product.save()
        return Response({'stock': product.stock})


# Router usage:
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductViewSet)
# Auto-generates all CRUD URLs


# ─────────────────────────────────────────────────────────────────────
# SCENARIO 2: Non-CRUD Logic → Use APIView
# ─────────────────────────────────────────────────────────────────────

class PasswordResetView(APIView):
    """
    ✅ CORRECT: APIView for non-CRUD endpoint
    
    This is NOT a resource operation. It's a one-off action.
    ViewSet would be awkward here - no model to CRUD.
    """
    permission_classes = []  # Public endpoint
    
    def post(self, request):
        email = request.data.get('email')
        
        # Custom business logic
        try:
            user = User.objects.get(email=email)
            # Send reset email logic
            return Response({'message': 'Reset email sent'})
        except User.DoesNotExist:
            # Security: Don't reveal if email exists
            return Response({'message': 'Reset email sent'})


class AnalyticsView(APIView):
    """
    ✅ CORRECT: APIView for aggregation/reporting
    
    Not operating on a single resource - returning computed data.
    """
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        from django.db.models import Count, Sum
        
        stats = Product.objects.aggregate(
            total_products=Count('id'),
            total_value=Sum('price')
        )
        return Response(stats)


# ─────────────────────────────────────────────────────────────────────
# ❌ WRONG: Using ViewSet for non-CRUD
# ─────────────────────────────────────────────────────────────────────

class WrongPasswordResetViewSet(viewsets.ViewSet):
    """
    ❌ ANTI-PATTERN: ViewSet for non-CRUD
    
    Problems:
    1. Must implement list(), create(), etc. even if not used
    2. Router expects resource URLs (/password-reset/{id}/)
    3. Confusing API design
    4. Extra boilerplate
    """
    def create(self, request):
        # Awkward - "create" a password reset?
        pass


"""
🎤 IDEAL THINK-ALOUD EXPLANATION:
──────────────────────────────────

"ViewSet is designed for CRUD operations on a resource. It provides list, create,
retrieve, update, and destroy methods out of the box. Use it when your endpoint
maps to a database model and follows RESTful resource patterns.

APIView is for custom logic that doesn't fit CRUD. Examples: login, password reset,
analytics, search, webhooks - anything that's not operating on a specific resource
instance. APIView gives you full control over HTTP methods without CRUD assumptions.

The key distinction: ViewSet = resource-oriented (nouns), APIView = action-oriented
(verbs). If your URL is /users/{id}/ → ViewSet. If it's /login/ → APIView."

🚫 COMMON WRONG ANSWER:
"ViewSet is just a convenience wrapper around APIView."
→ INCOMPLETE: Misses the resource-oriented design principle

❌ PRODUCTION FAILURE:
Using ViewSet for /login/ endpoint causes router to generate /login/{id}/ URL,
breaking mobile app which hardcoded /login/. Emergency hotfix required during
peak traffic.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1.4 ORM RESPONSIBILITY vs SERIALIZER RESPONSIBILITY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEW QUESTION:
"Should business logic go in the model, serializer, or view? Where do you
put validation, permissions, and side effects?"

WHAT INTERVIEWER IS TESTING:
• Do you understand separation of concerns?
• Do you know serializer validation flow?
• Can you avoid mixing responsibilities?
"""

# ─────────────────────────────────────────────────────────────────────
# MODEL: Data integrity and database-level logic
# ─────────────────────────────────────────────────────────────────────

class Order(models.Model):
    """
    ✅ MODEL RESPONSIBILITY:
    - Database constraints
    - Data integrity
    - Model-level methods (not business logic)
    - Properties/computed fields
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('shipped', 'Shipped'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        # ✅ Database-level constraints
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', 'status']),
        ]
    
    # ✅ Model method: data-level logic
    @property
    def is_editable(self):
        """Can this order be modified?"""
        return self.status == 'pending'
    
    # ❌ WRONG: Business logic in model
    # def process_payment(self):
    #     # NO! This is business logic, not data logic
    #     pass


# ─────────────────────────────────────────────────────────────────────
# SERIALIZER: API-level validation and transformation
# ─────────────────────────────────────────────────────────────────────

class OrderSerializer(serializers.ModelSerializer):
    """
    ✅ SERIALIZER RESPONSIBILITY:
    - API input validation
    - Data transformation (API ↔ Model)
    - Field-level permission checks
    - Related data handling
    """
    
    class Meta:
        model = Order
        fields = ['id', 'user', 'total', 'status', 'created_at']
        read_only_fields = ['created_at']
    
    # ✅ Field-level validation
    def validate_total(self, value):
        """Validate single field"""
        if value <= 0:
            raise serializers.ValidationError("Total must be positive")
        return value
    
    # ✅ Object-level validation
    def validate(self, attrs):
        """Validate multiple fields together"""
        if attrs.get('status') == 'paid' and attrs.get('total', 0) <= 0:
            raise serializers.ValidationError(
                "Paid orders must have positive total"
            )
        return attrs
    
    # ✅ Custom create logic
    def create(self, validated_data):
        """Transform API data to model instance"""
        # Can add default values, related objects, etc.
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
    
    # ❌ WRONG: Business logic in serializer
    # def create(self, validated_data):
    #     order = super().create(validated_data)
    #     # NO! Don't call external services here
    #     send_confirmation_email(order)  # WRONG PLACE
    #     charge_payment_gateway(order)   # WRONG PLACE
    #     return order


# ─────────────────────────────────────────────────────────────────────
# VIEW: Business logic orchestration
# ─────────────────────────────────────────────────────────────────────

class OrderViewSet(viewsets.ModelViewSet):
    """
    ✅ VIEW RESPONSIBILITY:
    - Business logic orchestration
    - Permission checks
    - Side effects (emails, events, external APIs)
    - Transaction management
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """✅ Filter data based on permissions"""
        if self.request.user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        """
        ✅ Business logic AFTER validation
        This is the correct place for side effects
        """
        # Save first (atomic)
        order = serializer.save()
        
        # Then side effects (can fail independently)
        try:
            self.send_confirmation_email(order)
        except Exception as e:
            # Log but don't fail request
            logger.error(f"Email failed: {e}")
        
        # Trigger async tasks
        from .tasks import process_order_payment
        process_order_payment.delay(order.id)
    
    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        """
        ✅ Custom action: business logic here
        """
        order = self.get_object()
        
        # Permission check
        if order.user != request.user and not request.user.is_staff:
            return Response(
                {'error': 'Not authorized'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        # Business rule
        if not order.is_editable:
            return Response(
                {'error': 'Cannot cancel non-pending order'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Business logic
        order.status = 'cancelled'
        order.save()
        
        # Side effects
        self.refund_payment(order)
        self.send_cancellation_email(order)
        
        return Response({'status': 'cancelled'})
    
    def send_confirmation_email(self, order):
        pass  # Implementation
    
    def refund_payment(self, order):
        pass  # Implementation
    
    def send_cancellation_email(self, order):
        pass  # Implementation


"""
🎤 IDEAL THINK-ALOUD EXPLANATION:
──────────────────────────────────

"There's a clear separation of concerns:

MODEL: Database-level concerns. Constraints, relationships, indexes, simple
properties. Think of it as 'what is valid in the database'. Don't put API-specific
or business logic here.

SERIALIZER: API-level validation and transformation. Converts between API format
and model format. Validates that incoming API data is valid. This is 'what is
valid from the API'. Don't put side effects here.

VIEW: Business logic orchestration. Permission checks, calling external services,
sending emails, triggering async tasks. This is 'what happens when the API is called'.

The validation flow is: View calls serializer.is_valid() → serializer validates →
if valid, view calls perform_create/update → view adds side effects.

If you put business logic in the serializer, you can't reuse the serializer in
different contexts. If you put API validation in the model, you break ORM usage
from management commands or Celery tasks."

🚫 COMMON WRONG ANSWER:
"It doesn't really matter, just keep it organized."
→ REJECT: Will mix concerns and create untestable code

❌ PRODUCTION FAILURE:
Developer puts payment processing in serializer.create(). During bulk order import
from admin panel, every order triggers payment API, causing rate limiting and
partial failures with no rollback. Financial reconciliation nightmare.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ═══════════════════════════════════════════════════════════════════════
# RAPID-FIRE ELIMINATION QUESTIONS (Code-Based)
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RAPID-FIRE ROUND (60 seconds per question)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q1: "What does request.data return if Content-Type is application/json?"
EXPECTED: "Parsed dict/list, automatically deserialized"
REJECT IF: "String" or "Doesn't know"

Q2: "Where do you put token validation logic?"
EXPECTED: "Authentication class, not middleware"
REJECT IF: "Middleware" or "View"

Q3: "When should you use ViewSet vs APIView?"
EXPECTED: "ViewSet for CRUD resources, APIView for custom actions"
REJECT IF: Can't distinguish

Q4: "What's the difference between perform_create and create?"
EXPECTED: "perform_create is for side effects after save, create is serializer method"
REJECT IF: "They're the same"

Q5: "Code review: Serializer sends email in create(). Correct?"
EXPECTED: "No - side effects belong in view's perform_create"
REJECT IF: "Yes" or hesitates

Q6: "Why shouldn't you put API validation in the model?"
EXPECTED: "Model used by ORM everywhere - admin, shell, tasks. API validation would break those."
REJECT IF: "It's fine"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ═══════════════════════════════════════════════════════════════════════
# SELF-ASSESSMENT
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CRITICAL (Must answer YES to ALL):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

□ Know request.data vs request.POST
□ Understand middleware runs for ALL requests
□ Know when to use APIView vs ViewSet
□ Understand serializer validation flow
□ Know Model vs Serializer vs View responsibility
□ Never put side effects in serializers
□ Never put API auth in middleware

SCORING:
< 7/7: FAIL - Missing fundamental DRF knowledge
7/7: PASS - Understand DRF core architecture

INTERVIEWER CONCLUSION:

IF FAIL:
"Candidate doesn't understand Django vs DRF separation. Would mix concerns,
create performance issues, and build unmaintainable APIs. REJECT."

IF PASS:
"Solid understanding of DRF architecture. Knows where logic belongs. Can design
clean APIs. PROCEED to next round."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
