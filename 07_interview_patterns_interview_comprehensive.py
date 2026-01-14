"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 INTERVIEW PATTERNS - SENIOR ENGINEER MASTERY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Interviewer: Principal Engineer | Pattern Recognition Expert
Level: 5+ YOE | Focus: INSTANTLY identify which pattern applies
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣ OVERVIEW
Pattern recognition separates senior from junior engineers.
You MUST identify pattern in < 30 seconds or you FAIL.

THE 7 CORE PATTERNS:
1. Two Pointers
2. Sliding Window
3. Hash Map (dict/set)
4. Stack
5. Binary Search
6. Fast & Slow Pointers
7. Dynamic Programming

INTERVIEWER EXPECTATION:
Hear problem → Identify pattern → State approach → Code

REJECTION SIGNALS:
❌ Can't identify pattern in 1 minute
❌ Jumps to brute force without pattern thinking
❌ Doesn't explain WHY pattern applies
❌ Confuses patterns (sliding window vs two pointers)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

2️⃣ PATTERN 1: TWO POINTERS
═══════════════════════════════════════════════════════════════════════

RECOGNITION SIGNALS:
• "Sorted array" + "find pair"
• "In-place" modification
• "Remove duplicates"
• "Reverse" array/string
• "Merge" two sorted arrays

TEMPLATE:
def two_pointers(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        if condition(arr[left], arr[right]):
            return (left, right)
        elif need_larger:
            left += 1
        else:
            right -= 1

COMPLEXITY: O(n) time, O(1) space

INTERVIEW QUESTIONS:

Q1: Two Sum II (sorted array)
STRONG: "Sorted array signals two pointers. Start at ends, move based on sum 
comparison. O(n) time, O(1) space."

def two_sum_sorted(nums, target):
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

Q2: Remove Duplicates (in-place)
def remove_duplicates(nums):
    if not nums: return 0
    slow = 1
    for fast in range(1, len(nums)):
        if nums[fast] != nums[fast-1]:
            nums[slow] = nums[fast]
            slow += 1
    return slow

Q3: Container With Most Water
SIGNAL: "Two ends", "maximize area"
APPROACH: Start at ends, move pointer with smaller height inward.

WHAT INTERVIEWERS LISTEN FOR:
✓ "Two pointers, one at each end..."
✓ Explains why sorted matters
✓ Mentions O(1) space advantage

❌ Doesn't recognize pattern
❌ Uses hash map when two pointers better

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

3️⃣ PATTERN 2: SLIDING WINDOW
═══════════════════════════════════════════════════════════════════════

RECOGNITION SIGNALS:
• "Subarray" or "substring"
• "Contiguous elements"
• "Maximum/minimum length"
• "Window of size k"
• "Longest/shortest with..."

TEMPLATE:
def sliding_window(arr, k):
    window_data = initialize()
    left = 0
    result = initial_value
    
    for right in range(len(arr)):
        # Add right element to window
        add_to_window(arr[right], window_data)
        
        # Shrink from left if invalid
        while window_invalid(window_data):
            remove_from_window(arr[left], window_data)
            left += 1
        
        # Update result
        result = update(result, window_data, right - left + 1)
    
    return result

COMPLEXITY: O(n) time, O(1) or O(k) space

INTERVIEW QUESTIONS:

Q1: Maximum Sum Subarray of Size K
STRONG: "Fixed window size signals sliding window. Compute initial window, then
slide by removing left, adding right. O(n) vs O(n*k) recomputing."

def max_sum_subarray(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i-k] + nums[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

Q2: Longest Substring Without Repeating
STRONG: "Variable window with constraint. Use set to track chars, shrink when duplicate."

def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len

Q3: Minimum Window Substring
SIGNAL: "Minimum window containing..."
APPROACH: Expand right until valid, shrink left while valid.

WHAT INTERVIEWERS LISTEN FOR:
✓ "Sliding window, expand right, shrink left..."
✓ Distinguishes fixed vs variable window
✓ Explains why O(n) not O(n²)

❌ Recomputes window from scratch each time
❌ Doesn't recognize subarray/substring signal

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

4️⃣ PATTERN 3: HASH MAP (Dict/Set)
═══════════════════════════════════════════════════════════════════════

RECOGNITION SIGNALS:
• "Find two elements that..."
• "Check if exists"
• "Count frequency"
• "Group by..."
• O(n²) → O(n) optimization

TEMPLATE:
def hash_map_pattern(items):
    seen = {}  # or set()
    for item in items:
        if condition(item, seen):
            return found(item, seen)
        seen[item] = value
    return not_found

COMPLEXITY: O(n) time, O(n) space

INTERVIEW QUESTIONS:

Q1: Two Sum (THE interview question)
STRONG: "Hash map for O(1) complement lookup. Store value->index as we go."

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None

Q2: Group Anagrams
STRONG: "Anagrams have same sorted chars. Use sorted tuple as hash key."

def group_anagrams(words):
    from collections import defaultdict
    groups = defaultdict(list)
    for word in words:
        key = tuple(sorted(word))
        groups[key].append(word)
    return list(groups.values())

Q3: Longest Consecutive Sequence
SIGNAL: "Consecutive", "unsorted array"
APPROACH: Set for O(1) lookup, only start from sequence beginnings.

WHAT INTERVIEWERS LISTEN FOR:
✓ "Hash map gives O(1) lookup..."
✓ "This optimizes from O(n²) to O(n)..."
✓ Mentions space-time tradeoff

❌ Can't code Two Sum in 3 minutes → DISQUALIFYING
❌ Uses nested loops when hash map obvious

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

5️⃣ PATTERN 4: STACK
═══════════════════════════════════════════════════════════════════════

RECOGNITION SIGNALS:
• "Valid parentheses"
• "Next greater element"
• "Evaluate expression"
• "Reverse" or "undo" operations
• LIFO (Last In, First Out)

TEMPLATE:
def stack_pattern(items):
    stack = []
    for item in items:
        # Push when condition met
        if should_push(item):
            stack.append(item)
        # Pop when condition met
        elif should_pop() and stack:
            stack.pop()
    return process(stack)

COMPLEXITY: O(n) time, O(n) space

INTERVIEW QUESTIONS:

Q1: Valid Parentheses
STRONG: "Stack for matching pairs. Push open, pop on close, check match."

def is_valid(s):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in s:
        if char in pairs:
            stack.append(char)
        elif stack and pairs[stack[-1]] == char:
            stack.pop()
        else:
            return False
    
    return len(stack) == 0

Q2: Daily Temperatures
STRONG: "Next greater element pattern. Monotonic decreasing stack."

def daily_temperatures(temps):
    result = [0] * len(temps)
    stack = []  # Stores indices
    
    for i, temp in enumerate(temps):
        while stack and temps[stack[-1]] < temp:
            prev_i = stack.pop()
            result[prev_i] = i - prev_i
        stack.append(i)
    
    return result

WHAT INTERVIEWERS LISTEN FOR:
✓ "Stack for LIFO operations..."
✓ Recognizes parentheses/bracket problems
✓ Knows monotonic stack variant

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

6️⃣ PATTERN 5: BINARY SEARCH
═══════════════════════════════════════════════════════════════════════

RECOGNITION SIGNALS:
• "Sorted array"
• "Find in O(log n)"
• "Search space reduction"
• "Find minimum/maximum where..."

TEMPLATE:
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

COMPLEXITY: O(log n) time, O(1) space

INTERVIEW QUESTIONS:

Q1: Search Insert Position
def search_insert(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left  # Insert position

Q2: Find Peak Element
SIGNAL: "Local maximum"
APPROACH: Binary search, move toward higher neighbor.

WHAT INTERVIEWERS LISTEN FOR:
✓ "Binary search for O(log n)..."
✓ Handles mid calculation without overflow
✓ Correct boundary conditions (< vs <=)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

7️⃣ PATTERN 6: FAST & SLOW POINTERS
═══════════════════════════════════════════════════════════════════════

RECOGNITION SIGNALS:
• "Linked list cycle"
• "Middle of linked list"
• "Find duplicate in array"
• "Circular" detection

TEMPLATE:
def fast_slow(head):
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True  # Cycle found
    
    return False

INTERVIEW QUESTIONS:

Q1: Linked List Cycle
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

Q2: Find Duplicate Number
SIGNAL: "Array with duplicates", "O(1) space"
APPROACH: Treat as linked list, use Floyd's cycle detection.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

8️⃣ PATTERN 7: DYNAMIC PROGRAMMING
═══════════════════════════════════════════════════════════════════════

RECOGNITION SIGNALS:
• "Maximum/minimum"
• "Number of ways"
• "Longest/shortest"
• Overlapping subproblems
• Optimal substructure

TEMPLATE:
def dp_pattern(n):
    dp = [initial_value] * (n + 1)
    dp[0] = base_case
    
    for i in range(1, n + 1):
        for decision in possible_decisions:
            dp[i] = optimize(dp[i], dp[prev_state] + cost)
    
    return dp[n]

INTERVIEW QUESTIONS:

Q1: Climbing Stairs
def climb_stairs(n):
    if n <= 2: return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

Q2: Coin Change
SIGNAL: "Minimum coins", "ways to make change"
APPROACH: DP with coin values as decisions.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

9️⃣ PATTERN DECISION TREE
═══════════════════════════════════════════════════════════════════════

PROBLEM TYPE → PATTERN MAPPING:

"Find pair that sums to X"
├─ Sorted array? → Two Pointers
└─ Unsorted? → Hash Map

"Substring/Subarray with property"
├─ Fixed size? → Sliding Window (fixed)
└─ Variable size? → Sliding Window (variable)

"Check if exists / count frequency"
└─ Hash Map (dict/set)

"Parentheses / Next Greater"
└─ Stack

"Sorted + Search"
└─ Binary Search

"Linked list cycle / middle"
└─ Fast & Slow Pointers

"Optimize over choices"
└─ Dynamic Programming

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔟 MOCK INTERVIEW: PATTERN RECOGNITION DRILL
═══════════════════════════════════════════════════════════════════════

INTERVIEWER: "I'll give you problem descriptions. Identify the pattern in < 15 seconds."

Q1: "Given sorted array, find two numbers that sum to target."
EXPECTED: "Two pointers - sorted array signal" [< 5 sec]

Q2: "Find longest substring with at most 2 distinct characters."
EXPECTED: "Sliding window - substring with constraint" [< 10 sec]

Q3: "Check if array contains duplicates."
EXPECTED: "Hash set - membership check" [< 5 sec]

Q4: "Valid parentheses string."
EXPECTED: "Stack - matching pairs" [< 5 sec]

Q5: "Find element in rotated sorted array."
EXPECTED: "Modified binary search" [< 10 sec]

Q6: "Detect cycle in linked list."
EXPECTED: "Fast & slow pointers" [< 5 sec]

Q7: "Minimum coins to make amount."
EXPECTED: "Dynamic programming - optimization" [< 10 sec]

SCORING:
7/7 in < 15 sec each: STRONG HIRE - Pattern mastery
5-6/7: HIRE - Solid pattern knowledge
< 5/7: NO HIRE - Can't recognize patterns

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⓫ SELF-ASSESSMENT
═══════════════════════════════════════════════════════════════════════

TIER 1: PATTERN IDENTIFICATION (7/7 REQUIRED)
□ Can identify two pointers from "sorted + pair"
□ Recognize sliding window from "subarray/substring"
□ Know hash map for "find elements that..."
□ Identify stack for "parentheses/next greater"
□ Binary search for "sorted + search"
□ Fast/slow for "linked list cycle"
□ DP for "optimize over choices"

TIER 2: PATTERN APPLICATION (5/7)
□ Can code two pointers in 3 min
□ Can code sliding window in 5 min
□ Can code Two Sum in 2 min (CRITICAL)
□ Can code valid parentheses in 3 min
□ Can code binary search without bugs
□ Know when NOT to use a pattern
□ Can mix patterns (e.g., sliding window + hash map)

CRITICAL CHECKPOINT:
Given: "Find two numbers that sum to target in array"
Can you identify pattern + code solution in < 4 minutes total?

NO → NOT READY. This is THE gateway skill.

INTERVIEWER CONCLUSION:
< 7/7 TIER 1: "Can't identify patterns. Will struggle with most problems. STRONG REJECT."
7/7 TIER 1, < 5/7 TIER 2: "Knows patterns but slow to apply. WEAK HIRE."
7/7 TIER 1, >= 5/7 TIER 2: "Pattern mastery. Will solve problems efficiently. STRONG HIRE."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FINAL MANDATE:
Pattern recognition is THE skill that separates those who pass interviews from
those who fail. You must identify pattern in < 30 seconds or you waste time.

Drill these 7 patterns until recognition is INSTANT.
This is not negotiable for senior positions.
"""
