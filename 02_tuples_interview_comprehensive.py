"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 PYTHON TUPLES - SENIOR ENGINEER INTERVIEW PREPARATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Interviewer: Senior Engineer | Bar-Raiser
Level: 5+ YOE | Focus: Immutability & Hashability Mastery
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣ OVERVIEW: WHY TUPLES MATTER
Tuples appear less frequently than lists/dicts but are CRITICAL for:
• Dictionary keys (coordinates, edges)
• Function returns (multiple values)
• Immutable data guarantees
• Hashable sequences
• Unpacking patterns (swapping, destructuring)

INTERVIEWERS EXPECT:
✓ Know tuple vs list - when to use which
✓ Tuple unpacking (a, b = b, a for swap)
✓ Use tuples as dict keys
✓ Understand immutability implications
✓ Single-element tuple syntax (x,)

STRONG vs WEAK:
STRONG: Uses tuples for coordinates immediately, swaps with unpacking
WEAK: Doesn't know single-element syntax, tries to modify tuples

REJECTION SIGNALS:
❌ Tries to modify tuple (append, remove)
❌ Forgets comma in (5,)
❌ Doesn't know tuples are hashable
❌ Can't explain shallow immutability

2️⃣ CONCEPT CLASSIFICATION
╔═══════════════════╦═══════════╦═══════════════════════════════╗
║ CONCEPT           ║ FREQUENCY ║ WHY TESTED / REJECTION        ║
╠═══════════════════╬═══════════╬═══════════════════════════════╣
║ Immutability      ║ HIGH      ║ Core understanding            ║
║                   ║           ║ REJECT: Tries to modify       ║
╠═══════════════════╬═══════════╬═══════════════════════════════╣
║ Dict keys         ║ HIGH      ║ Coordinates, memoization      ║
║                   ║           ║ REJECT: Uses list as key      ║
╠═══════════════════╬═══════════╬═══════════════════════════════╣
║ Unpacking         ║ HIGH      ║ Swapping, multiple returns    ║
║                   ║           ║ REJECT: Uses temp variable    ║
╠═══════════════════╬═══════════╬═══════════════════════════════╣
║ Single-element    ║ MEDIUM    ║ Common syntax trap            ║
║                   ║           ║ REJECT: (5) vs (5,)           ║
╠═══════════════════╬═══════════╬═══════════════════════════════╣
║ Shallow immutable ║ MEDIUM    ║ Nested mutability             ║
╚═══════════════════╩═══════════╩═══════════════════════════════╝

3️⃣ INTERVIEW QUESTIONS

SECTION 3A: IMMUTABILITY (HIGH)
① WARM-UP: Tuple vs list - when to use?
EXPECTED: "Tuple for immutable data (coordinates, returns). List for mutable collections.
Tuple is hashable, can be dict key. List cannot."

② CORE: Why use tuple for graph edges?
EXPECTED: "Edge (u,v) is immutable data. Tuple can be dict key for edge properties:
weights = {(0,1): 5, (1,2): 3}. List can't be key because it's mutable."

③ EDGE-CASE: Can you modify tuple with mutable elements?
t = ([1,2], [3,4])
t[0].append(99)  # Works! Modifies inner list

EXPECTED: "Tuple is shallow immutable. Can't reassign t[0] to new list, but CAN
modify existing list inside. This is a trap question."

④ FOLLOW-UP: Implement immutable point class.
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
# p.x = 5  # Error - truly immutable

SECTION 3B: DICT KEYS (HIGH)
① WARM-UP: Why can tuple be dict key but not list?
EXPECTED: "Dict keys must be hashable (immutable). Tuples are hashable, lists aren't.
If list could be key and you modify it, hash changes - dict breaks."

② CORE: Memoization for 2-parameter function.
def fib_2d(m, n, memo={}):
    if (m, n) in memo:  # Tuple as key!
        return memo[(m, n)]
    # ... compute result ...
    memo[(m, n)] = result
    return result

INTERVIEWER EXPECTS: Tuple key usage
✓ STRONG: Uses (m, n) automatically
✗ WEAK: Tries "m,n" string or doesn't know how

③ EDGE-CASE: Grid problem with visited cells.
visited = set()
visited.add((row, col))  # Tuple in set
if (r, c) in visited:  # O(1) check

EXPECTED: "Use tuple for coordinates because hashable. Can add to set/use as dict key."

④ FOLLOW-UP: Undirected graph edges.
# Problem: Edge (1,2) same as (2,1) in undirected graph
edges = {tuple(sorted([u, v])): weight}  # Normalize
# OR use frozenset (unordered, hashable)
edges = {frozenset([u, v]): weight}

SECTION 3C: UNPACKING (HIGH)
① WARM-UP: Pythonic way to swap variables?
EXPECTED: "a, b = b, a. Uses tuple packing/unpacking. No temp variable needed."

② CORE: Function returning multiple values.
def get_stats(nums):
    return min(nums), max(nums), sum(nums)

minimum, maximum, total = get_stats([1,2,3])  # Unpacking

INTERVIEWER EXPECTS: Natural tuple returns
✓ STRONG: Returns tuple, unpacks naturally
✗ WEAK: Returns dict or separate variables

③ EDGE-CASE: Extended unpacking with *.
first, *middle, last = (1, 2, 3, 4, 5)
# first=1, middle=[2,3,4], last=5

EXPECTED: "Star * captures variable-length middle. Useful for ignoring values:
_, *data = line.split()  # Ignore first element"

④ FOLLOW-UP: Ignoring values with _.
x, _, z = (10, 20, 30)  # Ignore middle
for _, value in enumerate(items):  # Ignore index

SECTION 3D: SINGLE-ELEMENT TRAP (MEDIUM)
① CORE: Create single-element tuple.
not_tuple = (5)      # int 5, parens ignored
is_tuple = (5,)      # tuple, comma required
also_tuple = 5,      # comma makes it tuple

EXPECTED: "Comma creates tuple, not parens. (5) is just 5 in parens. (5,) is tuple."

INTERVIEWER TESTS: Can you spot the bug?
coords = (x, y)  # Correct
single = (value)  # ❌ Bug! Not a tuple
single = (value,)  # ✅ Correct

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

4️⃣ THINK-ALOUD ANSWERS

PROBLEM: Swap two variables

STRONG: "I'll use tuple unpacking: a, b = b, a. Python packs right side into tuple
(b, a), then unpacks into a and b. No temp variable, Pythonic."

WEAK: "temp = a; a = b; b = temp"
INTERVIEWER: "More Pythonic way?"
WEAK: [Doesn't know] ✗ NO HIRE for 5+ YOE

PROBLEM: Track visited grid cells

STRONG: "I'll use set of (row, col) tuples. Tuples are hashable so can go in set.
O(1) membership check. visited.add((r, c)); if (r,c) in visited..."

WEAK: "List of lists? visited = [[False]*cols for _ in rows]"
INTERVIEWER: "That's O(m*n) space. Better?"
WEAK: [Suggests dict] ✗ Misses set + tuple solution

5️⃣ LIVE CODING: GRAPH PROBLEM WITH EDGES

PROBLEM: Build undirected graph, store edge weights.

BRUTE FORCE (List of lists):
weights = [[0]*n for _ in range(n)]  # O(n²) space
weights[u][v] = w
weights[v][u] = w

OPTIMAL (Dict with tuple keys):
weights = {}
for u, v, w in edges:
    weights[(u, v)] = w
    weights[(v, u)] = w  # Undirected

# Access: weights[(a, b)]

EVEN BETTER (Normalize with sorted):
weights = {}
for u, v, w in edges:
    edge = tuple(sorted([u, v]))  # (min, max)
    weights[edge] = w

# Access: weights[tuple(sorted([a, b]))]

INTERVIEWER EVALUATION:
✓ STRONG: Uses tuple keys immediately
✓ HIRE: Gets there with hints
✗ NO HIRE: Doesn't think of tuples

6️⃣ PATTERN RECOGNITION

PATTERN: COORDINATE STORAGE
Signal: "Grid", "matrix", "board", "2D positions"
Template: (row, col) as tuple, store in set/dict
Problems: Number of Islands, Word Search, Sudoku

PATTERN: MULTIPLE RETURNS
Signal: Function needs to return 2+ values
Template: return val1, val2, val3  # Tuple packing
Problems: Helper functions, divide and conquer splits

PATTERN: DICT KEY COMBINATIONS
Signal: Memoization with multiple params, caching
Template: memo[(param1, param2, param3)] = result
Problems: DP problems, graph state tracking

7️⃣ COMMON FAILURES

FAILURE #1: SINGLE-ELEMENT SYNTAX
❌ my_tuple = (5)  # This is int 5!
✓ my_tuple = (5,) # Comma makes it tuple

FAILURE #2: TRYING TO MODIFY
❌ t = (1, 2, 3)
   t[0] = 5  # TypeError!
✓ Create new tuple: t = (5, 2, 3)

FAILURE #3: USING LIST AS DICT KEY
❌ cache[[1, 2]] = value  # TypeError!
✓ cache[(1, 2)] = value   # Tuple works

FAILURE #4: NOT USING UNPACKING
❌ temp = a; a = b; b = temp
✓ a, b = b, a  # Pythonic swap

8️⃣ MOCK INTERVIEW

RAPID-FIRE (2 minutes):

Q1: "Tuple vs list - main difference?"
A: "Tuples immutable, hashable. Lists mutable, not hashable."

Q2: "How to create single-element tuple?"
A: "(value,) with comma"

Q3: "Swap a and b in one line."
A: "a, b = b, a"

Q4: "Can tuple be dict key?"
A: "Yes, because hashable"

Q5: "What's wrong: coords = (x, y, z)?"
A: "Nothing, that's correct 3-tuple"

MAIN PROBLEM (15 minutes):

"Store and query shortest path between node pairs in graph. Nodes 0-n."

STRONG CANDIDATE:
paths = {}  # (u, v) -> distance
for u, v, dist in edges:
    paths[(u, v)] = dist
    paths[(v, u)] = dist

def get_distance(a, b):
    return paths.get((a, b), float('inf'))

INTERVIEWER: ✓ HIRE - Tuple keys, clean solution

9️⃣ SELF-ASSESSMENT

TIER 1 MUST KNOW (6/6):
□ Tuple immutability
□ Single-element syntax (x,)
□ Tuple as dict key/set element
□ Unpacking (a, b = tuple)
□ Swap with unpacking
□ When tuple vs list

TIER 2 SHOULD KNOW (4/5):
□ Extended unpacking (*)
□ namedtuple
□ Shallow immutability
□ Multiple returns with tuples
□ frozenset for unordered keys

SCORING:
TIER 1 < 6/6: NOT READY
TIER 1 = 6/6, TIER 2 >= 3/5: READY

CRITICAL: Can you explain why tuples can be dict keys?
NO → Not ready

INTERVIEWER CONCLUSION:
< 6/6 TIER 1: "Doesn't understand immutability. Concerning gap. REJECT."
6/6 TIER 1: "Solid tuple knowledge. Will handle coordinate/key problems. HIRE."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FINAL: Tuples are your friend for immutable sequences and hashable keys.
Master (x,y) coordinates and you'll handle 80% of tuple interview scenarios.
"""
