"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 DJANGO CUSTOM USER MODEL - ELIMINATION INTERVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Interviewer: Senior Backend Engineer | Django Expert
Target: 3-7 YOE Backend Engineers
Focus: Custom User Implementation + Common Pitfalls
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ELIMINATION CRITERIA:
─────────────────────
• Doesn't set AUTH_USER_MODEL from start → REJECT
• Stores plain text passwords → INSTANT REJECT
• Can't explain AbstractUser vs AbstractBaseUser → REJECT
• Breaks migrations with late USER model change → REJECT
• Doesn't register User in admin → REJECT (production readiness)

This is THE MOST IMPORTANT topic for Django backend interviews.
Getting User model wrong destroys the entire application.
"""

# ═══════════════════════════════════════════════════════════════════════
# PART 2: CUSTOM USER MODEL (FULL PRODUCTION EXAMPLE)
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2.1 AbstractUser vs AbstractBaseUser - CRITICAL DECISION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEW QUESTION:
"You're starting a new Django project. Should you extend AbstractUser or
AbstractBaseUser? What's the difference and what breaks if you choose wrong?"

WHAT INTERVIEWER IS TESTING:
• Do you understand the User model inheritance hierarchy?
• Do you know when you need full control vs convenience?
• Can you explain the migration implications?
"""

# ─────────────────────────────────────────────────────────────────────
# OPTION 1: AbstractUser (RECOMMENDED for most projects)
# ─────────────────────────────────────────────────────────────────────

# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

class User(AbstractUser):
    """
    ✅ CORRECT: Extend AbstractUser to ADD fields
    
    AbstractUser provides:
    - username, password, email, first_name, last_name
    - is_staff, is_active, is_superuser
    - date_joined, last_login
    - groups, user_permissions
    - All authentication logic (password hashing, etc.)
    
    Use this when you want Django's default fields + your custom fields.
    """
    
    # Additional fields
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in format: '+999999999'"
            )
        ]
    )
    
    date_of_birth = models.DateField(null=True, blank=True)
    
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('N', 'Prefer not to say'),
    ]
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True
    )
    
    # Profile fields
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    
    # Business logic fields
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('vendor', 'Vendor'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='customer'
    )
    
    # Timestamp fields
    email_verified = models.BooleanField(default=False)
    email_verified_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-date_joined']
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['role']),
        ]
    
    def __str__(self):
        return self.email or self.username
    
    @property
    def full_name(self):
        """Get user's full name"""
        return f"{self.first_name} {self.last_name}".strip() or self.username
    
    def has_verified_email(self):
        """Check if user has verified their email"""
        return self.email_verified


# ─────────────────────────────────────────────────────────────────────
# OPTION 2: AbstractBaseUser (ONLY when you need FULL control)
# ─────────────────────────────────────────────────────────────────────

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    """
    ⚠️ WARNING: When using AbstractBaseUser, you MUST create custom manager
    
    Manager handles:
    - Creating regular users
    - Creating superusers
    - Password hashing
    """
    
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a regular user with email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # ✅ CRITICAL: Hash password
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and return a superuser with admin privileges.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    ⚠️ ADVANCED: Only use when you need complete control
    
    AbstractBaseUser provides ONLY:
    - password field
    - last_login field
    - is_active flag
    
    You must provide:
    - All other fields (email, name, etc.)
    - Custom Manager
    - USERNAME_FIELD setting
    - REQUIRED_FIELDS setting
    
    Use this when:
    - You want email-only login (no username)
    - You need radically different user structure
    - You understand the complexity trade-off
    """
    
    email = models.EmailField(
        'Email Address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.',
        }
    )
    full_name = models.CharField(max_length=150)
    
    is_staff = models.BooleanField(default=False)  # Must add manually
    is_active = models.BooleanField(default=True)  # Must add manually
    date_joined = models.DateTimeField(auto_now_add=True)  # Must add manually
    
    # Set the custom manager
    objects = CustomUserManager()
    
    # ✅ CRITICAL: Specify login field
    USERNAME_FIELD = 'email'  # Field used for login
    REQUIRED_FIELDS = ['full_name']  # Fields required when creating superuser
    
    class Meta:
        db_table = 'custom_users'
    
    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.full_name
    
    def get_short_name(self):
        return self.full_name.split()[0] if self.full_name else self.email


"""
🎤 IDEAL THINK-ALOUD EXPLANATION:
──────────────────────────────────

"Django provides two base classes for custom users:

AbstractUser is a COMPLETE user model with username, email, name fields, and all
authentication logic. You extend it to ADD fields. Use this 99% of the time. It
includes is_staff, is_active, groups, permissions - everything you need.

AbstractBaseUser is a MINIMAL base with only password and last_login. You must
build everything else yourself - create a custom manager, add is_staff, is_active,
define USERNAME_FIELD, etc. Only use this if you need radically different structure,
like email-only login with no username field.

Most projects should use AbstractUser. AbstractBaseUser is for when you understand
Django auth deeply and need full control. The maintenance cost is significantly
higher."

🚫 COMMON WRONG ANSWER:
"AbstractBaseUser is more flexible, so it's better."
→ REJECT: Doesn't understand complexity trade-off

❌ PRODUCTION FAILURE:
Junior dev uses AbstractBaseUser, forgets to add is_staff. Admin site breaks.
No one can access Django admin. Emergency fix during deployment window.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2.2 SETTINGS CONFIGURATION - DO THIS FIRST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEW QUESTION:
"When must you set AUTH_USER_MODEL? What breaks if you set it after
running migrations?"

WHAT INTERVIEWER IS TESTING:
• Do you understand Django initialization order?
• Do you know the migration disaster this causes?
• Have you experienced this failure in production?
"""

# settings.py

# ✅ CRITICAL: Set this BEFORE first migration
AUTH_USER_MODEL = 'accounts.User'  # format: 'app_label.ModelName'

# Other auth settings:
LOGIN_URL = '/api/auth/login/'
LOGIN_REDIRECT_URL = '/api/dashboard/'
LOGOUT_REDIRECT_URL = '/api/auth/login/'

# Password validation (important for security)
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 8}
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


"""
❌ CATASTROPHIC FAILURE SCENARIO:
──────────────────────────────────

Day 1: Create project, run migrations with default User model
Day 30: Realize you need custom fields, add AUTH_USER_MODEL
Result: MIGRATION HELL

What breaks:
1. ForeignKey(User) in other models points to wrong table
2. Django creates NEW users table, but data is in OLD table
3. All existing user references are broken
4. Authentication completely broken
5. Admin site crashes
6. Cannot create new migrations - circular dependencies

Fix requires:
- Data migration to copy old users to new table
- Update all ForeignKeys
- Manually fix migration dependencies
- High risk of data loss

This is why Django docs say: "Set AUTH_USER_MODEL before first migration"

🎤 CORRECT EXPLANATION:
"AUTH_USER_MODEL must be set before the first makemigrations command. Once Django
creates the auth tables with the default User model, changing AUTH_USER_MODEL
causes migration conflicts because existing ForeignKeys point to the old table.

You'd need complex data migrations to move data and update references. In production,
this means downtime and risk. The correct approach: decide on custom user model
BEFORE starting the project, set AUTH_USER_MODEL immediately, then run migrations."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2.3 SERIALIZERS FOR USER MODEL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEW QUESTION:
"Show me a UserSerializer. How do you handle password security? What fields
should be read-only? What about user registration vs profile update?"

WHAT INTERVIEWER IS TESTING:
• Do you use set_password() or store plain text?
• Do you expose password in API responses?
• Do you understand write_only and read_only?
"""

# accounts/serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    ✅ CORRECT: User registration with password hashing
    
    Key points:
    - password is write_only (never returned in response)
    - password2 for confirmation (not a model field)
    - Use set_password() to hash
    - Validate password strength
    """
    
    password = serializers.CharField(
        write_only=True,  # ✅ CRITICAL: Never return password
        required=True,
        validators=[validate_password],  # ✅ Use Django's validators
        style={'input_type': 'password'}
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )
    
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'password', 'password2',
            'first_name', 'last_name', 'phone_number', 'date_of_birth',
            'gender', 'role'
        ]
        read_only_fields = ['id']  # ✅ id is auto-generated
    
    def validate(self, attrs):
        """
        ✅ Validate passwords match
        """
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({
                "password": "Password fields didn't match."
            })
        return attrs
    
    def create(self, validated_data):
        """
        ✅ CRITICAL: Use set_password() to hash password
        ❌ NEVER DO: user.password = validated_data['password']
        """
        # Remove password2 (not a model field)
        validated_data.pop('password2')
        
        # Extract password
        password = validated_data.pop('password')
        
        # Create user without password first
        user = User.objects.create(**validated_data)
        
        # ✅ CRITICAL: Hash password properly
        user.set_password(password)  # This hashes the password
        user.save()
        
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    """
    ✅ CORRECT: Profile viewing (no password field)
    """
    
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'full_name', 'phone_number', 'date_of_birth', 'gender',
            'bio', 'avatar', 'role', 'email_verified', 'date_joined'
        ]
        read_only_fields = [
            'id', 'username', 'email', 'role', 'email_verified', 'date_joined'
        ]


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    """
    ✅ CORRECT: Profile updates (restricted fields)
    """
    
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'phone_number',
            'date_of_birth', 'gender', 'bio', 'avatar'
        ]
        # ❌ DON'T allow: username, email, role, password


class PasswordChangeSerializer(serializers.Serializer):
    """
    ✅ CORRECT: Separate serializer for password change
    """
    
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(
        required=True,
        write_only=True,
        validators=[validate_password]
    )
    new_password2 = serializers.CharField(required=True, write_only=True)
    
    def validate_old_password(self, value):
        """Verify old password is correct"""
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is incorrect")
        return value
    
    def validate(self, attrs):
        """Verify new passwords match"""
        if attrs['new_password'] != attrs['new_password2']:
            raise serializers.ValidationError({
                "new_password": "Password fields didn't match."
            })
        return attrs
    
    def save(self):
        """Update password"""
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user


# ❌ WRONG: Insecure serializer
class WrongUserSerializer(serializers.ModelSerializer):
    """
    ❌ SECURITY DISASTER - Multiple failures
    """
    password = serializers.CharField()  # ❌ NO write_only!
    
    class Meta:
        model = User
        fields = '__all__'  # ❌ EXPOSES EVERYTHING
    
    def create(self, validated_data):
        # ❌ DISASTER: Plain text password!
        user = User.objects.create(**validated_data)
        return user  # Password stored in plain text!


"""
🎤 IDEAL THINK-ALOUD EXPLANATION:
──────────────────────────────────

"For user registration, password must be write_only so it's never returned in API
responses. I use Django's validate_password to enforce strength requirements.

In create(), I MUST use set_password() to hash the password. NEVER assign password
directly - that stores plain text, which is a critical security vulnerability.

For profile updates, I use a separate serializer without password. Password changes
are a separate endpoint with old_password verification. This follows least privilege
principle.

I never use fields='__all__' - that exposes internal fields like is_staff, is_superuser,
which could lead to privilege escalation."

🚫 COMMON WRONG ANSWER:
"Just use ModelSerializer with all fields."
→ INSTANT REJECT: Massive security hole

❌ PRODUCTION FAILURE:
Serializer doesn't use write_only on password. GET /api/users/ returns hashed
passwords in response. Security audit fails. Company faces regulatory penalties.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2.4 VIEWS FOR USER OPERATIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

# accounts/views.py

from rest_framework import generics, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response


class UserRegistrationView(generics.CreateAPIView):
    """
    ✅ CORRECT: Public registration endpoint
    POST /api/auth/register/
    """
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]  # ✅ Public endpoint
    
    def create(self, request, *args, **kwargs):
        """
        Handle user registration with proper response
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Save triggers create() which hashes password
        user = serializer.save()
        
        # Send verification email (side effect in view, not serializer)
        from .tasks import send_verification_email
        send_verification_email.delay(user.id)
        
        return Response(
            {
                'user': UserProfileSerializer(user).data,
                'message': 'User created successfully. Please verify your email.'
            },
            status=status.HTTP_201_CREATED
        )


class UserProfileView(generics.RetrieveUpdateAPIView):
    """
    ✅ CORRECT: User profile operations
    GET/PATCH /api/auth/profile/
    """
    serializer_class = UserProfileUpdateSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        """Return current user"""
        return self.request.user
    
    def get_serializer_class(self):
        """Use different serializer for GET vs PATCH"""
        if self.request.method == 'GET':
            return UserProfileSerializer
        return UserProfileUpdateSerializer


class PasswordChangeView(generics.UpdateAPIView):
    """
    ✅ CORRECT: Password change endpoint
    POST /api/auth/change-password/
    """
    serializer_class = PasswordChangeSerializer
    permission_classes = [IsAuthenticated]
    
    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({
            'message': 'Password updated successfully'
        }, status=status.HTTP_200_OK)


"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2.5 ADMIN REGISTRATION (PRODUCTION REQUIREMENT)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEW QUESTION:
"Show me how you register your custom User in Django admin."

WHAT INTERVIEWER IS TESTING:
• Do you know admin is not automatic for custom User?
• Do you use UserAdmin for proper password handling?
• Production readiness awareness
"""

# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _


class CustomUserAdmin(BaseUserAdmin):
    """
    ✅ CORRECT: Extend UserAdmin for custom fields
    
    If you don't register admin, you can't manage users in admin panel!
    If you use regular admin.ModelAdmin, password handling breaks!
    """
    
    # Display in user list
    list_display = [
        'email', 'username', 'first_name', 'last_name',
        'role', 'is_staff', 'is_active', 'date_joined'
    ]
    list_filter = ['is_staff', 'is_active', 'role', 'gender']
    search_fields = ['email', 'username', 'first_name', 'last_name']
    ordering = ['-date_joined']
    
    # ✅ CRITICAL: Include custom fields in fieldsets
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal Info'), {
            'fields': (
                'first_name', 'last_name', 'email', 'phone_number',
                'date_of_birth', 'gender', 'bio', 'avatar'
            )
        }),
        (_('Business'), {'fields': ('role',)}),
        (_('Permissions'), {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        (_('Important Dates'), {
            'fields': ('last_login', 'date_joined', 'email_verified_at')
        }),
    )
    
    # Fields when creating user in admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'email', 'password1', 'password2',
                'first_name', 'last_name', 'role', 'is_staff', 'is_active'
            ),
        }),
    )


# ✅ CRITICAL: Register with custom admin
admin.site.register(User, CustomUserAdmin)


"""
❌ COMMON MISTAKES:
───────────────────

1. Not registering at all:
   → Admin panel shows no User model
   → Cannot create users via admin
   → Cannot debug user issues

2. Using plain ModelAdmin:
   admin.site.register(User)  # ❌ WRONG
   → Password stored in plain text!
   → No password validation
   → Security disaster

3. Not including custom fields in fieldsets:
   → Fields not editable in admin
   → Support team can't help users
   → Production debugging harder

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ═══════════════════════════════════════════════════════════════════════
# RAPID-FIRE ELIMINATION QUESTIONS
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RAPID-FIRE (30 seconds per question - INSTANT REJECT on wrong answer)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q1: "Should you extend AbstractUser or AbstractBaseUser?"
EXPECTED: "AbstractUser - unless you need full control"
REJECT IF: "AbstractBaseUser is better"

Q2: "When do you set AUTH_USER_MODEL?"
EXPECTED: "Before first migration - Day 1"
INSTANT REJECT IF: "Anytime" or "When needed"

Q3: "How do you store passwords in serializer create()?"
EXPECTED: "user.set_password(password)"
INSTANT REJECT IF: "user.password = password" or doesn't know

Q4: "Should password field be write_only?"
EXPECTED: "Yes - ALWAYS"
INSTANT REJECT IF: "No" or hesitates

Q5: "Do you need to register custom User in admin?"
EXPECTED: "Yes - with UserAdmin subclass"
REJECT IF: "It's automatic"

Q6: "What breaks if you change AUTH_USER_MODEL after migrations?"
EXPECTED: "ForeignKeys break, migration hell, data loss"
REJECT IF: "Nothing" or "Just run migrations again"

Q7: "Should you use fields='__all__' in UserSerializer?"
EXPECTED: "No - exposes sensitive fields"
INSTANT REJECT IF: "Yes"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ═══════════════════════════════════════════════════════════════════════
# SELF-ASSESSMENT
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CRITICAL (Must answer YES to ALL - one NO = FAIL):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

□ Know to set AUTH_USER_MODEL before first migration
□ Use AbstractUser (not AbstractBaseUser) for most projects
□ ALWAYS use set_password() - NEVER store plain text
□ Make password field write_only in serializers
□ Never use fields='__all__' in User serializers
□ Register User in admin with UserAdmin subclass
□ Use separate serializers for registration vs profile update
□ Validate password strength with Django validators

SCORING:
< 8/8: INSTANT FAIL - Critical security/architecture gaps
8/8: PASS - Safe to work on production user systems

INTERVIEWER CONCLUSION:

IF FAIL:
"Candidate would create massive security vulnerabilities or migration disasters.
Plain text passwords, broken migrations, insecure serializers. Cannot trust with
user authentication. INSTANT REJECT."

IF PASS:
"Understands Django User model at production level. Knows security best practices.
Understands migration timing. Can safely implement authentication. PROCEED."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BOTTOM LINE:
Custom User model is the FOUNDATION of any Django project. Get it wrong and
you've broken authentication, security, and database integrity. This is where
1 mistake = entire project failure.

If you don't know set_password(), you shouldn't touch production Django.
If you change AUTH_USER_MODEL late, prepare for migration hell.
If you expose passwords in API, expect security breach.

Master this file or don't claim Django expertise.
"""
