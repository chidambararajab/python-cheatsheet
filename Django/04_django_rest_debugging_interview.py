"""
Django REST Framework Interview - Part 4
Topic: Debugging and Failure Scenarios

Format per scenario:
1) Question
2) What is being tested
3) Ideal answer
4) Wrong answer
5) Reject reason
"""

SCENARIO 1 - Sudden 400 responses
1) Question
   The API started returning 400 for a POST that worked yesterday. No code
   changes. What do you check first and why?
2) What is being tested
   Root-cause reasoning under ambiguity.
3) Ideal answer
   Check request payload changes, content type, and serializer validation
   errors. Confirm if required fields or validators changed via migration or
   data constraints. Check for deployment of settings changes such as parser
   classes or stricter validation logic.
4) Wrong answer
   Restart the server; 400 means transient errors.
5) Reject reason
   Shows lack of diagnostics and reliance on superstition.

SCENARIO 2 - serializer.is_valid() behaves differently
1) Question
   serializer.is_valid() passes in one view but fails in another for the same
   input. Why?
2) What is being tested
   Understanding of context, partial updates, and differing serializers.
3) Ideal answer
   Differences can come from serializer class, context, partial=True, or
   different field requirements. Also check that data types are coerced
   differently when request.data is used versus manually built dicts.
4) Wrong answer
   is_valid is nondeterministic; DRF caches results.
5) Reject reason
   Shows poor understanding of serializer configuration and flow.

SCENARIO 3 - Adding a field broke migrations
1) Question
   You added a non-nullable field to a model and migrations fail on deploy.
   Why, and what is the safe fix?
2) What is being tested
   Migration planning and data backfill strategy.
3) Ideal answer
   Existing rows need a value; a non-nullable field requires a default or a
   multi-step migration: add nullable, backfill data, then enforce not null.
4) Wrong answer
   Mark the migration as applied without running it.
5) Reject reason
   Indicates unsafe migration practices and data integrity risk.

SCENARIO 4 - Endpoint slow under load
1) Question
   A list endpoint gets slow under load. How do you find the root cause?
2) What is being tested
   Performance debugging mindset and knowledge of common DRF pitfalls.
3) Ideal answer
   Inspect query counts, ORM query plans, and serializer behavior. Check for
   N+1 queries in nested serializers, missing select_related/prefetch_related,
   expensive SerializerMethodField, and lack of pagination.
4) Wrong answer
   Increase server workers; DRF is the bottleneck.
5) Reject reason
   Misses root-cause analysis and ignores database bottlenecks.

SCENARIO 5 - Permission leak
1) Question
   An endpoint is leaking data across tenants. The permission class is set.
   What went wrong?
2) What is being tested
   Ability to diagnose object-level permissions and queryset scoping.
3) Ideal answer
   Permission classes often only gate view access, not per-object filtering.
   The queryset must be scoped by tenant, and object-level permissions must be
   enforced in get_queryset or has_object_permission. Also verify actions in
   ViewSet that bypass expected checks.
4) Wrong answer
   If permission classes are set, data leaks cannot happen.
5) Reject reason
   Shows dangerous misunderstanding of access control in DRF.

SCENARIO 6 - Authentication fails intermittently
1) Question
   Token auth fails intermittently in production but works locally. Why?
2) What is being tested
   Ability to reason about environment differences and caching.
3) Ideal answer
   Look for multiple auth classes, caching inconsistencies, clock skew for
   expiring tokens, or load balancer issues. Check whether the same token is
   being stored in a different database or cache in prod.
4) Wrong answer
   DRF token auth is unreliable; switch to sessions.
5) Reject reason
   Avoids root cause and suggests random changes without evidence.

SCENARIO 7 - Unexpected 403 for admin user
1) Question
   An admin user gets 403 on an endpoint with IsAdminUser permission. Why?
2) What is being tested
   Understanding of user flags and custom user models.
3) Ideal answer
   IsAdminUser checks is_staff by default. If using a custom user model, the
   flag may not be set or stored differently. Also check authentication class
   and whether the request user is actually authenticated.
4) Wrong answer
   IsAdminUser checks superuser only, so staff should not pass.
5) Reject reason
   Indicates incorrect understanding of permission logic.
