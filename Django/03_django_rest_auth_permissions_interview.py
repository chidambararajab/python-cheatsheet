"""
Django REST Framework Interview - Part 3
Topic: Core DRF Design and Behavior

Format per topic:
1) Question
2) What is being tested
3) Ideal answer
4) Wrong answer
5) Reject reason
"""

TOPIC 1 - Serializer validation flow
1) Question
   Explain the full serializer validation flow, including field-level and
   object-level validation, and where errors are collected.
2) What is being tested
   Deep knowledge of serializer internals and error handling.
3) Ideal answer
   DRF runs field validation, then validate_<field> methods, then the general
   validate() for cross-field checks. Errors are collected per field and for
   non-field errors. is_valid must be called before accessing validated_data.
4) Wrong answer
   validate() always runs first, then field validators run.
5) Reject reason
   Indicates no real understanding of validation order and error reporting.

TOPIC 2 - create() vs update()
1) Question
   When does DRF call create() vs update(), and what must each return?
2) What is being tested
   Whether the candidate understands serializer save semantics.
3) Ideal answer
   create() is called for new instances; update() for existing instances
   passed as serializer instance. Both must return the model instance.
4) Wrong answer
   create() returns dict data, update() returns True/False.
5) Reject reason
   Demonstrates shallow serializer knowledge and likely runtime errors.

TOPIC 3 - Partial updates (PUT vs PATCH)
1) Question
   How do PUT and PATCH differ in DRF, and what does partial=True change?
2) What is being tested
   Correct HTTP semantics and serializer behavior.
3) Ideal answer
   PUT is a full replacement, PATCH is partial. In DRF, partial=True allows
   missing required fields and only validates provided fields. You should
   still enforce invariants in validate().
4) Wrong answer
   PATCH is just a smaller PUT and should overwrite missing fields to None.
5) Reject reason
   Shows incorrect HTTP semantics and risk of data loss.

TOPIC 4 - Nested serializers and performance
1) Question
   Your list endpoint uses nested serializers and is slow. What is happening
   and how do you fix it without changing the API?
2) What is being tested
   Awareness of N+1 queries and ORM optimization in DRF serialization.
3) Ideal answer
   Nested serializers can trigger N+1 queries. Fix with select_related and
   prefetch_related, or custom querysets in the view. Use SerializerMethodField
   carefully and avoid per-instance queries.
4) Wrong answer
   DRF caches nested serializers so performance is not an issue.
5) Reject reason
   Demonstrates lack of production performance awareness.

TOPIC 5 - Authentication vs permission vs throttling
1) Question
   Distinguish authentication, permission, and throttling in DRF with an
   example of each.
2) What is being tested
   Separation of security concerns.
3) Ideal answer
   Authentication identifies the user, permission checks access rights, and
   throttling limits request rates. Example: token auth for identity, IsAdminUser
   for access control, and UserRateThrottle for abuse prevention.
4) Wrong answer
   Permissions are only for rate limits; authentication is enough for access.
5) Reject reason
   Confuses critical security layers and indicates weak access control design.

TOPIC 6 - Pagination and filtering trade-offs
1) Question
   When would you avoid pagination, and what are the trade-offs of cursor
   pagination versus offset pagination?
2) What is being tested
   Knowledge of scalability and consistency trade-offs.
3) Ideal answer
   Avoid pagination only for small bounded datasets. Cursor pagination is
   stable under inserts/deletes and better for large datasets but less
   flexible for random access. Offset pagination is simpler but can skip or
   duplicate items under concurrent writes and becomes slow on large offsets.
4) Wrong answer
   Offset pagination is always correct and fast; cursor is unnecessary.
5) Reject reason
   Shows lack of scaling awareness and inconsistent data delivery risks.

TOPIC 7 - Status code correctness
1) Question
   Give correct status codes for create, update, validation errors, and auth
   failures in DRF.
2) What is being tested
   Correct HTTP semantics for API design.
3) Ideal answer
   Create: 201, update: 200 or 204, validation error: 400, auth failure:
   401 for unauthenticated, 403 for authenticated but forbidden.
4) Wrong answer
   Use 200 for everything to keep the API simple.
5) Reject reason
   Indicates low quality API design and interoperability problems.

TOPIC 8 - Versioning strategies
1) Question
   Compare URL, header, and accept-header versioning. When do you choose each?
2) What is being tested
   Ability to reason about API evolution and client compatibility.
3) Ideal answer
   URL versioning is explicit and easy for clients and caching. Header-based
   versioning keeps URLs stable but is harder to debug and cache. Accept-header
   versioning is content negotiation aligned but requires client sophistication.
   Choose based on client constraints and tooling.
4) Wrong answer
   Versioning is unnecessary if you keep backward compatibility forever.
5) Reject reason
   Shows lack of experience with real API lifecycle management.
