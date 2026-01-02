# 🚀 Python Interview Quick Reference

> Ultra-condensed cheat sheet for last-minute review

---

## 📊 Data Structures Cheat Sheet

### **List (Dynamic Array)**
```python
# Creation
arr = [1, 2, 3]
arr = [x**2 for x in range(5)]  # Comprehension
arr = [0] * n  # Initialize size n

# Access & Slicing
arr[0], arr[-1]              # First, last
arr[1:3]                     # Elements 1,2
arr[:3], arr[3:]             # First 3, from 3 onwards
arr[::2]                     # Every 2nd element
arr[::-1]                    # REVERSE

# Modification
arr.append(x)                # Add to end - O(1)
arr.extend([x,y])            # Add multiple - O(k)
arr.insert(i, x)             # Insert at i - O(n)
arr.remove(x)                # Remove first x - O(n)
arr.pop()                    # Remove last - O(1)
arr.pop(i)                   # Remove at i - O(n)

# Query
arr.index(x)                 # Find index - O(n), raises error if missing
arr.count(x)                 # Count occurrences - O(n)
x in arr                     # Check existence - O(n)

# Sort
arr.sort()                   # In-place - O(n log n), RETURNS NONE
sorted(arr)                  # New sorted list - O(n log n)
arr.reverse()                # In-place reverse - O(n), RETURNS NONE

# Aggregate
len(arr), min(arr), max(arr), sum(arr)
```

### **Dictionary (Hash Map)**
```python
# Creation
d = {"a": 1, "b": 2}
d = {k: v for k, v in pairs}  # Comprehension
d = dict(zip(keys, vals))     # From two lists

# Access
d["key"]                      # Direct - raises KeyError if missing
d.get("key", default)         # Safe - returns default if missing

# Modification
d["key"] = val               # Set/update
del d["key"]                 # Delete
d.pop("key", default)        # Remove and return
d.update({"x": 1, "y": 2})   # Merge

# Query
"key" in d                   # Check existence - O(1)
len(d)                       # Size

# Iteration (CRITICAL!)
for key in d:                # Keys only
for key in d.keys():         # Keys explicitly
for val in d.values():       # Values only
for k, v in d.items():       # Key-value pairs (MOST COMMON)

# Important variants
from collections import defaultdict, Counter
freq = defaultdict(int)      # Auto-initialize to 0
graph = defaultdict(list)    # Auto-initialize to []
count = Counter([1,2,2,3])   # {1:1, 2:2, 3:1}
count.most_common(k)         # Top k elements
```

### **Set (Hash Set)**
```python
# Creation
s = {1, 2, 3}
s = set([1, 2, 2, 3])        # From list, removes duplicates
s = {x for x in arr if x > 0}  # Comprehension
s = set()                    # Empty set (NOT {})

# Modification
s.add(x)                     # Add element - O(1)
s.remove(x)                  # Remove - O(1), raises error if missing
s.discard(x)                 # Remove - O(1), silent if missing
s.pop()                      # Remove arbitrary - O(1)
s.update([1,2,3])            # Add multiple

# Query
x in s                       # Check existence - O(1) ⭐
len(s)

# Set operations
s1 | s2, s1.union(s2)              # Union
s1 & s2, s1.intersection(s2)       # Intersection
s1 - s2, s1.difference(s2)         # Difference
s1 ^ s2, s1.symmetric_difference(s2)  # Symmetric diff

# Comparisons
s1.issubset(s2)              # s1 ⊆ s2
s1.issuperset(s2)            # s1 ⊇ s2
s1.isdisjoint(s2)            # No common elements
```

### **Tuple (Immutable Sequence)**
```python
# Creation
t = (1, 2, 3)
t = 1, 2, 3                  # Tuple packing (no parens needed)
t = (5,)                     # Single element (NOTE THE COMMA!)
t = tuple([1, 2, 3])         # From list

# Access
t[0], t[-1]                  # Indexing (same as list)
t[1:3]                       # Slicing (same as list)

# Unpacking (POWERFUL!)
x, y = (1, 2)                # Unpack
a, b = b, a                  # SWAP without temp!
first, *rest, last = (1,2,3,4,5)  # Extended unpacking

# Methods (only 2!)
t.count(x)                   # Count occurrences
t.index(x)                   # Find index

# Use cases
d[(x, y)] = value            # As dict key (lists can't!)
visited.add((row, col))      # In set (lists can't!)
return val1, val2            # Multiple returns
```

---

## 🛠️ Essential Utility Functions

### **Iteration**
```python
# range - Generate sequence
range(5)                     # 0,1,2,3,4
range(2, 5)                  # 2,3,4
range(0, 10, 2)              # 0,2,4,6,8
range(5, 0, -1)              # 5,4,3,2,1

# enumerate - Index + Value
for i, val in enumerate(arr):
    print(f"{i}: {val}")
for i, val in enumerate(arr, start=1):  # Custom start

# zip - Combine iterables
for a, b in zip(arr1, arr2):
    print(a, b)
names_ages = dict(zip(names, ages))  # Create dict

# Unzip
pairs = [(1,'a'), (2,'b')]
nums, letters = zip(*pairs)
```

### **String Methods**
```python
# join - Build string from list (CRITICAL!)
"".join(['a','b','c'])       # "abc"
" ".join(['hello','world'])  # "hello world"

# split - Break string into list
"a,b,c".split(",")           # ['a','b','c']
"hello world".split()        # ['hello','world']

# strip - Remove whitespace/chars
"  hello  ".strip()          # "hello"
"!!hello!!".strip("!")       # "hello"

# Other
s.replace("old", "new")      # Replace substring
s.startswith("pre")          # Check prefix
s.endswith("suf")            # Check suffix
s.lower(), s.upper()         # Case conversion
```

### **Sorting & Aggregation**
```python
# sorted - Return new sorted list
sorted([3,1,2])              # [1,2,3]
sorted(arr, reverse=True)    # Descending
sorted(arr, key=len)         # Sort by length
sorted(arr, key=lambda x: x[1])  # Sort by second element

# min/max - With custom key
max(words, key=len)          # Longest word
min(points, key=lambda p: p[0]+p[1])  # Min sum

# sum
sum([1,2,3])                 # 6
sum([1,2,3], 10)             # 16 (start from 10)

# any/all - Boolean checks
any(x > 0 for x in arr)      # True if ANY positive
all(x > 0 for x in arr)      # True if ALL positive
```

### **Type Checking**
```python
isinstance(x, int)           # Check type
isinstance(x, (int, float))  # Check multiple types
type(x) == int               # Exact type (use isinstance instead)
```

---

## 🎯 Interview Patterns Reference

### **Pattern 1: Two Pointers**
```python
# Template
left, right = 0, len(arr) - 1
while left < right:
    if condition:
        # Process
        left += 1
    else:
        right -= 1

# Use when: Sorted array, palindrome, pair finding
```

### **Pattern 2: Sliding Window**
```python
# Fixed size
window_sum = sum(arr[:k])
max_sum = window_sum
for i in range(k, len(arr)):
    window_sum = window_sum - arr[i-k] + arr[i]
    max_sum = max(max_sum, window_sum)

# Dynamic size
left = 0
for right in range(len(arr)):
    # Add arr[right] to window
    while window_invalid:
        # Remove arr[left] from window
        left += 1
    # Update result

# Use when: Subarray/substring problems, "maximum/minimum window"
```

### **Pattern 3: Hash Map (Two Sum)**
```python
seen = {}
for i, num in enumerate(arr):
    complement = target - num
    if complement in seen:
        return [seen[complement], i]
    seen[num] = i

# Use when: "Find pair that...", frequency counting
```

### **Pattern 4: Fast & Slow Pointers**
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True  # Cycle detected

# Use when: Linked list cycle, find middle
```

### **Pattern 5: Stack**
```python
stack = []
for char in s:
    if is_opening(char):
        stack.append(char)
    else:
        if not stack or not matches(stack[-1], char):
            return False
        stack.pop()
return len(stack) == 0

# Use when: Parentheses matching, next greater element, DFS
```

### **Pattern 6: Binary Search**
```python
left, right = 0, len(arr) - 1
while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
return -1

# Use when: Sorted array, "find in O(log n)"
```

### **Pattern 7: Dynamic Programming**
```python
# Top-down (Recursion + Memoization)
def solve(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= base_case:
        return base_value
    memo[n] = solve(n-1, memo) + solve(n-2, memo)
    return memo[n]

# Bottom-up (Iteration)
dp = [0] * (n + 1)
dp[0] = base_value
for i in range(1, n+1):
    dp[i] = dp[i-1] + dp[i-2]

# Use when: "Maximum/minimum", "count ways", optimization
```

---

## ⚡ Pythonic One-Liners

```python
# Reverse
arr[::-1]

# Swap
a, b = b, a

# Remove duplicates
list(set(arr))

# Frequency map
from collections import Counter
Counter(arr)

# Multiple conditions
if val in (1, 2, 3):  # Instead of val == 1 or val == 2 or val == 3

# Default dict value
d.get(key, 0)

# Check if all/any
all(x > 0 for x in arr)
any(x < 0 for x in arr)

# String palindrome
s == s[::-1]

# List comprehension with condition
[x for x in arr if x > 0]

# Dict comprehension
{k: v for k, v in pairs if v > 0}

# Find index safely
arr.index(x) if x in arr else -1

# Multiple return
return min(arr), max(arr)

# Chained comparison
if 0 <= x < n:  # Instead of x >= 0 and x < n
```

---

## 🚨 Common Mistakes to Avoid

```python
# ❌ Wrong: Empty set
d = {}  # This is a DICT, not set!
# ✅ Correct
s = set()

# ❌ Wrong: Single-element tuple
t = (5)  # This is just int 5
# ✅ Correct
t = (5,)  # Need comma

# ❌ Wrong: sort() returns None
arr = [3,1,2].sort()  # arr is None!
# ✅ Correct
arr = sorted([3,1,2])

# ❌ Wrong: Modifying while iterating
for key in d:
    del d[key]  # RuntimeError!
# ✅ Correct
for key in list(d.keys()):
    del d[key]

# ❌ Wrong: List as dict key
d[[1,2]] = "value"  # TypeError!
# ✅ Correct
d[(1,2)] = "value"  # Use tuple

# ❌ Wrong: Shallow copy for 2D array
matrix = [[0]*3] * 2  # All rows point to same list!
# ✅ Correct
matrix = [[0]*3 for _ in range(2)]

# ❌ Wrong: String concatenation in loop
result = ""
for char in s:
    result += char  # O(n²)
# ✅ Correct
result = "".join(s)  # O(n)

# ❌ Wrong: Using list for membership testing
if x in arr:  # O(n)
# ✅ Correct
arr_set = set(arr)
if x in arr_set:  # O(1)
```

---

## ⏱️ Time Complexity Quick Reference

| Operation | List | Dict | Set | Complexity |
|-----------|------|------|-----|------------|
| Access by index/key | `arr[i]` | `d[k]` | - | O(1) |
| Search | `x in arr` | `k in d` | `x in s` | O(n) / O(1) / O(1) |
| Insert | `append()` | `d[k]=v` | `add()` | O(1) / O(1) / O(1) |
| Delete | `pop()` | `del d[k]` | `remove()` | O(1) / O(1) / O(1) |
| Sort | `sort()` | - | - | O(n log n) |
| Min/Max | `min()` | - | - | O(n) |

---

## 📝 Interview Communication Template

```
1. "Let me make sure I understand: [restate problem]"
2. "A few clarifying questions: [ask 2-3 questions]"
3. "I'll start with brute force: [explain O(n²) approach]"
4. "To optimize, I'll use [data structure/pattern]: [explain]"
5. [Code while narrating your thought process]
6. "Let me test with the example: [walk through]"
7. "Time complexity: O(n), Space: O(n) because [explain]"
8. "Possible follow-ups: [mention optimizations]"
```

---

## 🎯 Pattern Recognition Flowchart

```
"Find pair/triplet with sum" → Hash Map (Two Sum)
"Maximum/minimum subarray" → Sliding Window or Kadane's
"Sorted array + O(1) space" → Two Pointers
"Frequency counting" → Counter or defaultdict(int)
"Parentheses/brackets" → Stack
"Cycle detection" → Fast & Slow Pointers
"Optimization problem" → Dynamic Programming
"Search in sorted" → Binary Search
"All subsets/permutations" → Backtracking
"Graph traversal" → BFS/DFS
```

---

## 🏆 Must-Know for Interviews

### **Top 5 Data Structures**
1. **Dict** - 70% of problems
2. **List** - 90% of problems
3. **Set** - O(1) lookup
4. **Tuple** - Coordinates, dict keys
5. **Counter** - Frequency problems

### **Top 5 Patterns**
1. **Hash Map** (Two Sum)
2. **Two Pointers**
3. **Sliding Window**
4. **Stack**
5. **Binary Search**

### **Top 5 Utility Functions**
1. **enumerate()** - Index + value
2. **sorted(key=...)** - Custom sorting
3. **join()** - Build strings
4. **any()/all()** - Boolean checks
5. **zip()** - Parallel iteration

---

**Print this page and keep it next to you while practicing!** 🚀

