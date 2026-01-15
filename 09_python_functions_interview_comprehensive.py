"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 PYTHON FUNCTIONS - ELIMINATION INTERVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Interviewer: Staff Engineer | Language Expert | Elimination Round
Target: 5+ YOE | Purpose: Filter candidates who misunderstand function mechanics
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣ OVERVIEW

WHY INTERVIEWERS ASK FUNCTION QUESTIONS:
────────────────────────────────────────
Function signatures reveal deep Python understanding. Candidates who've "used
Python for years" often get this catastrophically wrong.

THESE QUESTIONS FILTER:
• Those who don't understand mutable default arguments
• Candidates who can't explain *args/**kwargs correctly
• Engineers who confuse argument passing mechanisms
• People who don't know parameter ordering rules
• Those who treat Python like Java/C++

WHAT WEAK CANDIDATES MISUNDERSTAND:
───────────────────────────────────
❌ Think default arguments are evaluated at call time
❌ Can't explain *args vs **kwargs
❌ Don't know required parameter ordering
❌ Use mutable defaults without understanding consequences
❌ Confuse return with yield
❌ Don't understand positional-only / keyword-only

STRONG MENTAL MODEL:
───────────────────
✓ Explains default evaluation at definition time
✓ Knows *args = positional, **kwargs = keyword
✓ States parameter order: pos-only, regular, *args, keyword-only, **kwargs
✓ Identifies mutable default trap instantly
✓ Understands yield creates generator, not runs function
✓ Knows when to use keyword-only parameters

ELIMINATION CRITERIA:
────────────────────
- Can't explain mutable default trap → REJECT
- Doesn't know *args/**kwargs → REJECT (for 5+ YOE)
- Can't state parameter order rules → REJECT
- Confuses return with yield → REJECT

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

2️⃣ CONCEPT BREAKDOWN

╔═══════════════════════════╦═══════════╦════════════════════════════════╗
║ CONCEPT                   ║ FREQUENCY ║ WHAT INTERVIEWERS TEST         ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ Mutable default arguments ║ HIGH      ║ THE classic Python trap        ║
║                           ║           ║ REJECT: Uses list=[] default   ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ *args / **kwargs          ║ HIGH      ║ Variable arguments             ║
║                           ║           ║ REJECT: Can't explain          ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ Parameter ordering rules  ║ HIGH      ║ Syntax correctness             ║
║                           ║           ║ REJECT: Wrong order = SyntaxErr║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ return vs yield           ║ HIGH      ║ Generator mental model         ║
║                           ║           ║ REJECT: Thinks yield returns   ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ Keyword-only parameters   ║ MEDIUM    ║ Python 3 feature               ║
║                           ║           ║ REJECT: Doesn't know exists    ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ Positional-only params    ║ MEDIUM    ║ Python 3.8+                    ║
║                           ║           ║ REJECT: (Minor if missed)      ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ Default eval timing       ║ HIGH      ║ Definition vs call time        ║
║                           ║           ║ REJECT: Says "call time"       ║
╚═══════════════════════════╩═══════════╩════════════════════════════════╝

TYPICAL WRONG BELIEFS:
─────────────────────
❌ "Default [] creates new list each call" (WRONG - evaluated once)
❌ "*args is for any arguments" (IMPRECISE - positional only)
❌ "**kwargs is for optional arguments" (WRONG - keyword arguments)
❌ "yield returns a value" (WRONG - suspends, returns generator)
❌ "Parameter order doesn't matter" (WRONG - strict rules)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

3️⃣ INTERVIEW QUESTIONS

SECTION 3A: MUTABLE DEFAULT ARGUMENTS (HIGH - ELIMINATION TRAP)
────────────────────────────────────────────────────────────────

① WARM-UP ELIMINATION
──────────────────────
Q: "What's wrong with this code?"

def add_item(item, lst=[]):
    lst.append(item)
    return lst

STRONG ANSWER:
"Mutable default argument trap. Default [] is evaluated once at function definition,
not each call. All calls share the SAME list object. First call returns [item1],
second call returns [item1, item2], etc. Fix: use None and create new list inside."

WEAK ANSWER:
"Nothing wrong?" ✗ INSTANT REJECT
"The list gets shared?" ✗ VAGUE, doesn't explain why
"It's a bug in Python" ✗ SHOWS NO UNDERSTANDING

② CORE REASONING
─────────────────
Q: "Predict output. Explain why."

def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))
print(add_item(2))
print(add_item(3))

STRONG ANSWER:
"Prints [1], [1, 2], [1, 2, 3]. All three calls share the same default list object
because default is evaluated AT DEFINITION TIME (when def executes), not at call
time. Each call appends to the same shared list."

WEAK ANSWER:
"Prints [1], [2], [3]?" ✗ WRONG, fundamental misunderstanding
"Error?" ✗ WRONG

③ EDGE-CASE
────────────
Q: "Does this have the same problem?"

def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

STRONG ANSWER:
"No. None is immutable. if lst is None creates a NEW list each call. This is the
CORRECT pattern. Each call gets its own list. Prints [1], [2], [3] as expected."

④ FOLLOW-UP
────────────
Q: "Why does Python do this? Isn't it a design flaw?"

STRONG ANSWER:
"It's deliberate. Defaults are evaluated once at definition time for efficiency
and to allow certain patterns (like caching). The issue is that MUTABLE defaults
persist across calls. It's a trade-off: consistency (always eval at definition)
vs convenience (new list each call). Immutable defaults (None, 0, '') don't cause
issues because you can't mutate them."

WEAK: "It's just how Python works" ✗ DOESN'T EXPLAIN WHY

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 3B: *args / **kwargs (HIGH)
────────────────────────────────────

① WARM-UP
──────────
Q: "Explain *args and **kwargs. Be precise."

STRONG ANSWER:
"*args collects extra POSITIONAL arguments into a tuple. **kwargs collects extra
KEYWORD arguments into a dict. Names 'args' and 'kwargs' are convention, not required.
The * and ** operators are what matter."

WEAK ANSWER:
"They're for optional arguments?" ✗ WRONG CONCEPT
"They let you pass any arguments?" ✗ IMPRECISE
"I'd have to look it up" ✗ REJECT FOR 5+ YOE

② CORE REASONING
─────────────────
Q: "What does this function accept?"

def func(a, b, *args, c, **kwargs):
    pass

STRONG ANSWER:
"a and b: required positional or keyword arguments.
*args: zero or more additional positional arguments (tuple).
c: keyword-only argument (required, must use c=value).
**kwargs: zero or more additional keyword arguments (dict).

Call examples:
func(1, 2, c=3)              # Valid: a=1, b=2, c=3
func(1, 2, 3, 4, c=5, d=6)   # Valid: args=(3,4), kwargs={'d':6}
func(1, 2, 3)                # Invalid: missing c
func(1, b=2, c=3)            # Valid: a=1, b=2, c=3"

WEAK ANSWER:
"It accepts everything?" ✗ NOT PRECISE
Can't explain keyword-only ✗ SIGNIFICANT GAP

③ EDGE-CASE
────────────
Q: "What's the correct parameter order? Write a function with ALL parameter types."

STRONG ANSWER:
"Order: positional-only, regular, *args, keyword-only, **kwargs.

def full_signature(pos_only, /, regular, *args, kw_only, **kwargs):
    pass

/ marks end of positional-only (Python 3.8+)
* (alone or with *args) starts keyword-only parameters"

WEAK: Can't state order ✗ DOESN'T KNOW SYNTAX RULES

④ FOLLOW-UP
────────────
Q: "Why would you use keyword-only parameters?"

STRONG ANSWER:
"Prevent caller from passing by position - forces clarity. Example:

def connect(host, port, *, timeout=None, retry=3):
    pass

timeout and retry MUST be passed by name:
connect('localhost', 8080, timeout=5)  # Valid
connect('localhost', 8080, 5, 3)       # Invalid: positional after *

Benefits: API clarity, prevents positional errors, allows reordering parameters."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 3C: return vs yield (HIGH)
───────────────────────────────────

① WARM-UP
──────────
Q: "What's the fundamental difference between return and yield?"

STRONG ANSWER:
"return terminates function and returns value. yield suspends function, returns
generator object that produces values on demand. Function with yield is generator
function - calling it returns generator, doesn't execute body yet."

WEAK ANSWER:
"yield returns values in a loop?" ✗ IMPRECISE
"They're similar?" ✗ FUNDAMENTALLY DIFFERENT

② CORE REASONING
─────────────────
Q: "Predict output:"

def func():
    print("Start")
    yield 1
    print("Middle")
    yield 2
    print("End")

result = func()
print(type(result))
print(next(result))
print(next(result))

STRONG ANSWER:
"Prints:
<class 'generator'>
Start
1
Middle
2

Calling func() returns generator, doesn't execute body. First next() executes
until first yield, prints 'Start', yields 1. Second next() resumes, prints
'Middle', yields 2."

WEAK: "Prints Start, 1, Middle, 2?" ✗ Missing generator type understanding

③ EDGE-CASE
────────────
Q: "What if you call next() a third time?"

STRONG ANSWER:
"Raises StopIteration. Generator resumes after second yield, prints 'End', function
ends. No more values to yield. StopIteration signals exhaustion."

④ FOLLOW-UP
────────────
Q: "Can a function have both return and yield?"

STRONG ANSWER:
"Yes, but return in generator function doesn't return to caller - it raises
StopIteration with the return value as argument. Typically used to signal
completion with final value:

def gen():
    yield 1
    yield 2
    return 'done'  # Becomes StopIteration('done')

Not commonly used. Usually just let function end naturally."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 3D: PARAMETER ORDERING (HIGH - SYNTAX RULES)
─────────────────────────────────────────────────────

① CORE QUESTION
────────────────
Q: "Which of these are valid? Explain why."

# A
def f(a, b=1, c): pass

# B
def f(a, *args, b): pass

# C
def f(a, **kwargs, b): pass

# D  
def f(a, /, b, *, c): pass

STRONG ANSWER:
"A: Invalid. Required parameter (c) cannot follow default parameter (b=1).
Required must come first.

B: Valid. b is keyword-only parameter (after *args). Must be called with b=value.

C: Invalid. **kwargs must be last. Nothing can follow it.

D: Valid (Python 3.8+). a is positional-only (/), b is regular, c is keyword-only (*)."

WEAK: Gets any wrong ✗ DOESN'T UNDERSTAND SYNTAX

② FOLLOW-UP
────────────
Q: "Write function that requires first 2 args positional, accepts any additional
positional, and requires 'mode' keyword-only."

STRONG ANSWER:
def process(a, b, *args, mode):
    pass

# OR with positional-only:
def process(a, b, /, *args, mode):
    pass

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

4️⃣ THINK-ALOUD ANSWERS

QUESTION: "Explain why this is dangerous:"

def process_items(items=[]):
    items.append('processed')
    return items

STRONG CANDIDATE:
"This is the classic mutable default trap. The empty list [] is evaluated ONCE
when the function is defined, not each time it's called. Every call to process_items()
without an argument uses the SAME list object. So the first call returns
['processed'], second call returns ['processed', 'processed'], and so on.

The fix is to use None as default and create a new list inside the function:

def process_items(items=None):
    if items is None:
        items = []
    items.append('processed')
    return items

This way, each call gets its own list. This is a fundamental Python gotcha that
every senior engineer must know."

KEYWORDS INTERVIEWERS LISTEN FOR:
✓ "Evaluated once at definition time"
✓ "Shared across calls"
✓ "Use None and create inside"
✓ "Mutable default"

WEAK CANDIDATE:
"Hmm, the list keeps growing? Maybe it's a memory leak?"

RED FLAGS:
❌ Doesn't mention "evaluated once"
❌ Doesn't explain timing
❌ Can't state the fix
❌ Calls it a "leak" (wrong concept)

INTERVIEWER: "This is elimination-level knowledge. REJECT."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

5️⃣ OUTPUT PREDICTION

PROBLEM 1:
──────────
def mystery(x, y, *args, **kwargs):
    print(f"x={x}, y={y}")
    print(f"args={args}")
    print(f"kwargs={kwargs}")

mystery(1, 2, 3, 4, a=5, b=6)

OUTPUT:
x=1, y=2
args=(3, 4)
kwargs={'a': 5, 'b': 6}

REASONING: "First two positional go to x, y. Remaining positional (3, 4) collected
by *args as tuple. Keyword arguments (a=5, b=6) collected by **kwargs as dict."

───────────────────────────────────────────────────────────────────────

PROBLEM 2:
──────────
def add_to_list(value, lst=[]):
    lst.append(value)
    return lst

a = add_to_list(1)
b = add_to_list(2)
c = add_to_list(3, [])
print(a is b)
print(b is c)

OUTPUT:
True
False

REASONING: "a and b reference the SAME default list (evaluated once). a is b → True.
c passes explicit [], which is different object. b is c → False."

───────────────────────────────────────────────────────────────────────

PROBLEM 3:
──────────
def generate():
    print("Starting")
    yield 1
    yield 2
    print("Ending")

g = generate()
print("Created generator")
x = next(g)
print(f"Got {x}")

OUTPUT:
Created generator
Starting
Got 1

REASONING: "generate() returns generator without executing body. 'Created generator'
prints. First next() executes until first yield, prints 'Starting', yields 1.
'Ending' not printed yet - generator suspended."

COMMON WRONG: Thinks "Starting" prints immediately when generate() called ✗

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

6️⃣ COMMON FAILURE MODES

FAILURE #1: MUTABLE DEFAULTS
═════════════════════════════

MISTAKE:
def add_task(task, tasks=[]):  # WRONG!
    tasks.append(task)
    return tasks

CORRECT:
def add_task(task, tasks=None):
    if tasks is None:
        tasks = []
    tasks.append(task)
    return tasks

WHY IT'S WRONG: Default [] evaluated once, shared across all calls.

───────────────────────────────────────────────────────────────────────

FAILURE #2: WRONG PARAMETER ORDER
══════════════════════════════════

MISTAKE:
def func(**kwargs, *args):  # SyntaxError!
    pass

CORRECT ORDER:
Regular → *args → keyword-only → **kwargs

def func(a, *args, b, **kwargs):  # Correct
    pass

───────────────────────────────────────────────────────────────────────

FAILURE #3: CONFUSING RETURN WITH YIELD
════════════════════════════════════════

WRONG BELIEF: "yield returns a value like return"

REALITY:
- return: exits function, returns value
- yield: suspends function, returns generator that yields values

def with_return():
    return [1, 2, 3]  # Returns list

def with_yield():
    yield 1
    yield 2
    yield 3  # Returns generator

result1 = with_return()  # result1 is list [1, 2, 3]
result2 = with_yield()   # result2 is generator object

───────────────────────────────────────────────────────────────────────

FAILURE #4: NOT KNOWING KEYWORD-ONLY
═════════════════════════════════════

QUESTION: "How do you force caller to use keyword arguments?"

WRONG: "Can't do that in Python"

CORRECT: Use * to start keyword-only section:

def func(a, b, *, c, d):  # c and d are keyword-only
    pass

func(1, 2, 3, 4)        # Error!
func(1, 2, c=3, d=4)    # Correct

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

7️⃣ MOCK INTERVIEW (ELIMINATION ROUND)

RAPID-FIRE (2 minutes):

Q1: "Default arguments evaluated at definition or call time?"
EXPECTED: "Definition time" [< 3 seconds]
REJECT IF: "Call time"

Q2: "What does *args collect?"
EXPECTED: "Extra positional arguments as tuple" [< 5 seconds]
REJECT IF: "All arguments" or vague

Q3: "What does **kwargs collect?"
EXPECTED: "Extra keyword arguments as dict" [< 5 seconds]

Q4: "This code - error or output?"
    def f(a, b=1, c): pass
EXPECTED: "SyntaxError - required after default" [< 10 seconds]

Q5: "Fix mutable default: def f(x, lst=[])"
EXPECTED: "Use None, create inside: if lst is None: lst = []" [< 10 seconds]

Q6: "Does calling generator function execute its body?"
EXPECTED: "No - returns generator, body executes on next()" [< 10 seconds]
REJECT IF: "Yes"

Q7: "Make parameter keyword-only"
EXPECTED: "Put * before it: def f(a, *, b)" [< 10 seconds]

PRESSURE TEST:

INTERVIEWER: "You said definition time. Are you SURE?"

STRONG: "Yes. I can prove it:

def f(lst=[]):
    lst.append(1)
    return lst

print(f())  # [1]
print(f())  # [1, 1] - same list!

If evaluated at call time, would be [1] both times."

WEAK: "Um, maybe call time?" ✗ CAVES UNDER PRESSURE

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

8️⃣ SELF-ASSESSMENT

CRITICAL (Must answer YES to ALL):
───────────────────────────────────
□ Can explain mutable default trap
□ Know *args collects positional as tuple
□ Know **kwargs collects keyword as dict
□ Can state parameter order rules
□ Know difference between return and yield
□ Can write keyword-only parameters
□ Know defaults evaluated at definition time

IMPORTANT (5/7):
─────────────────
□ Can write all parameter types correctly
□ Know positional-only parameters (/)
□ Understand generator function creation
□ Can fix mutable default bugs
□ Know when to use keyword-only
□ Understand why mutable defaults persist
□ Can identify syntax errors in signatures

SCORING:

CRITICAL < 7/7: FAIL - Missing fundamental function knowledge. Cannot proceed.
CRITICAL = 7/7, IMPORTANT < 5/7: BORDERLINE - Know basics, lack depth.
CRITICAL = 7/7, IMPORTANT >= 5/7: PASS - Solid function understanding.

INTERVIEWER CONCLUSION:

IF PASS: "Understands function mechanics, parameter passing, and common traps.
Can write correct signatures. Knows generators vs regular functions."

IF FAIL: "Does not understand Python functions. Would write buggy code with
mutable defaults. Cannot structure APIs correctly. REJECT."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BOTTOM LINE:
If you use mutable defaults or can't explain *args/**kwargs, you're not ready.
These are FUNDAMENTAL to Python functions. 5+ YOE engineers must know this cold.
"""
