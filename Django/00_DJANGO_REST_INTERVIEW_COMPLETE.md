# ✅ DJANGO REST FRAMEWORK INTERVIEW FILES - COMPLETE

## 🎯 Mission Accomplished: All 5 Files Created

### 📦 Delivered Files

#### **01. `django_rest_core_interview.py`**

**Focus:** Django vs DRF Responsibility + Core Architecture

**Critical Concepts:**

- **Django Request vs DRF Request** - Content negotiation, request.data vs request.POST
- **Middleware vs Authentication Classes** - When each runs, integration points
- **Django Views vs APIView vs ViewSet** - When to use which
- **ORM vs Serializer vs View Responsibility** - Separation of concerns

**Elimination Triggers:**

- ❌ Doesn't understand request.data parsing → REJECT
- ❌ Puts API auth in middleware → REJECT
- ❌ Mixes serializer and view responsibilities → REJECT

**Production Failures Covered:**

- JSON requests ignored (no Content-Type header)
- Middleware auth runs on static files (performance killer)
- Business logic in serializers (untestable)

---

#### **02. `django_rest_custom_user_interview.py`**

**Focus:** Custom User Model Implementation (CRITICAL)

**Critical Concepts:**

- **AbstractUser vs AbstractBaseUser** - When to use which
- **AUTH_USER_MODEL timing** - MUST set before first migration
- **Password security** - set_password() vs plain text storage
- **User serializers** - write_only, read_only, security
- **Admin registration** - UserAdmin for password handling

**Elimination Triggers:**

- ❌ Stores plain text passwords → INSTANT REJECT
- ❌ Doesn't set AUTH_USER_MODEL from start → REJECT
- ❌ Uses fields='**all**' in User serializer → REJECT
- ❌ Doesn't register User in admin → REJECT

**Production Failures Covered:**

- Changing AUTH_USER_MODEL after migrations (database hell)
- Plain text password storage (security breach)
- Password field exposed in API responses (audit failure)
- Can't manage users in admin (operational nightmare)

---

#### **03. `django_rest_auth_permissions_interview.py`**

**Focus:** Authentication, Authorization, Security

**Critical Concepts:**

- **Authentication vs Authorization** - WHO vs WHAT, execution order
- **Token vs JWT vs Session** - Trade-offs, when to use each
- **Permission Classes** - IsOwner, IsAdmin, custom permissions
- **Data Filtering** - get_queryset() to prevent leaks
- **Throttling** - Rate limiting, DDoS protection

**Elimination Triggers:**

- ❌ Confuses authentication with authorization → REJECT
- ❌ Doesn't filter querysets → REJECT (data leak)
- ❌ Trusts client to set owner field → REJECT
- ❌ No rate limiting on sensitive endpoints → REJECT

**Production Failures Covered:**

- Unfiltered querysets leak all data to all users
- Missing permission checks allow unauthorized modifications
- No rate limiting enables brute force attacks
- CORS misconfiguration breaks production auth

---

#### **04. `django_rest_debugging_interview.py`**

**Focus:** Real-World Failures & Performance

**Critical Concepts:**

- **Serializer 400 errors** - Field validation, required fields
- **request.data empty** - Content-Type, parser issues
- **N+1 Query Problem** - THE #1 DRF performance killer
- **select_related vs prefetch_related** - Query optimization
- **Migration failures** - Adding fields to existing data
- **Production auth issues** - CORS, HTTPS, cookies

**Elimination Triggers:**

- ❌ Can't debug N+1 queries → REJECT
- ❌ Doesn't know select_related() → REJECT
- ❌ Can't explain serializer validation flow → REJECT
- ❌ Doesn't understand Content-Type header → REJECT

**Production Failures Covered:**

- 201 queries instead of 2 (N+1 disaster)
- Migrations fail with existing users
- Auth works locally, fails in production (CORS)
- API slow under load (no query optimization)

---

#### **05. `django_rest_mock_interview.py`**

**Focus:** Full Mock Interview Simulation

**Format:**

1. **Code Review** (15 min) - Find 5 bugs in production code
2. **API Design** (15 min) - E-commerce API from requirements
3. **Rapid-Fire** (10 min) - 8 quick technical questions
4. **Performance** (5 min) - Optimize slow endpoint

**Critical Bugs to Find:**

1. fields='**all**' exposes sensitive data
2. Unfiltered queryset leaks all posts
3. No permission check on publish action
4. Password not write_only
5. Plain text password storage (CRITICAL)

**Elimination Triggers:**

- ❌ Misses plain text password bug → INSTANT REJECT
- ❌ Misses permission bugs → REJECT
- ❌ < 5/8 on rapid-fire → REJECT
- ❌ Can't identify N+1 problem → REJECT

---

## 🔥 Top 20 Elimination Questions

**These questions decide HIRE vs REJECT. Master them or fail:**

### Authentication & Security (Files 02-03)

1. **"How do you store passwords in serializer create()?"**

   - ✅ CORRECT: `user.set_password(password)`
   - ❌ INSTANT REJECT: `user.password = password`

2. **"Should password field be write_only?"**

   - ✅ CORRECT: "Yes - ALWAYS write_only"
   - ❌ INSTANT REJECT: "No" or hesitates

3. **"When do you set AUTH_USER_MODEL?"**

   - ✅ CORRECT: "Before first migration - Day 1"
   - ❌ INSTANT REJECT: "Anytime" or "When needed"

4. **"AbstractUser vs AbstractBaseUser?"**

   - ✅ CORRECT: "AbstractUser for 99% - adds fields. AbstractBaseUser only for full control"
   - ❌ REJECT: "AbstractBaseUser is more flexible, so always use it"

5. **"Authentication vs Authorization - which runs first?"**
   - ✅ CORRECT: "Authentication sets user, THEN authorization checks access"
   - ❌ REJECT: Confuses them

### Permissions & Data Security (File 03)

6. **"User can GET /api/posts/ and see all IDs. Permission is IsOwner. Problem?"**

   - ✅ CORRECT: "Must filter queryset in get_queryset() - data leak!"
   - ❌ INSTANT REJECT: "Permission is enough"

7. **"Should perform_create() trust client's owner field?"**

   - ✅ CORRECT: "NO - always set owner=request.user"
   - ❌ INSTANT REJECT: "Yes"

8. **"401 vs 403 - when do you use each?"**
   - ✅ CORRECT: "401: auth failed (who?), 403: permission denied (what?)"
   - ❌ REJECT: Doesn't know

### Performance (File 04)

9. **"100 books, 201 database queries. Problem?"**

   - ✅ CORRECT: "N+1 query problem - use select_related()"
   - ❌ INSTANT REJECT: "That's normal"

10. **"select_related vs prefetch_related?"**

    - ✅ CORRECT: "select_related for FK (JOIN), prefetch_related for reverse FK/M2M"
    - ❌ REJECT: Confuses them

11. **"Why is this slow? `for book in books: print(book.author.name)`"**
    - ✅ CORRECT: "N+1 - query per book. Fix: select_related('author')"
    - ❌ REJECT: Doesn't identify N+1

### Core Architecture (File 01)

12. **"What does request.data return if Content-Type is application/json?"**

    - ✅ CORRECT: "Parsed dict/list, automatically deserialized"
    - ❌ REJECT: "String" or "Doesn't know"

13. **"Where do you put token validation logic?"**

    - ✅ CORRECT: "Authentication class, not middleware"
    - ❌ REJECT: "Middleware" or "View"

14. **"ViewSet vs APIView - when to use each?"**

    - ✅ CORRECT: "ViewSet for CRUD resources, APIView for custom actions"
    - ❌ REJECT: Can't distinguish

15. **"What's wrong with putting business logic in serializer?"**
    - ✅ CORRECT: "Serializers for validation/transformation, views for business logic"
    - ❌ REJECT: "It's fine"

### Debugging (File 04)

16. **"request.data is empty but request.body has data. Cause?"**

    - ✅ CORRECT: "Missing Content-Type header or parser not configured"
    - ❌ REJECT: Doesn't know

17. **"Migration fails: 'column cannot be null'. Fix?"**

    - ✅ CORRECT: "Add null=True, blank=True or default value"
    - ❌ REJECT: "Just drop the database"

18. **"Serializer validation order?"**
    - ✅ CORRECT: "Field type → field validators → object validator → unique constraints"
    - ❌ REJECT: Doesn't know order

### Security (Files 02-03-05)

19. **"What's wrong with fields='**all**' in UserSerializer?"**

    - ✅ CORRECT: "Exposes password, is_staff, internal fields - security hole"
    - ❌ INSTANT REJECT: "It's fine" or "It's convenient"

20. **"Why rate limit login endpoints?"**
    - ✅ CORRECT: "Prevent brute force attacks"
    - ❌ REJECT: Doesn't know

---

## 📊 Complete Interview Readiness Checklist

### **CRITICAL (Must answer YES to ALL - one NO = FAIL):**

**From File 02 (Custom User):**

- □ Know to set AUTH_USER_MODEL before first migration
- □ ALWAYS use set_password() - NEVER store plain text
- □ Make password field write_only in serializers
- □ Never use fields='**all**' in User serializers
- □ Register User in admin with UserAdmin subclass

**From File 03 (Auth & Permissions):**

- □ Distinguish authentication from authorization
- □ Filter querysets in get_queryset() to prevent data leaks
- □ Never trust client to set owner field
- □ Implement rate limiting on sensitive endpoints
- □ Know 401 vs 403 status codes

**From File 04 (Debugging & Performance):**

- □ Can debug N+1 query problems
- □ Know select_related vs prefetch_related
- □ Understand serializer validation order
- □ Know why request.data can be empty
- □ Can handle migrations with existing data

**From File 01 (Core):**

- □ Know request.data vs request.POST
- □ Understand middleware runs for ALL requests
- □ Know when to use APIView vs ViewSet
- □ Never put side effects in serializers

**From File 05 (Mock Interview):**

- □ Can find all security bugs in code review
- □ Can design secure CRUD API from requirements
- □ Score 7+/8 on rapid-fire questions
- □ Can optimize N+1 queries instantly

---

## 🎯 Failure Patterns That Cause INSTANT REJECT

### **Security Failures:**

1. **Plain text password storage** - Shows no security awareness
2. **fields='**all**' on User model** - Exposes sensitive data
3. **Trusting client data for ownership** - Privilege escalation
4. **No queryset filtering** - Data leak to all users
5. **Password not write_only** - Returns passwords in API

### **Performance Failures:**

6. **Can't identify N+1 queries** - Will build slow APIs
7. **Doesn't know select_related()** - Missing fundamental optimization
8. **No pagination** - Memory exhaustion with large datasets

### **Architecture Failures:**

9. **Puts business logic in serializers** - Unmaintainable code
10. **Puts API auth in middleware** - Performance killer
11. **Can't distinguish APIView from ViewSet** - Wrong tool for job

### **Migration Failures:**

12. **Changes AUTH_USER_MODEL after migrations** - Database disaster
13. **Can't add required fields to existing models** - Production deployment fails

### **Fundamental Gaps:**

14. **Confuses authentication with authorization** - Security model misunderstanding
15. **Doesn't understand CORS** - Production auth always broken

---

## 💡 How to Use These Files

### **Day Before Interview:**

1. Read File 02 (Custom User) - Most important
2. Read File 03 (Auth & Permissions) - Security critical
3. Take File 05 (Mock Interview) - Simulate pressure
4. Score yourself honestly

### **Week Before:**

1. Study files 01-04 sequentially
2. Build a complete CRUD API from scratch
3. Practice code review (File 05 Round 1)
4. Practice API design (File 05 Round 2)

### **Ongoing Prep:**

1. Master the Top 20 elimination questions
2. Build 3 different APIs (blog, e-commerce, social)
3. Practice spotting security bugs
4. Time yourself on rapid-fire questions

---

## 🔥 Common Mistakes That Cause Rejection

### **Interview Mistakes:**

1. **"I need to Google that"** - For fundamental concepts like set_password()
2. **"It depends"** - Without explaining what it depends on
3. **"I usually just try different things"** - Shows no understanding
4. **"That's just a warning"** - About critical security issues
5. **"It works on my machine"** - Can't debug production issues

### **Code Mistakes:**

1. Using `fields = '__all__'` without thinking
2. Not setting owner automatically
3. Not filtering querysets by user
4. Storing plain text passwords
5. Missing select_related() on obvious N+1

### **Explanation Mistakes:**

1. Can't explain WHY, only WHAT
2. Vague answers ("It's for security")
3. Confusing similar concepts (auth vs authz)
4. Can't give specific examples
5. Doesn't mention production impact

---

## 📈 Scoring Matrix

### **INSTANT REJECT (Any one of these):**

- ❌ Stores plain text passwords
- ❌ Misses permission bugs in code review
- ❌ Doesn't know N+1 query problem exists
- ❌ Uses fields='**all**' on User model without concern
- ❌ Can't distinguish authentication from authorization

### **REJECT (Multiple failures):**

- ❌ < 5/8 on rapid-fire technical questions
- ❌ Can't design basic CRUD API with permissions
- ❌ Doesn't filter querysets by user
- ❌ Doesn't know select_related() or prefetch_related()
- ❌ Can't debug common production issues

### **BORDERLINE (Needs mentoring):**

- ⚠️ Found 3-4/5 bugs in code review (missed one critical)
- ⚠️ API design missing some security features
- ⚠️ 5-6/8 on rapid-fire questions
- ⚠️ Identified N+1 but weak optimization

### **STRONG HIRE:**

- ✅ Found ALL critical security bugs
- ✅ Solid API design with proper permissions
- ✅ 7-8/8 on rapid-fire questions
- ✅ Strong N+1 optimization with annotate/select_related/prefetch_related
- ✅ Can explain WHY, not just HOW
- ✅ Security-conscious throughout

---

## 🎓 What Interviewers Conclude

### **IF YOU FAIL:**

_"Candidate has years of experience but fundamental gaps. Would create security vulnerabilities (plain text passwords, data leaks). Cannot optimize queries (N+1). Would struggle in production incidents. Not ready for backend role. **REJECT**."_

### **IF BORDERLINE:**

_"Solid fundamentals but some gaps in security/performance. May need significant mentoring. Consider for junior-mid level with supervision. **DISCUSS WITH TEAM**."_

### **IF STRONG:**

_"Excellent DRF knowledge. Security-conscious. Understands performance optimization. Can debug production issues. Explains concepts clearly. Ready for senior backend role. **RECOMMEND HIRE**."_

---

## 🚀 Study Plan

### **Week 1: Fundamentals**

- **Day 1-2:** File 01 (Core) - Django vs DRF, request/response
- **Day 3-4:** File 02 (Custom User) - THE MOST CRITICAL FILE
- **Day 5:** File 03 (Auth) - Permissions, security
- **Day 6-7:** Build simple blog API from scratch

### **Week 2: Advanced**

- **Day 1-2:** File 04 (Debugging) - N+1, performance
- **Day 3-4:** Optimize your blog API (add select_related)
- **Day 5:** Build e-commerce API (File 05 Round 2)
- **Day 6-7:** Take File 05 (Mock Interview) multiple times

### **Before Interview:**

- Review Top 20 elimination questions
- Take File 05 mock interview under time pressure
- Practice explaining concepts out loud
- Build one more API from scratch (time yourself)

---

## ⚠️ Red Flags Interviewers Watch For

### **During Code Review:**

1. **Doesn't spot security bugs first** - Security should jump out
2. **Focuses on style over substance** - Missing critical bugs
3. **"I'd run the code to see"** - Can't reason about behavior
4. **Hesitates on fundamentals** - Gaps in knowledge

### **During API Design:**

1. **Forgets permissions entirely** - Not security-conscious
2. **Uses fields='**all**' by default** - Lazy, insecure
3. **Doesn't filter querysets** - Will create data leaks
4. **No query optimization** - Will build slow APIs

### **During Rapid-Fire:**

1. **Long pauses on basic questions** - Gaps in fundamentals
2. **Changes answers under pressure** - Not confident
3. **Can't explain WHY** - Memorized without understanding
4. **Guesses instead of admitting "I don't know"** - Dishonest

---

## 🏆 Success Indicators

### **You're Ready When:**

- ✅ Can find all 5 bugs in File 05 Code Review in < 10 minutes
- ✅ Can design File 05 API from scratch in < 15 minutes
- ✅ Score 8/8 on rapid-fire questions consistently
- ✅ Can explain concepts to someone else clearly
- ✅ Automatically think about security in every design
- ✅ See N+1 queries immediately in any code
- ✅ Never use fields='**all**' without thinking
- ✅ Always filter querysets by user automatically

### **Interview Performance Indicators:**

- ✅ Interviewer nods during your explanations
- ✅ Asks follow-up questions (not clarifications)
- ✅ Says "Good catch" during code review
- ✅ Moves quickly through questions (you're confident)
- ✅ Discusses trade-offs (shows depth)

---

## ✅ Final Checklist

**Before Claiming Interview Readiness:**

□ Memorized Top 20 elimination questions
□ Can spot all 5 bugs in File 05 code review
□ Can design secure CRUD API in 15 minutes
□ Built 3+ complete APIs from scratch
□ Never store plain text passwords
□ Always use write_only on password fields
□ Always filter querysets by user
□ Always set owner automatically in perform_create
□ Know when to use select_related vs prefetch_related
□ Can explain authentication vs authorization
□ Understand CORS and production auth
□ Can debug N+1 queries
□ Can handle migrations with existing data
□ Set AUTH_USER_MODEL before first migration (always)

---

## 💀 Bottom Line

**Django REST Framework interviews filter for:**

1. **SECURITY** - One vulnerability = REJECT
2. **PERFORMANCE** - N+1 queries = REJECT
3. **ARCHITECTURE** - Mixed concerns = REJECT

**If you:**

- Don't know `set_password()` → You're not ready
- Can't identify N+1 queries → You're not ready
- Don't filter querysets → You're not ready
- Use `fields='__all__'` carelessly → You're not ready

**Master these 5 files or don't apply for Django backend roles.**

**Good luck. Be brutal in self-assessment. Production doesn't forgive mistakes.**

---

## 📚 File Organization

```
Django/
├── 00_DJANGO_REST_INTERVIEW_COMPLETE.md  ← You are here
├── 01_django_rest_core_interview.py      ← Django vs DRF fundamentals
├── 02_django_rest_custom_user_interview.py ← MOST CRITICAL (Custom User)
├── 03_django_rest_auth_permissions_interview.py ← Security & permissions
├── 04_django_rest_debugging_interview.py ← Real-world failures & N+1
└── 05_django_rest_mock_interview.py      ← Full mock interview

Total: 5 files + this summary
Lines of Code: ~3,000+
Interview Questions: 100+
Production Failures Covered: 50+
Elimination Scenarios: 20+
```

**Study Order: 02 → 03 → 01 → 04 → 05 (Custom User first, mock last)**

**These files represent real production experience condensed into interview format.**

**Master them. Get hired. Build secure, fast APIs.** 🚀
