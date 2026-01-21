"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 PYTHON SETS - INTERVIEW MASTERY GUIDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
For 5+ YOE Developer | Interview-Focused | Complete Reference
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 WHAT IS IT?
-------------
Set = Unordered collection of unique elements backed by hash table
- Internally: Hash table (like HashMap keys in Java, Set in JS)
- O(1) average case for add, remove, lookup
- Automatically handles duplicates

📌 WHY IT EXISTS?
----------------
✓ Fast membership testing (O(1) vs O(n) for lists)
✓ Duplicate removal
✓ Set operations (union, intersection, difference)
✓ Track visited nodes in graph problems

📌 WHEN INTERVIEWERS EXPECT IT?
------------------------------
✓ "Check if element exists" → Use set, not list!
✓ Find duplicates in array
✓ Graph BFS/DFS visited tracking
✓ Two Sum, Three Sum type problems
✓ Finding unique elements
✓ Set theory problems (intersection, union)

🚨 COMMON MISTAKES THAT FAIL INTERVIEWS
---------------------------------------
❌ Using list when you need O(1) lookup (interviewer will ask to optimize)
❌ Trying to add unhashable types (lists, dicts)
❌ Expecting order preservation (use set, not assume ordering)
❌ Forgetting set comprehension exists
❌ Not knowing difference between remove() and discard()
❌ Using 'in' with lists when you should use sets

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

# ═══════════════════════════════════════════════════════════════════════
# 1️⃣ CREATION & BASIC OPERATIONS
# ═══════════════════════════════════════════════════════════════════════

# Basic creation
nums = {1, 2, 3, 4, 5}
print(f"Set: {nums}")

# 🚨 TRAP: Empty set
empty_dict = {}      # ❌ This is a DICT, not a set!
empty_set = set()    # ✅ Correct way to create empty set
print(f"Type of {{}}: {type(empty_dict)}")  # Type of {}: <class 'dict'>

# From iterable (automatic duplicate removal)
from_list = set([1, 2, 2, 3, 3, 3, 4])
print(f"set([1,2,2,3,3,3,4]) = {from_list}")  # {1, 2, 3, 4}

from_string = set("hello")
print(f"set('hello') = {from_string}")  # {'h', 'e', 'l', 'o'}

# Set comprehension (INTERVIEW FAVORITE)
squares = {x**2 for x in range(5)}
print(f"Square set: {squares}")  # {0, 1, 4, 9, 16}

evens = {x for x in range(10) if x % 2 == 0}
print(f"Even set: {evens}") # {0, 2, 4, 6, 8}

# 🎤 INTERVIEWER NARRATION:
"""
"I'll convert the list to a set to remove duplicates, then convert back
to a list. This is O(n) time and more Pythonic than manual deduplication."
"""
numbers_data = [1, 2, 3, 2, 4, 1, 5]
unique_numbers = list(set(numbers_data))
print(f"Unique Numbers: {unique_numbers}")  # [1, 2, 3, 4, 5]


# ═══════════════════════════════════════════════════════════════════════
# 2️⃣ O(1) LOOKUP - THE KILLER FEATURE
# ═══════════════════════════════════════════════════════════════════════

print("\n📌 O(1) LOOKUP POWER:")

# ❌ SLOW: Using list for membership testing
nums_list = list(range(10000))
# 5000 in nums_list  # O(n) - scans entire list

# ✅ FAST: Using set
nums_set = set(range(10000))
# 5000 in nums_set  # O(1) - hash table lookup

# Real interview example: Two Sum
def two_sum_with_set(nums, target):
    """
    🎤 INTERVIEWER NARRATION:
    "I'll use a set to track numbers I've seen. For each number, I check
    if (target - num) exists in the set. Since set lookup is O(1), this
    gives us O(n) time with O(n) space, better than O(n²) brute force."
    """
    seen = set()
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:  # O(1) lookup!
            # Return indices (need dict for this, see dict section)
            return True
        seen.add(num)
    
    return False

result = two_sum_with_set([2, 7, 11, 15], 9)
print(f"Two sum exists: {result}")


# ═══════════════════════════════════════════════════════════════════════
# 3️⃣ MODIFICATION METHODS
# ═══════════════════════════════════════════════════════════════════════

print("\n📌 MODIFICATION METHODS:")

# add(element) - Add single element | O(1)
nums = {1, 2, 3}
nums.add(4)
print(f"After add(4): {nums}")  # {1, 2, 3, 4}

nums.add(2)  # Duplicate - no effect
print(f"After add(2): {nums}")  # Still {1, 2, 3, 4}

# update(iterable) - Add multiple elements | O(k)
nums.update([5, 6, 7])
print(f"After update([5,6,7]): {nums}")

nums.update({8, 9}, [10])  # Can take multiple iterables
print(f"After multiple update: {nums}")

# remove(element) - Remove element | O(1) | RAISES KeyError if not found
nums = {1, 2, 3, 4, 5}
nums.remove(3)
print(f"After remove(3): {nums}")  # {1, 2, 4, 5}

try:
    nums.remove(99)  # ❌ Raises KeyError
except KeyError:
    print("⚠️  remove() raises KeyError if element not in set")

# discard(element) - Remove element | O(1) | Silent if not found
nums.discard(99)  # ✅ No error
print(f"After discard(99): {nums} (no error)")  # {1, 2, 3, 4, 5}

# 🎤 INTERVIEWER NARRATION:
"""
"I'll use discard() instead of remove() because I don't want to check
if the element exists first. discard() is safer - it won't throw an error."
"""

# pop() - Remove and return arbitrary element | O(1)
nums = {1, 2, 3, 4, 5}
popped = nums.pop()
print(f"Popped {popped}, remaining: {nums}")  # Popped 5, remaining: {1, 2, 3, 4}

# ⚠️ Order is arbitrary! Don't rely on it!

# clear() - Remove all elements | O(n)
nums.clear()
print(f"After clear(): {nums}")  # {} (empty set)


# ═══════════════════════════════════════════════════════════════════════
# 4️⃣ SET OPERATIONS (HIGH-FREQUENCY INTERVIEW TOPIC)
# ═══════════════════════════════════════════════════════════════════════

print("\n📌 SET OPERATIONS:")

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Union: All elements from both sets
union1 = A | B                    # Operator
union2 = A.union(B)               # Method
print(f"A | B = {union1}")        # {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection: Common elements
intersection1 = A & B
intersection2 = A.intersection(B)
print(f"A & B = {intersection1}")  # {4, 5}

# Difference: In A but not in B
difference1 = A - B
difference2 = A.difference(B)
print(f"A - B = {difference1}")    # {1, 2, 3}
print(f"B - A = {B - A}")          # {6, 7, 8}

# Symmetric Difference: In A or B but not both
sym_diff1 = A ^ B
sym_diff2 = A.symmetric_difference(B)
print(f"A ^ B = {sym_diff1}")      # {1, 2, 3, 6, 7, 8}

# In-place operations (modify original set)
A_copy = A.copy()
A_copy |= B                        # A = A | B
print(f"A |= B: {A_copy}")  # {1, 2, 3, 4, 5, 6, 7, 8}

A_copy = A.copy()
A_copy &= B                        # A = A & B
print(f"A &= B: {A_copy}")  # {1, 2, 3}

A_copy = A.copy()
A_copy -= B                        # A = A - B
print(f"A -= B: {A_copy}")  # {4, 5}

A_copy = A.copy()
A_copy ^= B                        # A = A ^ B
print(f"A ^= B: {A_copy}")  # {1, 2, 3, 6, 7, 8}


# ═══════════════════════════════════════════════════════════════════════
# 5️⃣ SET COMPARISON METHODS
# ═══════════════════════════════════════════════════════════════════════

print("\n📌 SET COMPARISONS:")

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 3}

# issubset() - Is every element in A also in B?
print(f"A.issubset(B): {A.issubset(B)}")      # True
print(f"B.issubset(A): {B.issubset(A)}")      # False
print(f"A <= B: {A <= B}")                    # Operator form

# issuperset() - Is every element in B also in A?
print(f"B.issuperset(A): {B.issuperset(A)}")  # True
print(f"B >= A: {B >= A}")                    # Operator form

# isdisjoint() - No common elements?
print(f"{1,2}.isdisjoint({3,4}): {set([1,2]).isdisjoint({3,4})}")  # True
print(f"{1,2}.isdisjoint({2,3}): {set([1,2]).isdisjoint({2,3})}")  # False

# Equality
print(f"A == C: {A == C}")                    # True
print(f"A == B: {A == B}")                    # False


# ═══════════════════════════════════════════════════════════════════════
# 6️⃣ HASHABILITY CONSTRAINT
# ═══════════════════════════════════════════════════════════════════════

print("\n📌 HASHABILITY:")

# ✅ Can add hashable types
valid_set = {1, "hello", 3.14, True, (1, 2)}
print(f"Valid set: {valid_set}")

# ❌ Cannot add unhashable types
try:
    bad_set = {1, 2, [3, 4]}  # Lists are unhashable
except TypeError as e:
    print(f"❌ Cannot add list to set: {e}")

try:
    bad_set = {1, 2, {3: 4}}  # Dicts are unhashable
except TypeError as e:
    print(f"❌ Cannot add dict to set: {e}")

# ✅ But can add tuples!
coords_set = {(0, 0), (0, 1), (1, 0)}
print(f"✅ Tuple coordinates in set: {coords_set}")

# 🎤 INTERVIEWER NARRATION:
"""
"I need to track visited coordinates. I'll use a set of (row, col) tuples
since tuples are hashable. This gives me O(1) lookup for visited cells."
"""


# ═══════════════════════════════════════════════════════════════════════
# 7️⃣ INTERVIEW PATTERNS WITH SETS
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("🔥 INTERVIEW PATTERNS")
print("="*70)

# ────────────────────────────────────────────────────────────────────────
# PATTERN 1: FIND DUPLICATES
# ────────────────────────────────────────────────────────────────────────

def contains_duplicate(nums):
    """
    🎤 INTERVIEWER NARRATION:
    "I'll iterate through the array once, adding each element to a set.
    If I try to add an element that's already in the set, we have a duplicate.
    This is O(n) time and O(n) space."
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Even simpler: Compare lengths
def contains_duplicate_v2(nums):
    """
    🎤 INTERVIEWER NARRATION:
    "Actually, I can make this even simpler. If the set is smaller than
    the list, there must be duplicates. One-liner solution."
    """
    return len(nums) != len(set(nums))

print("\n▶ FIND DUPLICATES:")
print(f"[1,2,3,1] has duplicate: {contains_duplicate([1,2,3,1])}")
print(f"[1,2,3,4] has duplicate: {contains_duplicate([1,2,3,4])}")


# ────────────────────────────────────────────────────────────────────────
# PATTERN 2: INTERSECTION OF ARRAYS
# ────────────────────────────────────────────────────────────────────────

def intersection(nums1, nums2):
    """
    🎤 INTERVIEWER NARRATION:
    "I'll convert both arrays to sets, then use the intersection operator.
    This is O(n+m) time and much cleaner than nested loops."
    """
    return list(set(nums1) & set(nums2))

# Follow-up: With duplicates counted
def intersection_with_count(nums1, nums2):
    """
    🎤 INTERVIEWER NARRATION:
    "For the follow-up where duplicates matter, I'll use a dictionary
    to count frequencies instead. But for unique elements, sets are perfect."
    """
    from collections import Counter
    count1 = Counter(nums1)
    count2 = Counter(nums2)
    
    result = []
    for num in count1:
        if num in count2:
            result.extend([num] * min(count1[num], count2[num]))
    return result

print("\n▶ ARRAY INTERSECTION:")
print(f"Intersection: {intersection([1,2,2,1], [2,2])}")
print(f"With counts: {intersection_with_count([1,2,2,1], [2,2])}")


# ────────────────────────────────────────────────────────────────────────
# PATTERN 3: VISITED TRACKING (GRAPH PROBLEMS)
# ────────────────────────────────────────────────────────────────────────

def num_islands_bfs(grid):
    """
    🎤 INTERVIEWER NARRATION:
    "I'll use BFS with a set to track visited cells. Sets give us O(1)
    lookup to check if we've visited a cell, and we can store (row, col)
    tuples directly."
    """
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    count = 0
    
    def bfs(r, c):
        queue = [(r, c)]
        visited.add((r, c))
        
        while queue:
            row, col = queue.pop(0)
            
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = row + dr, col + dc
                if (0 <= nr < rows and 0 <= nc < cols and
                    grid[nr][nc] == '1' and (nr, nc) not in visited):
                    queue.append((nr, nc))
                    visited.add((nr, nc))
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                bfs(r, c)
                count += 1
    
    return count

print("\n▶ VISITED TRACKING (BFS):")
grid = [
    ['1', '1', '0'],
    ['1', '0', '1'],
    ['0', '0', '1']
]
print(f"Number of islands: {num_islands_bfs(grid)}")


# ────────────────────────────────────────────────────────────────────────
# PATTERN 4: LONGEST CONSECUTIVE SEQUENCE
# ────────────────────────────────────────────────────────────────────────

def longest_consecutive(nums):
    """
    🎤 INTERVIEWER NARRATION:
    "The trick is using a set for O(1) lookup. For each number, I check if
    it's the start of a sequence (no num-1 exists). Then I count forward.
    This visits each element at most twice, so it's O(n)."
    """
    if not nums:
        return 0
    
    num_set = set(nums)
    max_length = 0
    
    for num in num_set:
        # Only start counting from the beginning of a sequence
        if num - 1 not in num_set:
            current = num
            length = 1
            
            while current + 1 in num_set:
                current += 1
                length += 1
            
            max_length = max(max_length, length)
    
    return max_length

print("\n▶ LONGEST CONSECUTIVE SEQUENCE:")
print(f"Longest sequence: {longest_consecutive([100, 4, 200, 1, 3, 2])}")
# [1, 2, 3, 4] → 4


# ────────────────────────────────────────────────────────────────────────
# PATTERN 5: SET OPERATIONS FOR WORD PROBLEMS
# ────────────────────────────────────────────────────────────────────────

def unique_email_addresses(emails):
    """
    🎤 INTERVIEWER NARRATION:
    "I'll normalize each email and add to a set. The set automatically
    handles duplicates, so the final size is the answer."
    """
    unique = set()
    
    for email in emails:
        local, domain = email.split('@')
        # Remove dots and everything after +
        local = local.split('+')[0].replace('.', '')
        unique.add(f"{local}@{domain}")
    
    return len(unique)

print("\n▶ SET FOR COUNTING UNIQUE:")
emails = [
    "test.email+alex@leetcode.com",
    "test.e.mail+bob.cathy@leetcode.com",
    "testemail+david@lee.tcode.com"
]
print(f"Unique emails: {unique_email_addresses(emails)}")


# ═══════════════════════════════════════════════════════════════════════
# 8️⃣ COMPARISON WITH JAVA/JAVASCRIPT
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("📊 LANGUAGE COMPARISON")
print("="*70)

comparison = """
╔═══════════════════════════╦═══════════════════════╦═══════════════════════╗
║ OPERATION                 ║ PYTHON                ║ JAVA / JAVASCRIPT     ║
╠═══════════════════════════╬═══════════════════════╬═══════════════════════╣
║ Create                    ║ {1, 2, 3}             ║ new HashSet<>()       ║
║                           ║ set([1,2,3])          ║ new Set([1,2,3]) (JS) ║
╠═══════════════════════════╬═══════════════════════╬═══════════════════════╣
║ Add element               ║ s.add(x)              ║ set.add(x)            ║
╠═══════════════════════════╬═══════════════════════╬═══════════════════════╣
║ Remove element            ║ s.remove(x)           ║ set.remove(x)         ║
║                           ║ s.discard(x)          ║ set.delete(x) (JS)    ║
╠═══════════════════════════╬═══════════════════════╬═══════════════════════╣
║ Contains                  ║ x in s                ║ set.contains(x)       ║
║                           ║                       ║ set.has(x) (JS)       ║
╠═══════════════════════════╬═══════════════════════╬═══════════════════════╣
║ Size                      ║ len(s)                ║ set.size()            ║
║                           ║                       ║ set.size (JS)         ║
╠═══════════════════════════╬═══════════════════════╬═══════════════════════╣
║ Union                     ║ s1 | s2               ║ No operator           ║
║                           ║                       ║ Manual merging        ║
╠═══════════════════════════╬═══════════════════════╬═══════════════════════╣
║ Intersection              ║ s1 & s2               ║ No operator           ║
║                           ║                       ║ retainAll(s2)         ║
╠═══════════════════════════╬═══════════════════════╬═══════════════════════╣
║ Difference                ║ s1 - s2               ║ No operator           ║
║                           ║                       ║ removeAll(s2)         ║
╠═══════════════════════════╬═══════════════════════╬═══════════════════════╣
║ Iterate                   ║ for x in s:           ║ for(int x : set)      ║
║                           ║                       ║ for(let x of set)     ║
╚═══════════════════════════╩═══════════════════════╩═══════════════════════╝

KEY ADVANTAGE:
Python sets have beautiful operator syntax (|, &, -, ^) for set operations.
Java/JS require method calls or manual implementation.
"""
print(comparison)


# ═══════════════════════════════════════════════════════════════════════
# 9️⃣ FROZENSET (IMMUTABLE SETS)
# ═══════════════════════════════════════════════════════════════════════

print("\n📌 FROZENSET (Bonus):")

# frozenset = Immutable set (can be dict key or set element)
fs = frozenset([1, 2, 3])
print(f"Frozenset: {fs}")

# Can be used as dict key
graph = {
    frozenset([1, 2]): 5,  # Edge {1,2} with weight 5
    frozenset([2, 3]): 3
}
print(f"Undirected graph: {graph}")

# Can be element of another set
set_of_sets = {
    frozenset([1, 2]),
    frozenset([3, 4]),
    frozenset([1, 2])  # Duplicate - ignored
}
print(f"Set of frozensets: {set_of_sets}")

# 🎤 INTERVIEWER NARRATION:
"""
"For representing undirected edges where order doesn't matter, I'll use
frozenset. frozenset([1,2]) equals frozenset([2,1]), perfect for
undirected graphs."
"""


# ═══════════════════════════════════════════════════════════════════════
# 🎯 INTERVIEW CHECKLIST - SETS
# ═══════════════════════════════════════════════════════════════════════

checklist = """
┌─────────────────────────────────────────────────────────────────────┐
│ ✅ BEFORE USING SETS IN AN INTERVIEW                                │
├─────────────────────────────────────────────────────────────────────┤
│ □ Do I need O(1) lookup? (Use set, not list!)                      │
│ □ Are duplicates irrelevant? (Set removes them automatically)      │
│ □ Am I tracking visited nodes/cells? (Set of tuples)               │
│ □ Do I need set operations (union, intersection)? (Use operators!) │
│ □ Are elements hashable? (No lists/dicts allowed)                  │
│ □ Does order matter? (Sets are unordered)                          │
│ □ Should I use remove() or discard()? (discard() is safer)         │
│ □ Can I use a set comprehension to make code cleaner?              │
└─────────────────────────────────────────────────────────────────────┘
"""
print(checklist)


# ═══════════════════════════════════════════════════════════════════════
# 🔥 TIME COMPLEXITY SUMMARY
# ═══════════════════════════════════════════════════════════════════════

complexity_table = """
╔═══════════════════════════════════════════════════════════════════════╗
║                  SET TIME COMPLEXITY CHEAT SHEET                      ║
╠═══════════════════════════╦══════════════════╦════════════════════════╣
║ OPERATION                 ║ AVERAGE CASE     ║ WORST CASE             ║
╠═══════════════════════════╬══════════════════╬════════════════════════╣
║ x in s                    ║ O(1)             ║ O(n) [hash collision]  ║
║ s.add(x)                  ║ O(1)             ║ O(n)                   ║
║ s.remove(x)               ║ O(1)             ║ O(n)                   ║
║ s.discard(x)              ║ O(1)             ║ O(n)                   ║
║ s.pop()                   ║ O(1)             ║ O(1)                   ║
║ s.clear()                 ║ O(n)             ║ O(n)                   ║
║ len(s)                    ║ O(1)             ║ O(1)                   ║
║ s1 | s2 (union)           ║ O(len(s1)+len(s2))                       ║
║ s1 & s2 (intersection)    ║ O(min(len(s1),len(s2)))                  ║
║ s1 - s2 (difference)      ║ O(len(s1))                               ║
║ s1 ^ s2 (sym difference)  ║ O(len(s1)+len(s2))                       ║
║ s.copy()                  ║ O(n)             ║ O(n)                   ║
╠═══════════════════════════╩══════════════════╩════════════════════════╣
║ 💡 Hash collisions are rare with good hash functions                 ║
║ 💡 For interviews, assume O(1) operations                            ║
╚═══════════════════════════════════════════════════════════════════════╝
"""
print(complexity_table)

print("\n✅ SET MASTERY COMPLETE - Moving to Dictionaries (the most important!)!")

