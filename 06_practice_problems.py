"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 PYTHON INTERVIEW PRACTICE PROBLEMS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
For 5+ YOE Developer | Real Interview Questions | Complete Solutions
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Each problem includes:
✓ Problem statement
✓ Think-aloud interview narration
✓ Multiple solutions (brute force → optimized)
✓ Time & space complexity
✓ Common mistakes
✓ Follow-up questions

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

# ═══════════════════════════════════════════════════════════════════════
# WARM-UP PROBLEMS (5-10 minutes each)
# ═══════════════════════════════════════════════════════════════════════

print("🔥 WARM-UP PROBLEMS\n" + "="*70)

# ────────────────────────────────────────────────────────────────────────
# WARM-UP 1: REVERSE STRING
# ────────────────────────────────────────────────────────────────────────

print("\n📌 PROBLEM 1: Reverse String")
print("-" * 70)
print("Write a function to reverse a string in-place (as a list of chars).")

def reverse_string_v1(s):
    """
    🎤 INTERVIEWER NARRATION:
    "I'll use Python's slicing with [::-1]. This creates a new list,
    which technically violates 'in-place', but it's the Pythonic way.
    For true in-place, I'll use two pointers."
    
    Time: O(n), Space: O(n) [new list created]
    """
    s[:] = s[::-1]  # s[:] modifies in-place

def reverse_string_v2(s):
    """
    🎤 INTERVIEWER NARRATION:
    "For true in-place, I'll use two pointers. Left starts at 0, right
    at the end. Swap elements and move pointers inward until they meet."
    
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        s[left], s[right] = s[right], s[left]  # Pythonic swap!
        left += 1
        right -= 1

# Test
s = list("hello")
reverse_string_v2(s)
print(f"✅ Result: {''.join(s)}")  # "olleh"


# ────────────────────────────────────────────────────────────────────────
# WARM-UP 2: VALID ANAGRAM
# ────────────────────────────────────────────────────────────────────────

print("\n📌 PROBLEM 2: Valid Anagram")
print("-" * 70)
print("Given two strings s and t, return true if t is an anagram of s.")

def is_anagram_v1(s, t):
    """
    🎤 INTERVIEWER NARRATION:
    "First approach: sort both strings. If they're anagrams, sorted
    versions will be identical. This is O(n log n) due to sorting."
    
    Time: O(n log n), Space: O(1) [ignoring space for sorting]
    """
    return sorted(s) == sorted(t)

def is_anagram_v2(s, t):
    """
    🎤 INTERVIEWER NARRATION:
    "Better approach: use Counter to count character frequencies.
    If counts match, they're anagrams. This is O(n) time."
    
    Time: O(n), Space: O(1) [at most 26 letters]
    """
    from collections import Counter
    return Counter(s) == Counter(t)

def is_anagram_v3(s, t):
    """
    🎤 INTERVIEWER NARRATION:
    "Manual frequency map using dict. Same complexity as Counter,
    but shows I can implement it without imports."
    
    Time: O(n), Space: O(1)
    """
    if len(s) != len(t):
        return False
    
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    
    for char in t:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False
    
    return True

# Test
print(f"✅ is_anagram('anagram', 'nagaram') = {is_anagram_v2('anagram', 'nagaram')}")
print(f"✅ is_anagram('rat', 'car') = {is_anagram_v2('rat', 'car')}")


# ────────────────────────────────────────────────────────────────────────
# WARM-UP 3: CONTAINS DUPLICATE
# ────────────────────────────────────────────────────────────────────────

print("\n📌 PROBLEM 3: Contains Duplicate")
print("-" * 70)
print("Return true if any value appears at least twice in the array.")

def contains_duplicate_v1(nums):
    """
    🎤 INTERVIEWER NARRATION:
    "Simplest approach: convert to set. If lengths differ, there's a duplicate.
    This is O(n) time and very Pythonic."
    
    Time: O(n), Space: O(n)
    """
    return len(nums) != len(set(nums))

def contains_duplicate_v2(nums):
    """
    🎤 INTERVIEWER NARRATION:
    "Alternative: scan through once, adding to set. If we see a number
    already in the set, return True immediately. Same complexity but
    can short-circuit earlier."
    
    Time: O(n), Space: O(n)
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Test
print(f"✅ contains_duplicate([1,2,3,1]) = {contains_duplicate_v1([1,2,3,1])}")
print(f"✅ contains_duplicate([1,2,3,4]) = {contains_duplicate_v1([1,2,3,4])}")


# ═══════════════════════════════════════════════════════════════════════
# MEDIUM PROBLEMS (15-25 minutes each)
# ═══════════════════════════════════════════════════════════════════════

print("\n\n🔥 MEDIUM PROBLEMS\n" + "="*70)

# ────────────────────────────────────────────────────────────────────────
# MEDIUM 1: TWO SUM
# ────────────────────────────────────────────────────────────────────────

print("\n📌 PROBLEM 4: Two Sum")
print("-" * 70)
print("Given array of integers, return indices of two numbers that add to target.")

def two_sum_brute(nums, target):
    """
    🎤 INTERVIEWER NARRATION:
    "Brute force: try all pairs. This works but is O(n²)."
    
    Time: O(n²), Space: O(1)
    
    ❌ INTERVIEW FAIL: Interviewer will ask for better solution!
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None

def two_sum_optimized(nums, target):
    """
    🎤 INTERVIEWER NARRATION:
    "Optimized: use a hash map. For each number, I check if (target - num)
    exists in the map. If yes, we found the pair. If no, add current number
    to the map with its index. This reduces time to O(n) with O(n) space."
    
    Time: O(n), Space: O(n)
    
    ✅ This is what interviewers expect!
    """
    seen = {}  # value -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return None

# Test
nums = [2, 7, 11, 15]
target = 9
print(f"✅ two_sum({nums}, {target}) = {two_sum_optimized(nums, target)}")

print("\n📝 FOLLOW-UP QUESTIONS:")
print("  Q: What if array is sorted?")
print("  A: Use two pointers (left=0, right=n-1), O(n) time, O(1) space")
print("  Q: What if there are multiple pairs?")
print("  A: Store all pairs in a list instead of returning first")
print("  Q: What if we need to return values, not indices?")
print("  A: Return [nums[i], nums[j]] instead of [i, j]")


# ────────────────────────────────────────────────────────────────────────
# MEDIUM 2: GROUP ANAGRAMS
# ────────────────────────────────────────────────────────────────────────

print("\n📌 PROBLEM 5: Group Anagrams")
print("-" * 70)
print("Given array of strings, group anagrams together.")

def group_anagrams(strs):
    """
    🎤 INTERVIEWER NARRATION:
    "I'll use a dictionary where the key is a sorted tuple of characters.
    All anagrams will hash to the same key. I'll use defaultdict(list)
    to avoid checking if key exists."
    
    Time: O(n * k log k) where n=number of strings, k=max length
    Space: O(n * k)
    """
    from collections import defaultdict
    
    groups = defaultdict(list)
    
    for word in strs:
        # Sorted tuple as key (immutable, hashable)
        key = tuple(sorted(word))
        groups[key].append(word)
    
    return list(groups.values())

# Test
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(strs)
print(f"✅ group_anagrams: {result}")

print("\n📝 FOLLOW-UP QUESTIONS:")
print("  Q: Can you do better than O(n * k log k)?")
print("  A: Yes! Use character count as key instead of sorting.")
print("     Build key as tuple of counts: (count_a, count_b, ..., count_z)")
print("     This makes it O(n * k) time.")


# ────────────────────────────────────────────────────────────────────────
# MEDIUM 3: LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS
# ────────────────────────────────────────────────────────────────────────

print("\n📌 PROBLEM 6: Longest Substring Without Repeating Characters")
print("-" * 70)
print("Find length of longest substring without repeating characters.")

def length_of_longest_substring_brute(s):
    """
    🎤 INTERVIEWER NARRATION:
    "Brute force: check all substrings. For each starting position,
    extend as far as possible without duplicates."
    
    Time: O(n³), Space: O(min(n, m)) where m = charset size
    
    ❌ Too slow for interview!
    """
    max_len = 0
    n = len(s)
    
    for i in range(n):
        seen = set()
        for j in range(i, n):
            if s[j] in seen:
                break
            seen.add(s[j])
            max_len = max(max_len, j - i + 1)
    
    return max_len

def length_of_longest_substring_optimized(s):
    """
    🎤 INTERVIEWER NARRATION:
    "Optimized: sliding window with a set. I maintain a window [left, right]
    with no duplicates. When I find a duplicate, I shrink from the left
    until it's removed. This ensures each character is visited at most
    twice (once by right, once by left), giving O(n) time."
    
    Time: O(n), Space: O(min(n, m)) where m = charset size
    
    ✅ This is the optimal solution!
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

def length_of_longest_substring_v3(s):
    """
    🎤 INTERVIEWER NARRATION:
    "Even better: use dict to store last seen index. When we find a
    duplicate, we can jump left pointer directly to (last_seen + 1)
    instead of incrementing one by one."
    
    Time: O(n), Space: O(min(n, m))
    """
    char_index = {}
    left = 0
    max_len = 0
    
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            # Jump left pointer past the duplicate
            left = char_index[char] + 1
        
        char_index[char] = right
        max_len = max(max_len, right - left + 1)
    
    return max_len

# Test
s = "abcabcbb"
print(f"✅ longest_substring('{s}') = {length_of_longest_substring_optimized(s)}")

s = "pwwkew"
print(f"✅ longest_substring('{s}') = {length_of_longest_substring_optimized(s)}")


# ────────────────────────────────────────────────────────────────────────
# MEDIUM 4: VALID PARENTHESES
# ────────────────────────────────────────────────────────────────────────

print("\n📌 PROBLEM 7: Valid Parentheses")
print("-" * 70)
print("Given string with '()[]{}', determine if brackets are valid.")

def is_valid_parentheses(s):
    """
    🎤 INTERVIEWER NARRATION:
    "Classic stack problem. For opening brackets, push to stack. For
    closing brackets, check if top of stack matches. At the end, stack
    should be empty. I'll use a dict to map closing to opening brackets."
    
    Time: O(n), Space: O(n)
    """
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in pairs:  # Closing bracket
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
        else:  # Opening bracket
            stack.append(char)
    
    return len(stack) == 0

# Test
print(f"✅ is_valid('()[]{{}}') = {is_valid_parentheses('()[]{}')}")
print(f"✅ is_valid('([)]') = {is_valid_parentheses('([)]')}")
print(f"✅ is_valid('{{[]}}') = {is_valid_parentheses('{[]}')}")


# ────────────────────────────────────────────────────────────────────────
# MEDIUM 5: PRODUCT OF ARRAY EXCEPT SELF
# ────────────────────────────────────────────────────────────────────────

print("\n📌 PROBLEM 8: Product of Array Except Self")
print("-" * 70)
print("Return array where output[i] = product of all elements except nums[i].")
print("Constraint: O(n) time without division!")

def product_except_self_brute(nums):
    """
    🎤 INTERVIEWER NARRATION:
    "Brute force: for each position, multiply all other elements.
    This is O(n²), won't pass interview."
    
    Time: O(n²), Space: O(1) [excluding output]
    
    ❌ Too slow!
    """
    n = len(nums)
    result = []
    
    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= nums[j]
        result.append(product)
    
    return result

def product_except_self_optimized(nums):
    """
    🎤 INTERVIEWER NARRATION:
    "Key insight: result[i] = (product of all elements to left of i) *
    (product of all elements to right of i). I'll use two passes:
    first pass computes left products, second pass computes right products
    and multiplies them in. This achieves O(n) time, O(1) extra space."
    
    Time: O(n), Space: O(1) [output array doesn't count]
    
    ✅ This is the optimal solution!
    """
    n = len(nums)
    result = [1] * n
    
    # First pass: compute left products
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]
    
    # Second pass: multiply by right products
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    
    return result

# Test
nums = [1, 2, 3, 4]
print(f"✅ product_except_self({nums}) = {product_except_self_optimized(nums)}")
# Expected: [24, 12, 8, 6]

print("\n📝 KEY INSIGHT:")
print("  For [1,2,3,4]:")
print("  result[0] = 1*2*3*4 = (1) * (2*3*4)")
print("  result[1] = 1*3*4   = (1) * (3*4)")
print("  result[2] = 1*2*4   = (1*2) * (4)")
print("  result[3] = 1*2*3   = (1*2*3) * (1)")
print("  Left products: [1, 1, 2, 6]")
print("  Right products: [24, 12, 4, 1]")


# ────────────────────────────────────────────────────────────────────────
# MEDIUM 6: MAXIMUM SUBARRAY (Kadane's Algorithm)
# ────────────────────────────────────────────────────────────────────────

print("\n📌 PROBLEM 9: Maximum Subarray")
print("-" * 70)
print("Find contiguous subarray with largest sum.")

def max_subarray_brute(nums):
    """
    🎤 INTERVIEWER NARRATION:
    "Brute force: try all possible subarrays. For each start position,
    try all end positions and track maximum sum."
    
    Time: O(n²), Space: O(1)
    
    ❌ Too slow!
    """
    max_sum = float('-inf')
    
    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum)
    
    return max_sum

def max_subarray_kadane(nums):
    """
    🎤 INTERVIEWER NARRATION:
    "This is Kadane's algorithm, a classic DP solution. Key insight:
    at each position, we decide: should I extend the previous subarray
    or start a new one? If previous sum is negative, it's better to
    start fresh. This gives us O(n) time."
    
    Time: O(n), Space: O(1)
    
    ✅ This is the optimal solution!
    """
    max_sum = nums[0]
    current_sum = nums[0]
    
    for i in range(1, len(nums)):
        # Either extend previous subarray or start new one
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Test
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"✅ max_subarray({nums}) = {max_subarray_kadane(nums)}")
# Expected: 6 (subarray [4,-1,2,1])

print("\n📝 FOLLOW-UP: Return the subarray itself")

def max_subarray_with_indices(nums):
    """Return max sum and the subarray"""
    max_sum = nums[0]
    current_sum = nums[0]
    start = 0
    end = 0
    temp_start = 0
    
    for i in range(1, len(nums)):
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            temp_start = i
        else:
            current_sum = current_sum + nums[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    
    return max_sum, nums[start:end+1]

max_sum, subarray = max_subarray_with_indices(nums)
print(f"✅ Max sum: {max_sum}, Subarray: {subarray}")


# ═══════════════════════════════════════════════════════════════════════
# EDGE CASE TRAPS (Common Interview Gotchas)
# ═══════════════════════════════════════════════════════════════════════

print("\n\n🔥 EDGE CASE TRAPS\n" + "="*70)

print("\n📌 TRAP 1: Empty Input")
print("-" * 70)

def safe_max(nums):
    """Always check for empty input!"""
    if not nums:  # ✅ Check first!
        return None
    return max(nums)

print(f"✅ safe_max([]) = {safe_max([])}")


print("\n📌 TRAP 2: Single Element")
print("-" * 70)

def longest_palindrome(s):
    """Single character is always a palindrome"""
    if len(s) <= 1:  # ✅ Edge case
        return s
    # ... rest of logic


print("\n📌 TRAP 3: Negative Numbers")
print("-" * 70)

def product_array(nums):
    """Be careful with negatives in product problems"""
    # Track both min and max (negatives flip signs!)
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] < 0:
            # Swap max and min when multiplying by negative
            max_product, min_product = min_product, max_product
        
        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])
        result = max(result, max_product)
    
    return result


print("\n📌 TRAP 4: Integer Overflow")
print("-" * 70)
print("Python: No integer overflow! 🎉")
print("But mention you're aware of it for Java/C++")


print("\n📌 TRAP 5: Sorting Modifies Original")
print("-" * 70)

def process_array(nums):
    # ❌ BAD: Modifies original
    nums.sort()
    
    # ✅ GOOD: Work with sorted copy
    sorted_nums = sorted(nums)


# ═══════════════════════════════════════════════════════════════════════
# COMPLEXITY ANALYSIS GUIDE
# ═══════════════════════════════════════════════════════════════════════

complexity_guide = """
╔═══════════════════════════════════════════════════════════════════════╗
║              TIME COMPLEXITY - INTERVIEW CHEAT SHEET                  ║
╠═══════════════════════════╦═══════════════════════════════════════════╣
║ COMPLEXITY                ║ OPERATIONS                                ║
╠═══════════════════════════╬═══════════════════════════════════════════╣
║ O(1)                      ║ Array access, dict lookup, math ops       ║
║ O(log n)                  ║ Binary search, balanced tree ops          ║
║ O(n)                      ║ Single loop through n elements            ║
║ O(n log n)                ║ Sorting, merge sort, heap operations      ║
║ O(n²)                     ║ Nested loops over n elements              ║
║ O(2^n)                    ║ Recursive subsets, backtracking           ║
║ O(n!)                     ║ Permutations                              ║
╚═══════════════════════════╩═══════════════════════════════════════════╝

🎤 HOW TO EXPLAIN COMPLEXITY IN INTERVIEWS:

"This solution runs in O(n) time because we make a single pass through
the array. The space complexity is O(n) for the hash map, which in the
worst case stores all n elements."

ALWAYS MENTION:
  1. Time complexity
  2. Space complexity (excluding output)
  3. Worst-case scenario
  4. Any trade-offs made
"""
print(complexity_guide)


# ═══════════════════════════════════════════════════════════════════════
# FINAL TIPS
# ═══════════════════════════════════════════════════════════════════════

tips = """
╔═══════════════════════════════════════════════════════════════════════╗
║                   🏆 INTERVIEW SUCCESS CHECKLIST                      ║
╚═══════════════════════════════════════════════════════════════════════╝

BEFORE CODING:
  ✅ Repeat problem back to interviewer
  ✅ Ask clarifying questions (input size? edge cases? constraints?)
  ✅ Discuss brute force approach first
  ✅ Explain optimization before coding
  ✅ Agree on approach with interviewer

WHILE CODING:
  ✅ Think aloud - narrate your thought process
  ✅ Start with function signature
  ✅ Write clean, readable code
  ✅ Use descriptive variable names
  ✅ Handle edge cases (empty input, single element, etc.)

AFTER CODING:
  ✅ Walk through with example
  ✅ Test with edge cases
  ✅ State time & space complexity
  ✅ Discuss trade-offs
  ✅ Mention possible optimizations

PYTHONIC PRACTICES:
  ✅ Use list comprehensions when clear
  ✅ Prefer enumerate() over range(len())
  ✅ Use get() for dicts with defaults
  ✅ Use 'in' for membership testing
  ✅ Use tuple unpacking for swaps: a, b = b, a

RED FLAGS (AVOID THESE!):
  ❌ Starting to code immediately without discussion
  ❌ Silent coding - talk through your process!
  ❌ Not testing your solution
  ❌ Ignoring hints from interviewer
  ❌ Using confusing variable names (i, j, k without context)
  ❌ Not handling edge cases
  ❌ Writing unnecessarily complex code
"""
print(tips)

print("\n" + "="*70)
print("✅ PRACTICE PROBLEMS COMPLETE!")
print("💡 Run this file to see all solutions in action!")
print("🚀 Now you're ready for real interviews!")
print("="*70)

