"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 PYTHON EXECUTION MODEL - ELIMINATION INTERVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Interviewer: Principal Engineer | Runtime Expert | Elimination Round
Target: 5+ YOE | Purpose: Filter those who don't understand Python's object model
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣ OVERVIEW

WHY EXECUTION MODEL QUESTIONS:
──────────────────────────────
This is where "experienced" candidates reveal they've been writing Python without
understanding WHAT HAPPENS when code executes. These questions ruthlessly filter.

FILTERS:
• Those who think variables contain values (Java/C++ thinking)
• Candidates who confuse assignment with mutation
• Engineers who don't understand object identity
• People who can't explain is vs ==
• Those who don't grasp reference semantics

WEAK CANDIDATES MISUNDERSTAND:
──────────────────────────────
❌ Think variables "store" values like boxes
❌ Confuse rebinding with mutation
❌ Don't understand everything is an object
❌ Can't explain when is vs == differ
❌ Think copying is automatic
❌ Don't know what id() returns
❌ Treat immutable objects like mutable ones

STRONG MENTAL MODEL:
───────────────────
✓ Variables are NAME BINDINGS, not containers
✓ Assignment creates binding, doesn't copy
✓ Mutation modifies object, assignment rebinds name
✓ id() is object identity (memory address)
✓ is checks identity, == checks value
✓ Immutable objects can't be changed in-place
✓ Mutable objects can be aliased

ELIMINATION:
───────────
- Thinks x = y copies y → REJECT
- Doesn't know is vs == → REJECT
- Can't explain aliasing → REJECT
- Confuses binding with mutation → REJECT

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

2️⃣ CONCEPT BREAKDOWN

╔═══════════════════════════╦═══════════╦════════════════════════════════╗
║ CONCEPT                   ║ FREQUENCY ║ WHAT INTERVIEWERS TEST         ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ Name binding vs mutation  ║ HIGH      ║ Assignment creates binding     ║
║                           ║           ║ REJECT: Thinks it copies       ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ is vs ==                  ║ HIGH      ║ Identity vs equality           ║
║                           ║           ║ REJECT: Uses interchangeably   ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ Mutable vs immutable      ║ HIGH      ║ What can be changed in-place   ║
║                           ║           ║ REJECT: Thinks strings mutable ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ Object identity (id)      ║ HIGH      ║ What id() means                ║
║                           ║           ║ REJECT: Doesn't know           ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ Shallow vs deep copy      ║ MEDIUM    ║ Nested object copying          ║
║                           ║           ║ REJECT: Doesn't know difference║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ Reference passing         ║ HIGH      ║ How arguments are passed       ║
║                           ║           ║ REJECT: Says "pass by value"   ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ Garbage collection basics ║ LOW       ║ When objects deleted           ║
╚═══════════════════════════╩═══════════╩════════════════════════════════╝

WRONG BELIEFS:
─────────────
❌ "x = y copies the value" (WRONG - creates second binding to same object)
❌ "is and == are similar" (WRONG - identity vs equality)
❌ "Strings are mutable" (WRONG - immutable)
❌ "Python passes by value" (IMPRECISE - passes object reference)
❌ "Assignment to list element creates new list" (WRONG - mutation)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

3️⃣ INTERVIEW QUESTIONS

SECTION 3A: NAME BINDING VS MUTATION (HIGH - FUNDAMENTAL)
──────────────────────────────────────────────────────────

① WARM-UP ELIMINATION
──────────────────────
Q: "What does x = y do in Python?"

STRONG ANSWER:
"Creates a new binding. Variable x now refers to the same object that y refers to.
Does NOT create a copy of the object. Both names point to the same object in memory."

WEAK ANSWER:
"Assigns y to x?" ✗ VAGUE
"Copies the value?" ✗ WRONG, fundamental misunderstanding
"Makes x equal to y?" ✗ IMPRECISE

② CORE REASONING
─────────────────
Q: "Predict output. Explain why."

a = [1, 2, 3]
b = a
b.append(4)
print(a)

STRONG ANSWER:
"Prints [1, 2, 3, 4]. Statement 'b = a' creates binding - b refers to SAME list
object as a. They're aliases. When we mutate via b.append(4), we're modifying
the single shared list. Both a and b see the change because they reference the
same object."

WEAK ANSWER:
"Prints [1, 2, 3]?" ✗ WRONG, thinks b is a copy
"Depends?" ✗ WRONG, deterministic behavior

③ EDGE-CASE
────────────
Q: "What about this?"

a = [1, 2, 3]
b = a
b = [4, 5, 6]
print(a)

STRONG ANSWER:
"Prints [1, 2, 3]. First 'b = a' makes b refer to same list. Then 'b = [4,5,6]'
REBINDS b to a NEW list object. This is ASSIGNMENT, not mutation. a still refers
to original list, unchanged. Assignment changes what name refers to, doesn't
modify the object."

WEAK: Can't distinguish rebinding from mutation ✗ FUNDAMENTAL GAP

④ FOLLOW-UP
────────────
Q: "How do you actually copy a list?"

STRONG ANSWER:
"Shallow copy: b = a[:] or b = a.copy() or b = list(a)
Deep copy: import copy; b = copy.deepcopy(a)

Shallow copies top-level list but nested objects are still shared.
Deep copy recursively copies all nested objects."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 3B: is vs == (HIGH)
────────────────────────────

① WARM-UP
──────────
Q: "What's the difference between is and ==?"

STRONG ANSWER:
"is checks object IDENTITY - whether two names refer to the exact same object in
memory. Compares id() values. == checks VALUE EQUALITY - whether objects have
equivalent values. Calls __eq__() method."

WEAK ANSWER:
"is is stricter?" ✗ VAGUE
"They're similar?" ✗ WRONG
"is checks type?" ✗ WRONG, that's isinstance

② CORE REASONING
─────────────────
Q: "Predict output:"

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)

STRONG ANSWER:
"Prints True, False. a == b is True because lists have same VALUES. a is b is
False because they're DIFFERENT objects in memory (different id values). Two
separate list objects that happen to contain same elements."

WEAK: Can't explain ✗ DOESN'T UNDERSTAND IDENTITY

③ EDGE-CASE
────────────
Q: "What about this?"

a = 256
b = 256
print(a is b)

c = 257
d = 257
print(c is d)

STRONG ANSWER:
"First prints True, second typically prints False (implementation detail). Python
INTERNS small integers (-5 to 256 in CPython) for efficiency. a and b reference
SAME integer object. Larger integers (257) not interned, so c and d are different
objects even with same value. This is an optimization, not guaranteed by spec."

CRITICAL: Never use 'is' to compare values, only for singleton checks like 'is None'.

④ FOLLOW-UP
────────────
Q: "When should you use is?"

STRONG ANSWER:
"Use is ONLY for identity checks with singletons:
- x is None (recommended)
- x is True / is False (rare, usually just 'if x:')
- x is NotImplemented

Never use is to compare values like numbers or strings. Always use == for that."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 3C: MUTABLE VS IMMUTABLE (HIGH)
────────────────────────────────────────

① WARM-UP
──────────
Q: "List immutable and mutable built-in types."

STRONG ANSWER:
"Immutable: int, float, str, tuple, frozenset, bytes
Mutable: list, dict, set, bytearray

Immutable objects cannot be modified in-place. Operations create new objects.
Mutable objects can be modified in-place via methods like append(), pop()."

WEAK: Can't list them ✗ FUNDAMENTAL GAP

② CORE REASONING
─────────────────
Q: "Explain this behavior:"

s = "hello"
print(id(s))
s = s + " world"
print(id(s))
# Different ids

vs

lst = [1, 2]
print(id(lst))
lst.append(3)
print(id(lst))
# Same ids

STRONG ANSWER:
"Strings are immutable. s + ' world' creates NEW string object. Assignment rebinds
s to new object. id changes because s refers to different object.

Lists are mutable. append() modifies EXISTING list object in-place. id stays same
because lst still refers to same object, just modified."

③ EDGE-CASE
────────────
Q: "What about tuple with mutable element?"

t = ([1, 2], 3)
t[0].append(99)
print(t)

STRONG ANSWER:
"Prints ([1, 2, 99], 3). Tuple itself is immutable - can't reassign t[0]. But
tuple CONTAINS reference to mutable list. We can mutate that list via t[0].append().
This is shallow immutability. Tuple structure can't change, but contained objects
can be mutated if they're mutable."

WEAK: "Error?" ✗ WRONG
"Tuple prevents changes?" ✗ OVERSIMPLIFIED

④ FOLLOW-UP
────────────
Q: "Why are immutable objects used as dict keys?"

STRONG ANSWER:
"Dict keys must be hashable. Hashable objects have constant hash value throughout
lifetime. Immutable objects satisfy this - their hash can't change because their
value can't change. Mutable objects can't be keys because modifying them would
invalidate their hash, breaking the dict."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 3D: REFERENCE PASSING (HIGH)
─────────────────────────────────────

① WARM-UP
──────────
Q: "Does Python pass by value or by reference?"

STRONG ANSWER:
"Neither - Python passes object REFERENCES by value. When you call function with
argument, Python passes the reference to the object. Inside function, parameter
name binds to same object. You can't rebind caller's variable, but you CAN mutate
the object if it's mutable."

WEAK ANSWER:
"Pass by value?" ✗ IMPRECISE
"Pass by reference?" ✗ IMPRECISE  
"Depends on type?" ✗ WRONG

② CORE REASONING
─────────────────
Q: "Predict output:"

def modify(lst):
    lst.append(4)
    lst = [99]  # Does this affect caller?

original = [1, 2, 3]
modify(original)
print(original)

STRONG ANSWER:
"Prints [1, 2, 3, 4]. Inside modify, lst initially refers to same list as original.
lst.append(4) mutates that shared list. Then 'lst = [99]' REBINDS lst to NEW list.
This doesn't affect original - rebinding is local. Caller sees mutation (append)
but not rebinding."

WEAK: "Prints [99]?" ✗ DOESN'T UNDERSTAND REBINDING VS MUTATION

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

4️⃣ THINK-ALOUD ANSWERS

QUESTION: "Explain this:"

a = [1, 2, 3]
b = a
a.append(4)
print(b)

STRONG CANDIDATE:
"Prints [1, 2, 3, 4]. When we write 'b = a', we're not copying the list. We're
creating a second NAME that refers to the SAME list object in memory. Both a and b
are bindings to the same object. When we call a.append(4), we're mutating the
shared list object. Since b refers to that same object, printing b shows the
modified list. They're aliases - two names for one thing."

KEYWORDS:
✓ "Same object"
✓ "Binding" or "reference"
✓ "Not copying"
✓ "Aliases"

WEAK:
"Because b equals a?"

RED FLAGS:
❌ Doesn't mention "same object"
❌ No understanding of binding
❌ Can't explain mechanism

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

5️⃣ OUTPUT PREDICTION

PROBLEM 1:
──────────
x = [1, 2]
y = x
y += [3]
print(x)

OUTPUT: [1, 2, 3]
REASONING: "y = x creates alias. y += [3] is IN-PLACE for lists (calls __iadd__,
modifies object). x sees change because x and y reference same object."

───────────────────────────────────────────────────────────────────────

PROBLEM 2:
──────────
x = (1, 2)
y = x
y += (3,)
print(x)
print(x is y)

OUTPUT: (1, 2)
        False
REASONING: "Tuples immutable. y += (3,) creates NEW tuple, rebinds y. x unchanged,
still refers to original. x is y False because different objects after rebinding."

───────────────────────────────────────────────────────────────────────

PROBLEM 3:
──────────
a = [1, [2, 3], 4]
b = a[:]  # Shallow copy
b[1].append(99)
print(a)

OUTPUT: [1, [2, 99, 3], 4]
REASONING: "Shallow copy copies top-level list only. Nested list [2,3] is SHARED
between a and b. Modifying via b[1].append affects the shared nested list. Both
see change."

COMMON WRONG: "[1, [2, 3], 4]" ✗ Doesn't understand shallow copy

───────────────────────────────────────────────────────────────────────

PROBLEM 4:
──────────
a = 1000
b = 1000
print(a is b)

OUTPUT: Likely False (implementation dependent)
REASONING: "Large integers not interned. Two separate 1000 objects created. a is b
compares identity (False). Note: a == b would be True. Never rely on integer
interning for correctness."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

6️⃣ COMMON FAILURE MODES

FAILURE #1: THINKING ASSIGNMENT COPIES
═══════════════════════════════════════

WRONG BELIEF: "x = y copies y's value to x"

REALITY: Creates binding. x refers to same object as y.

CODE:
a = [1, 2]
b = a  # NOT a copy!
b.append(3)
print(a)  # [1, 2, 3] - SURPRISE to those who think b is copy

FIX: Explicitly copy if needed: b = a[:] or b = a.copy()

───────────────────────────────────────────────────────────────────────

FAILURE #2: MISUSING is FOR EQUALITY
═════════════════════════════════════

WRONG:
if name is "John":  # WRONG! Checks identity, not value
    ...

CORRECT:
if name == "John":  # Checks value equality
    ...

ONLY use is for: None, True, False, NotImplemented

───────────────────────────────────────────────────────────────────────

FAILURE #3: NOT UNDERSTANDING SHALLOW COPY
═══════════════════════════════════════════

TRAP:
matrix = [[1, 2], [3, 4]]
copy_matrix = matrix[:]
copy_matrix[0][0] = 999
print(matrix)  # [[999, 2], [3, 4]] - SURPRISE!

REASON: Shallow copy. Inner lists are shared.

FIX: import copy; copy_matrix = copy.deepcopy(matrix)

───────────────────────────────────────────────────────────────────────

FAILURE #4: CONFUSING MUTABILITY
═════════════════════════════════

WRONG: Thinking += always creates new object

REALITY:
- For mutable (list): x += y modifies in-place
- For immutable (tuple/str): x += y creates new, rebinds x

PROOF:
lst = [1]
id_before = id(lst)
lst += [2]
id_after = id(lst)
# Same id - modified in-place

tup = (1,)
id_before = id(tup)
tup += (2,)
id_after = id(tup)
# Different id - new tuple created

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

7️⃣ MOCK INTERVIEW

RAPID-FIRE (2 minutes):

Q1: "What does x = y do?"
EXPECTED: "Creates binding - x refers to same object as y" [< 5 sec]
REJECT IF: "Copies y"

Q2: "Difference between is and ==?"
EXPECTED: "is checks identity, == checks equality" [< 5 sec]

Q3: "Name 3 immutable types"
EXPECTED: "int, str, tuple" [< 5 sec]

Q4: "This code - what prints?"
    a = [1]; b = a; b.append(2); print(a)
EXPECTED: "[1, 2]" [< 10 sec]
REJECT IF: "[1]"

Q5: "How to check if x is None?"
EXPECTED: "x is None" [< 3 sec]
REJECT IF: "x == None" (works but not idiomatic)

Q6: "What does id() return?"
EXPECTED: "Object identity / memory address" [< 5 sec]

Q7: "Can you modify a tuple?"
EXPECTED: "No - immutable. Can modify mutable elements inside though" [< 10 sec]

PRESSURE:

INTERVIEWER: "You said b = a doesn't copy. So what DOES it do?"

STRONG: "Creates a new binding. Variable b now refers to the same object that a
refers to. They're aliases. One object, two names."

WEAK: "Um... it links them?" ✗ VAGUE, doesn't use proper terminology

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

8️⃣ SELF-ASSESSMENT

CRITICAL (ALL required):
────────────────────────
□ Understand assignment creates binding, not copy
□ Know is checks identity, == checks equality
□ Can list immutable and mutable types
□ Understand mutation vs rebinding
□ Know when to use is (only None, True, False)
□ Understand shared object references
□ Know difference shallow vs deep copy

IMPORTANT (5/7):
─────────────────
□ Can predict aliasing behavior
□ Know what id() returns
□ Understand += behavior differs by type
□ Know why lists can't be dict keys
□ Understand tuple with mutable elements
□ Can explain pass-by-object-reference
□ Know integer interning (small ints)

SCORING:

CRITICAL < 7/7: FAIL - Missing fundamental Python execution model
CRITICAL = 7/7, IMPORTANT < 5/7: BORDERLINE
CRITICAL = 7/7, IMPORTANT >= 5/7: PASS

INTERVIEWER CONCLUSION:

IF PASS: "Understands Python's object model and reference semantics. Knows binding
vs mutation, identity vs equality. Won't write bugs due to aliasing."

IF FAIL: "Treats Python like Java/C++. Doesn't understand how Python actually
works. Would cause production bugs. REJECT."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BOTTOM LINE:
If you think x = y copies y, you don't understand Python. This is FOUNDATIONAL.
Master binding, identity, and mutability before claiming Python expertise.
"""
