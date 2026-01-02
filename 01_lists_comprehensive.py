"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 PYTHON LISTS - INTERVIEW MASTERY GUIDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
For 5+ YOE Developer | Interview-Focused | Complete Reference
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 WHAT IS IT?
-------------
List = Dynamic Array (like ArrayList in Java, Array in JS)
- Resizable, mutable, ordered collection
- Internally: Array with over-allocation for amortized O(1) append
- Can hold mixed types (but don't do this in interviews)

📌 WHY IT EXISTS?
----------------
Python's workhorse data structure for:
✓ Array-based problems (90% of interview questions)
✓ Stacks (append/pop)
✓ Queues (collections.deque is better, but lists work)

📌 WHEN INTERVIEWERS EXPECT IT?
------------------------------
✓ Two pointers problems
✓ Sliding window
✓ Dynamic programming (DP arrays)
✓ Graph adjacency lists
✓ BFS/DFS traversal storage

🚨 COMMON MISTAKES THAT FAIL INTERVIEWS
---------------------------------------
❌ Confusing list mutation vs. returning new list
❌ Using remove() in loops (causes skipping)
❌ Not knowing slicing creates shallow copies
❌ Sorting in-place when you need original
❌ Using append when you mean extend

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

# ═══════════════════════════════════════════════════════════════════════
# 1️⃣ CREATION & BASIC OPERATIONS
# ═══════════════════════════════════════════════════════════════════════

# Basic creation
nums = [1, 2, 3, 4, 5]
empty = []
mixed = [1, "hello", 3.14]  # Legal, but avoid in interviews

# List comprehension (INTERVIEW FAVORITE)
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# Pre-allocated list (DP problems)
dp = [0] * 10  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
matrix = [[0] * 3 for _ in range(2)]  # [[0,0,0], [0,0,0]]

# 🚨 INTERVIEW TRAP: Shallow copy issue
wrong_matrix = [[0] * 3] * 2  # ❌ All rows point to SAME list!
wrong_matrix[0][0] = 1  # Changes BOTH rows!
print(f"Wrong matrix: {wrong_matrix}")  # [[1,0,0], [1,0,0]]

correct_matrix = [[0] * 3 for _ in range(2)]  # ✅ Each row is separate
correct_matrix[0][0] = 1
print(f"Correct matrix: {correct_matrix}")  # [[1,0,0], [0,0,0]]


# ═══════════════════════════════════════════════════════════════════════
# 2️⃣ INDEXING & SLICING (HIGH-FREQUENCY INTERVIEW TOPIC)
# ═══════════════════════════════════════════════════════════════════════

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic indexing
first = arr[0]      # 0
last = arr[-1]      # 9 (negative = from end)
second_last = arr[-2]  # 8

# Slicing: arr[start:end:step]
# Rule: Includes start, EXCLUDES end
print("\n📌 SLICING EXAMPLES:")
print(f"arr[2:5] = {arr[2:5]}")      # [2, 3, 4] (index 2,3,4)
print(f"arr[:3] = {arr[:3]}")        # [0, 1, 2] (first 3)
print(f"arr[7:] = {arr[7:]}")        # [7, 8, 9] (from index 7 to end)
print(f"arr[::2] = {arr[::2]}")      # [0, 2, 4, 6, 8] (every 2nd element)
print(f"arr[1::2] = {arr[1::2]}")    # [1, 3, 5, 7, 9] (odd indices)
print(f"arr[::-1] = {arr[::-1]}")    # [9,8,7,6,5,4,3,2,1,0] (REVERSE!)
print(f"arr[-3:] = {arr[-3:]}")      # [7, 8, 9] (last 3 elements)
print(f"arr[:-2] = {arr[:-2]}")      # [0,1,2,3,4,5,6,7] (all but last 2)

# 🎤 INTERVIEWER NARRATION:
"""
"I'll use slicing to reverse the array. arr[::-1] reads:
 - Start from beginning (empty start)
 - Go to end (empty end)  
 - Step backwards (step=-1)
This creates a NEW list, doesn't modify original."
"""

# COMPARE WITH JAVA:
"""
Java: Arrays.copyOfRange(arr, 2, 5)  // Python: arr[2:5]
JS:   arr.slice(2, 5)                // Python: arr[2:5]
"""


# ═══════════════════════════════════════════════════════════════════════
# 3️⃣ MUTABILITY & MODIFICATION METHODS
# ═══════════════════════════════════════════════════════════════════════

print("\n📌 MODIFICATION METHODS:")

# append(x) - Add to end | O(1) amortized
nums = [1, 2, 3]
nums.append(4)
print(f"After append(4): {nums}")  # [1, 2, 3, 4]

# extend(iterable) - Add multiple elements | O(k) where k=length of iterable
nums.extend([5, 6])
print(f"After extend([5,6]): {nums}")  # [1, 2, 3, 4, 5, 6]

# 🚨 INTERVIEW TRAP: append vs extend
wrong = [1, 2, 3]
wrong.append([4, 5])  # ❌ Adds list as SINGLE element
print(f"append([4,5]): {wrong}")  # [1, 2, 3, [4, 5]]

right = [1, 2, 3]
right.extend([4, 5])  # ✅ Adds each element
print(f"extend([4,5]): {right}")  # [1, 2, 3, 4, 5]

# insert(index, value) - Insert at position | O(n)
nums = [1, 2, 4, 5]
nums.insert(2, 3)  # Insert 3 at index 2
print(f"After insert(2, 3): {nums}")  # [1, 2, 3, 4, 5]

# remove(value) - Remove FIRST occurrence | O(n)
nums = [1, 2, 3, 2, 4]
nums.remove(2)  # Removes first 2 only
print(f"After remove(2): {nums}")  # [1, 3, 2, 4]

# 🚨 INTERVIEW TRAP: remove() in loop
print("\n⚠️  DANGEROUS: Removing while iterating")
nums = [1, 2, 3, 4, 5]
for num in nums:
    if num % 2 == 0:
        nums.remove(num)  # ❌ Skips elements!
print(f"Buggy result: {nums}")  # Doesn't remove all evens!

# ✅ CORRECT: List comprehension
nums = [1, 2, 3, 4, 5]
nums = [x for x in nums if x % 2 != 0]
print(f"Correct result: {nums}")  # [1, 3, 5]

# pop(index=-1) - Remove and return element | O(1) for last, O(n) for middle
nums = [1, 2, 3, 4, 5]
last = nums.pop()      # Returns 5, nums=[1,2,3,4]
second = nums.pop(1)   # Returns 2, nums=[1,3,4]
print(f"Popped {last}, then {second}. Remaining: {nums}")

# 🎤 INTERVIEWER NARRATION:
"""
"I'll use pop() to implement a stack. Since pop() removes from the end
and that's O(1), the list acts as an efficient stack structure."
"""

# clear() - Remove all elements | O(n)
nums = [1, 2, 3]
nums.clear()
print(f"After clear(): {nums}")  # []


# ═══════════════════════════════════════════════════════════════════════
# 4️⃣ SEARCH & QUERY METHODS
# ═══════════════════════════════════════════════════════════════════════

print("\n📌 SEARCH & QUERY:")

# index(value, start=0, end=len) - Find first index | O(n)
nums = [10, 20, 30, 20, 40]
idx = nums.index(20)      # 1 (first occurrence)
idx2 = nums.index(20, 2)  # 3 (search from index 2)
print(f"index(20) = {idx}, index(20, 2) = {idx2}")

# 🚨 INTERVIEW TRAP: index() raises ValueError if not found
try:
    nums.index(999)
except ValueError:
    print("⚠️  index() throws ValueError if element not found")

# ✅ BETTER: Use 'in' operator first, or use dict/set
if 30 in nums:
    idx = nums.index(30)
    print(f"Found 30 at index {idx}")

# count(value) - Count occurrences | O(n)
nums = [1, 2, 2, 3, 2, 4]
count = nums.count(2)
print(f"count(2) = {count}")  # 3


# ═══════════════════════════════════════════════════════════════════════
# 5️⃣ SORTING & REVERSING (CRITICAL FOR INTERVIEWS)
# ═══════════════════════════════════════════════════════════════════════

print("\n📌 SORTING & REVERSING:")

# sort() - In-place sort | O(n log n) | RETURNS NONE!
nums = [3, 1, 4, 1, 5, 9, 2, 6]
nums.sort()
print(f"After sort(): {nums}")  # [1, 1, 2, 3, 4, 5, 6, 9]

nums.sort(reverse=True)
print(f"sort(reverse=True): {nums}")  # [9, 6, 5, 4, 3, 2, 1, 1]

# 🚨 INTERVIEW TRAP: sort() returns None
wrong = [3, 1, 2].sort()
print(f"[3,1,2].sort() returns: {wrong}")  # None (not the sorted list!)

# sorted(iterable) - Returns NEW sorted list | O(n log n)
original = [3, 1, 4, 1, 5]
sorted_copy = sorted(original)
print(f"Original: {original}, Sorted copy: {sorted_copy}")

# Custom sorting with key parameter (INTERVIEW ESSENTIAL)
words = ["apple", "pie", "a", "cherry"]
by_length = sorted(words, key=len)  # Sort by length
print(f"Sorted by length: {by_length}")  # ['a', 'pie', 'apple', 'cherry']

# Sort by custom criteria
points = [(1, 5), (3, 2), (2, 8), (3, 1)]
by_x = sorted(points, key=lambda p: p[0])      # Sort by x
by_y = sorted(points, key=lambda p: p[1])      # Sort by y
by_sum = sorted(points, key=lambda p: p[0] + p[1])  # Sort by sum
print(f"By x: {by_x}")
print(f"By y: {by_y}")

# 🎤 INTERVIEWER NARRATION:
"""
"I need to sort intervals by start time. I'll use sorted() with a lambda
that returns the first element of each tuple. This maintains the original
list and gives me O(n log n) time complexity."
"""

# reverse() - In-place reverse | O(n) | RETURNS NONE!
nums = [1, 2, 3, 4, 5]
nums.reverse()
print(f"After reverse(): {nums}")  # [5, 4, 3, 2, 1]

# Compare with slicing reverse
nums = [1, 2, 3, 4, 5]
reversed_copy = nums[::-1]  # Creates new list
print(f"Original: {nums}, Reversed copy: {reversed_copy}")


# ═══════════════════════════════════════════════════════════════════════
# 6️⃣ COPYING (INTERVIEW TRAP ZONE)
# ═══════════════════════════════════════════════════════════════════════

print("\n📌 COPYING LISTS:")

original = [1, 2, 3]

# Reference (NOT a copy!)
ref = original
ref.append(4)
print(f"Original: {original}")  # [1, 2, 3, 4] (MODIFIED!)

# Shallow copy methods
original = [1, 2, 3]
copy1 = original.copy()     # Method
copy2 = original[:]         # Slicing (INTERVIEW PREFERRED)
copy3 = list(original)      # Constructor
import copy
copy4 = copy.copy(original) # copy module

copy1.append(4)
print(f"Original: {original}, Copy: {copy1}")  # Original unchanged

# 🚨 SHALLOW COPY TRAP with nested lists
matrix = [[1, 2], [3, 4]]
shallow = matrix.copy()
shallow[0][0] = 999  # Modifies BOTH!
print(f"Original matrix: {matrix}")  # [[999, 2], [3, 4]]

# ✅ DEEP COPY for nested structures
import copy
matrix = [[1, 2], [3, 4]]
deep = copy.deepcopy(matrix)
deep[0][0] = 999
print(f"Original: {matrix}, Deep copy: {deep}")


# ═══════════════════════════════════════════════════════════════════════
# 7️⃣ AGGREGATE FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════

print("\n📌 AGGREGATE FUNCTIONS:")

nums = [1, 2, 3, 4, 5]

length = len(nums)      # 5
minimum = min(nums)     # 1
maximum = max(nums)     # 5
total = sum(nums)       # 15

print(f"len={length}, min={minimum}, max={maximum}, sum={total}")

# Works with custom objects using key
points = [(1, 5), (3, 2), (2, 8)]
highest_y = max(points, key=lambda p: p[1])
print(f"Point with highest y: {highest_y}")  # (2, 8)


# ═══════════════════════════════════════════════════════════════════════
# 8️⃣ INTERVIEW PATTERNS WITH LISTS
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("🔥 INTERVIEW PATTERNS")
print("="*70)

# ────────────────────────────────────────────────────────────────────────
# PATTERN 1: TWO POINTERS
# ────────────────────────────────────────────────────────────────────────

def two_sum_sorted(nums, target):
    """
    🎤 INTERVIEWER NARRATION:
    "Since the array is sorted, I'll use two pointers. Left starts at 0,
    right at the end. If sum is too small, move left up. If too large,
    move right down. This gives us O(n) time, O(1) space."
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return None

print("\n▶ TWO POINTERS PATTERN:")
result = two_sum_sorted([1, 2, 3, 4, 6], 6)
print(f"Two Sum (sorted): {result}")


# ────────────────────────────────────────────────────────────────────────
# PATTERN 2: SLIDING WINDOW
# ────────────────────────────────────────────────────────────────────────

def max_sum_subarray(nums, k):
    """
    🎤 INTERVIEWER NARRATION:
    "I'll use a sliding window of size k. First, compute the sum of the
    first k elements. Then slide the window: subtract the element leaving,
    add the element entering. This avoids recomputing the sum each time,
    giving us O(n) instead of O(n*k)."
    """
    if len(nums) < k:
        return 0
    
    # Initial window
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

print("\n▶ SLIDING WINDOW PATTERN:")
result = max_sum_subarray([1, 4, 2, 10, 23, 3, 1, 0, 20], 4)
print(f"Max sum of subarray size 4: {result}")


# ────────────────────────────────────────────────────────────────────────
# PATTERN 3: IN-PLACE ARRAY MODIFICATION
# ────────────────────────────────────────────────────────────────────────

def remove_duplicates_sorted(nums):
    """
    🎤 INTERVIEWER NARRATION:
    "I'll use two pointers for in-place modification. 'slow' tracks the
    position for the next unique element, 'fast' scans the array. When
    we find a different element, we place it at 'slow' and increment.
    This gives O(n) time with O(1) extra space."
    """
    if not nums:
        return 0
    
    slow = 1  # Position for next unique element
    
    for fast in range(1, len(nums)):
        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]
            slow += 1
    
    return slow  # Length of unique elements

print("\n▶ IN-PLACE MODIFICATION PATTERN:")
arr = [1, 1, 2, 2, 2, 3, 4, 4, 5]
length = remove_duplicates_sorted(arr)
print(f"Unique elements: {arr[:length]}")


# ═══════════════════════════════════════════════════════════════════════
# 9️⃣ COMPARISON WITH JAVA/JAVASCRIPT
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("📊 LANGUAGE COMPARISON")
print("="*70)

comparison = """
╔═══════════════════════╦═══════════════════════╦═══════════════════════╗
║ OPERATION             ║ PYTHON                ║ JAVA / JAVASCRIPT     ║
╠═══════════════════════╬═══════════════════════╬═══════════════════════╣
║ Create                ║ [1, 2, 3]             ║ new int[]{1,2,3}      ║
║                       ║                       ║ [1, 2, 3] (JS)        ║
╠═══════════════════════╬═══════════════════════╬═══════════════════════╣
║ Length                ║ len(arr)              ║ arr.length            ║
╠═══════════════════════╬═══════════════════════╬═══════════════════════╣
║ Add to end            ║ arr.append(x)         ║ list.add(x)           ║
║                       ║                       ║ arr.push(x) (JS)      ║
╠═══════════════════════╬═══════════════════════╬═══════════════════════╣
║ Remove from end       ║ arr.pop()             ║ list.remove(last)     ║
║                       ║                       ║ arr.pop() (JS)        ║
╠═══════════════════════╬═══════════════════════╬═══════════════════════╣
║ Insert at index       ║ arr.insert(i, x)      ║ list.add(i, x)        ║
║                       ║                       ║ arr.splice(i,0,x) JS  ║
╠═══════════════════════╬═══════════════════════╬═══════════════════════╣
║ Sort in-place         ║ arr.sort()            ║ Arrays.sort(arr)      ║
║                       ║                       ║ arr.sort() (JS)       ║
╠═══════════════════════╬═══════════════════════╬═══════════════════════╣
║ Slice/Subarray        ║ arr[1:4]              ║ Arrays.copyOfRange()  ║
║                       ║                       ║ arr.slice(1,4) (JS)   ║
╠═══════════════════════╬═══════════════════════╬═══════════════════════╣
║ Reverse               ║ arr[::-1]             ║ Collections.reverse() ║
║                       ║                       ║ arr.reverse() (JS)    ║
╠═══════════════════════╬═══════════════════════╬═══════════════════════╣
║ Find element          ║ x in arr              ║ list.contains(x)      ║
║                       ║                       ║ arr.includes(x) (JS)  ║
╚═══════════════════════╩═══════════════════════╩═══════════════════════╝
"""
print(comparison)


# ═══════════════════════════════════════════════════════════════════════
# 🎯 INTERVIEW CHECKLIST - ALWAYS ASK YOURSELF
# ═══════════════════════════════════════════════════════════════════════

checklist = """
┌─────────────────────────────────────────────────────────────────────┐
│ ✅ BEFORE USING A LIST IN AN INTERVIEW                              │
├─────────────────────────────────────────────────────────────────────┤
│ □ Do I need to modify in-place or create new list?                 │
│ □ Is the input sorted? (Can I use two pointers?)                   │
│ □ Do I need to preserve original? (copy vs reference)              │
│ □ Am I iterating and modifying? (Don't use remove in loop!)        │
│ □ Am I sorting? (sort() vs sorted(), and does order matter?)       │
│ □ Am I using list as stack/queue? (Consider deque for queue)       │
│ □ Do I need O(1) lookup? (Use set/dict instead!)                   │
│ □ Is this a 2D array? (Watch out for shallow copy trap!)           │
└─────────────────────────────────────────────────────────────────────┘
"""
print(checklist)


# ═══════════════════════════════════════════════════════════════════════
# 🔥 TIME COMPLEXITY SUMMARY
# ═══════════════════════════════════════════════════════════════════════

complexity_table = """
╔═══════════════════════════════════════════════════════════════════════╗
║                    TIME COMPLEXITY CHEAT SHEET                        ║
╠═══════════════════════════╦═══════════════════════════════════════════╣
║ OPERATION                 ║ COMPLEXITY                                ║
╠═══════════════════════════╬═══════════════════════════════════════════╣
║ arr[i] (access)           ║ O(1)                                      ║
║ arr.append(x)             ║ O(1) amortized                            ║
║ arr.pop()                 ║ O(1)                                      ║
║ arr.pop(i)                ║ O(n)                                      ║
║ arr.insert(i, x)          ║ O(n)                                      ║
║ arr.remove(x)             ║ O(n)                                      ║
║ arr.index(x)              ║ O(n)                                      ║
║ arr.count(x)              ║ O(n)                                      ║
║ arr.sort()                ║ O(n log n)                                ║
║ arr.reverse()             ║ O(n)                                      ║
║ x in arr                  ║ O(n)                                      ║
║ arr.extend(other)         ║ O(k) where k=len(other)                   ║
║ arr[:] (copy)             ║ O(n)                                      ║
║ min(arr), max(arr)        ║ O(n)                                      ║
║ sum(arr)                  ║ O(n)                                      ║
╚═══════════════════════════╩═══════════════════════════════════════════╝
"""
print(complexity_table)

print("\n✅ LIST MASTERY COMPLETE - Ready for next data structure!")

