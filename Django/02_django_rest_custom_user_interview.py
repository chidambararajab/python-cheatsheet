"""
Django REST Framework Interview - Part 2
Topic: Custom User Model and Authentication (Elimination Zone)

Format per scenario:
1) Question
2) What is being tested
3) Ideal answer
4) Wrong answer
5) Reject reason
"""

SCENARIO 1 - AbstractUser vs AbstractBaseUser
1) Question
   You need email login, a required phone number, and role flags. Do you use
   AbstractUser or AbstractBaseUser, and why?
2) What is being tested
   Trade-off reasoning between built-in fields/admin support and full control.
3) Ideal answer
   AbstractUser if the default fields are acceptable and you only need to add
   a few fields. AbstractBaseUser if you need to change the identifier or
   remove username entirely. Email-as-username is doable in both, but with
   AbstractBaseUser you must implement USERNAME_FIELD, REQUIRED_FIELDS, and
   a custom manager, plus admin integration.
4) Wrong answer
   Always use AbstractBaseUser because it is more flexible and future-proof.
5) Reject reason
   Shows lack of understanding of implementation cost and admin integration.

SCENARIO 2 - What breaks if done late?
1) Question
   You already shipped using the default User model. The team now wants a
   custom user model. What breaks if done late?
2) What is being tested
   Awareness of migration constraints and foreign key dependencies.
3) Ideal answer
   Swapping the user model after migrations exist is painful: foreign keys
   point to auth.User, swappable dependencies can mismatch, and existing
   migrations hardcode model references. You can face data migration, auth
   app migration conflicts, and third-party apps assuming auth.User. The
   safe answer is: do it early or plan a careful migration and dependency
   graph with data transfer and downtime.
4) Wrong answer
   Just change AUTH_USER_MODEL and run migrations; Django handles it.
5) Reject reason
   Signals dangerous oversimplification and lack of production risk awareness.

SCENARIO 3 - AUTH_USER_MODEL safety
1) Question
   Where do you set AUTH_USER_MODEL and what mistakes cause runtime errors?
2) What is being tested
   Proper settings placement and avoiding circular import and migration traps.
3) Ideal answer
   Set AUTH_USER_MODEL in settings before the first migration. Use string
   label "app_label.ModelName". Avoid importing the model in settings. Ensure
   apps that reference the user model use get_user_model or settings.AUTH_USER_MODEL.
4) Wrong answer
   Set AUTH_USER_MODEL in the app config or import the model directly.
5) Reject reason
   Shows the candidate does not understand app loading and migration order.

SCENARIO 4 - Migration ordering and failure
1) Question
   You added a non-nullable field to the custom user model and migrations fail
   in production. What happened and how do you fix it?
2) What is being tested
   Ability to reason about migration data defaults and deployment safety.
3) Ideal answer
   Existing rows do not have a value for the new non-nullable field. You must
   provide a default or a two-step migration: add nullable, backfill, then
   make it non-nullable. For sensitive data, use a data migration.
4) Wrong answer
   Just fake the migration or set a default in code after deployment.
5) Reject reason
   Indicates risk of data inconsistency and unsafe deployment behavior.

SCENARIO 5 - Backward compatibility traps
1) Question
   A third-party app uses auth.User foreign keys. How do you keep it working
   with a custom user model?
2) What is being tested
   Awareness of swappable model patterns and dependency scanning.
3) Ideal answer
   Use swappable model references where supported. For apps that hardcode
   auth.User, you may need a fork or adapter model. Review migrations for
   foreign keys, use settings.AUTH_USER_MODEL in your own apps, and validate
   the third-party dependencies before switching.
4) Wrong answer
   It will work because Django aliases auth.User automatically.
5) Reject reason
   Shows lack of practical integration experience and release risk.

SCENARIO 6 - Admin integration
1) Question
   You built a custom user model and the admin add/change pages break. Why?
2) What is being tested
   Understanding of ModelAdmin and UserCreationForm requirements.
3) Ideal answer
   The default UserAdmin expects username and specific fields. With custom
   user models you must provide custom forms, fieldsets, add_fieldsets, and
   set appropriate list_display. You also need a custom manager that supports
   create_user and create_superuser.
4) Wrong answer
   Admin should work automatically; no changes needed.
5) Reject reason
   Shows inability to integrate core Django components.

SCENARIO 7 - Password handling and security
1) Question
   How should you handle password storage and updates in a custom user model?
2) What is being tested
   Security awareness and correct use of Django hashing utilities.
3) Ideal answer
   Never store raw passwords. Use set_password and check_password, keep
   write-only fields in serializers, and enforce update flows that rehash.
   In DRF, validate password complexity in serializer and avoid returning
   hashes in responses.
4) Wrong answer
   Store a hashed password manually in a custom field for flexibility.
5) Reject reason
   Security risk and violation of Django's authentication framework.

SCENARIO 8 - Scaling and future changes
1) Question
   You need to add organization membership and role-based access later. How
   should the user model be designed today to avoid schema pain?
2) What is being tested
   Ability to model relationships and avoid bloating the user table.
3) Ideal answer
   Keep the user model minimal. Model roles and org membership in related
   tables and use through models for many-to-many with metadata. This keeps
   the user model stable and migrations manageable.
4) Wrong answer
   Put all role and org fields directly on the user for simplicity.
5) Reject reason
   Shows poor data modeling and scaling awareness.
