"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 PYTHON TUPLES - INTERVIEW MASTERY GUIDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
For 5+ YOE Developer | Interview-Focused | Complete Reference
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 WHAT IS IT?
-------------
Tuple = Immutable sequence (like a read-only list)
- Fixed size after creation
- Faster than lists (slight performance edge)
- Hashable (can be dict keys or set elements)

📌 WHY IT EXISTS?
----------------
✓ Data integrity: Prevent accidental modification
✓ Dict keys: Lists can't be keys, tuples can
✓ Multiple return values from functions
✓ Memory optimization: Slightly more efficient than lists
✓ Signal intent: "This data shouldn't change"

📌 WHEN INTERVIEWERS EXPECT IT?
------------------------------
✓ Returning multiple values from helper functions
✓ Dictionary keys for coordinates: (x, y)
✓ Graph edges: (u, v) or (u, v, weight)
✓ Memoization keys for multi-parameter problems
✓ Immutable data structures

🚨 COMMON MISTAKES THAT FAIL INTERVIEWS
---------------------------------------
❌ Trying to modify tuple (causes TypeError)
❌ Forgetting comma for single-element tuple: (5) vs (5,)
❌ Not knowing tuples are hashable (perfect for dict keys)
❌ Creating tuple when list is more appropriate
❌ Not understanding tuple unpacking

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

# ═══════════════════════════════════════════════════════════════════════
# 1️⃣ CREATION & BASIC OPERATIONS
# ═══════════════════════════════════════════════════════════════════════

# Basic creation
coords = (10, 20)
rgb = (255, 128, 0)
mixed = (1, "hello", 3.14)

# Without parentheses (tuple packing)
point = 5, 10  # Same as (5, 10)
print(f"Point: {point}, Type: {type(point)}")

# Empty tuple
empty = ()

# 🚨 SINGLE-ELEMENT TUPLE TRAP
not_a_tuple = (5)      # This is just int 5 with parens!
print(f"(5) is type: {type(not_a_tuple)}")  # <class 'int'>

is_a_tuple = (5,)      # ✅ Comma makes it a tuple
print(f"(5,) is type: {type(is_a_tuple)}")  # <class 'tuple'>

# From iterable
tuple_from_list = tuple([1, 2, 3])
tuple_from_string = tuple("abc")  # ('a', 'b', 'c')
print(f"tuple('abc') = {tuple_from_string}")


# ═══════════════════════════════════════════════════════════════════════
# 2️⃣ IMMUTABILITY (CORE CONCEPT)
# ═══════════════════════════════════════════════════════════════════════

print("\n📌 IMMUTABILITY:")

coords = (10, 20)

# ❌ CANNOT modify elements
try:
    coords[0] = 15
except TypeError as e:
    print(f"❌ Cannot modify: {e}")

# ❌ CANNOT add elements
try:
    coords.append(30)
except AttributeError as e:
    print(f"❌ No append method: {e}")

# ✅ CAN create new tuple
coords = (15, 25)  # Reassignment (not mutation)
new_coords = coords + (30,)  # Concatenation creates new tuple
print(f"New coords: {new_coords}")

# 🎤 INTERVIEWER NARRATION:
"""
"I'm using a tuple for coordinates because they shouldn't change after
creation. This also lets me use them as dictionary keys for memoization."
"""

# ⚠️ IMMUTABILITY IS SHALLOW
nested = ([1, 2], [3, 4])
nested[0].append(99)  # ✅ Can modify the LIST inside
print(f"Modified nested tuple: {nested}")  # ([1, 2, 99], [3, 4])


# ═══════════════════════════════════════════════════════════════════════
# 3️⃣ TUPLE UNPACKING (INTERVIEW ESSENTIAL)
# ═══════════════════════════════════════════════════════════════════════

print("\n📌 TUPLE UNPACKING:")

# Basic unpacking
point = (10, 20)
x, y = point
print(f"x={x}, y={y}")

# Multiple return values (MOST COMMON USE CASE)
def get_min_max(nums):
    return min(nums), max(nums)  # Returns tuple

minimum, maximum = get_min_max([3, 1, 4, 1, 5])
print(f"Min: {minimum}, Max: {maximum}")

# 🎤 INTERVIEWER NARRATION:
"""
"My helper function returns both the index and value. I'll use tuple
unpacking to assign them to separate variables: idx, val = find_peak(arr)"
"""

# Unpacking with * (extended unpacking)
first, *middle, last = (1, 2, 3, 4, 5)
print(f"first={first}, middle={middle}, last={last}")
# first=1, middle=[2, 3, 4], last=5

# Ignoring values with _
x, _, z = (10, 20, 30)  # Ignore second value
print(f"x={x}, z={z}")

# Swapping variables (PYTHONIC WAY)
a, b = 5, 10
a, b = b, a  # Swap without temp variable!
print(f"After swap: a={a}, b={b}")

# Compare with Java:
"""
Java:  int temp = a; a = b; b = temp;
Python: a, b = b, a  # Much cleaner!
"""


# ═══════════════════════════════════════════════════════════════════════
# 4️⃣ TUPLE METHODS (Only 2!)
# ═══════════════════════════════════════════════════════════════════════

print("\n📌 TUPLE METHODS:")

data = (1, 2, 3, 2, 4, 2, 5)

# count(value) - Count occurrences
count_2 = data.count(2)
print(f"count(2) = {count_2}")  # 3

# index(value, start=0, end=len) - Find first occurrence
idx = data.index(2)
idx_after = data.index(2, 2)  # Search from index 2
print(f"index(2) = {idx}, index(2, 2) = {idx_after}")

# That's it! Only 2 methods because tuples are immutable


# ═══════════════════════════════════════════════════════════════════════
# 5️⃣ INDEXING & SLICING (Same as Lists)
# ═══════════════════════════════════════════════════════════════════════

print("\n📌 INDEXING & SLICING:")

data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

first = data[0]       # 0
last = data[-1]       # 9
sub = data[2:5]       # (2, 3, 4)
reversed_t = data[::-1]  # (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)

print(f"data[2:5] = {sub}")
print(f"data[::-1] = {reversed_t}")


# ═══════════════════════════════════════════════════════════════════════
# 6️⃣ TUPLES AS DICTIONARY KEYS (INTERVIEW CRITICAL)
# ═══════════════════════════════════════════════════════════════════════

print("\n📌 TUPLES AS DICT KEYS:")

# Graph adjacency with weights
graph = {
    (0, 1): 5,    # Edge from 0 to 1 with weight 5
    (0, 2): 3,
    (1, 2): 2,
    (2, 3): 7
}

print(f"Weight of edge (0,1): {graph[(0, 1)]}")

# Memoization for 2D DP
memo = {}

def longest_common_subsequence(s1, s2, i, j):
    """
    🎤 INTERVIEWER NARRATION:
    "I'll memoize using a tuple (i, j) as the key. This represents the
    current indices in both strings. Tuples are hashable unlike lists,
    so they work perfectly as dict keys."
    """
    if (i, j) in memo:
        return memo[(i, j)]
    
    # ... LCS logic ...
    result = 0  # placeholder
    memo[(i, j)] = result
    return result

# Coordinate-based problems
visited = set()
visited.add((0, 0))
visited.add((0, 1))
visited.add((1, 0))

if (0, 0) in visited:
    print("Position (0,0) already visited")

# 🚨 INTERVIEW TRAP: Can't use lists as keys
try:
    bad_dict = {[1, 2]: "value"}
except TypeError as e:
    print(f"❌ Can't use list as key: {e}")

# ✅ Use tuple instead
good_dict = {(1, 2): "value"}
print(f"✅ Tuple as key works: {good_dict[(1, 2)]}")


# ═══════════════════════════════════════════════════════════════════════
# 7️⃣ TUPLE vs LIST - WHEN TO USE WHICH?
# ═══════════════════════════════════════════════════════════════════════

print("\n📌 TUPLE vs LIST DECISION TREE:")

decision_tree = """
┌─────────────────────────────────────────────────────────────────────┐
│ USE TUPLE WHEN:                                                     │
├─────────────────────────────────────────────────────────────────────┤
│ ✅ Data shouldn't change (coordinates, RGB values)                  │
│ ✅ Need to use as dict key or set element                          │
│ ✅ Returning multiple values from function                         │
│ ✅ Representing fixed structure (name, age, city)                  │
│ ✅ Slight performance gain matters (rare in interviews)            │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ USE LIST WHEN:                                                      │
├─────────────────────────────────────────────────────────────────────┤
│ ✅ Data needs to change (append, remove, sort)                     │
│ ✅ Building result dynamically                                     │
│ ✅ Need list-specific methods (append, pop, sort)                  │
│ ✅ Working with homogeneous data (all same type)                   │
│ ✅ Size will change during algorithm                               │
└─────────────────────────────────────────────────────────────────────┘
"""
print(decision_tree)


# ═══════════════════════════════════════════════════════════════════════
# 8️⃣ INTERVIEW PATTERNS WITH TUPLES
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("🔥 INTERVIEW PATTERNS")
print("="*70)

# ────────────────────────────────────────────────────────────────────────
# PATTERN 1: MULTIPLE RETURN VALUES
# ────────────────────────────────────────────────────────────────────────

def binary_search(arr, target):
    """
    🎤 INTERVIEWER NARRATION:
    "I'll return both the index and whether we found it. This is cleaner
    than returning -1 for not found."
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True, mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False, -1

print("\n▶ MULTIPLE RETURN VALUES:")
found, index = binary_search([1, 3, 5, 7, 9], 5)
print(f"Found: {found}, Index: {index}")


# ────────────────────────────────────────────────────────────────────────
# PATTERN 2: SORTING WITH TUPLES
# ────────────────────────────────────────────────────────────────────────

def merge_intervals(intervals):
    """
    🎤 INTERVIEWER NARRATION:
    "Each interval is a tuple (start, end). Python sorts tuples
    lexicographically - first by start, then by end. This naturally
    gives us intervals sorted by start time."
    """
    if not intervals:
        return []
    
    # Sort by start time (automatic with tuples!)
    intervals = sorted(intervals)
    result = [intervals[0]]
    
    for current in intervals[1:]:
        last = result[-1]
        if current[0] <= last[1]:  # Overlap
            # Merge by extending end
            result[-1] = (last[0], max(last[1], current[1]))
        else:
            result.append(current)
    
    return result

print("\n▶ SORTING TUPLES:")
intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
merged = merge_intervals(intervals)
print(f"Merged intervals: {merged}")


# ────────────────────────────────────────────────────────────────────────
# PATTERN 3: COORDINATES & GRID PROBLEMS
# ────────────────────────────────────────────────────────────────────────

def number_of_islands(grid):
    """
    🎤 INTERVIEWER NARRATION:
    "I'll use tuples for coordinates and a set for visited cells.
    Since tuples are hashable, I can add them to the set efficiently."
    """
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    count = 0
    
    def dfs(r, c):
        if (r, c) in visited:
            return
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] == '0':
            return
        
        visited.add((r, c))  # Tuple as set element
        
        # Visit neighbors
        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:  # Direction tuples
            dfs(r + dr, c + dc)
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                dfs(r, c)
                count += 1
    
    return count

print("\n▶ COORDINATES AS TUPLES:")
grid = [
    ['1', '1', '0', '0'],
    ['1', '0', '0', '1'],
    ['0', '0', '1', '1'],
]
islands = number_of_islands(grid)
print(f"Number of islands: {islands}")


# ────────────────────────────────────────────────────────────────────────
# PATTERN 4: MEMOIZATION WITH MULTI-PARAMETER KEYS
# ────────────────────────────────────────────────────────────────────────

def edit_distance(s1, s2):
    """
    🎤 INTERVIEWER NARRATION:
    "For DP with multiple parameters, I need a hashable key for memoization.
    I'll use a tuple (i, j) representing indices in both strings."
    """
    memo = {}
    
    def dp(i, j):
        # Base cases
        if i == len(s1):
            return len(s2) - j
        if j == len(s2):
            return len(s1) - i
        
        # Check memo
        if (i, j) in memo:
            return memo[(i, j)]
        
        # Recursive case
        if s1[i] == s2[j]:
            result = dp(i + 1, j + 1)
        else:
            insert = dp(i, j + 1) + 1
            delete = dp(i + 1, j) + 1
            replace = dp(i + 1, j + 1) + 1
            result = min(insert, delete, replace)
        
        memo[(i, j)] = result  # Tuple key
        return result
    
    return dp(0, 0)

print("\n▶ TUPLE KEYS FOR MEMOIZATION:")
distance = edit_distance("horse", "ros")
print(f"Edit distance: {distance}")


# ═══════════════════════════════════════════════════════════════════════
# 9️⃣ NAMED TUPLES (BONUS - PRODUCTION CODE)
# ═══════════════════════════════════════════════════════════════════════

print("\n📌 NAMED TUPLES (Bonus):")

from collections import namedtuple

# Create named tuple class
Point = namedtuple('Point', ['x', 'y'])

p1 = Point(10, 20)
print(f"Point: {p1}")
print(f"Access: p1.x={p1.x}, p1[0]={p1[0]}")  # Both work!

# More readable than regular tuples
Person = namedtuple('Person', ['name', 'age', 'city'])
person = Person('Alice', 30, 'NYC')

print(f"Name: {person.name}, Age: {person.age}")

# 🎤 INTERVIEWER NARRATION:
"""
"For production code, I'd use a named tuple here for better readability.
But for interview coding, regular tuples are faster to type and sufficient."
"""


# ═══════════════════════════════════════════════════════════════════════
# 🔟 COMPARISON WITH JAVA/JAVASCRIPT
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("📊 LANGUAGE COMPARISON")
print("="*70)

comparison = """
╔═══════════════════════════════════════════════════════════════════════╗
║ PYTHON TUPLE                    ║ JAVA / JAVASCRIPT EQUIVALENT         ║
╠═════════════════════════════════╬══════════════════════════════════════╣
║ (1, 2, 3)                       ║ No direct equivalent                 ║
║                                 ║ Java: Use List.of() or custom class  ║
║                                 ║ JS: Use Object.freeze([1,2,3])       ║
╠═════════════════════════════════╬══════════════════════════════════════╣
║ x, y = (10, 20)                 ║ Java: Pair<Integer, Integer>         ║
║                                 ║ JS: [x, y] = [10, 20]                ║
╠═════════════════════════════════╬══════════════════════════════════════╣
║ a, b = b, a  # swap             ║ Java: int temp=a; a=b; b=temp;       ║
║                                 ║ JS: [a, b] = [b, a]                  ║
╠═════════════════════════════════╬══════════════════════════════════════╣
║ return x, y  # multiple values  ║ Java: return new Pair<>(x, y)        ║
║                                 ║ JS: return [x, y] or {x, y}          ║
╠═════════════════════════════════╬══════════════════════════════════════╣
║ dict[(x,y)] = value             ║ Java: map.put(new Point(x,y), value) ║
║                                 ║ JS: map.set(x+','+y, value)  [hack]  ║
╚═════════════════════════════════╩══════════════════════════════════════╝

KEY INSIGHT:
Python tuples are unique. They combine:
  - Immutability
  - Hashability (dict keys)
  - Easy syntax
  - Multiple return values
  
This makes Python especially elegant for interview problems!
"""
print(comparison)


# ═══════════════════════════════════════════════════════════════════════
# 🎯 INTERVIEW CHECKLIST - TUPLES
# ═══════════════════════════════════════════════════════════════════════

checklist = """
┌─────────────────────────────────────────────────────────────────────┐
│ ✅ BEFORE USING TUPLES IN AN INTERVIEW                              │
├─────────────────────────────────────────────────────────────────────┤
│ □ Do I need this data to be immutable?                             │
│ □ Am I using this as a dict key? (Must use tuple!)                 │
│ □ Am I returning multiple values?                                  │
│ □ Am I representing a fixed structure (coordinates, pairs)?        │
│ □ Did I remember comma for single-element tuple? (5,)              │
│ □ Can I use tuple unpacking to make code cleaner?                  │
│ □ Am I using tuples for coordinates in a grid problem?             │
└─────────────────────────────────────────────────────────────────────┘
"""
print(checklist)


# ═══════════════════════════════════════════════════════════════════════
# 🔥 TIME COMPLEXITY SUMMARY
# ═══════════════════════════════════════════════════════════════════════

complexity_table = """
╔═══════════════════════════════════════════════════════════════════════╗
║                TUPLE TIME COMPLEXITY CHEAT SHEET                      ║
╠═══════════════════════════╦═══════════════════════════════════════════╣
║ OPERATION                 ║ COMPLEXITY                                ║
╠═══════════════════════════╬═══════════════════════════════════════════╣
║ t[i] (access)             ║ O(1)                                      ║
║ x in t                    ║ O(n)                                      ║
║ t.index(x)                ║ O(n)                                      ║
║ t.count(x)                ║ O(n)                                      ║
║ t1 + t2 (concatenate)     ║ O(n+m)                                    ║
║ t * k (repeat)            ║ O(nk)                                     ║
║ len(t)                    ║ O(1)                                      ║
║ tuple(iterable)           ║ O(n)                                      ║
║ sorted(t)                 ║ O(n log n)                                ║
║ min(t), max(t)            ║ O(n)                                      ║
║                           ║                                           ║
║ 💡 Slightly faster than list for iteration due to immutability      ║
╚═══════════════════════════╩═══════════════════════════════════════════╝
"""
print(complexity_table)

print("\n✅ TUPLE MASTERY COMPLETE - Moving to Sets next!")

