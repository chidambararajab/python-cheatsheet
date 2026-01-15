"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 PYTHON OBJECT MODEL - ELIMINATION INTERVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Interviewer: Principal Engineer | Elimination Round
Target: 5+ YOE | Purpose: Filter those who don't understand Python's object model
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣ OVERVIEW

WHY OBJECT MODEL QUESTIONS:
──────────────────────────
Understanding __eq__, __hash__, __repr__ separates senior engineers from those
who just use classes without understanding how Python objects work.

WEAK CANDIDATES:
───────────────
❌ Don't know __eq__ and __hash__ must be consistent
❌ Override __eq__ without __hash__
❌ Think __repr__ and __str__ are same
❌ Don't understand why objects can't be dict keys after overriding __eq__

STRONG MENTAL MODEL:
───────────────────
✓ __eq__ defines equality, __hash__ enables hashing
✓ If override __eq__, must override __hash__ or set to None
✓ __repr__ for developers, __str__ for users
✓ Immutable objects can be hashable, mutable cannot
✓ Hashable = immutable + implements __hash__

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

2️⃣ CONCEPT BREAKDOWN

╔═══════════════════════════╦═══════════╦════════════════════════════════╗
║ CONCEPT                   ║ FREQUENCY ║ WHAT TESTED                    ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ __eq__ vs __hash__        ║ HIGH      ║ Consistency requirement        ║
║                           ║           ║ REJECT: Breaks consistency     ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ Hashability rules         ║ HIGH      ║ When object can be dict key    ║
║                           ║           ║ REJECT: Doesn't understand     ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ __repr__ vs __str__       ║ MEDIUM    ║ Developer vs user string       ║
║                           ║           ║ REJECT: Confuses them          ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ dataclass behavior        ║ MEDIUM    ║ Auto-generated methods         ║
╚═══════════════════════════╩═══════════╩════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

3️⃣ INTERVIEW QUESTIONS

SECTION 3A: __eq__ and __hash__ (HIGH - CRITICAL)
──────────────────────────────────────────────────

① WARM-UP
──────────
Q: "What's the relationship between __eq__ and __hash__?"

STRONG: "Objects that compare equal must have same hash. If a == b, then hash(a)
must equal hash(b). If you override __eq__, must override __hash__ to maintain
this invariant, or set __hash__ = None to make object unhashable."

WEAK: "They're both for comparisons?" ✗ VAGUE

② CORE
──────
Q: "What's wrong with this?"

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

STRONG: "Overrides __eq__ without __hash__. Python makes class unhashable by
default when __eq__ overridden. Can't use as dict key or in set. Must either:
1. Define __hash__ based on immutable attributes
2. Set __hash__ = None explicitly to document it's unhashable"

③ EDGE-CASE
────────────
Q: "Is this object hashable?"

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))

p = Point(1, 2)
p.x = 3  # Mutated!

STRONG: "Technically hashable (implements __hash__), but DANGEROUS. Attributes are
mutable. If you add to dict, then mutate, hash changes - dict breaks. Should either:
1. Make attributes immutable (use __slots__ or property with no setter)
2. Set __hash__ = None
3. Use frozen dataclass"

④ FOLLOW-UP
────────────
Q: "How does dataclass handle this?"

from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

STRONG: "dataclass auto-generates __init__, __eq__, __repr__. By default, does
NOT generate __hash__ if __eq__ generated. To make hashable, use @dataclass(frozen=True)
which makes attributes immutable and generates __hash__."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 3B: __repr__ vs __str__ (MEDIUM)
─────────────────────────────────────────

① WARM-UP
──────────
Q: "Difference between __repr__ and __str__?"

STRONG:
"__repr__: For developers. Should be unambiguous, ideally eval(repr(obj)) recreates obj.
         Used by repr(), shown in REPL, used as fallback for str().
__str__:  For users. Human-readable. Used by str(), print().

If only one, implement __repr__."

② CORE
──────
Q: "What should Point(1, 2)'s __repr__ return?"

STRONG: "'Point(1, 2)' - valid Python expression that recreates object.

def __repr__(self):
    return f'Point({self.x}, {self.y})'

Not 'x=1, y=2' or '<Point object>' - should be recreatable."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

4️⃣ THINK-ALOUD

QUESTION: "Why can't I add this object to a set?"

class Person:
    def __init__(self, name):
        self.name = name
    
    def __eq__(self, other):
        return self.name == other.name

p = Person("Alice")
s = {p}  # TypeError!

STRONG: "When you override __eq__, Python sets __hash__ = None by default. This
makes object unhashable. Can't add to set or use as dict key. Must implement
__hash__ that's consistent with __eq__:

def __hash__(self):
    return hash(self.name)

And ideally make name immutable."

WEAK: "It's a bug in Python?" ✗ DOESN'T UNDERSTAND

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

5️⃣ OUTPUT PREDICTION

PROBLEM 1:
──────────
class Point:
    def __init__(self, x):
        self.x = x
    def __eq__(self, other):
        return self.x == other.x

p1 = Point(1)
p2 = Point(1)
print(p1 == p2)
print(hash(p1))

OUTPUT:
True
TypeError: unhashable type: 'Point'

REASONING: "__eq__ overridden, so __hash__ set to None. Can compare but not hash."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

6️⃣ COMMON FAILURES

FAILURE #1: OVERRIDING __eq__ WITHOUT __hash__
═══════════════════════════════════════════════

WRONG:
class User:
    def __eq__(self, other):
        return self.id == other.id
# Now unhashable! Can't use in dict/set

CORRECT:
class User:
    def __eq__(self, other):
        return self.id == other.id
    def __hash__(self):
        return hash(self.id)  # Use immutable attribute

FAILURE #2: MUTABLE + HASHABLE
═══════════════════════════════

DANGEROUS:
class Point:
    def __init__(self, x):
        self.x = x  # Mutable!
    def __hash__(self):
        return hash(self.x)

p = Point(1)
d = {p: "value"}
p.x = 2  # Hash changed! Dict broken!

FIX: Use frozen dataclass or make attributes read-only.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

7️⃣ MOCK INTERVIEW

Q1: "Override __eq__, what must you do?"
EXPECTED: "Override __hash__ or set to None" [< 10 sec]

Q2: "Why can't mutable objects be dict keys?"
EXPECTED: "Hash would change, breaking dict" [< 10 sec]

Q3: "__repr__ vs __str__?"
EXPECTED: "__repr__ for devs (unambiguous), __str__ for users" [< 10 sec]

Q4: "What does @dataclass(frozen=True) do?"
EXPECTED: "Makes immutable, auto-generates __hash__" [< 10 sec]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

8️⃣ SELF-ASSESSMENT

CRITICAL (ALL required):
────────────────────────
□ Know __eq__ and __hash__ must be consistent
□ Know overriding __eq__ makes unhashable by default
□ Understand why mutable objects can't be dict keys
□ Know difference __repr__ vs __str__
□ Can implement correct __hash__

SCORING:
< 5/5: FAIL
5/5: PASS

INTERVIEWER:
IF FAIL: "Doesn't understand Python object model. Would break dicts/sets. REJECT."
"""
