"""
Django REST Framework Interview - Part 5
Topic: Mock Interview Round (Pressure Style)

Format per prompt:
- Question
- Interruption
- Follow-up trade-off push
- Strong answer target
- Reject trigger
"""

PROMPT 1
- Question
  Your API returns a list of orders with nested items. Why might this be
  slow, and what is your first fix?
- Interruption
  "Do not say caching. Explain the query pattern."
- Follow-up trade-off push
  "If you add prefetch_related, what risk do you introduce?"
- Strong answer target
  N+1 queries from nested serializers; use select_related/prefetch_related.
  Risk: large joins or memory use; must tune queryset and pagination.
- Reject trigger
  Blames DRF or suggests adding more servers without checking queries.

PROMPT 2
- Question
  You switched to AbstractBaseUser. Login works, but admin add-user fails.
  Why?
- Interruption
  "Give me the specific admin components you changed."
- Follow-up trade-off push
  "Would you still choose AbstractBaseUser for a small product?"
- Strong answer target
  Need custom UserAdmin, UserCreationForm, fieldsets, and a custom manager.
  For small products, AbstractUser is often lower risk unless requirements
  demand full control.
- Reject trigger
  Claims admin should just work without changes.

PROMPT 3
- Question
  Why does PATCH succeed but PUT fails for the same payload?
- Interruption
  "Do not talk about serializers generically. Tell me what partial=True does."
- Follow-up trade-off push
  "When should you reject PATCH even if partial=True?"
- Strong answer target
  PATCH with partial=True allows missing required fields. PUT expects full
  representation. Reject PATCH if it breaks invariants or cross-field rules.
- Reject trigger
  Says PUT and PATCH are identical in DRF.

PROMPT 4
- Question
  Your API returns 200 on create. Is that acceptable? Why or why not?
- Interruption
  "Give me the exact status code you expect."
- Follow-up trade-off push
  "What about asynchronous create?"
- Strong answer target
  Create should return 201 with the resource or 202 for async accepted.
  200 hides semantics and can break clients.
- Reject trigger
  "200 is fine for everything."

PROMPT 5
- Question
  A user can access another tenant's data. Permissions are set. What is the
  first place you look?
- Interruption
  "No theory. Name the method."
- Follow-up trade-off push
  "What if you use ViewSet actions?"
- Strong answer target
  Check get_queryset for tenant scoping and object-level permissions.
  Ensure custom actions also enforce the same filters.
- Reject trigger
  Assumes permissions alone prevent data leaks.

PROMPT 6
- Question
  You added a required field to User and migrations fail in prod. Fix?
- Interruption
  "Do not say 'just fake it'."
- Follow-up trade-off push
  "How do you backfill without downtime?"
- Strong answer target
  Two-step migration: add nullable, backfill via data migration or batch job,
  then enforce not null. Consider defaults and rollout order.
- Reject trigger
  Suggests faking migrations or manual DB edits only.

PROMPT 7
- Question
  Why would serializer.is_valid() behave differently for the same data?
- Interruption
  "Be precise. What parameters change the behavior?"
- Follow-up trade-off push
  "How do you make it deterministic across views?"
- Strong answer target
  Different serializer class, context, partial=True, or request.data parsing.
  Standardize serializer usage and context, and ensure consistent payloads.
- Reject trigger
  Says DRF is inconsistent or random.

PROMPT 8
- Question
  Versioning: URL vs header. Which do you choose and why?
- Interruption
  "Answer for a public API with external partners."
- Follow-up trade-off push
  "How does caching affect the choice?"
- Strong answer target
  URL versioning is explicit and cache-friendly; header versioning is cleaner
  but harder for clients and caches. For partners, URL versioning is safer.
- Reject trigger
  Says versioning is unnecessary.
