"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 DJANGO REST AUTH & PERMISSIONS - ELIMINATION INTERVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Interviewer: Senior Backend Engineer | Security Expert
Target: 3-7 YOE Backend Engineers
Focus: Authentication, Permissions, Throttling, Security
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ELIMINATION CRITERIA:
─────────────────────
• Confuses authentication with authorization → REJECT
• Doesn't understand permission evaluation order → REJECT
• Creates data leakage via permissions → REJECT
• Can't explain token vs session auth → REJECT
• Doesn't implement rate limiting → REJECT (production readiness)

Security failures = instant rejection. This is non-negotiable.
"""

# ═══════════════════════════════════════════════════════════════════════
# PART 3: AUTHENTICATION, PERMISSIONS, THROTTLING
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3.1 AUTHENTICATION vs AUTHORIZATION (CRITICAL DISTINCTION)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEW QUESTION:
"Explain authentication vs authorization. When does each run? Can you have
one without the other?"

WHAT INTERVIEWER IS TESTING:
• Do you understand the security model?
• Do you know the execution order?
• Can you explain real-world scenarios?
"""

"""
🎤 IDEAL EXPLANATION:
─────────────────────

AUTHENTICATION = WHO are you?
- Identifies the user
- Runs FIRST
- Sets request.user
- Can succeed with AnonymousUser
- Examples: Token, Session, JWT, OAuth

AUTHORIZATION (Permissions) = WHAT can you do?
- Determines access rights
- Runs AFTER authentication
- Uses request.user to decide
- Can deny authenticated users
- Examples: IsAuthenticated, IsOwner, IsAdmin

EXECUTION FLOW:
1. Request arrives
2. Authentication classes run → set request.user
3. Permission classes run → check request.user
4. If all pass → view executes
5. If any fail → 401 (auth) or 403 (permission)

You can have:
- Auth without permissions: Public API with user tracking
- Permissions without auth: Anonymous users can READ, authenticated can WRITE
- Both: Most secure endpoints
- Neither: Completely public

STATUS CODES:
- 401 Unauthorized: Authentication failed (who are you?)
- 403 Forbidden: Permission denied (you can't do this)
"""

from rest_framework import permissions, authentication, status
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.views import APIView


"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3.2 AUTHENTICATION CLASSES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEW QUESTION:
"Compare TokenAuthentication, SessionAuthentication, and JWT. When would
you use each? What are the trade-offs?"
"""

# ─────────────────────────────────────────────────────────────────────
# OPTION 1: Token Authentication (DRF built-in)
# ─────────────────────────────────────────────────────────────────────

from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginView(APIView):
    """
    ✅ Token Authentication Pattern
    
    POST /api/auth/login/
    {
        "username": "user@example.com",
        "password": "password123"
    }
    
    Response:
    {
        "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b",
        "user_id": 1,
        "username": "user@example.com"
    }
    
    Usage:
    Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
    """
    permission_classes = []  # Public endpoint
    
    def post(self, request):
        from django.contrib.auth import authenticate
        
        username = request.data.get('username')
        password = request.data.get('password')
        
        # Authenticate
        user = authenticate(username=username, password=password)
        
        if user is None:
            return Response(
                {'error': 'Invalid credentials'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        # Get or create token
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            'token': token.key,
            'user_id': user.id,
            'username': user.username
        })


class ProtectedTokenView(APIView):
    """
    ✅ Using Token Authentication
    
    GET /api/protected/
    Headers: Authorization: Token <token>
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        return Response({
            'message': f'Hello, {request.user.username}',
            'user_id': request.user.id
        })


"""
TOKEN AUTHENTICATION PROS/CONS:
────────────────────────────────

✅ PROS:
- Simple to implement
- Stateless (token stored client-side)
- Works across domains (CORS-friendly)
- Single token per user (can be revoked)
- No cookie issues

❌ CONS:
- Token never expires (security risk)
- Requires database lookup on every request (performance)
- If token stolen, valid until manually revoked
- No refresh mechanism
- Token visible in headers (HTTPS required)

USE WHEN:
- Mobile apps
- Simple APIs
- Single-page apps
- Quick prototypes
"""


# ─────────────────────────────────────────────────────────────────────
# OPTION 2: JWT (JSON Web Token)
# ─────────────────────────────────────────────────────────────────────

"""
⚠️ Requires: pip install djangorestframework-simplejwt

settings.py:
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}
"""

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    ✅ Custom JWT with extra claims
    """
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['role'] = user.role  # Custom field
        
        return token


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    POST /api/auth/token/
    {
        "username": "user@example.com",
        "password": "password123"
    }
    
    Response:
    {
        "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
    }
    
    Usage:
    Authorization: Bearer <access_token>
    """
    serializer_class = CustomTokenObtainPairSerializer


"""
JWT PROS/CONS:
──────────────

✅ PROS:
- No database lookup (stateless - token contains data)
- Auto-expires (security)
- Refresh token mechanism
- Can include custom claims
- Scalable (no server-side storage)

❌ CONS:
- Cannot revoke before expiry (unless using blacklist)
- Larger payload (sent with every request)
- Refresh token complexity
- Requires secure storage client-side
- Clock skew issues possible

USE WHEN:
- Microservices (no shared session store)
- High-scale APIs
- Need stateless auth
- Mobile/SPA with token refresh
"""


# ─────────────────────────────────────────────────────────────────────
# OPTION 3: Session Authentication
# ─────────────────────────────────────────────────────────────────────

class SessionLoginView(APIView):
    """
    ✅ Session Authentication (Django built-in)
    
    POST /api/auth/session-login/
    
    Sets session cookie (sessionid)
    
    USE WHEN:
    - Traditional web app
    - Same domain (frontend + backend)
    - Django templates + DRF API
    - Don't need mobile app support
    
    DON'T USE:
    - Mobile apps (cookies problematic)
    - Cross-domain requests (CORS issues)
    - Stateless architecture
    """
    permission_classes = []
    
    def post(self, request):
        from django.contrib.auth import login, authenticate
        
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is None:
            return Response(
                {'error': 'Invalid credentials'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        # Creates session, sets cookie
        login(request, user)
        
        return Response({
            'message': 'Logged in successfully'
        })


"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3.3 PERMISSION CLASSES (CRITICAL)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEW QUESTION:
"Write a permission class that allows users to edit their own objects but
not others'. How do you prevent data leakage?"
"""

from rest_framework import permissions
from django.db import models


# ─────────────────────────────────────────────────────────────────────
# BUILT-IN PERMISSIONS (Know these)
# ─────────────────────────────────────────────────────────────────────

class BuiltInPermissionsExamples(APIView):
    """
    DRF Built-in Permissions:
    
    1. AllowAny - No restriction (default)
    2. IsAuthenticated - Must be logged in
    3. IsAdminUser - Must be staff user
    4. IsAuthenticatedOrReadOnly - Read public, write authenticated
    """
    
    # Example combinations:
    
    # Public read, authenticated write
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    # Only authenticated users
    # permission_classes = [permissions.IsAuthenticated]
    
    # Only admin users
    # permission_classes = [permissions.IsAdminUser]
    
    pass


# ─────────────────────────────────────────────────────────────────────
# CUSTOM PERMISSION: IsOwner
# ─────────────────────────────────────────────────────────────────────

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    ✅ CORRECT: Object-level permission
    
    - List/Create: Any authenticated user
    - Retrieve: Any authenticated user
    - Update/Delete: Only owner
    
    CRITICAL: Prevents user A from modifying user B's data
    """
    
    def has_permission(self, request, view):
        """
        View-level permission: Check before database query
        
        Called for:
        - list() - GET /api/posts/
        - create() - POST /api/posts/
        """
        # Allow all authenticated users to list/create
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        """
        Object-level permission: Check after object retrieved
        
        Called for:
        - retrieve() - GET /api/posts/{id}/
        - update() - PUT/PATCH /api/posts/{id}/
        - destroy() - DELETE /api/posts/{id}/
        
        ⚠️ CRITICAL: This is called AFTER get_object()
        ⚠️ If your queryset is not filtered, data leaks!
        """
        
        # Read permissions: anyone can read
        if request.method in permissions.SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True
        
        # Write permissions: only owner
        return obj.owner == request.user


# ─────────────────────────────────────────────────────────────────────
# MODEL + ViewSet USING IsOwnerOrReadOnly
# ─────────────────────────────────────────────────────────────────────

class Post(models.Model):
    """Example model with owner"""
    title = models.CharField(max_length=200)
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)


from rest_framework import viewsets, serializers

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'owner', 'created_at']


class PostViewSet(viewsets.ModelViewSet):
    """
    ✅ CORRECT: Secure ViewSet with permissions
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    
    def get_queryset(self):
        """
        ✅ CRITICAL: Filter queryset by user
        
        Without this, users can see all posts IDs even if they can't modify them.
        This prevents enumeration attacks and data leakage.
        """
        if self.action == 'list':
            # List only user's own posts
            return Post.objects.filter(owner=self.request.user)
        else:
            # For retrieve/update/delete, allow all (permission checks in has_object_permission)
            # Or filter here too for extra security
            return Post.objects.all()
    
    def perform_create(self, serializer):
        """
        ✅ CRITICAL: Set owner automatically
        Don't trust client to send owner field!
        """
        serializer.save(owner=self.request.user)


"""
❌ COMMON SECURITY FAILURE:
───────────────────────────

class WrongPostViewSet(viewsets.ModelViewSet):
    '''
    ❌ SECURITY DISASTER: No queryset filtering
    '''
    queryset = Post.objects.all()  # ❌ Shows ALL posts!
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    # ❌ Problem: User can GET /api/posts/ and see all post IDs
    # ❌ Even if they can't modify them, data leak!
    # ❌ Enumeration attack possible


ATTACK SCENARIO:
Attacker iterates: GET /api/posts/1/, GET /api/posts/2/, ...
Even with IsOwnerOrReadOnly, they can retrieve and READ all posts.
Only WRITE is protected, but READ leaks everything!

FIX: Filter queryset in get_queryset() + use has_object_permission()
"""


# ─────────────────────────────────────────────────────────────────────
# PERMISSION: Role-based
# ─────────────────────────────────────────────────────────────────────

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    ✅ CORRECT: Role-based permission
    
    - Read: Anyone
    - Write: Only admins (user.role == 'admin')
    """
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Check custom role field
        return (
            request.user and
            request.user.is_authenticated and
            request.user.role == 'admin'
        )


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    ✅ CORRECT: Combined permission
    Owner OR Admin can modify
    """
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Owner can modify their own
        if obj.owner == request.user:
            return True
        
        # Admin can modify anything
        if request.user.role == 'admin':
            return True
        
        return False


"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3.4 THROTTLING (RATE LIMITING)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEW QUESTION:
"How do you prevent API abuse? Show me rate limiting implementation."

WHAT INTERVIEWER IS TESTING:
• Production readiness
• Security awareness
• DDoS protection understanding
"""

from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


# settings.py configuration:
"""
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',    # Anonymous users: 100 requests per day
        'user': '1000/day',   # Authenticated: 1000 per day
        'burst': '10/minute', # Burst protection
        'login': '5/hour',    # Login attempts
    }
}
"""


class LoginThrottle(UserRateThrottle):
    """
    ✅ CRITICAL: Prevent brute-force login attacks
    """
    rate = '5/hour'  # 5 login attempts per hour


class LoginViewWithThrottle(APIView):
    """
    ✅ CORRECT: Rate-limited login endpoint
    
    Prevents:
    - Brute force password attacks
    - Credential stuffing
    - Account enumeration
    """
    throttle_classes = [LoginThrottle]
    permission_classes = []
    
    def post(self, request):
        # Login logic
        pass


class CustomRateThrottle(UserRateThrottle):
    """
    ✅ Custom throttle for expensive operations
    """
    rate = '10/minute'


class ExpensiveOperationView(APIView):
    """
    ✅ CORRECT: Throttle expensive operations separately
    
    Example: PDF generation, report exports, bulk operations
    """
    throttle_classes = [CustomRateThrottle]
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        # Expensive operation
        return Response({'status': 'processing'})


"""
THROTTLING BEST PRACTICES:
──────────────────────────

1. Different rates for different endpoints:
   - Login: 5/hour (prevent brute force)
   - Read APIs: 1000/day (generous)
   - Write APIs: 100/day (more restrictive)
   - Expensive ops: 10/minute (very restrictive)

2. Anonymous vs Authenticated:
   - Anonymous: Stricter limits
   - Authenticated: More generous
   - Premium users: Even higher limits

3. Production considerations:
   - Use Redis for distributed throttling
   - Monitor throttle hits (indicates abuse or UX issue)
   - Provide clear error messages (rate limit info)
   - Consider IP-based throttling for public endpoints

❌ PRODUCTION FAILURE:
No rate limiting on login endpoint. Attacker brute-forces passwords.
10,000 login attempts per minute. Database overload. Site down.
"""


"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3.5 COMBINING AUTH + PERMISSIONS + THROTTLING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

class SecureProductionViewSet(viewsets.ModelViewSet):
    """
    ✅ PRODUCTION-READY: All security layers
    
    1. Authentication: JWT tokens
    2. Permissions: IsAuthenticated + IsOwner
    3. Throttling: Rate limiting
    4. Queryset filtering: Data isolation
    """
    serializer_class = PostSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    throttle_classes = [UserRateThrottle]
    
    def get_queryset(self):
        """Filter data by user"""
        return Post.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        """Set owner automatically"""
        serializer.save(owner=self.request.user)
    
    def get_throttles(self):
        """Different throttles per action"""
        if self.action == 'create':
            # More restrictive for create
            return [CustomRateThrottle()]
        return super().get_throttles()


# ═══════════════════════════════════════════════════════════════════════
# RAPID-FIRE ELIMINATION QUESTIONS
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RAPID-FIRE (30 seconds per question)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q1: "Authentication vs authorization - which runs first?"
EXPECTED: "Authentication sets user, then authorization checks access"
REJECT IF: Confuses them

Q2: "401 vs 403 - when do you use each?"
EXPECTED: "401: auth failed (who?), 403: permission denied (what?)"
REJECT IF: Doesn't know

Q3: "JWT vs Token - which requires database lookup?"
EXPECTED: "Token does, JWT doesn't (stateless)"
REJECT IF: Wrong answer

Q4: "has_permission vs has_object_permission - when does each run?"
EXPECTED: "has_permission before query, has_object_permission after get_object()"
REJECT IF: Doesn't know

Q5: "User can GET /api/posts/ and see all IDs. Permission is IsOwner. Problem?"
EXPECTED: "Must filter queryset in get_queryset() - data leak!"
INSTANT REJECT IF: "Permission is enough"

Q6: "Why rate limit login endpoints?"
EXPECTED: "Prevent brute force attacks"
REJECT IF: Doesn't know

Q7: "Should perform_create() trust client's owner field?"
EXPECTED: "NO - always set owner=request.user"
INSTANT REJECT IF: "Yes"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ═══════════════════════════════════════════════════════════════════════
# SELF-ASSESSMENT
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CRITICAL (Must answer YES to ALL):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

□ Distinguish authentication from authorization
□ Know 401 vs 403 status codes
□ Understand JWT vs Token trade-offs
□ Filter querysets in get_queryset() to prevent data leaks
□ Never trust client to set owner field
□ Use has_object_permission for object-level checks
□ Implement rate limiting on sensitive endpoints
□ Know permission evaluation order

SCORING:
< 8/8: FAIL - Security vulnerabilities, data leaks
8/8: PASS - Can implement secure APIs

INTERVIEWER CONCLUSION:

IF FAIL:
"Candidate would create security holes. Data leaks via unfiltered querysets.
No rate limiting. Trusts client data. Cannot deploy to production. REJECT."

IF PASS:
"Understands DRF security model. Implements defense in depth. Filters data,
validates permissions, implements throttling. Production-ready. PROCEED."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BOTTOM LINE:
Security is non-negotiable. One unfiltered queryset = data leak to all users.
One missing rate limit = DDoS vulnerability. One wrong permission = privilege escalation.

If you don't filter querysets, you're exposing data.
If you don't implement throttling, you're begging to be attacked.
If you confuse authentication with authorization, you don't understand security.

Master this file or don't build production APIs.
"""
