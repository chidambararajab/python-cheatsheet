"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 DJANGO REST FRAMEWORK - FULL MOCK INTERVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Interviewer: Senior Backend Engineer | Hiring Manager
Target: 3-7 YOE Backend Engineers
Format: Real Interview Simulation with Code Review
Duration: 45 minutes
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEW FORMAT:
─────────────────
1. Code Review (15 min) - Find bugs in production code
2. Design Question (15 min) - Design API from requirements
3. Rapid-Fire (10 min) - Quick technical questions
4. Performance (5 min) - Optimize slow endpoint

ELIMINATION CRITERIA:
─────────────────────
• Cannot spot security bugs → INSTANT REJECT
• Doesn't understand N+1 → REJECT
• Can't design basic CRUD API → REJECT
• Confuses fundamental concepts → REJECT

This simulates a real interview. No hints. No second chances.
"""

from rest_framework import serializers, viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# ═══════════════════════════════════════════════════════════════════════
# ROUND 1: CODE REVIEW (Find ALL the bugs)
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEWER:
"Here's code from a pull request. It's for a blog API. Find all the bugs
and security issues. Be specific about what breaks and why."

TIME LIMIT: 15 minutes
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

# Models
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)


# ❌ BUG-FILLED CODE - Find all issues!
class BlogPostSerializer(serializers.ModelSerializer):
    """
    Serializer for blog posts
    How many bugs can you find?
    """
    class Meta:
        model = BlogPost
        fields = '__all__'  # ❌ BUG #1: What's wrong with this?


class BlogPostViewSet(viewsets.ModelViewSet):
    """
    API for blog posts
    Multiple critical bugs here
    """
    queryset = BlogPost.objects.all()  # ❌ BUG #2: What's the problem?
    serializer_class = BlogPostSerializer
    
    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        """Publish a blog post"""
        post = self.get_object()  # ❌ BUG #3: Security issue?
        post.is_published = True
        post.save()
        return Response({'status': 'published'})


class UserRegistrationSerializer(serializers.ModelSerializer):
    """User registration"""
    password = serializers.CharField()  # ❌ BUG #4: Major security hole!
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def create(self, validated_data):
        user = User.objects.create(**validated_data)  # ❌ BUG #5: Critical!
        return user


"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EXPECTED ANSWERS (Candidate should find ALL):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🐛 BUG #1: fields = '__all__'
───────────────────────────────
PROBLEM:
- Exposes ALL model fields including internal ones
- Author field can be set by client (security issue)
- No control over read-only fields
- May expose sensitive data

FIX:
```python
fields = ['id', 'title', 'content', 'author', 'created_at', 'is_published']
read_only_fields = ['id', 'author', 'created_at']
```

IMPACT: Security - privilege escalation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🐛 BUG #2: queryset = BlogPost.objects.all()
─────────────────────────────────────────────
PROBLEM:
- Returns ALL blog posts to ALL users
- Users can read others' unpublished drafts
- No filtering by author or publication status
- Data leak

FIX:
```python
def get_queryset(self):
    if self.action == 'list':
        # Show only published posts, or user's own
        if self.request.user.is_authenticated:
            return BlogPost.objects.filter(
                models.Q(is_published=True) | models.Q(author=self.request.user)
            )
        return BlogPost.objects.filter(is_published=True)
    return BlogPost.objects.all()
```

IMPACT: Security - information disclosure

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🐛 BUG #3: No permission check in publish()
────────────────────────────────────────────
PROBLEM:
- Anyone can publish ANYONE's blog post
- No check if post.author == request.user
- Privilege escalation

FIX:
```python
@action(detail=True, methods=['post'])
def publish(self, request, pk=None):
    post = self.get_object()
    
    # ✅ Check ownership
    if post.author != request.user:
        return Response(
            {'error': 'Not authorized'},
            status=status.HTTP_403_FORBIDDEN
        )
    
    post.is_published = True
    post.save()
    return Response({'status': 'published'})
```

IMPACT: Security - unauthorized modification

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🐛 BUG #4: password not write_only
───────────────────────────────────
PROBLEM:
- Password returned in API responses
- GET /api/users/ returns passwords (even hashed, still bad)
- Security violation

FIX:
```python
password = serializers.CharField(write_only=True)  # ✅
```

IMPACT: Security - information disclosure

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🐛 BUG #5: Plain text password storage
───────────────────────────────────────
PROBLEM:
- User.objects.create() stores password as plain text
- CRITICAL security vulnerability
- Violates GDPR, PCI-DSS, every security standard

FIX:
```python
def create(self, validated_data):
    password = validated_data.pop('password')
    user = User.objects.create(**validated_data)
    user.set_password(password)  # ✅ Hash password
    user.save()
    return user
```

IMPACT: CRITICAL - Authentication bypass, compliance violation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SCORING:
────────
Found 0-2 bugs: REJECT - Missing critical security issues
Found 3-4 bugs: BORDERLINE - Missed at least one critical bug
Found ALL 5 bugs: PASS - Solid security awareness

INTERVIEWER NOTES:
──────────────────
- Bug #5 is INSTANT REJECT if missed
- Bug #3 is INSTANT REJECT if missed
- Candidate should explain IMPACT, not just spot bug
"""


# ═══════════════════════════════════════════════════════════════════════
# ROUND 2: API DESIGN QUESTION
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEWER:
"Design a REST API for a simple e-commerce system. Requirements:

1. Products (name, price, stock, seller)
2. Users can list/view products
3. Only sellers can create/edit their own products
4. Users can add products to cart
5. Users can checkout (create order from cart)

Show me:
- Models
- Serializers
- ViewSets/Views
- Permissions
- URL routing

Focus on correctness, not perfection. 15 minutes."
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

"""
✅ EXPECTED SOLUTION (Strong Candidate):
"""

from django.db import models
from django.contrib.auth import get_user_model
from rest_framework import serializers, viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

User = get_user_model()


# ─────────────────────────────────────────────────────────────────────
# MODELS
# ─────────────────────────────────────────────────────────────────────

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user', 'product']  # ✅ One cart item per product per user


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # ✅ Snapshot price


# ─────────────────────────────────────────────────────────────────────
# PERMISSIONS
# ─────────────────────────────────────────────────────────────────────

class IsSellerOrReadOnly(permissions.BasePermission):
    """
    ✅ CORRECT: Only sellers can create/edit their products
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Check if user is seller (assuming User has is_seller flag or role)
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only seller who owns the product can edit
        return obj.seller == request.user


# ─────────────────────────────────────────────────────────────────────
# SERIALIZERS
# ─────────────────────────────────────────────────────────────────────

class ProductSerializer(serializers.ModelSerializer):
    seller_name = serializers.CharField(source='seller.username', read_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'seller', 'seller_name', 'created_at']
        read_only_fields = ['id', 'seller', 'created_at']


class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_price = serializers.DecimalField(source='product.price', max_digits=10, decimal_places=2, read_only=True)
    
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_name', 'product_price', 'quantity', 'added_at']
        read_only_fields = ['id', 'added_at']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'price']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'user', 'total', 'status', 'items', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']


# ─────────────────────────────────────────────────────────────────────
# VIEWSETS
# ─────────────────────────────────────────────────────────────────────

class ProductViewSet(viewsets.ModelViewSet):
    """
    ✅ CORRECT: CRUD for products with proper permissions
    """
    queryset = Product.objects.select_related('seller')  # ✅ Optimize query
    serializer_class = ProductSerializer
    permission_classes = [IsSellerOrReadOnly]
    
    def perform_create(self, serializer):
        """✅ Set seller automatically"""
        serializer.save(seller=self.request.user)


class CartViewSet(viewsets.ViewSet):
    """
    ✅ CORRECT: Cart operations (not standard CRUD)
    """
    permission_classes = [permissions.IsAuthenticated]
    
    def list(self, request):
        """GET /api/cart/ - View cart"""
        cart_items = CartItem.objects.filter(user=request.user).select_related('product')
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def add_item(self, request):
        """POST /api/cart/add_item/ - Add product to cart"""
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)
        
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Get or create cart item
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,
            product=product,
            defaults={'quantity': quantity}
        )
        
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        
        return Response(CartItemSerializer(cart_item).data, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['post'])
    def checkout(self, request):
        """POST /api/cart/checkout/ - Create order from cart"""
        cart_items = CartItem.objects.filter(user=request.user).select_related('product')
        
        if not cart_items.exists():
            return Response({'error': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Calculate total
        total = sum(item.product.price * item.quantity for item in cart_items)
        
        # Create order
        order = Order.objects.create(user=request.user, total=total)
        
        # Create order items
        for cart_item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity,
                price=cart_item.product.price  # ✅ Snapshot current price
            )
        
        # Clear cart
        cart_items.delete()
        
        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)


class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ✅ CORRECT: View orders (read-only)
    """
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        """✅ Users only see their own orders"""
        return Order.objects.filter(user=self.request.user).prefetch_related('items')


# ─────────────────────────────────────────────────────────────────────
# URL ROUTING
# ─────────────────────────────────────────────────────────────────────

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'orders', OrderViewSet, basename='order')

# URLs: urls.py
# urlpatterns = [
#     path('api/', include(router.urls)),
# ]


"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SCORING:
────────
Must have:
✅ Proper models with relationships
✅ Seller permission check
✅ Set seller automatically in perform_create
✅ Filter orders by user
✅ Cart operations (add, checkout)
✅ Price snapshot in OrderItem

Bonus points:
✅ select_related/prefetch_related
✅ unique_together on CartItem
✅ Proper serializer fields selection

REJECT IF:
❌ No permission checks
❌ Doesn't filter orders by user
❌ Doesn't set seller automatically
❌ No cart functionality

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ═══════════════════════════════════════════════════════════════════════
# ROUND 3: RAPID-FIRE TECHNICAL QUESTIONS
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEWER: "Quick questions. 30 seconds each."
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q1: "This code. What prints?"

serializer = ProductSerializer(data={'name': 'Test', 'price': 'invalid'})
print(serializer.is_valid())
print(serializer.errors)

EXPECTED: "False, then error dict with 'price' validation error"
REJECT IF: "Raises exception"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q2: "When does perform_create run?"

EXPECTED: "After serializer.is_valid() passes, when serializer.save() is called"
REJECT IF: "Before validation"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q3: "JWT vs Session auth for mobile app?"

EXPECTED: "JWT - stateless, no cookie issues, works cross-domain"
REJECT IF: "Session"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q4: "This returns 403. Why?"

class MyView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]

EXPECTED: "Both permissions must pass. If IsOwner returns False, 403"
REJECT IF: "Wrong explanation"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q5: "100 products, each has author. How many queries?"

Product.objects.all()
for product in products:
    print(product.author.name)

EXPECTED: "101 - one for products, 100 for authors. N+1 problem"
INSTANT REJECT IF: "1"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q6: "Fix the N+1:"

EXPECTED: "Product.objects.select_related('author')"
REJECT IF: Doesn't know

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q7: "Why is this insecure?"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

EXPECTED: "Exposes password, is_staff, internal fields"
INSTANT REJECT IF: "It's fine"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q8: "Should password be write_only or read_only?"

EXPECTED: "write_only - accept in requests, never return in responses"
INSTANT REJECT IF: "read_only"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SCORING:
────────
7-8 correct: PASS
5-6 correct: BORDERLINE
<5 correct: FAIL - fundamental gaps
"""


# ═══════════════════════════════════════════════════════════════════════
# ROUND 4: PERFORMANCE OPTIMIZATION
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEWER:
"This endpoint is slow. 500ms response time with 200 users in database.
Optimize it."
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

# ❌ SLOW CODE
class SlowUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    
    def list(self, request):
        users = User.objects.all()
        data = []
        for user in users:
            data.append({
                'id': user.id,
                'username': user.username,
                'post_count': user.blogpost_set.count(),  # ❌ Query for each user!
                'last_post_title': user.blogpost_set.order_by('-created_at').first().title if user.blogpost_set.exists() else None,  # ❌ More queries!
            })
        return Response(data)


"""
PROBLEMS:
1. Manual serialization (not using serializer)
2. N+1 query for post_count
3. N+1 query for last post
4. No pagination

✅ OPTIMIZED VERSION:
"""

from django.db.models import Count, Prefetch

class OptimizedUserSerializer(serializers.ModelSerializer):
    post_count = serializers.IntegerField(read_only=True)
    last_post_title = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'username', 'post_count', 'last_post_title']
    
    def get_last_post_title(self, obj):
        # Access prefetched data
        if hasattr(obj, 'recent_posts') and obj.recent_posts:
            return obj.recent_posts[0].title
        return None


class OptimizedUserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ✅ OPTIMIZED: 3 queries total instead of 400+
    """
    serializer_class = OptimizedUserSerializer
    
    def get_queryset(self):
        # ✅ Single query with JOIN for count
        # ✅ Single query for recent posts (prefetch)
        return User.objects.annotate(
            post_count=Count('blogpost')
        ).prefetch_related(
            Prefetch(
                'blogpost_set',
                queryset=BlogPost.objects.order_by('-created_at')[:1],
                to_attr='recent_posts'
            )
        )


"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EXPECTED EXPLANATION:
─────────────────────

"The slow code has multiple N+1 query problems:
1. blogpost_set.count() runs a COUNT query for each user
2. blogpost_set.order_by/first() runs another query for each user
3. No pagination means fetching all 200 users

I'd optimize by:
1. Use annotate(Count('blogpost')) to get counts in one query via JOIN
2. Use prefetch_related with Prefetch object to get recent posts efficiently
3. Add pagination (DRF PageNumberPagination)

This reduces 400+ queries to about 3 queries regardless of user count."

SCORING:
────────
✅ Identifies N+1: PASS
✅ Uses annotate: STRONG
✅ Uses prefetch_related correctly: STRONG
✅ Mentions pagination: BONUS

REJECT IF:
❌ Doesn't identify N+1
❌ Suggests caching without fixing queries
❌ Doesn't know select_related/prefetch_related

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ═══════════════════════════════════════════════════════════════════════
# FINAL ASSESSMENT
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OVERALL SCORING MATRIX
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ROUND 1 (Code Review):
□ Found plain text password bug (CRITICAL)
□ Found permission bug (CRITICAL)
□ Found fields='__all__' bug
□ Found queryset filtering bug
□ Found write_only bug

ROUND 2 (API Design):
□ Proper models with relationships
□ Permission classes implemented
□ Filtering querysets by user
□ perform_create sets owner
□ Cart operations work

ROUND 3 (Rapid-Fire):
□ 7-8/8 correct

ROUND 4 (Performance):
□ Identified N+1 problem
□ Used select_related/prefetch_related/annotate

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FINAL VERDICT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INSTANT REJECT IF:
❌ Missed plain text password bug
❌ Missed permission bugs
❌ Doesn't understand N+1 queries
❌ Can't design basic CRUD API
❌ < 5/8 on rapid-fire

BORDERLINE IF:
⚠️ Found 3-4/5 bugs in code review
⚠️ API design missing permissions
⚠️ 5-6/8 on rapid-fire
⚠️ Identified N+1 but weak fix

STRONG HIRE IF:
✅ Found ALL critical security bugs
✅ Solid API design with permissions
✅ 7-8/8 on rapid-fire
✅ Strong N+1 optimization

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEWER FINAL THOUGHTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

IF REJECT:
"Candidate has gaps in fundamental DRF knowledge. Security issues missed.
Cannot optimize queries. Would create production bugs. NOT READY."

IF BORDERLINE:
"Solid fundamentals but some gaps. May need mentoring on security/performance.
Consider for junior-mid level. DISCUSS WITH TEAM."

IF STRONG HIRE:
"Excellent DRF knowledge. Security-conscious. Understands performance optimization.
Can debug production issues. Ready for senior backend role. RECOMMEND HIRE."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

HOW TO PREPARE:
───────────────

If you failed this mock interview:
1. Review files 01-04 in this folder
2. Build a complete CRUD API from scratch
3. Practice spotting security bugs
4. Master select_related/prefetch_related
5. Take this mock again in 1 week

You're not ready until you can:
- Find ALL security bugs in code review
- Design secure API without notes
- Optimize N+1 queries instantly
- Answer rapid-fire without hesitation

Django REST Framework is about SECURITY, PERFORMANCE, and CORRECTNESS.
Not just making endpoints work.

Master this or don't interview for backend roles.
"""
