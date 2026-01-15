"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 EASY LIVE CODING CHALLENGES - REAL INTERVIEW SIMULATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Interviewer: Senior Engineer | Hiring Bar-Raiser
Target: 3-7 YOE | Python Engineers
Time: 10-15 minutes per problem
Focus: Correctness, Edge Cases, Clear Communication
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEW RULES:
────────────────
• Think aloud - silence is a red flag
• Ask clarifying questions FIRST
• Start with brute force if needed
• Test with examples as you code
• Handle edge cases explicitly
• Write clean, readable code

ELIMINATION TRIGGERS:
─────────────────────
• Silent coding (no communication) → REJECT
• Doesn't ask about edge cases → REJECT
• Jumps to code without examples → REJECT
• Cannot explain their own code → REJECT
"""

# ═══════════════════════════════════════════════════════════════════════
# PROBLEM 1: TWO SUM
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1️⃣ PROBLEM STATEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Given an array of integers and a target sum, return the indices of two numbers
that add up to the target.

Example:
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]
    Explanation: nums[0] + nums[1] = 2 + 7 = 9

Constraints:
- Each input has exactly one solution
- You may not use the same element twice
- Return indices, not values
- Array is not sorted

Ambiguities to clarify:
- Can there be negative numbers? (YES)
- Can there be duplicates? (YES)
- Should I return first pair or any pair? (ANY)
- What if no solution exists? (Won't happen per problem statement)
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2️⃣ INTERVIEW THINK-ALOUD FLOW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STRONG CANDIDATE SAYS:

"Let me make sure I understand. I need to find two numbers that sum to target,
and return their indices. The array isn't sorted, and there's exactly one solution.

Let me think through approaches:

BRUTE FORCE: Check every pair - nested loops. O(n²) time, O(1) space.
For each number, check if target - num exists later in array.

OPTIMIZED: Use a hash map. As I iterate, store numbers I've seen.
For each num, check if (target - num) is in my hash map.
O(n) time, O(n) space.

Let me trace through an example:
nums = [2, 7, 11, 15], target = 9
- i=0, num=2, need 7, seen={}, add 2 → seen={2:0}
- i=1, num=7, need 2, 2 in seen! Return [0, 1]

Edge cases to consider:
- Negative numbers: [-1, -2, -3], target = -5 → should work
- Duplicates: [3, 3], target = 6 → need to handle not using same index
- Zero: [0, 4, 3], target = 4 → should work

I'll implement the hash map solution."
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3️⃣ INTENTIONAL TRAP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TRAP: Using the same element twice

Example: nums = [3, 2, 4], target = 6
WRONG APPROACH:
    for i in range(len(nums)):
        if nums[i] + nums[i] == target:  # ❌ Using nums[i] twice!
            return [i, i]

WHY CANDIDATES FALL FOR IT:
They check if "num * 2 == target" without considering it's the same index.

Example that breaks:
nums = [3, 3], target = 6  # Two different 3's - VALID
nums = [3], target = 6     # One 3 - INVALID

HOW TO DETECT:
When checking hash map, ensure we're not looking at the current index.
Store indices in hash map, check i != seen[complement]

CORRECT CHECK:
    complement = target - nums[i]
    if complement in seen and seen[complement] != i:
        return [seen[complement], i]

But actually, if we check BEFORE adding current, we naturally avoid this!
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4️⃣ SOLUTION (INTERVIEW-ACCEPTABLE)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def two_sum(nums, target):
    """
    Find two numbers that sum to target, return their indices.
    
    Approach: Hash map to store seen numbers and their indices.
    As we iterate, check if complement exists in our map.
    
    Time: O(n) - single pass through array
    Space: O(n) - hash map stores up to n elements
    
    Args:
        nums: List of integers
        target: Target sum
    
    Returns:
        List of two indices [i, j] where nums[i] + nums[j] = target
    """
    # Store seen numbers: {number: index}
    seen = {}
    
    for i, num in enumerate(nums):
        # Calculate what number we need to reach target
        complement = target - num
        
        # Check if we've seen the complement before
        if complement in seen:
            # Found it! Return the pair
            return [seen[complement], i]
        
        # Haven't found pair yet, store current number
        seen[num] = i
    
    # Per problem statement, solution always exists
    # But defensive programming:
    return []


"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5️⃣ COMMON BUT BAD SOLUTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def two_sum_brute_force(nums, target):
    """
    ❌ BRUTE FORCE - Works but signals junior-level thinking
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

"""
WHY INTERVIEWERS DISLIKE IT:
─────────────────────────────
1. O(n²) time complexity - doesn't scale
2. Shows no optimization thinking
3. For easy problem, expected to recognize hash map pattern
4. Signals: "I can write loops but not optimize"

WHAT IT SIGNALS:
Candidate either:
- Doesn't know hash map pattern (fundamental gap)
- Knows it but defaults to brute force (not senior-level)
- Doesn't think about performance (red flag)

WHEN IT'S ACCEPTABLE:
If candidate says:
"I'll start with brute force to ensure correctness, then optimize."
and actually optimizes → Shows good process.

But staying with brute force → WEAK HIRE or REJECT
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
6️⃣ EXPLANATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHY THIS WORKS:
───────────────
The key insight: if nums[i] + nums[j] = target, then nums[j] = target - nums[i].

Instead of checking all pairs, we store numbers as we see them.
For each new number, we check if its "complement" (target - num) was seen before.

Example walkthrough:
nums = [2, 7, 11, 15], target = 9

Step 1: i=0, num=2
  - complement = 9 - 2 = 7
  - 7 not in seen {}
  - Add 2: seen = {2: 0}

Step 2: i=1, num=7
  - complement = 9 - 7 = 2
  - 2 IS in seen!
  - Return [seen[2], i] = [0, 1] ✓

KEY PYTHON CONCEPTS:
────────────────────
- Dictionary for O(1) lookup
- enumerate() for index + value
- 'in' operator for dict membership test
- Early return when solution found

TRADE-OFFS:
───────────
- Space: O(n) for hash map vs O(1) for brute force
- But time improvement O(n) vs O(n²) is worth it
- Classic time-space tradeoff
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
7️⃣ TIME & SPACE COMPLEXITY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TIME: O(n)
- Single pass through array: n iterations
- Each dict lookup/insert: O(1) average
- Total: O(n)

SPACE: O(n)
- Hash map stores up to n elements in worst case
- Example: [1,2,3,4,5], target=100 → stores all 5 before realizing no solution
- Each entry: key (int) + value (int) → O(1) per entry

WHY IT'S ACCEPTABLE:
─────────────────────
- Linear time is optimal for this problem (must see each element)
- Linear space is reasonable trade-off for linear time
- Can't do better than O(n) time (must read all inputs)
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
8️⃣ IF TIME RUNS OUT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT PARTIAL PROGRESS EARNS POINTS:
────────────────────────────────────
✓ Correct problem understanding (asked clarifying questions)
✓ Identified brute force approach (shows problem-solving)
✓ Recognized need for optimization (shows awareness)
✓ Started implementing hash map (shows right direction)
✓ Handled one example correctly (shows testing mindset)

WHAT TO SAY:
────────────
"I'm running short on time, but let me outline the rest. I'd use a hash map
to store seen numbers, check for complements as I iterate. Would handle edge
cases like negatives and duplicates. Time O(n), space O(n)."

SHOWS: Understanding even without complete implementation.

WHAT NOT TO SAY:
────────────────
❌ "I'm stuck, I don't know" - Shows giving up
❌ "This is harder than I thought" - Complaining
❌ "Can I Google it?" - Not interview-appropriate
❌ Silence - Worst response

INSTEAD: Explain your thinking, show the approach, demonstrate understanding.
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
9️⃣ FOLLOW-UP QUESTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEWER: "What if the array is sorted?"

STRONG ANSWER:
"With sorted array, I could use two pointers instead of hash map.
Start with left=0, right=len-1. If sum < target, move left++.
If sum > target, move right--. Still O(n) time but O(1) space.

But since input isn't guaranteed sorted, hash map is more general."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEWER: "What if there could be multiple solutions?"

STRONG ANSWER:
"To return all pairs, I'd collect results instead of returning immediately.
Still use hash map but continue iterating. Time O(n), space O(n) + O(k)
where k is number of pairs."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEWER: "How would you test this?"

STRONG ANSWER:
"Test cases:
- Normal case: [2,7,11,15], target=9 → [0,1]
- Negatives: [-1,-2,-3,-4,-5], target=-8 → find pair
- Duplicates: [3,3], target=6 → [0,1]
- Single pair: [1,2], target=3 → [0,1]
- Large numbers: handle overflow? (Python int unlimited)
- Edge: [0,4,3,0], target=0 → [0,3]"
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔟 INTERVIEWER EVALUATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ HIRE SIGNALS:
────────────────
- Asked clarifying questions about duplicates, negatives
- Explained approach before coding
- Chose optimal O(n) solution
- Clean, readable code with comments
- Tested with examples
- Handled edge cases
- Explained time/space complexity correctly
- Communicated throughout

⚠️ BORDERLINE SIGNALS:
───────────────────────
- Jumped to code without examples
- Needed hints to optimize from brute force
- Code works but messy variable names
- Forgot to handle edge case until prompted
- Weak complexity analysis

❌ NO-HIRE SIGNALS:
───────────────────
- Silent coding (no communication)
- Stuck on brute force, couldn't optimize
- Code doesn't handle edge cases
- Can't explain their own code
- Doesn't test with examples
- Wrong complexity analysis
- Defensive/argumentative when given feedback

EXACT BEHAVIORS:
────────────────
HIRE: "Let me clarify...I'll use hash map...Time is O(n)...Testing with..."
BORDERLINE: Coded silently, needed prompting, got there eventually
NO-HIRE: "I'm not sure...I'll just try things...Why didn't this work?"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ═══════════════════════════════════════════════════════════════════════
# PROBLEM 2: VALID PALINDROME
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1️⃣ PROBLEM STATEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Given a string, determine if it's a valid palindrome, considering only
alphanumeric characters and ignoring case.

Example 1:
    Input: "A man, a plan, a canal: Panama"
    Output: True
    Explanation: "amanaplanacanalpanama" is palindrome

Example 2:
    Input: "race a car"
    Output: False
    Explanation: "raceacar" is not palindrome

Constraints:
- Empty string is considered palindrome
- Only consider alphanumeric (letters and numbers)
- Case-insensitive

Ambiguities to clarify:
- What about spaces? (IGNORE)
- What about special characters? (IGNORE)
- What about Unicode? (Assume ASCII)
- Empty string? (TRUE)
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2️⃣ INTERVIEW THINK-ALOUD FLOW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STRONG CANDIDATE:

"Let me understand: check if string is palindrome, but only alphanumeric matter,
case-insensitive. Spaces and punctuation ignored.

Approaches:
1. Clean string first: filter alphanumeric, lowercase, check if s == s[::-1]
2. Two pointers: left and right, skip non-alphanumeric, compare

Let me think about trade-offs:
- Approach 1: Simple, creates new string O(n) space
- Approach 2: In-place comparison, O(1) space

For interview, I'll use approach 2 (two pointers) to show space optimization.

Example trace:
'A man, a plan'
 ^           ^  (left=0, right=12)
- left='A', right='n' → skip non-alpha
- left='A', right='n' → compare 'a'=='n'? No! But wait...
- Actually need to move right to alphanumeric

Let me trace more carefully:
'A man'
 0123  indices
- left=0 'A', right=4 'n' (after skipping space)
- 'a' == 'n'? No, not palindrome

Wait, that's wrong example. Let me use:
'aba'
- left=0 'a', right=2 'a' → equal, move both
- left=1 'b', right=1 'b' → equal, done

Edge cases:
- Empty string: '' → True
- Single char: 'a' → True
- All spaces: '   ' → True (no alphanumeric)
- Mixed: 'a b a' → True"
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3️⃣ INTENTIONAL TRAP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TRAP: Forgetting to skip non-alphanumeric on BOTH sides

BAD CODE:
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
            continue  # ❌ Only skips left!
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1

WHAT BREAKS:
Input: "a."
- left=0 'a', right=1 '.'
- 'a' is alnum, doesn't skip
- Compares 'a' vs '.' → False (WRONG! Should be True)

CORRECT APPROACH:
Must skip non-alphanumeric on BOTH sides before comparing:
- Skip left forward while not alnum
- Skip right backward while not alnum
- Then compare

WHY CANDIDATES MISS IT:
They handle one side at a time, forget the other side also has special chars.
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4️⃣ SOLUTION (INTERVIEW-ACCEPTABLE)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def is_palindrome(s):
    """
    Check if string is valid palindrome (alphanumeric only, case-insensitive).
    
    Approach: Two pointers from both ends, skip non-alphanumeric, compare.
    
    Time: O(n) - single pass
    Space: O(1) - only pointers
    
    Args:
        s: Input string
    
    Returns:
        bool: True if palindrome, False otherwise
    """
    # Edge case: empty string is palindrome
    if not s:
        return True
    
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
        
        # Move pointers
        left += 1
        right -= 1
    
    return True


"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5️⃣ COMMON BUT BAD SOLUTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def is_palindrome_naive(s):
    """
    ❌ WORKS BUT NOT OPTIMAL
    """
    # Filter and clean
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    # Check palindrome
    return cleaned == cleaned[::-1]

"""
WHY INTERVIEWERS DISLIKE:
─────────────────────────
1. Creates intermediate string → O(n) space
2. Two passes: one to clean, one to reverse
3. String slicing [::-1] creates another copy
4. Doesn't show pointer technique understanding

WHEN IT'S ACCEPTABLE:
If candidate says "This is simpler but uses O(n) space. In production I'd
use this for readability unless memory is constrained." → Shows awareness

But if they don't mention space trade-off → BORDERLINE

WHAT IT SIGNALS:
- Knows Python string operations (good)
- Doesn't think about space complexity (bad)
- Takes easy path without optimization (borderline for senior)
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
6️⃣ EXPLANATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

KEY INSIGHT:
Palindrome reads same forwards and backwards. Use two pointers to compare
from both ends simultaneously.

ALGORITHM:
1. Start with left=0, right=len-1
2. Skip non-alphanumeric characters from both sides
3. Compare characters (case-insensitive)
4. If different → not palindrome
5. If same → move both pointers inward
6. If pointers meet/cross → palindrome

CRITICAL DETAILS:
- Must check left < right in BOTH skip loops (prevents out of bounds)
- lowercase() for case-insensitive comparison
- isalnum() checks if character is letter or digit
- Return True if we finish loop (all compared characters matched)

PYTHON CONCEPTS:
- Two-pointer technique
- str.isalnum() method
- str.lower() for case conversion
- while loops with compound conditions
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
7️⃣ TIME & SPACE COMPLEXITY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TIME: O(n)
- Single pass through string (pointers move toward each other)
- Each character visited at most once
- isalnum() and lower() are O(1)
- Total: O(n)

SPACE: O(1)
- Only two pointer variables
- No additional data structures
- In-place comparison

COMPARISON TO NAIVE:
Naive solution: O(n) time, O(n) space (creates new strings)
Optimal solution: O(n) time, O(1) space

WHY IT'S BETTER:
Space optimization matters for large inputs or memory-constrained systems.
Two-pointer is a fundamental technique seniors should know.
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
8️⃣ IF TIME RUNS OUT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT TO SAY IF NOT COMPLETE:
"I'm implementing two-pointer approach for O(1) space. I'd skip non-alphanumeric
from both sides, compare characters case-insensitively, and return False if any
mismatch. The key is handling the pointer logic correctly to avoid out-of-bounds."

PARTIAL CREDIT:
✓ Identified two-pointer approach
✓ Mentioned need to skip non-alphanumeric
✓ Mentioned case-insensitive comparison
✓ Showed understanding even without complete code

ALTERNATIVE:
"If pressed for time, I could use the simpler cleaned == cleaned[::-1] approach,
acknowledging it uses O(n) space but is more readable."
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
9️⃣ FOLLOW-UP QUESTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEWER: "What if we need to preserve the original string?"

ANSWER: "Current solution doesn't modify input, only reads. Already preserves it."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEWER: "How would you handle Unicode characters?"

ANSWER: "isalnum() works for Unicode. Python 3 strings are Unicode by default.
For ASCII-only, could add: if ord(c) < 128 check."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEWER: "What about performance with very long strings?"

ANSWER: "Two-pointer is optimal O(n). Can't do better since we must examine all
characters. For extremely long strings, could early exit on first mismatch."
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔟 INTERVIEWER EVALUATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ HIRE SIGNALS:
- Used two-pointer approach (space-optimal)
- Correctly handled skipping non-alphanumeric on BOTH sides
- Case-insensitive comparison
- Handled edge cases (empty string, all spaces)
- Clean, readable code
- Explained time/space complexity

⚠️ BORDERLINE:
- Used naive approach but acknowledged space trade-off
- Forgot to skip right pointer initially, fixed after testing
- Code works but variable names unclear

❌ NO-HIRE:
- Couldn't figure out how to skip special characters
- Only skipped from one side, not both
- Didn't handle case-insensitivity
- Confused about when to move pointers
- Silent coding with bugs

DECISION FACTORS:
- Two-pointer mastery separates senior from junior
- Edge case handling shows thoroughness
- Space optimization shows performance awareness
"""


# ═══════════════════════════════════════════════════════════════════════
# PROBLEM 3: MERGE TWO SORTED LISTS
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1️⃣ PROBLEM STATEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Merge two sorted lists into one sorted list.

Example:
    Input: list1 = [1, 3, 5], list2 = [2, 4, 6]
    Output: [1, 2, 3, 4, 5, 6]

Constraints:
- Both input lists are already sorted
- Return new list (don't modify inputs)
- Lists can have different lengths
- Elements are integers

Ambiguities:
- Can lists be empty? (YES - return other list)
- Can lists have duplicates? (YES - keep all)
- Should we modify inputs? (NO - return new list)
- What if both empty? (Return empty list)
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2️⃣ THINK-ALOUD FLOW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"This is a classic merge problem, similar to merge step in merge sort.

Approach:
Use two pointers, one for each list. Compare elements, take smaller,
advance that pointer. Continue until one list exhausted, then append rest.

Example:
list1 = [1, 3, 5]
list2 = [2, 4, 6]

i=0, j=0: 1 < 2 → take 1, i++, result=[1]
i=1, j=0: 3 > 2 → take 2, j++, result=[1,2]
i=1, j=1: 3 < 4 → take 3, i++, result=[1,2,3]
i=2, j=1: 5 > 4 → take 4, j++, result=[1,2,3,4]
i=2, j=2: 5 < 6 → take 5, i++, result=[1,2,3,4,5]
i=3: list1 done, append rest of list2 → result=[1,2,3,4,5,6]

Edge cases:
- One empty: return other list
- Both empty: return []
- Different lengths: handled by appending remainder
- All duplicates: [1,1] + [1,1] → [1,1,1,1]"
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3️⃣ TRAP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TRAP: Forgetting to append remaining elements

BAD CODE:
result = []
while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        result.append(list1[i])
        i += 1
    else:
        result.append(list2[j])
        j += 1
# ❌ FORGOT TO APPEND REST!
return result

WHAT BREAKS:
[1,3,5] + [2,4,6]
After loop: result = [1,2,3,4]
Missing: [5,6] because loop exited when j reached end

FIX:
After loop, append remaining:
result.extend(list1[i:])
result.extend(list2[j:])

One will be empty, one might have remaining elements.
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4️⃣ SOLUTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def merge_sorted_lists(list1, list2):
    """
    Merge two sorted lists into one sorted list.
    
    Time: O(n + m) where n, m are lengths
    Space: O(n + m) for result list
    """
    # Handle empty lists
    if not list1:
        return list2[:]  # Return copy
    if not list2:
        return list1[:]
    
    result = []
    i, j = 0, 0
    
    # Merge while both have elements
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    
    # Append remaining elements (one will be empty)
    result.extend(list1[i:])
    result.extend(list2[j:])
    
    return result


"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5️⃣ BAD SOLUTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def merge_bad(list1, list2):
    """❌ Works but destroys sorted property"""
    result = list1 + list2
    result.sort()
    return result

"""
WHY BAD:
- Doesn't use fact that inputs are sorted!
- O((n+m)log(n+m)) due to sort
- Could just be: "concatenate and sort" - doesn't show algorithm skills
- Interview asks to merge sorted lists, not "combine and sort"

SIGNALS: Doesn't understand or use the constraints given.
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REST OF SECTIONS (abbreviated for space - same structure as above)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

6️⃣ EXPLANATION: Two-pointer merge, leveraging sorted property
7️⃣ COMPLEXITY: O(n+m) time, O(n+m) space - optimal
8️⃣ TIME OUT: "I'd use two pointers to merge, appending smaller element each time"
9️⃣ FOLLOW-UP: "What if lists are very long?" → Consider generators for memory
🔟 EVALUATION: Must recognize two-pointer pattern, handle remainders correctly
"""


# ═══════════════════════════════════════════════════════════════════════
# TESTING FRAMEWORK (To verify solutions)
# ═══════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # Test Two Sum
    print("Testing Two Sum:")
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    print("✓ All Two Sum tests passed\n")
    
    # Test Palindrome
    print("Testing Palindrome:")
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    print("✓ All Palindrome tests passed\n")
    
    # Test Merge
    print("Testing Merge Sorted Lists:")
    assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted_lists([], [1, 2]) == [1, 2]
    assert merge_sorted_lists([1], []) == [1]
    print("✓ All Merge tests passed\n")
    
    print("🎉 ALL EASY PROBLEMS TESTED SUCCESSFULLY")
