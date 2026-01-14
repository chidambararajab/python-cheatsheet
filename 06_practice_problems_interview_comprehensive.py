"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 PRACTICE PROBLEMS - REAL INTERVIEW SCENARIOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Interviewer: Senior Bar-Raiser | Real Problems from FAANG
Level: 5+ YOE | Time Limit: 45 minutes per session
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Each problem includes:
• Problem statement
• Pattern identification
• Brute force approach
• Optimal solution
• Complexity analysis
• Common mistakes
• Interviewer evaluation criteria

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

# ═══════════════════════════════════════════════════════════════════════
# PROBLEM 1: TWO SUM (THE GATEWAY PROBLEM)
# ═══════════════════════════════════════════════════════════════════════

"""
PROBLEM STATEMENT:
Given array of integers nums and integer target, return indices of two numbers
that add up to target. Assume exactly one solution exists.

Example: nums = [2,7,11,15], target = 9 → [0,1] (2 + 7 = 9)

DIFFICULTY: Easy
PATTERN: Hash Map
TIME LIMIT: Must code in < 3 minutes or FAIL
FREQUENCY: Appears in 80% of initial screens

WHAT INTERVIEWER EXPECTS:
✓ Immediately suggests hash map
✓ Explains O(n²) → O(n) optimization
✓ Codes without bugs in 2-3 minutes
✓ Handles edge cases (empty, no solution)
"""

# BRUTE FORCE - O(n²) - ❌ Interviewer will ask to optimize
def two_sum_brute(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None

# OPTIMAL - O(n) - ✓ What interviewer wants
def two_sum(nums, target):
    """
    Time: O(n) - single pass
    Space: O(n) - hash map
    
    THINK-ALOUD NARRATION:
    "I'll use hash map to store values we've seen. For each number, I check if
    its complement (target - num) exists in map. This gives O(1) lookup per element,
    O(n) total instead of O(n²) nested loops."
    """
    seen = {}  # value -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return None

"""
COMMON MISTAKES:
❌ Returns values instead of indices
❌ Doesn't check if complement exists before accessing seen[complement]
❌ Uses nested loops instead of hash map
❌ Takes > 5 minutes to code

INTERVIEWER DECISION:
< 3 min, working code: STRONG HIRE
3-5 min, working code: HIRE
> 5 min or bugs: NO HIRE (for 5+ YOE, this is disqualifying)
"""


# ═══════════════════════════════════════════════════════════════════════
# PROBLEM 2: VALID ANAGRAM
# ═══════════════════════════════════════════════════════════════════════

"""
PROBLEM: Check if two strings are anagrams (same characters, different order).
Example: "anagram" and "nagaram" → True

PATTERN: Hash Map / Counter
TIME: Should code in < 2 minutes
"""

def is_anagram_manual(s, t):
    """Manual frequency counting"""
    if len(s) != len(t):
        return False
    
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    for char in t:
        if char not in freq or freq[char] == 0:
            return False
        freq[char] -= 1
    
    return True

def is_anagram_pythonic(s, t):
    """Pythonic - what strong candidates do"""
    from collections import Counter
    return Counter(s) == Counter(t)

def is_anagram_sorting(s, t):
    """Alternative - O(n log n)"""
    return sorted(s) == sorted(t)

"""
INTERVIEWER EVALUATION:
✓ STRONG: Uses Counter immediately
✓ HIRE: Manual approach but clean
✗ WEAK: Doesn't know Counter for 5+ YOE
"""


# ═══════════════════════════════════════════════════════════════════════
# PROBLEM 3: CONTAINS DUPLICATE
# ═══════════════════════════════════════════════════════════════════════

"""
PROBLEM: Return True if any value appears at least twice in array.
Example: [1,2,3,1] → True

PATTERN: Set
TIME: Must code in < 30 seconds
"""

# ONE-LINER - What interviewer wants
def contains_duplicate(nums):
    return len(nums) != len(set(nums))

# ALTERNATIVE - Explicit approach
def contains_duplicate_explicit(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

"""
COMMON MISTAKES:
❌ Uses nested loops O(n²)
❌ Sorts array O(n log n) when O(n) possible
❌ Takes > 1 minute to code

REJECTION SIGNAL:
If candidate can't code this in 1 minute, serious concern about fundamentals.
"""


# ═══════════════════════════════════════════════════════════════════════
# PROBLEM 4: VALID PARENTHESES
# ═══════════════════════════════════════════════════════════════════════

"""
PROBLEM: Given string of brackets, determine if valid (properly opened/closed).
Example: "()[]{}" → True, "([)]" → False

PATTERN: Stack
TIME: 3-4 minutes
"""

def is_valid_parentheses(s):
    """
    THINK-ALOUD:
    "This is classic stack problem. For each open bracket, push to stack. For close
    bracket, pop and check if it matches. Stack empty at end means valid."
    """
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in s:
        if char in pairs:  # Opening bracket
            stack.append(char)
        else:  # Closing bracket
            if not stack or pairs[stack[-1]] != char:
                return False
            stack.pop()
    
    return len(stack) == 0

"""
COMMON MISTAKES:
❌ Doesn't check if stack empty before pop
❌ Forgets to check stack empty at end
❌ Overcomplicated logic with multiple if-elses

INTERVIEWER EXPECTS:
✓ Immediately identifies stack pattern
✓ Clean implementation with bracket mapping
✓ Handles edge cases
"""


# ═══════════════════════════════════════════════════════════════════════
# PROBLEM 5: MAXIMUM SUBARRAY SUM (Kadane's Algorithm)
# ═══════════════════════════════════════════════════════════════════════

"""
PROBLEM: Find contiguous subarray with largest sum.
Example: [-2,1,-3,4,-1,2,1,-5,4] → 6 (subarray [4,-1,2,1])

PATTERN: Dynamic Programming
TIME: 5-7 minutes
"""

def max_subarray(nums):
    """
    Kadane's Algorithm
    
    THINK-ALOUD:
    "I'll track current sum and max sum. At each element, decide: extend current
    subarray or start new one. If current sum negative, starting fresh is better."
    """
    max_sum = current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

"""
BRUTE FORCE: O(n²) - check all subarrays
OPTIMAL: O(n) - Kadane's algorithm

COMMON MISTAKES:
❌ Forgets to handle all negative array
❌ Doesn't explain why greedy works here
❌ Overcomplicated with unnecessary variables
"""


# ═══════════════════════════════════════════════════════════════════════
# PROBLEM 6: MERGE INTERVALS
# ═══════════════════════════════════════════════════════════════════════

"""
PROBLEM: Given intervals, merge overlapping ones.
Example: [[1,3],[2,6],[8,10],[15,18]] → [[1,6],[8,10],[15,18]]

PATTERN: Sort + Merge
TIME: 7-10 minutes
"""

def merge_intervals(intervals):
    """
    THINK-ALOUD:
    "First sort by start time. Then iterate, checking if current overlaps with
    previous. If yes, extend previous end. If no, add new interval."
    """
    if not intervals:
        return []
    
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        
        if current[0] <= last[1]:  # Overlap
            last[1] = max(last[1], current[1])  # Extend
        else:
            merged.append(current)  # No overlap
    
    return merged

"""
COMMON MISTAKES:
❌ Doesn't sort first
❌ Modifies original intervals without copying
❌ Doesn't handle edge case: empty input
❌ Wrong overlap condition (< instead of <=)

INTERVIEWER EXPECTS:
✓ Immediately suggests sorting
✓ Clear overlap logic
✓ Handles edge cases
"""


# ═══════════════════════════════════════════════════════════════════════
# PROBLEM 7: LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS
# ═══════════════════════════════════════════════════════════════════════

"""
PROBLEM: Find length of longest substring with all unique characters.
Example: "abcabcbb" → 3 ("abc")

PATTERN: Sliding Window + Set
TIME: 8-10 minutes
"""

def length_longest_substring(s):
    """
    THINK-ALOUD:
    "Sliding window with set to track unique chars. Expand right, shrink left when
    duplicate found. Track max length throughout."
    """
    char_set = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        # Shrink window until no duplicate
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len

"""
OPTIMIZATION: Use dict to store last seen index, jump left pointer directly
COMMON MISTAKES:
❌ Forgets to update max_len inside loop
❌ Doesn't handle empty string
❌ Uses list instead of set (O(n) check vs O(1))
"""


# ═══════════════════════════════════════════════════════════════════════
# PROBLEM 8: 3SUM
# ═══════════════════════════════════════════════════════════════════════

"""
PROBLEM: Find all unique triplets that sum to zero.
Example: [-1,0,1,2,-1,-4] → [[-1,-1,2],[-1,0,1]]

PATTERN: Sort + Two Pointers
TIME: 10-15 minutes
DIFFICULTY: Medium-Hard
"""

def three_sum(nums):
    """
    THINK-ALOUD:
    "Sort array first. Fix first element, use two pointers for remaining two.
    Skip duplicates to ensure unique triplets. O(n²) - best possible for this problem."
    """
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 2):
        # Skip duplicates for first element
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left, right = i + 1, n - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for second element
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                # Skip duplicates for third element
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return result

"""
COMMON MISTAKES:
❌ Doesn't sort array first
❌ Forgets to skip duplicates
❌ Off-by-one errors in duplicate skipping
❌ Uses set() to remove duplicates (inefficient)

STRONG CANDIDATES:
✓ Reduces 3Sum to 2Sum with fixed first element
✓ Handles duplicates cleanly
✓ Explains why sorting is necessary
"""


# ═══════════════════════════════════════════════════════════════════════
# PROBLEM 9: PRODUCT OF ARRAY EXCEPT SELF
# ═══════════════════════════════════════════════════════════════════════

"""
PROBLEM: Return array where output[i] = product of all elements except nums[i].
Cannot use division. Must be O(n).
Example: [1,2,3,4] → [24,12,8,6]

PATTERN: Prefix/Suffix Product
TIME: 10 minutes
"""

def product_except_self(nums):
    """
    THINK-ALOUD:
    "Calculate prefix products going left-to-right, then suffix products right-to-left.
    Result at each position is prefix * suffix. This avoids division and is O(n)."
    """
    n = len(nums)
    result = [1] * n
    
    # Calculate prefix products
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    
    # Calculate suffix products and multiply
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    
    return result

"""
BRUTE FORCE: O(n²) - for each position, multiply all others
CLEVER BUT WRONG: Use total product and divide (fails with zeros)
OPTIMAL: O(n) with prefix/suffix arrays

INTERVIEWER TESTS:
"What if array contains zeros?" (Common follow-up)
"Can you do it in O(1) extra space?" (Result array doesn't count)
"""


# ═══════════════════════════════════════════════════════════════════════
# PROBLEM 10: VALID PALINDROME
# ═══════════════════════════════════════════════════════════════════════

"""
PROBLEM: Check if string is palindrome, considering only alphanumeric, case-insensitive.
Example: "A man, a plan, a canal: Panama" → True

PATTERN: Two Pointers
TIME: 5 minutes
"""

def is_palindrome(s):
    """Two pointers from ends, skip non-alphanumeric"""
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

"""
ALTERNATIVE: Filter and compare
def is_palindrome_pythonic(s):
    filtered = ''.join(c.lower() for c in s if c.isalnum())
    return filtered == filtered[::-1]

INTERVIEWER PREFERS: Two pointers (O(1) space vs O(n))
"""


# ═══════════════════════════════════════════════════════════════════════
# MOCK INTERVIEW SESSION: 45 MINUTES
# ═══════════════════════════════════════════════════════════════════════

"""
INTERVIEWER: "We'll do 3 problems in 45 minutes. Code and explain your approach."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ROUND 1: WARM-UP (10 minutes)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PROBLEM: "Remove duplicates from sorted array in-place. Return new length."

STRONG CANDIDATE:
[Immediately identifies two pointers pattern]
"This is in-place modification with sorted array - two pointers pattern. Slow pointer
tracks write position, fast scans for unique elements."
[Codes in 3 minutes]

WEAK CANDIDATE:
"Can I use a set?"
INTERVIEWER: "In-place means O(1) extra space."
[Struggles for 8 minutes]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ROUND 2: MAIN PROBLEM (25 minutes)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PROBLEM: "Find all anagram groups in list of strings."

STRONG CANDIDATE:
"Anagrams have same sorted characters. I'll use dict with sorted string as key,
group words with same signature. O(n * k log k) where k is max word length."
[Codes with defaultdict, clean solution]

INTERVIEWER PRESSURE TESTS:
"What if strings are very long?" 
→ "Could use character count tuple instead of sorting, O(n*k) vs O(n*k log k)"

"What's space complexity?"
→ "O(n*k) for storing all words in groups"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ROUND 3: OPTIMIZATION CHALLENGE (10 minutes)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEWER: "Find if array contains duplicates within k distance."
Example: nums = [1,2,3,1], k = 3 → True (indices 0 and 3, distance = 3)

STRONG CANDIDATE:
"Sliding window with set. Maintain window of size k, check if current in set."
[Codes in 7 minutes]

def contains_nearby_duplicate(nums, k):
    window = set()
    for i, num in enumerate(nums):
        if num in window:
            return True
        window.add(num)
        if len(window) > k:
            window.remove(nums[i - k])
    return False

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FINAL EVALUATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STRONG HIRE:
✓ Solved all 3 problems
✓ Optimal solutions
✓ Clean code
✓ Good communication
✓ Handled follow-ups

HIRE:
✓ Solved 2/3 optimally
✓ Got 3rd with hints
✓ Decent code quality
✓ Some communication gaps

NO HIRE:
✗ Solved < 2 problems
✗ Multiple bugs
✗ Poor complexity
✗ Silent coding
"""


# ═══════════════════════════════════════════════════════════════════════
# SELF-ASSESSMENT CHECKLIST
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAN YOU CODE THESE WITHOUT LOOKING? (Time limits strict)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TIER 1: MUST CODE IN TIME LIMIT (8/8 required)
□ Two Sum (3 min)
□ Valid Anagram (2 min)
□ Contains Duplicate (1 min)
□ Valid Parentheses (4 min)
□ Maximum Subarray (5 min)
□ Merge Intervals (10 min)
□ Longest Substring (10 min)
□ Valid Palindrome (5 min)

TIER 2: SHOULD CODE (5/7)
□ 3Sum (15 min)
□ Product Except Self (10 min)
□ Group Anagrams (7 min)
□ Move Zeroes (5 min)
□ Find All Duplicates (10 min)
□ Top K Frequent (7 min)
□ Container With Most Water (7 min)

SCORING:
──────────
< 8/8 TIER 1: NOT READY
  → Cannot code fundamentals fast enough

8/8 TIER 1, < 5/7 TIER 2: BORDERLINE
  → Knows basics, needs practice on medium problems

8/8 TIER 1, >= 5/7 TIER 2: READY
  → Can handle most interview problems

CRITICAL REALITY CHECK:
If you can't code Two Sum in 3 minutes WITHOUT LOOKING, you are NOT ready.
This is the absolute minimum bar for 5+ YOE positions.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FINAL PREPARATION CHECKLIST:
────────────────────────────

Before your interview:
□ Can code all TIER 1 problems from memory
□ Can explain pattern for each problem
□ Can state time/space complexity without thinking
□ Have practiced think-aloud narration
□ Can handle "optimize this" follow-ups
□ Know when to use which data structure
□ Can spot patterns in < 30 seconds

If ANY box unchecked → Study more

Your interview performance will directly correlate with how many problems you can
code from memory under time pressure. There is no substitute for practice.

Good luck.
"""
