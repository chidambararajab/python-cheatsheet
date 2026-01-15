"""
Django REST Framework Interview - Part 1
Topic: Django vs DRF Responsibility Boundaries

Format per topic:
1) Interview question
2) What the interviewer is testing
3) Ideal think-aloud answer
4) Common wrong answer
5) Why it causes rejection
"""

TOPIC 1 - Request/response lifecycle (Django vs DRF)
1) Interview question
   Walk me through the request/response lifecycle for a JSON API in Django
   with DRF enabled. Where does Django stop and DRF start?
2) What the interviewer is testing
   Whether the candidate can cleanly separate WSGI/Django middleware stack
   from DRF's request parsing, content negotiation, and response rendering.
3) Ideal think-aloud answer
   Django receives the request, runs URL routing and middleware. DRF wraps the
   Django HttpRequest into a DRF Request at the view layer. DRF then performs
   authentication, throttling, and permission checks, parses the body via
   parsers, then calls the view method. After the view returns data, DRF
   handles content negotiation and renders to Response, which becomes a Django
   HttpResponse that passes back through middleware.
4) Common wrong answer
   DRF handles the request lifecycle end-to-end, including middleware and URL
   routing, and Django only renders templates.
5) Why it causes rejection
   Confuses core Django request handling with DRF extensions, showing a weak
   mental model that breaks down in debugging and performance analysis.

TOPIC 2 - Middleware vs authentication classes
1) Interview question
   When do you implement authentication in Django middleware versus DRF
   authentication classes, and why?
2) What the interviewer is testing
   Understanding of separation of concerns and the difference between global
   request processing and per-view API auth.
3) Ideal think-aloud answer
   Django middleware runs for every request, before view resolution, and is
   best for cross-cutting concerns like session handling or request logging.
   DRF authentication classes run within the DRF view, after routing, and are
   designed to authenticate API requests with access to the DRF Request and
   the view context. For API auth, use DRF auth classes; use middleware only
   for truly global request processing not tied to API views.
4) Common wrong answer
   Use middleware for all auth because it is faster and more secure, and skip
   DRF auth classes entirely.
5) Why it causes rejection
   Shows poor grasp of DRF's pipeline and can lead to bypassed permissions or
   inconsistent auth behavior between API and non-API endpoints.

TOPIC 3 - Django views vs APIView vs ViewSet
1) Interview question
   Compare Django function-based views, Django class-based views, DRF APIView,
   and DRF ViewSet in terms of responsibilities and when you choose each.
2) What the interviewer is testing
   Ability to map abstraction levels to use cases and to avoid overusing
   ViewSets without understanding routing and action mapping.
3) Ideal think-aloud answer
   Django views are for general HTTP handling; CBVs add structure like mixins.
   DRF APIView adds parsing, auth, permission, and renderer support for APIs.
   ViewSets bundle related actions and work with routers for standard REST
   patterns. I choose ViewSet when I want consistent REST actions; APIView
   when I need custom method control or non-standard endpoints; Django views
   when DRF features are not needed.
4) Common wrong answer
   ViewSets are always better and should replace all views since they generate
   routes automatically.
5) Why it causes rejection
   Indicates a cargo-cult approach that produces incorrect routing, weak
   separation, and hard-to-debug behavior.

TOPIC 4 - Django ORM vs serializer responsibilities
1) Interview question
   Where do you put validation and transformation logic: in Django models,
   serializers, or views? Give a concrete example and justify.
2) What the interviewer is testing
   Understanding of data validation boundaries and avoiding duplicated or
   conflicting rules.
3) Ideal think-aloud answer
   Model validation captures invariants at the data layer that apply anywhere
   the model is saved; serializer validation is API-specific input validation.
   Example: uniqueness constraint belongs in the model; validating that a
   field is present for a particular endpoint belongs in the serializer.
   Views should orchestrate, not validate.
4) Common wrong answer
   Put all validation in the view so it is explicit and fast, and avoid model
   validation because it is too slow.
5) Why it causes rejection
   Demonstrates unsafe layering that leads to inconsistent data integrity and
   breaks when models are saved outside the API path.
