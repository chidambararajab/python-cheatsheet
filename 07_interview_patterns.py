"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 PYTHON INTERVIEW PATTERNS & TECHNIQUES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
For 5+ YOE Developer | Pattern Recognition | Problem-Solving Framework
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Master these patterns and you'll recognize 80% of interview problems!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

# ═══════════════════════════════════════════════════════════════════════
# PATTERN 1: TWO POINTERS
# ═══════════════════════════════════════════════════════════════════════

print("🔥 PATTERN 1: TWO POINTERS\n" + "="*70)

pattern = """
📌 WHEN TO USE:
  - Array/string problems with linear scan
  - "Find pair/triplet that satisfies condition"
  - Sorted array problems
  - Palindrome checking
  - In-place array modification

📌 VARIATIONS:
  1. Opposite ends (left=0, right=n-1)
  2. Same direction (slow/fast pointers)
  3. Sliding window (left/right expanding/contracting)

📌 TIME COMPLEXITY: Usually O(n)
"""
print(pattern)

# ────────────────────────────────────────────────────────────────────────
# Variation 1: Opposite Ends
# ────────────────────────────────────────────────────────────────────────

print("\n▶ Variation 1: Opposite Ends (Two Sum - Sorted)")

def two_sum_sorted(nums, target):
    """
    🎤 INTERVIEWER NARRATION:
    "Since the array is sorted, I'll use two pointers starting from
    opposite ends. If the sum is too small, move left pointer right
    to increase sum. If too large, move right pointer left to decrease.
    This gives O(n) time, O(1) space."
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

print(f"✅ two_sum_sorted([1,2,3,4,6], 6) = {two_sum_sorted([1,2,3,4,6], 6)}")


# ────────────────────────────────────────────────────────────────────────
# Variation 2: Same Direction (Remove Duplicates)
# ────────────────────────────────────────────────────────────────────────

print("\n▶ Variation 2: Same Direction (Slow/Fast)")

def remove_duplicates(nums):
    """
    🎤 INTERVIEWER NARRATION:
    "I'll use slow/fast pointers. Slow tracks where to place the next
    unique element. Fast scans ahead. When fast finds a new element,
    we place it at slow and increment slow. This modifies in-place."
    """
    if not nums:
        return 0
    
    slow = 1  # Position for next unique element
    
    for fast in range(1, len(nums)):
        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]
            slow += 1
    
    return slow

arr = [1, 1, 2, 2, 3, 4, 4, 5]
length = remove_duplicates(arr)
print(f"✅ Unique elements: {arr[:length]}")


# ────────────────────────────────────────────────────────────────────────
# Pattern Recognition
# ────────────────────────────────────────────────────────────────────────

recognition = """
🎯 RECOGNIZE TWO POINTERS WHEN YOU SEE:
  - "Find pair/triplet with sum..."
  - "Remove duplicates in-place"
  - "Is palindrome?"
  - "Container with most water"
  - "Trapping rain water"
  - Sorted array + O(1) space requirement
"""
print(recognition)


# ═══════════════════════════════════════════════════════════════════════
# PATTERN 2: SLIDING WINDOW
# ═══════════════════════════════════════════════════════════════════════

print("\n\n🔥 PATTERN 2: SLIDING WINDOW\n" + "="*70)

pattern = """
📌 WHEN TO USE:
  - "Maximum/minimum subarray of size k"
  - "Longest substring with condition"
  - Problems involving contiguous sequences
  - Optimization over all windows

📌 TYPES:
  1. Fixed-size window
  2. Dynamic-size window

📌 TIME COMPLEXITY: Usually O(n)
"""
print(pattern)

# ────────────────────────────────────────────────────────────────────────
# Type 1: Fixed-Size Window
# ────────────────────────────────────────────────────────────────────────

print("\n▶ Type 1: Fixed-Size Window")

def max_sum_subarray(nums, k):
    """
    🎤 INTERVIEWER NARRATION:
    "I'll use a fixed-size sliding window. First, compute sum of first k
    elements. Then slide: subtract element leaving, add element entering.
    This avoids recalculating the entire sum each time, giving O(n) vs O(nk)."
    """
    if len(nums) < k:
        return 0
    
    # Initial window
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    # Slide window
    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

print(f"✅ max_sum_subarray([1,4,2,10,23,3,1,0,20], 4) = {max_sum_subarray([1,4,2,10,23,3,1,0,20], 4)}")


# ────────────────────────────────────────────────────────────────────────
# Type 2: Dynamic-Size Window
# ────────────────────────────────────────────────────────────────────────

print("\n▶ Type 2: Dynamic-Size Window")

def longest_substring_k_distinct(s, k):
    """
    🎤 INTERVIEWER NARRATION:
    "I'll use a dynamic sliding window with a frequency map. Expand right
    to grow window. When we exceed k distinct characters, shrink from left
    until valid. Track maximum length seen."
    """
    from collections import defaultdict
    
    char_freq = defaultdict(int)
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        char_freq[s[right]] += 1
        
        # Shrink while invalid
        while len(char_freq) > k:
            char_freq[s[left]] -= 1
            if char_freq[s[left]] == 0:
                del char_freq[s[left]]
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length

print(f"✅ longest_substring_k_distinct('eceba', 2) = {longest_substring_k_distinct('eceba', 2)}")

recognition = """
🎯 RECOGNIZE SLIDING WINDOW WHEN YOU SEE:
  - "Maximum/minimum subarray/substring"
  - "Longest/shortest window with condition"
  - "Find all subarrays with..."
  - Contiguous sequence problems
  - "At most k distinct..."
"""
print(recognition)


# ═══════════════════════════════════════════════════════════════════════
# PATTERN 3: HASH MAP / FREQUENCY COUNTING
# ═══════════════════════════════════════════════════════════════════════

print("\n\n🔥 PATTERN 3: HASH MAP / FREQUENCY COUNTING\n" + "="*70)

pattern = """
📌 WHEN TO USE:
  - "Find elements that sum to X"
  - Frequency/occurrence counting
  - "Check if anagram"
  - Graph adjacency lists
  - Caching/memoization

📌 KEY INSIGHT:
  Dict trades O(n) space for O(1) lookup time
  Often converts O(n²) brute force to O(n)

📌 PYTHON TOOLS:
  - dict with get(key, default)
  - defaultdict(int/list/set)
  - Counter for frequency counting
"""
print(pattern)

# ────────────────────────────────────────────────────────────────────────
# Application: Two Sum Pattern
# ────────────────────────────────────────────────────────────────────────

print("\n▶ Application: Two Sum Pattern")

def two_sum(nums, target):
    """Classic hash map pattern for O(n) solution"""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None

# ────────────────────────────────────────────────────────────────────────
# Application: Frequency Count Pattern
# ────────────────────────────────────────────────────────────────────────

print("\n▶ Application: Frequency Counting")

def first_unique_char(s):
    """
    🎤 INTERVIEWER NARRATION:
    "I'll use Counter to get frequencies in O(n). Then scan through
    the string again to find first character with count 1. Total O(n)."
    """
    from collections import Counter
    freq = Counter(s)
    
    for i, char in enumerate(s):
        if freq[char] == 1:
            return i
    return -1

print(f"✅ first_unique_char('leetcode') = {first_unique_char('leetcode')}")

recognition = """
🎯 RECOGNIZE HASH MAP WHEN YOU SEE:
  - "Find two elements that..."
  - "Count occurrences/frequency"
  - "Check if anagram"
  - "Group by property"
  - Need O(1) lookup
"""
print(recognition)


# ═══════════════════════════════════════════════════════════════════════
# PATTERN 4: FAST & SLOW POINTERS (Floyd's Cycle Detection)
# ═══════════════════════════════════════════════════════════════════════

print("\n\n🔥 PATTERN 4: FAST & SLOW POINTERS\n" + "="*70)

pattern = """
📌 WHEN TO USE:
  - Linked list cycle detection
  - Find middle of linked list
  - Detect start of cycle
  - Happy number problem

📌 KEY INSIGHT:
  Slow moves 1 step, fast moves 2 steps
  If cycle exists, they'll meet

📌 TIME COMPLEXITY: O(n), SPACE: O(1)
"""
print(pattern)

# ────────────────────────────────────────────────────────────────────────
# Application: Cycle Detection Pattern
# ────────────────────────────────────────────────────────────────────────

print("\n▶ Application: Happy Number (Cycle Detection in Sequence)")

def is_happy(n):
    """
    🎤 INTERVIEWER NARRATION:
    "I'll use fast/slow pointers to detect a cycle. Slow calculates
    next number once, fast calculates twice. If they meet and it's not 1,
    there's a cycle and the number isn't happy."
    """
    def get_next(num):
        total = 0
        while num > 0:
            digit = num % 10
            total += digit ** 2
            num //= 10
        return total
    
    slow = n
    fast = get_next(n)
    
    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))
    
    return fast == 1

print(f"✅ is_happy(19) = {is_happy(19)}")

recognition = """
🎯 RECOGNIZE FAST/SLOW POINTERS WHEN YOU SEE:
  - "Detect cycle in linked list"
  - "Find middle of linked list"
  - "Happy number"
  - Problems with potential infinite loops
"""
print(recognition)


# ═══════════════════════════════════════════════════════════════════════
# PATTERN 5: STACK
# ═══════════════════════════════════════════════════════════════════════

print("\n\n🔥 PATTERN 5: STACK\n" + "="*70)

pattern = """
📌 WHEN TO USE:
  - Parentheses/bracket matching
  - "Next greater/smaller element"
  - Expression evaluation
  - Backtracking problems
  - Undo operations

📌 PYTHON IMPLEMENTATION:
  Use list with append() and pop()
  
📌 TIME COMPLEXITY: O(1) for push/pop
"""
print(pattern)

# ────────────────────────────────────────────────────────────────────────
# Application: Next Greater Element
# ────────────────────────────────────────────────────────────────────────

print("\n▶ Application: Next Greater Element")

def next_greater_elements(nums):
    """
    🎤 INTERVIEWER NARRATION:
    "I'll use a monotonic decreasing stack. For each element, I pop
    all smaller elements from stack - current element is their next
    greater. Then push current element. This processes each element
    once, giving O(n) time."
    """
    n = len(nums)
    result = [-1] * n
    stack = []  # Store indices
    
    # Process array twice for circular behavior
    for i in range(2 * n):
        idx = i % n
        
        while stack and nums[stack[-1]] < nums[idx]:
            result[stack.pop()] = nums[idx]
        
        if i < n:
            stack.append(idx)
    
    return result

print(f"✅ next_greater([1,2,1]) = {next_greater_elements([1,2,1])}")

recognition = """
🎯 RECOGNIZE STACK WHEN YOU SEE:
  - "Valid parentheses"
  - "Next greater/smaller element"
  - "Evaluate expression"
  - "Backtracking" (DFS)
  - Need LIFO behavior
"""
print(recognition)


# ═══════════════════════════════════════════════════════════════════════
# PATTERN 6: BINARY SEARCH
# ═══════════════════════════════════════════════════════════════════════

print("\n\n🔥 PATTERN 6: BINARY SEARCH\n" + "="*70)

pattern = """
📌 WHEN TO USE:
  - Sorted array search
  - "Find first/last occurrence"
  - "Search in rotated array"
  - "Find peak element"
  - Optimization problems (minimize/maximize)

📌 KEY INSIGHT:
  Reduce search space by half each iteration
  
📌 TIME COMPLEXITY: O(log n)

📌 TEMPLATE:
  left, right = 0, len(arr) - 1
  while left <= right:
      mid = (left + right) // 2
      if condition:
          # update answer, move pointers
"""
print(pattern)

# ────────────────────────────────────────────────────────────────────────
# Template Implementation
# ────────────────────────────────────────────────────────────────────────

print("\n▶ Binary Search Template")

def binary_search(nums, target):
    """
    🎤 INTERVIEWER NARRATION:
    "I'll use binary search on the sorted array. Compare middle element
    with target. If equal, found it. If target is larger, search right half.
    If smaller, search left half. This gives O(log n) time."
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

print(f"✅ binary_search([1,2,3,4,5], 3) = {binary_search([1,2,3,4,5], 3)}")

# ────────────────────────────────────────────────────────────────────────
# Advanced: First Occurrence
# ────────────────────────────────────────────────────────────────────────

print("\n▶ Advanced: Find First Occurrence")

def first_occurrence(nums, target):
    """
    🎤 INTERVIEWER NARRATION:
    "To find first occurrence, when I find target, I don't return
    immediately. Instead, I record it and continue searching left half
    to find an earlier occurrence."
    """
    left, right = 0, len(nums) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            result = mid  # Record and keep searching left
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

print(f"✅ first_occurrence([1,2,2,2,3], 2) = {first_occurrence([1,2,2,2,3], 2)}")

recognition = """
🎯 RECOGNIZE BINARY SEARCH WHEN YOU SEE:
  - Sorted array
  - "Find in O(log n)"
  - "Search in rotated sorted array"
  - "Find peak"
  - "Minimize/maximize with condition"
"""
print(recognition)


# ═══════════════════════════════════════════════════════════════════════
# PATTERN 7: DYNAMIC PROGRAMMING (DP)
# ═══════════════════════════════════════════════════════════════════════

print("\n\n🔥 PATTERN 7: DYNAMIC PROGRAMMING\n" + "="*70)

pattern = """
📌 WHEN TO USE:
  - Optimization problems (min/max)
  - Counting problems
  - "Can you reach..."
  - Problems with overlapping subproblems
  - Problems with optimal substructure

📌 APPROACHES:
  1. Top-Down (Recursion + Memoization)
  2. Bottom-Up (Iterative + DP array)

📌 STEPS:
  1. Define state (what does dp[i] represent?)
  2. Find recurrence relation
  3. Identify base cases
  4. Implement with memoization or iteration
"""
print(pattern)

# ────────────────────────────────────────────────────────────────────────
# Example: Climbing Stairs
# ────────────────────────────────────────────────────────────────────────

print("\n▶ Example: Climbing Stairs")

def climb_stairs_recursive(n, memo=None):
    """
    🎤 INTERVIEWER NARRATION:
    "Top-down DP: I'll use recursion with memoization. At each step,
    I can climb 1 or 2 stairs, so ways(n) = ways(n-1) + ways(n-2).
    Memoization prevents recomputing same subproblems."
    
    Time: O(n), Space: O(n)
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 2:
        return n
    
    memo[n] = climb_stairs_recursive(n - 1, memo) + climb_stairs_recursive(n - 2, memo)
    return memo[n]

def climb_stairs_iterative(n):
    """
    🎤 INTERVIEWER NARRATION:
    "Bottom-up DP: I'll build solution iteratively. dp[i] represents
    ways to reach step i. Base cases: dp[1]=1, dp[2]=2. Then
    dp[i] = dp[i-1] + dp[i-2]. This is just Fibonacci!"
    
    Time: O(n), Space: O(n)
    """
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

def climb_stairs_optimized(n):
    """
    🎤 INTERVIEWER NARRATION:
    "Space optimization: Since I only need previous two values,
    I can use two variables instead of array. This reduces space
    to O(1)."
    
    Time: O(n), Space: O(1)
    """
    if n <= 2:
        return n
    
    prev2 = 1
    prev1 = 2
    
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1

print(f"✅ climb_stairs(5) = {climb_stairs_optimized(5)}")

recognition = """
🎯 RECOGNIZE DP WHEN YOU SEE:
  - "Maximum/minimum path/cost"
  - "Count ways to..."
  - "Longest/shortest subsequence"
  - "Can you partition..."
  - "Coin change"
  - "House robber"
"""
print(recognition)


# ═══════════════════════════════════════════════════════════════════════
# PATTERN RECOGNITION FLOWCHART
# ═══════════════════════════════════════════════════════════════════════

flowchart = """
╔═══════════════════════════════════════════════════════════════════════╗
║                  🎯 PATTERN RECOGNITION FLOWCHART                     ║
╚═══════════════════════════════════════════════════════════════════════╝

START
  │
  ├─ Is array/string sorted?
  │   └─ YES → Try TWO POINTERS or BINARY SEARCH
  │
  ├─ Need to find pair/triplet with sum?
  │   └─ Use HASH MAP (two sum pattern)
  │
  ├─ Problem about contiguous subarray/substring?
  │   └─ Try SLIDING WINDOW
  │
  ├─ Need to track visited/seen elements?
  │   └─ Use SET or HASH MAP
  │
  ├─ Problem has parentheses/brackets?
  │   └─ Use STACK
  │
  ├─ Linked list cycle detection?
  │   └─ Use FAST & SLOW POINTERS
  │
  ├─ Optimization problem (max/min)?
  │   └─ Consider DYNAMIC PROGRAMMING or GREEDY
  │
  ├─ Need to explore all possibilities?
  │   └─ Use BACKTRACKING or DFS
  │
  ├─ Counting frequencies/occurrences?
  │   └─ Use COUNTER or defaultdict
  │
  └─ Graph traversal?
      └─ BFS (shortest path) or DFS (explore all)
"""
print(flowchart)


# ═══════════════════════════════════════════════════════════════════════
# PYTHON-SPECIFIC INTERVIEW TRICKS
# ═══════════════════════════════════════════════════════════════════════

tricks = """
╔═══════════════════════════════════════════════════════════════════════╗
║              🐍 PYTHON-SPECIFIC INTERVIEW TRICKS                      ║
╚═══════════════════════════════════════════════════════════════════════╝

1️⃣ SWAPPING WITHOUT TEMP VARIABLE
   a, b = b, a

2️⃣ MULTIPLE RETURN VALUES
   def min_max(arr):
       return min(arr), max(arr)
   
   minimum, maximum = min_max([1,2,3])

3️⃣ DEFAULT DICT FOR FREQUENCY
   from collections import defaultdict
   freq = defaultdict(int)
   for num in nums:
       freq[num] += 1  # No need to check if key exists!

4️⃣ COUNTER FOR TOP K ELEMENTS
   from collections import Counter
   counter = Counter(nums)
   top_k = counter.most_common(k)

5️⃣ SET FOR O(1) LOOKUP
   seen = set(nums)
   if target in seen:  # O(1) instead of O(n)

6️⃣ ENUMERATE INSTEAD OF RANGE(LEN())
   # ❌ BAD
   for i in range(len(arr)):
       print(i, arr[i])
   
   # ✅ GOOD
   for i, val in enumerate(arr):
       print(i, val)

7️⃣ ZIP FOR PARALLEL ITERATION
   names = ['Alice', 'Bob']
   ages = [25, 30]
   for name, age in zip(names, ages):
       print(f"{name}: {age}")

8️⃣ LIST COMPREHENSION OVER MAP/FILTER
   # More Pythonic
   evens = [x for x in nums if x % 2 == 0]

9️⃣ STRING BUILDING WITH JOIN
   # ❌ SLOW: O(n²)
   result = ""
   for char in chars:
       result += char
   
   # ✅ FAST: O(n)
   result = "".join(chars)

🔟 ANY/ALL FOR BOOLEAN CHECKS
   if all(x > 0 for x in nums):
       print("All positive")
   
   if any(x < 0 for x in nums):
       print("Has negative")
"""
print(tricks)


# ═══════════════════════════════════════════════════════════════════════
# FINAL SUMMARY
# ═══════════════════════════════════════════════════════════════════════

summary = """
╔═══════════════════════════════════════════════════════════════════════╗
║                    🏆 MASTERY CHECKLIST                               ║
╚═══════════════════════════════════════════════════════════════════════╝

DATA STRUCTURES:
  ✅ List - Dynamic array, O(1) access
  ✅ Tuple - Immutable, hashable
  ✅ Set - O(1) lookup, uniqueness
  ✅ Dict - Hash map, THE most important!

PATTERNS:
  ✅ Two Pointers
  ✅ Sliding Window
  ✅ Hash Map / Frequency Count
  ✅ Fast & Slow Pointers
  ✅ Stack
  ✅ Binary Search
  ✅ Dynamic Programming

UTILITY FUNCTIONS:
  ✅ enumerate, zip, range
  ✅ sorted, min, max, sum
  ✅ any, all
  ✅ join, split, strip
  ✅ isinstance, type

INTERVIEW SKILLS:
  ✅ Think aloud - narrate your process
  ✅ Start with brute force, then optimize
  ✅ Test with edge cases
  ✅ State time & space complexity
  ✅ Write clean, Pythonic code

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎉 YOU'RE NOW READY FOR PYTHON INTERVIEWS! 🎉
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
print(summary)

