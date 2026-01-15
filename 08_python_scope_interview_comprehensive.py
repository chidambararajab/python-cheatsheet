"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 PYTHON SCOPE & NAMESPACES - ELIMINATION INTERVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Interviewer: Principal Engineer | Language Expert | Elimination Round
Target: 5+ YOE | Purpose: Filter candidates who don't understand Python's scope model
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

# ═══════════════════════════════════════════════════════════════════════
# 1️⃣ FILE INTERVIEW OVERVIEW
# ═══════════════════════════════════════════════════════════════════════

"""
WHY INTERVIEWERS ASK SCOPE QUESTIONS:
─────────────────────────────────────
Scope is where candidates with "years of experience" reveal they've been
writing Python without understanding HOW IT WORKS.

These questions filter:
• Candidates who treat Python like Java/C++
• Those who guess based on "it worked once"
• Engineers who can't reason about execution
• People who don't understand name binding

WHAT WEAK CANDIDATES MISUNDERSTAND:
───────────────────────────────────
❌ Think variables are "declared" like Java
❌ Confuse assignment with mutation
❌ Don't understand closure capture
❌ Can't explain LEGB rule
❌ Use global without understanding consequences
❌ Don't know why loop variables "leak"
❌ Confuse nonlocal with global

WHAT STRONG MENTAL MODEL LOOKS LIKE:
────────────────────────────────────
✓ Explains LEGB without hesitation
✓ Knows assignment creates local binding
✓ Understands closure captures reference, not value
✓ Can predict output without running code
✓ Knows when global/nonlocal are necessary
✓ Explains scope chains precisely
✓ Identifies late binding bugs immediately

ELIMINATION CRITERIA:
────────────────────
If candidate:
- Can't explain LEGB → REJECT
- Guesses at closure behavior → REJECT
- Doesn't know global vs nonlocal → REJECT
- Can't predict simple scope output → REJECT

This is FUNDAMENTAL. Getting this wrong = doesn't know Python.
"""


# ═══════════════════════════════════════════════════════════════════════
# 2️⃣ CONCEPT BREAKDOWN
# ═══════════════════════════════════════════════════════════════════════

"""
╔═══════════════════════════╦═══════════╦════════════════════════════════╗
║ CONCEPT                   ║ FREQUENCY ║ WHAT INTERVIEWERS TEST         ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ LEGB Rule                 ║ HIGH      ║ Name lookup order              ║
║                           ║           ║ REJECT: Can't recite it        ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ Assignment creates local  ║ HIGH      ║ Why UnboundLocalError happens  ║
║                           ║           ║ REJECT: Thinks it's a bug      ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ global vs nonlocal        ║ HIGH      ║ When each is needed            ║
║                           ║           ║ REJECT: Uses global for nested ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ Closure late binding      ║ HIGH      ║ Loop variable capture bug      ║
║                           ║           ║ REJECT: Can't explain why      ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ Scope in comprehensions   ║ MEDIUM    ║ List comp doesn't leak (3.x)   ║
║                           ║           ║ REJECT: Thinks it does         ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ Class scope peculiarities ║ MEDIUM    ║ Class body != function scope   ║
║                           ║           ║ REJECT: Treats them same       ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ Shadowing                 ║ LOW       ║ Local shadows outer            ║
╚═══════════════════════════╩═══════════╩════════════════════════════════╝

TYPICAL WRONG BELIEFS:
─────────────────────
❌ "Variables must be declared before use" (Java thinking)
❌ "global makes variables accessible everywhere" (wrong direction)
❌ "Closures capture values" (they capture references)
❌ "Assignment modifies existing variable" (it creates local binding)
❌ "Loop variables are scoped to loop body" (they leak in Python)
"""


# ═══════════════════════════════════════════════════════════════════════
# 3️⃣ INTERVIEW QUESTIONS
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 3A: LEGB RULE (HIGH FREQUENCY - ELIMINATION QUESTION)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

① WARM-UP ELIMINATION QUESTION
───────────────────────────────
Q: "Explain Python's name lookup order. Be precise."

STRONG ANSWER:
"LEGB: Local, Enclosing, Global, Built-in. Python searches scopes in this order.
Local = current function. Enclosing = outer functions in nested definitions.
Global = module level. Built-in = Python's built-in namespace like len, print."

WEAK ANSWER:
"Uh, it checks local first then... global?" ✗ VAGUE, INCOMPLETE
"It looks in the function, then outside" ✗ NO PRECISION
"I'd have to look that up" ✗ INSTANT REJECT

INTERVIEWER EVALUATION:
Can't recite LEGB confidently? → REJECT. This is Python 101.

② CORE REASONING QUESTION
──────────────────────────
Q: "Predict the output. Explain your reasoning."

x = 10

def outer():
    x = 20
    def inner():
        print(x)
    return inner

f = outer()
f()

STRONG ANSWER:
"Prints 20. When inner() executes, it looks for x using LEGB. Not found in Local
(inner has no x). Found in Enclosing scope (outer's x = 20). Stops searching.
Closure captures reference to outer's x."

WEAK ANSWER:
"Prints 10?" ✗ WRONG, doesn't understand enclosing scope
"Depends on where you call it?" ✗ WRONG, doesn't understand closures
"Error?" ✗ WRONG, doesn't understand name lookup

③ EDGE-CASE / TRICK QUESTION
──────────────────────────────
Q: "What happens here and WHY?"

x = 10

def func():
    print(x)
    x = 20

func()

STRONG ANSWER:
"UnboundLocalError. Python sees assignment 'x = 20' in function body, so marks x
as local variable. When print(x) executes, x is local but not yet assigned.
This is NOT about execution order - it's about compile-time analysis."

WEAK ANSWER:
"Prints 10 then assigns 20?" ✗ Doesn't understand local binding rules
"Syntax error?" ✗ Wrong, runs fine until print
"It's a bug in Python" ✗ REJECT, doesn't understand design

KEY INSIGHT:
Assignment ANYWHERE in function makes variable local to entire function.
This is determined at compile time, not runtime.

④ FOLLOW-UP DEEP DIVE
──────────────────────
Q: "How do you fix this to print global x, then create local x?"

STRONG ANSWER:
"Use global keyword before any assignment:

def func():
    global x
    print(x)  # Prints global x (10)
    x = 20    # Modifies global x

OR, if you want local x without error, don't try to read it first."

WEAK ANSWER:
"Just don't assign to x?" ✗ Doesn't solve the problem
"Use self.x?" ✗ Wrong context, shows confusion

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 3B: global vs nonlocal (HIGH FREQUENCY)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

① WARM-UP
──────────
Q: "What's the difference between global and nonlocal?"

STRONG ANSWER:
"global declares name refers to module-level variable. nonlocal declares name
refers to nearest enclosing function's variable (not module level). nonlocal
only works inside nested functions. global works anywhere."

WEAK ANSWER:
"Both make variables accessible?" ✗ WRONG DIRECTION
"nonlocal is for classes?" ✗ CONFUSED WITH self
"They're the same?" ✗ REJECT

② CORE REASONING
─────────────────
Q: "Predict output. Explain."

count = 0

def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

f = outer()
print(f())
print(f())
print(count)

STRONG ANSWER:
"Prints 1, 2, 0. nonlocal binds to outer's count. First call increments outer's
count to 1. Second call to 2. Module-level count unchanged because nonlocal refers
to enclosing scope, not global."

WEAK ANSWER:
"Prints 1, 2, 2?" ✗ Doesn't understand nonlocal doesn't affect global
"Error?" ✗ Wrong
"All zeros?" ✗ Doesn't understand nonlocal works

③ EDGE-CASE
────────────
Q: "What happens if you use nonlocal at module level?"

def func():
    nonlocal x  # What happens?
    x = 10

STRONG ANSWER:
"SyntaxError: 'no binding for nonlocal x found'. nonlocal requires enclosing
function scope. Module level is global scope, not enclosing. Use global instead."

WEAK ANSWER:
"It works?" ✗ WRONG
"It's the same as global?" ✗ WRONG
"Don't know" ✗ SHOWS GUESSING

④ FOLLOW-UP
────────────
Q: "When would you use global vs nonlocal in production code?"

STRONG ANSWER:
"Rarely use either - both are code smells. global for module-level state (avoid,
use classes instead). nonlocal for closure-based state (factory functions,
decorators with state). Prefer class attributes over global, return values over
nonlocal when possible."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 3C: CLOSURE LATE BINDING (HIGH FREQUENCY - CLASSIC TRAP)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

① WARM-UP
──────────
Q: "What does 'closures capture references, not values' mean?"

STRONG ANSWER:
"Closure captures the variable name, not the value at capture time. When closure
executes, it looks up current value of that variable. If variable changed between
capture and execution, closure sees new value."

② CORE REASONING (THE CLASSIC TRAP)
────────────────────────────────────
Q: "Predict output. Explain."

funcs = []
for i in range(3):
    funcs.append(lambda: i)

print([f() for f in funcs])

STRONG ANSWER:
"Prints [2, 2, 2], not [0, 1, 2]. All lambdas capture reference to variable i.
Loop completes with i=2. When lambdas execute later, they all look up i and see 2.
This is late binding - value determined at call time, not definition time."

WEAK ANSWER:
"Prints [0, 1, 2]?" ✗ WRONG, doesn't understand late binding
"Prints [3, 3, 3]?" ✗ Off by one, but shows some understanding
"Don't know why" ✗ GUESSING

③ EDGE-CASE
────────────
Q: "How do you fix this to capture values?"

STRONG ANSWER:
"Use default argument to capture value at definition time:

funcs = []
for i in range(3):
    funcs.append(lambda i=i: i)  # i=i captures current value

OR use functools.partial, OR comprehension (doesn't have same issue):
funcs = [lambda i=i: i for i in range(3)]"

WEAK ANSWER:
"Use a different variable?" ✗ DOESN'T SOLVE IT
"Use global?" ✗ MAKES IT WORSE

④ FOLLOW-UP
────────────
Q: "Does this have the same problem?"

funcs = [lambda: i for i in range(3)]

STRONG ANSWER:
"No! List comprehension has its own scope in Python 3. Each iteration's i is
isolated. This DOES capture values correctly. Output: [0, 1, 2]. This is
different from regular for loop."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 3D: SCOPE IN COMPREHENSIONS (MEDIUM)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

① CORE QUESTION
────────────────
Q: "Does loop variable leak from list comprehension in Python 3?"

i = "outer"
result = [i for i in range(3)]
print(i)

STRONG ANSWER:
"Prints 'outer'. In Python 3, list comprehensions have their own scope. Loop
variable i doesn't leak. Note: This was DIFFERENT in Python 2 where it did leak."

WEAK ANSWER:
"Prints 2?" ✗ WRONG, thinking it leaks
"Error?" ✗ WRONG

② FOLLOW-UP
────────────
Q: "What about regular for loops?"

i = "outer"
for i in range(3):
    pass
print(i)

STRONG ANSWER:
"Prints 2. Regular for loops DO leak. Loop variable i overwrites outer i.
This is intentional Python behavior. Only comprehensions are isolated."
"""


# ═══════════════════════════════════════════════════════════════════════
# 4️⃣ THINK-ALOUD ANSWERS
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT STRONG CANDIDATES SAY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

QUESTION: "Explain this error:"

x = 10
def f():
    x += 1
f()

STRONG CANDIDATE:
"This raises UnboundLocalError. Python sees the augmented assignment x += 1,
which is really x = x + 1. Because there's an assignment to x in the function,
Python marks x as a local variable at compile time. When the function executes,
it tries to read local x before it's assigned, causing UnboundLocalError.

The fix is to declare 'global x' before the assignment if we want to modify
the module-level x. Without global, Python assumes any assigned variable is local."

KEYWORDS INTERVIEWERS LISTEN FOR:
✓ "UnboundLocalError" (precise error name)
✓ "Compile time" (understands when decision is made)
✓ "Assignment creates local binding"
✓ "global keyword" (knows the fix)

───────────────────────────────────────────────────────────────────────

WEAK CANDIDATE:
"Uh, it can't find x? Maybe because it's outside the function?"

INTERVIEWER: "But x is defined before the function..."

WEAK: "Oh, maybe it's a scope thing? I'd have to run it to see."

RED FLAGS:
❌ Doesn't know error name
❌ Explains as runtime issue, not compile-time
❌ Needs to "run it to see"
❌ Doesn't mention global keyword

INTERVIEWER THINKING: "Doesn't understand Python's scope model. REJECT."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

QUESTION: "Why does this print [2, 2, 2]?"

funcs = [lambda: i for i in range(3)]
# wait, wrong example

funcs = []
for i in range(3):
    funcs.append(lambda: i)
print([f() for f in funcs])

STRONG CANDIDATE:
"Prints [2, 2, 2] due to late binding in closures. All three lambdas capture
a reference to the variable i, not the value. After the loop completes, i equals 2.
When we call the lambdas later, they all look up i and see 2. This is a common
Python trap. The fix is to use default arguments: lambda i=i: i to capture the
value at definition time."

KEYWORDS:
✓ "Late binding"
✓ "Capture reference, not value"
✓ "Default argument to fix"

WEAK:
"Because... the loop overwrites i each time?"

INTERVIEWER: "So why don't they print [0, 1, 2]?"

WEAK: "Um... timing issue?"

RED FLAGS:
❌ Can't explain mechanism
❌ Uses vague terms like "timing issue"
❌ Doesn't know the fix

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ═══════════════════════════════════════════════════════════════════════
# 5️⃣ LIVE CODING / OUTPUT PREDICTION
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OUTPUT PREDICTION ROUND (Must explain BEFORE running)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PROBLEM 1:
──────────
x = []
def add(item):
    x.append(item)

add(1)
add(2)
print(x)

OUTPUT: [1, 2]
REASONING: "No UnboundLocalError because we're calling method on x, not assigning
to x. append() mutates existing object. No assignment to x, so Python looks it up
in global scope. Mutation doesn't create local binding, only assignment does."

COMMON WRONG ANSWER: "Error?" ✗ Doesn't understand mutation vs assignment

───────────────────────────────────────────────────────────────────────

PROBLEM 2:
──────────
def outer():
    x = []
    def inner():
        x.append(1)
    inner()
    inner()
    return x

print(outer())

OUTPUT: [1, 1]
REASONING: "inner() mutates x from enclosing scope. No assignment to x in inner(),
just mutation via method call. x found in enclosing scope (outer's local). Each
call to inner() appends 1."

───────────────────────────────────────────────────────────────────────

PROBLEM 3:
──────────
def outer():
    x = []
    def inner():
        x = [1]  # Assignment!
        return x
    inner()
    return x

print(outer())

OUTPUT: []
REASONING: "Prints empty list. Assignment 'x = [1]' in inner() creates NEW local
variable in inner's scope. This doesn't affect outer's x. outer returns its own
unchanged x. This demonstrates assignment creates local binding."

COMMON WRONG: "[1]" ✗ Thinks assignment affects outer's x

───────────────────────────────────────────────────────────────────────

PROBLEM 4:
──────────
def make_multiplier(n):
    return lambda x: x * n

triple = make_multiplier(3)
print(triple(10))

OUTPUT: 30
REASONING: "Closure captures n from enclosing scope. When make_multiplier(3) is
called, n=3 in that scope. Lambda captures reference to that scope's n. When
triple(10) executes, it looks up n (still 3) and returns 10 * 3 = 30."

───────────────────────────────────────────────────────────────────────

PROBLEM 5 (THE KILLER):
───────────────────────
multipliers = []
for n in [2, 3, 4]:
    multipliers.append(lambda x: x * n)

print(multipliers[0](10))  # What?
print(multipliers[1](10))  # What?
print(multipliers[2](10))  # What?

OUTPUT: 40, 40, 40
REASONING: "All print 40. Late binding trap. All lambdas capture reference to
variable n. After loop, n=4. When any lambda executes, looks up n and sees 4.
So all multiply by 4.

Fix with default argument:
multipliers.append(lambda x, n=n: x * n)

This captures value of n at definition time."

COMMON WRONG: "20, 30, 40" ✗ DOESN'T UNDERSTAND LATE BINDING (REJECT)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ═══════════════════════════════════════════════════════════════════════
# 6️⃣ COMMON FAILURE MODES
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PYTHON-SPECIFIC MENTAL MODEL MISTAKES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FAILURE #1: TREATING PYTHON LIKE JAVA
═════════════════════════════════════

WRONG BELIEF: "Variables need to be declared"

def wrong_thinking():
    x  # "Declare" x?
    x = 10

REALITY: No declaration in Python. Assignment creates binding. Reading undefined
variable is NameError (if truly undefined) or UnboundLocalError (if assigned later
in same scope).

───────────────────────────────────────────────────────────────────────

FAILURE #2: CONFUSING ASSIGNMENT WITH MUTATION
═══════════════════════════════════════════════

WRONG: "Both x = 5 and x.append(5) modify x"

REALITY:
x = 5     # Assignment - creates new binding
x.append(5)  # Mutation - modifies existing object

Assignment makes variable local. Mutation doesn't.

TRAP CODE:
count = 0
def increment():
    count += 1  # UnboundLocalError! count += 1 is assignment

───────────────────────────────────────────────────────────────────────

FAILURE #3: NOT UNDERSTANDING LATE BINDING
═══════════════════════════════════════════

WRONG: "Closures capture values at creation time"

REALITY: Closures capture variable reference. Value looked up at call time.

TRAP:
funcs = [lambda: i for i in range(3)]  # WRONG - regular for loop
# All lambdas will return same final value of i

FIX:
funcs = [lambda i=i: i for i in range(3)]  # Capture value with default

───────────────────────────────────────────────────────────────────────

FAILURE #4: MISUSING global
═══════════════════════════

WRONG: "global makes variables accessible everywhere"

REALITY: global tells Python "this name refers to module-level variable, don't
create local". It's about binding direction, not accessibility.

BAD CODE:
def func():
    print(global_var)  # Don't need global here!
    # Only need global if you're ASSIGNING

CORRECT:
global_var = 10

def read_it():
    print(global_var)  # No global needed - just reading

def modify_it():
    global global_var  # Needed here!
    global_var = 20

───────────────────────────────────────────────────────────────────────

FAILURE #5: CONFUSING nonlocal WITH global
═══════════════════════════════════════════

WRONG: "Use global to modify outer function's variable"

def outer():
    x = 0
    def inner():
        global x  # WRONG! Refers to module-level x
        x += 1
    inner()

CORRECT: Use nonlocal

def outer():
    x = 0
    def inner():
        nonlocal x  # Refers to outer's x
        x += 1
    inner()
    return x

───────────────────────────────────────────────────────────────────────

FAILURE #6: FORGETTING COMPREHENSION SCOPE
═══════════════════════════════════════════

CONFUSION: "Does loop variable leak?"

i = "outer"
[i for i in range(3)]  # Does this change i?

ANSWER: NO in Python 3 (list comp has own scope). YES in Python 2.
Regular for loops ALWAYS leak.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ═══════════════════════════════════════════════════════════════════════
# 7️⃣ MOCK INTERVIEW ROUND (ELIMINATION STYLE)
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RAPID-FIRE ELIMINATION ROUND (3 minutes - MUST answer without hesitation)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEWER: "Quick-fire scope questions. Answer immediately."

Q1: "What does LEGB stand for?"
EXPECTED: "Local, Enclosing, Global, Built-in" [< 3 seconds]
REJECT IF: Hesitates or gets order wrong

Q2: "This code. Error or output?"
    x = 10
    def f(): print(x)
    f()
EXPECTED: "10 - no error" [< 5 seconds]

Q3: "This code. Error or output?"
    x = 10
    def f(): print(x); x = 20
    f()
EXPECTED: "UnboundLocalError - assignment makes x local" [< 10 seconds]
REJECT IF: Says "10" or "NameError"

Q4: "Fix it to print 10 then assign local 20."
EXPECTED: "Remove print OR don't assign OR use global x" [< 10 seconds]

Q5: "What does nonlocal do?"
EXPECTED: "Refers to nearest enclosing function's variable" [< 5 seconds]
REJECT IF: Says "makes it accessible" or "same as global"

INTERVIEWER: [Interrupts] "Wait, global vs nonlocal - key difference?"
EXPECTED: "global = module level, nonlocal = enclosing function"

Q6: "Predict output:"
    funcs = []
    for i in range(3):
        funcs.append(lambda: i)
    print(funcs[0]())
EXPECTED: "2 - late binding, all capture reference to i" [< 15 seconds]
REJECT IF: Says "0" without explaining why wrong

Q7: "How to fix it?"
EXPECTED: "lambda i=i: i - default argument captures value" [< 10 seconds]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRESSURE TEST: "Are you sure?"
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEWER: "You said UnboundLocalError. Are you SURE it's not NameError?"

STRONG CANDIDATE: "Yes, I'm sure. NameError is when name is truly undefined.
UnboundLocalError is a subclass of NameError, raised specifically when a local
variable is referenced before assignment. Python knows it's local due to the
assignment later in the function."

WEAK CANDIDATE: "Um... maybe NameError? They're similar?"
→ SHOWS UNCERTAINTY, DOESN'T KNOW PRECISE ERRORS

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EDGE-CASE PUSHING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEWER: "What if you use global inside a class method?"

class MyClass:
    def method(self):
        global x
        x = 10

STRONG: "Works, but usually wrong. global refers to module level, not class.
If you want class-level, use self.x or cls.x. global in class method is code smell."

WEAK: "You can't use global in classes?" ✗ WRONG
"It makes it a class variable?" ✗ CONFUSED

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FINAL VERDICT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PASS (6/7+ correct, confident):
"Candidate understands Python's scope model. Knows LEGB, assignment vs mutation,
late binding. Can reason about code without running it. PROCEED TO NEXT ROUND."

BORDERLINE (4-5/7, some hesitation):
"Knows basics but gaps in understanding. May have memorized without deep model.
WEAK HIRE if other areas strong."

FAIL (< 4/7 or major confusion):
"Does not understand Python's scope model. Missing fundamental knowledge.
Cannot reason about closures or binding. REJECT."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ═══════════════════════════════════════════════════════════════════════
# 8️⃣ SELF-ASSESSMENT CHECK
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARE YOU READY? (BE HONEST)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CRITICAL (Must answer YES to ALL):
───────────────────────────────────
□ Can recite LEGB without hesitation
□ Know when UnboundLocalError occurs
□ Understand assignment creates local binding
□ Know difference between global and nonlocal
□ Can explain closure late binding
□ Can predict output of scope puzzles
□ Know when to use global (and when NOT to)

IMPORTANT (Should answer YES to 5/7):
──────────────────────────────────────
□ Understand mutation vs assignment distinction
□ Know how to fix late binding trap
□ Understand list comprehension scope in Python 3
□ Can explain why x += 1 causes UnboundLocalError
□ Know that loop variables leak (except comprehensions)
□ Can explain when nonlocal is appropriate
□ Understand closure captures reference, not value

ADVANCED (Bonus - 3/5):
───────────────────────
□ Know that UnboundLocalError is subclass of NameError
□ Understand compile-time vs runtime scope analysis
□ Can explain class scope differences
□ Know Python 2 vs 3 comprehension scope differences
□ Understand when closures share vs don't share variables

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SCORING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CRITICAL < 7/7:
"FAIL - Missing fundamental understanding of Python scope. This is elimination-level
knowledge. Cannot proceed without mastering these concepts."

CRITICAL = 7/7, IMPORTANT < 5/7:
"BORDERLINE - Knows basics but lacks depth. Practice scope puzzles and edge cases.
May struggle with complex closure scenarios."

CRITICAL = 7/7, IMPORTANT >= 5/7:
"PASS - Solid understanding of Python scope model. Can reason about code behavior.
Ready for this portion of interview."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT INTERVIEWERS CONCLUDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

IF YOU PASS:
"Candidate has correct mental model of Python's scope. Can reason about name
binding, closures, and variable lifetime. Understands LEGB and when to use
global/nonlocal. This is senior-level Python knowledge."

IF YOU FAIL:
"Candidate has been writing Python but doesn't understand how it works. Likely
learned through trial and error without grasping the model. Would cause bugs in
production. Cannot trust to make correct scope decisions. REJECT."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EXACT TOPICS TO REVISIT IF FAILING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Missed LEGB questions? → Read Python docs on Name Resolution
Missed UnboundLocalError? → Practice assignment vs read distinctions
Missed late binding? → Study closure variable capture, practice loop+lambda
Missed global/nonlocal? → Understand scope modification semantics
Missed predictions? → Work through more output puzzles, explain reasoning

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BOTTOM LINE:
If you can't predict scope behavior WITHOUT running code, you're not ready.
This is FUNDAMENTAL Python. No exceptions for 5+ YOE positions.

Study until you can explain EVERY scope puzzle confidently.
"""
