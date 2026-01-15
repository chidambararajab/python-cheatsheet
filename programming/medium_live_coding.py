"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 MEDIUM LIVE CODING CHALLENGES - REAL INTERVIEW SIMULATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Interviewer: Senior Engineer | Hiring Bar-Raiser
Target: 3-7 YOE | Python Engineers
Time: 25-40 minutes per problem
Focus: Pattern Recognition, Optimization, Trade-offs
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MEDIUM EXPECTATIONS:
────────────────────
• Recognize problem patterns (sliding window, two pointers, hash map)
• Optimize from brute force to efficient solution
• Explain trade-offs clearly
• Handle complex edge cases
• Think through examples before coding
• Test as you build

ELIMINATION TRIGGERS:
─────────────────────
• Can't move past brute force → REJECT
• Doesn't recognize standard patterns → BORDERLINE
• Can't explain complexity → REJECT
• Breaks on edge cases → BORDERLINE
• No testing strategy → BORDERLINE
"""

# ═══════════════════════════════════════════════════════════════════════
# PROBLEM 1: LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1️⃣ PROBLEM STATEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Given a string, find the length of the longest substring without repeating characters.

Example 1:
    Input: "abcabcbb"
    Output: 3
    Explanation: "abc" is longest substring without repeating

Example 2:
    Input: "bbbbb"
    Output: 1
    Explanation: "b" is longest

Example 3:
    Input: "pwwkew"
    Output: 3
    Explanation: "wke" is longest

Constraints:
- String contains letters, digits, symbols, spaces
- Return length, not substring itself
- Empty string returns 0

Ambiguities to clarify:
- Case sensitive? (YES)
- Space counts as character? (YES)
- Only ASCII? (YES, assume ASCII)
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2️⃣ INTERVIEW THINK-ALOUD FLOW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STRONG CANDIDATE:

"I need to find longest substring with no repeating characters.

Let me think through approaches:

BRUTE FORCE: Check all substrings. For each starting position, expand until
we hit a repeat. Track maximum length. O(n²) or O(n³) depending on implementation.

OPTIMIZED: Sliding window with hash map. Expand right, track characters seen.
When we hit a repeat, shrink from left until no more repeats. O(n) time.

Let me trace through 'abcabcbb':
- Window: 'a' → length 1, max=1, seen={'a':0}
- Window: 'ab' → length 2, max=2, seen={'a':0, 'b':1}
- Window: 'abc' → length 3, max=3, seen={'a':0, 'b':1, 'c':2}
- Add 'a': REPEAT! 'a' at index 3, last seen at 0
  - Move left to 1 (after previous 'a')
  - Window: 'bca' → length 3, max=3
- Add 'b': REPEAT! Move left to 2
  - Window: 'cab' → length 3, max=3
- Continue...

Key insight: When we find repeat, we don't restart - we just move left pointer
to skip the repeated character.

Edge cases:
- Empty string: '' → 0
- All same: 'aaaa' → 1
- All unique: 'abcd' → 4
- Single char: 'a' → 1

I'll implement sliding window with hash map."
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3️⃣ INTENTIONAL TRAP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TRAP: Not moving left pointer correctly when duplicate found

BAD LOGIC:
When we find duplicate at position i:
  left = seen[s[i]] + 1  # ❌ WRONG!

WHAT BREAKS:
Input: "abba"
- Window "ab", seen={'a':0, 'b':1}
- Add 'b': duplicate at index 2, last seen at 1
  - left = 1 + 1 = 2
  - Window now starts at 'b' (index 2)
  - seen={'a':0, 'b':2}
- Add 'a': 'a' seen at index 0
  - left = 0 + 1 = 1  # ❌ MOVING BACKWARDS!
  - Now left=1 but right=3, window is "bba" which has duplicate!

CORRECT LOGIC:
left = max(left, seen[s[i]] + 1)

Only move left FORWARD, never backwards. Left pointer can only advance.

WHY CANDIDATES MISS IT:
They don't realize left pointer can be ahead of where duplicate was seen.
Must ensure left never goes backwards.
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4️⃣ SOLUTION (INTERVIEW-ACCEPTABLE)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def length_of_longest_substring(s):
    """
    Find length of longest substring without repeating characters.
    
    Approach: Sliding window with hash map
    - Expand right pointer, add characters to window
    - Track last seen position of each character
    - When duplicate found, move left pointer to skip it
    - Track maximum window size
    
    Time: O(n) - each character visited at most twice (by left and right)
    Space: O(min(n, m)) where m is charset size (ASCII = 128)
    
    Args:
        s: Input string
    
    Returns:
        int: Length of longest substring without repeating characters
    """
    if not s:
        return 0
    
    # Track last seen index of each character
    char_index = {}
    max_length = 0
    left = 0
    
    for right, char in enumerate(s):
        # If character seen before and within current window
        if char in char_index and char_index[char] >= left:
            # Move left pointer to after previous occurrence
            # Use max to ensure left only moves forward
            left = char_index[char] + 1
        
        # Update last seen position
        char_index[char] = right
        
        # Update max length
        current_length = right - left + 1
        max_length = max(max_length, current_length)
    
    return max_length


"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5️⃣ COMMON BUT BAD SOLUTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def length_of_longest_substring_brute(s):
    """
    ❌ BRUTE FORCE - Check all substrings
    """
    if not s:
        return 0
    
    max_length = 0
    
    # Try every starting position
    for i in range(len(s)):
        seen = set()
        # Expand from this starting position
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
        max_length = max(max_length, len(seen))
    
    return max_length

"""
WHY INTERVIEWERS DISLIKE:
─────────────────────────
1. O(n²) time - doesn't scale
2. Nested loops - inefficient
3. Doesn't recognize sliding window pattern
4. For medium problem, optimization expected

WHAT IT SIGNALS:
- Can solve problem, but not optimally
- Doesn't know sliding window technique
- Might struggle with optimization questions

WHEN ACCEPTABLE:
If candidate says: "This is O(n²) brute force. Let me optimize using sliding
window..." and actually does → GOOD PROCESS.

Staying with brute force → BORDERLINE for medium level.
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
6️⃣ EXPLANATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SLIDING WINDOW TECHNIQUE:
─────────────────────────
Maintain a window [left, right] representing current substring.
- Expand right: add new character
- When duplicate found: shrink from left until no duplicate
- Track maximum window size seen

CRITICAL INSIGHT:
Don't need to check every substring. Once we find a repeat, we know all
substrings starting before the previous occurrence won't be longer than
what we've already found.

Example trace: "abcabcbb"
Step | Window    | left | right | char | Action              | max
-----|-----------|------|-------|------|---------------------|----
0    | 'a'       | 0    | 0     | a    | Add, update max     | 1
1    | 'ab'      | 0    | 1     | b    | Add, update max     | 2
2    | 'abc'     | 0    | 2     | c    | Add, update max     | 3
3    | 'bca'     | 1    | 3     | a    | 'a' repeat, left=1  | 3
4    | 'cab'     | 2    | 4     | b    | 'b' repeat, left=2  | 3
5    | 'abc'     | 3    | 5     | c    | 'c' repeat, left=3  | 3
6    | 'bcb'     | 4    | 6     | b    | 'b' repeat, left=5  | 3
7    | 'cb'      | 6    | 7     | b    | 'b' repeat, left=7  | 3

PYTHON CONCEPTS:
- Sliding window pattern
- Hash map for O(1) lookup
- enumerate() for index + value
- max() for tracking maximum

KEY DETAIL:
Check `char_index[char] >= left` ensures we only care about duplicates
within current window, not earlier in string.
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
7️⃣ TIME & SPACE COMPLEXITY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TIME: O(n)
- Right pointer moves through string once: n iterations
- Left pointer only moves forward, at most n times total
- Each character visited at most twice (by right, then by left)
- Hash map operations (lookup, insert) are O(1)
- Total: O(2n) = O(n)

SPACE: O(min(n, m))
- Hash map stores unique characters
- In worst case (all unique), stores n characters
- But charset size m limits it (ASCII = 128, so at most 128)
- Therefore O(min(n, m))

WHY IT'S OPTIMAL:
Must examine every character at least once → can't do better than O(n) time.
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
8️⃣ IF TIME RUNS OUT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT TO SAY:
"I'm implementing sliding window. Two pointers track current window. Hash map
stores last seen position of each character. When I find a duplicate, I move
left pointer past the previous occurrence. Track maximum window size throughout.
Time O(n), space O(m) for charset size."

PARTIAL CREDIT:
✓ Identified sliding window pattern
✓ Explained hash map for tracking seen characters
✓ Mentioned need to update left pointer on duplicate
✓ Even without complete code, shows understanding

WHAT NOT TO SAY:
❌ "I need more time to figure this out" - vague
❌ "Can I use a library?" - Shows dependency
❌ "This is impossible" - Gives up

RECOVERY:
"If pressed for time, I can implement brute force first to show correctness,
then discuss how sliding window would optimize it."
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
9️⃣ FOLLOW-UP QUESTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEWER: "What if you need to return the substring itself, not just length?"

ANSWER:
"I'd track the starting position and length of the maximum window. When I update
max_length, also store the starting position:

if current_length > max_length:
    max_length = current_length
    max_start = left

Then return: s[max_start:max_start + max_length]
"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEWER: "How would you handle Unicode strings?"

ANSWER:
"Python 3 strings are Unicode by default. Hash map handles any hashable character.
Space complexity changes to O(min(n, m)) where m is Unicode charset size (much
larger), but algorithmically the same."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEWER: "What if we allow k repeats?"

ANSWER:
"Modified problem: longest substring with at most k repeating characters.
Track count of duplicates. When count > k, shrink window from left until
count <= k. More complex but same sliding window pattern."
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔟 INTERVIEWER EVALUATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ HIRE SIGNALS:
- Quickly recognized sliding window pattern
- Correctly handled left pointer logic (max to prevent backwards movement)
- Efficient O(n) solution
- Explained why check `>= left` is necessary
- Clean code with clear variable names
- Tested with examples
- Handled edge cases (empty string)

⚠️ BORDERLINE SIGNALS:
- Started with brute force, needed hint to optimize
- Forgot to check `>= left`, caught during testing
- Code works but took long to implement
- Weak complexity analysis

❌ NO-HIRE SIGNALS:
- Couldn't recognize sliding window pattern
- Stuck on brute force O(n²) solution
- Moved left pointer backwards (bug)
- Couldn't explain why solution works
- No testing or edge case handling
- Poor time management (ran out of time)

DECISION FACTORS:
Pattern recognition is KEY for medium problems. Sliding window is a fundamental
pattern. Not knowing it at 3-7 YOE is a red flag.

Correct pointer management separates strong from weak candidates. The `max(left, ...)`
detail shows attention to correctness.
"""


# ═══════════════════════════════════════════════════════════════════════
# PROBLEM 2: GROUP ANAGRAMS
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1️⃣ PROBLEM STATEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Given an array of strings, group anagrams together.

Example:
    Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
    Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

Note: Order within groups and order of groups doesn't matter.

Constraints:
- All strings are lowercase
- Return list of lists
- Empty input returns empty list

Anagram: Two words with same characters in different order
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2️⃣ THINK-ALOUD FLOW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Need to group anagrams. Anagrams have same characters, different order.

Key insight: If two words are anagrams, sorting their characters produces
the same string.

Example: 'eat' and 'tea'
- sorted('eat') = 'aet'
- sorted('tea') = 'aet'
- Same sorted form → anagrams!

Approach: Use hash map where key is sorted characters, value is list of words.

Algorithm:
1. For each word, create key by sorting its characters
2. Use key to group words in hash map
3. Return all groups (values of hash map)

Example trace:
['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

- 'eat' → sorted='aet' → groups={'aet': ['eat']}
- 'tea' → sorted='aet' → groups={'aet': ['eat', 'tea']}
- 'tan' → sorted='ant' → groups={'aet': ['eat','tea'], 'ant': ['tan']}
- 'ate' → sorted='aet' → groups={'aet': ['eat','tea','ate'], 'ant': ['tan']}
- etc.

Result: list(groups.values())

Edge cases:
- Empty list: [] → []
- Single word: ['a'] → [['a']]
- No anagrams: ['a','b','c'] → [['a'],['b'],['c']]
- All anagrams: ['a','a','a'] → [['a','a','a']]"
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3️⃣ TRAP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TRAP: Using list as hash map key

BAD CODE:
key = list(word)
key.sort()
groups[key].append(word)  # ❌ TypeError: unhashable type: 'list'

WHY IT BREAKS:
Lists are mutable, can't be used as dictionary keys. Must be hashable (immutable).

FIX OPTIONS:
1. Convert sorted list to tuple: key = tuple(sorted(word))
2. Convert sorted list to string: key = ''.join(sorted(word))

Both work, string is slightly more readable.

WHY CANDIDATES MISS IT:
They sort() the characters but forget Python dict keys must be immutable.
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4️⃣ SOLUTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def group_anagrams(strs):
    """
    Group anagrams together using sorted characters as key.
    
    Time: O(n * k log k) where n = number of strings, k = max string length
    Space: O(n * k) to store all strings
    
    Args:
        strs: List of strings
    
    Returns:
        List of lists, each sublist contains anagrams
    """
    from collections import defaultdict
    
    if not strs:
        return []
    
    # Map: sorted characters → list of original words
    anagram_groups = defaultdict(list)
    
    for word in strs:
        # Sort characters to create key
        # Anagrams will have same sorted form
        key = ''.join(sorted(word))
        anagram_groups[key].append(word)
    
    # Return all groups
    return list(anagram_groups.values())


"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5️⃣ BAD SOLUTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def group_anagrams_bad(strs):
    """❌ Compare every pair - O(n²)"""
    if not strs:
        return []
    
    def are_anagrams(s1, s2):
        return sorted(s1) == sorted(s2)
    
    groups = []
    used = [False] * len(strs)
    
    for i in range(len(strs)):
        if used[i]:
            continue
        group = [strs[i]]
        used[i] = True
        
        for j in range(i + 1, len(strs)):
            if not used[j] and are_anagrams(strs[i], strs[j]):
                group.append(strs[j])
                used[j] = True
        
        groups.append(group)
    
    return groups

"""
WHY BAD:
- O(n²) comparisons → doesn't scale
- Sorts same string multiple times
- Complex logic with used flags
- Signals: Doesn't recognize hash map pattern
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
6️⃣ EXPLANATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

KEY INSIGHT:
Anagrams have identical sorted character sequences. Use this as grouping key.

ALGORITHM:
1. Create hash map (defaultdict for cleaner code)
2. For each word:
   - Sort its characters
   - Use sorted form as key
   - Append original word to that key's list
3. Return all lists (values) from hash map

PYTHON CONCEPTS:
- defaultdict(list) - auto-creates empty list for new keys
- sorted() returns new sorted list
- ''.join() combines characters back to string
- dict.values() returns all values

TIME BREAKDOWN:
- n strings to process
- Each string length k needs sorting: O(k log k)
- Total: O(n * k log k)

ALTERNATIVE: Character count as key
Instead of sorting, count character frequencies:
key = tuple(sorted(Counter(word).items()))

Same complexity but more complex code. Sorting is clearer for interview.
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REMAINING SECTIONS ABBREVIATED FOR SPACE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

7️⃣ COMPLEXITY: O(n * k log k) time, O(n * k) space - optimal for this approach
8️⃣ TIME OUT: "Use hash map with sorted characters as key to group anagrams"
9️⃣ FOLLOW-UP: "What if strings are very long?" → Consider character counting instead of sorting
🔟 EVALUATION: Must recognize hash map grouping pattern, avoid O(n²) comparison
"""


# ═══════════════════════════════════════════════════════════════════════
# PROBLEM 3: PRODUCT OF ARRAY EXCEPT SELF
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1️⃣ PROBLEM STATEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Given an integer array, return array where each element is the product of
all other elements EXCEPT itself.

Example:
    Input: [1, 2, 3, 4]
    Output: [24, 12, 8, 6]
    Explanation:
        result[0] = 2 * 3 * 4 = 24
        result[1] = 1 * 3 * 4 = 12
        result[2] = 1 * 2 * 4 = 8
        result[3] = 1 * 2 * 3 = 6

Constraint: **You cannot use division.**
Time requirement: O(n)
Space requirement: O(1) extra space (output array doesn't count)
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2️⃣ THINK-ALOUD FLOW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Product of all except self. Can't use division.

If division allowed: total_product / nums[i]. But constraint says no division.

Key insight: For each position i, result is:
(product of all elements to the LEFT) * (product of all elements to the RIGHT)

Example: [1, 2, 3, 4]
Position 0: left=1 (nothing left), right=2*3*4=24, result=1*24=24
Position 1: left=1, right=3*4=12, result=1*12=12
Position 2: left=1*2=2, right=4, result=2*4=8
Position 3: left=1*2*3=6, right=1 (nothing right), result=6*1=6

Algorithm:
1. First pass: compute left products, store in result
2. Second pass: multiply by right products

To achieve O(1) space, build result array in-place:
- First pass left-to-right: store left products
- Second pass right-to-left: multiply by right products

Edge cases:
- Array with zeros: [0, 1, 2] → handle carefully
- Single element: [5] → return [?] (undefined, but per constraints won't happen)
- Two elements: [3, 4] → [4, 3]"
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3️⃣ TRAP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TRAP: Trying to use division despite constraint

TEMPTING BUT WRONG:
total = 1
for num in nums:
    total *= num
result = [total // num for num in nums]  # ❌ Violates constraint!

Also breaks if nums contains 0 (division by zero).

ANOTHER TRAP: Creating extra arrays for left and right products

code:
left = [1] * len(nums)
right = [1] * len(nums)
# ...build left and right arrays
result = [left[i] * right[i] for i in range(len(nums))]

This works but uses O(n) extra space, violating space requirement.

CORRECT: Build result array in-place with two passes.
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4️⃣ SOLUTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def product_except_self(nums):
    """
    Compute product of array except self without division.
    
    Approach: Two passes
    - Left pass: multiply all elements to the left
    - Right pass: multiply all elements to the right
    
    Time: O(n)
    Space: O(1) excluding output array
    
    Args:
        nums: List of integers
    
    Returns:
        List where result[i] = product of all elements except nums[i]
    """
    n = len(nums)
    result = [1] * n
    
    # Left pass: result[i] contains product of all elements to left of i
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]
    
    # Right pass: multiply by product of all elements to right of i
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    
    return result


"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EXAMPLE TRACE: [1, 2, 3, 4]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LEFT PASS:
i=0: result[0]=1 (left_product=1), then left_product=1*1=1
i=1: result[1]=1 (left_product=1), then left_product=1*2=2
i=2: result[2]=2 (left_product=2), then left_product=2*3=6
i=3: result[3]=6 (left_product=6), then left_product=6*4=24
Result after left pass: [1, 1, 2, 6]

RIGHT PASS:
i=3: result[3]=6*1=6, then right_product=1*4=4
i=2: result[2]=2*4=8, then right_product=4*3=12
i=1: result[1]=1*12=12, then right_product=12*2=24
i=0: result[0]=1*24=24, then right_product=24*1=24
Final result: [24, 12, 8, 6] ✓
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5-10 SECTIONS ABBREVIATED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

5️⃣ BAD: Create separate left/right arrays → O(n) extra space
6️⃣ KEY: Understand product = left_product * right_product
7️⃣ COMPLEXITY: O(n) time, O(1) space (excluding output)
8️⃣ TIME OUT: "Two passes: left products, then multiply by right products"
9️⃣ FOLLOW-UP: "What if array has zeros?" → Works correctly, test it
🔟 EVALUATION: Must achieve O(n) time and O(1) space - tough constraint test
"""


# ═══════════════════════════════════════════════════════════════════════
# PROBLEM 4: 3SUM
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1️⃣ PROBLEM STATEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Given an integer array, return all unique triplets that sum to zero.

Example:
    Input: nums = [-1, 0, 1, 2, -1, -4]
    Output: [[-1, -1, 2], [-1, 0, 1]]

Constraints:
- No duplicate triplets in result
- Order of triplets doesn't matter
- Can use same element value multiple times if at different indices
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2️⃣ THINK-ALOUD FLOW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"3Sum - finding three numbers that sum to zero.

Key insight: Fix one number, then it's a 2Sum problem for the remaining two!

Algorithm:
1. Sort the array
2. For each number nums[i]:
   - Find two numbers that sum to -nums[i] (makes total zero)
   - Use two pointers on remaining sorted array
3. Skip duplicates to avoid duplicate triplets

Example: [-1, 0, 1, 2, -1, -4]
Sorted: [-4, -1, -1, 0, 1, 2]
- i=0, nums[i]=-4, need two that sum to 4 → not found
- i=1, nums[i]=-1, need two that sum to 1 → found: 0,1 and -1,2
- Skip duplicate -1 at i=2
- Continue...

Critical: Must skip duplicates to avoid repeated triplets!"
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3️⃣ TRAP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TRAP: Not skipping duplicates properly

Without skipping duplicates:
[-1, 0, 1] might appear multiple times if there are duplicate -1's

Must skip:
1. Duplicate i values: if nums[i] == nums[i-1], skip
2. Duplicate left values after finding match
3. Duplicate right values after finding match
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4️⃣ SOLUTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def three_sum(nums):
    """
    Find all unique triplets that sum to zero.
    
    Approach: Sort + two pointers
    - Fix first number
    - Use two pointers for remaining two
    - Skip duplicates carefully
    
    Time: O(n²) - n iterations * O(n) two-pointer search
    Space: O(1) excluding output
    """
    nums.sort()  # Sort first for two-pointer approach
    result = []
    n = len(nums)
    
    for i in range(n - 2):
        # Skip duplicate values for first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Two pointers for remaining two numbers
        left, right = i + 1, n - 1
        target = -nums[i]  # Need two numbers that sum to this
        
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for left pointer
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicates for right pointer
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
                
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
    return result


"""
5️⃣ BAD: O(n³) checking all triplets without sorting
6️⃣ KEY: Sort + fix one + two pointers for other two
7️⃣ COMPLEXITY: O(n²) time (optimal), O(1) space
8️⃣ TIME OUT: "Sort array, fix first, two pointers for remaining two"
9️⃣ FOLLOW-UP: "kSum?" → Generalize with recursion
🔟 EVALUATION: Must skip duplicates correctly, achieve O(n²)
"""


# ═══════════════════════════════════════════════════════════════════════
# PROBLEM 5: CONTAINER WITH MOST WATER
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1️⃣ PROBLEM STATEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Given n non-negative integers representing heights, where width between
each line is 1, find two lines that together with x-axis form a container
that holds the most water.

Example:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: Lines at index 1 (height 8) and 8 (height 7),
                 distance = 7, area = min(8,7) * 7 = 49

Note: Container area = min(height[i], height[j]) * (j - i)
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2️⃣ THINK-ALOUD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Finding maximum water container between two lines.

Area = min(left_height, right_height) * distance

Brute force: Check all pairs → O(n²)

Optimized: Two pointers from ends
- Start with maximum width
- Move pointer with smaller height inward (only way to increase area)
- Track maximum area seen

Why this works: With maximum width, only way to improve is taller heights.
Moving the shorter one might find taller height. Moving taller one can't help
because area limited by shorter one anyway.

Example: [1,8,6,2,5,4,8,3,7]
left=0 (h=1), right=8 (h=7): area = min(1,7)*8 = 8
Move left (shorter): left=1 (h=8), area = min(8,7)*7 = 49
Move right (shorter): left=1, right=7 (h=3): area = min(8,3)*6 = 18
..."
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3️⃣ TRAP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TRAP: Moving the taller pointer instead of shorter

If you move the taller pointer:
- Width decreases
- Height can't increase (limited by shorter one)
- Area guaranteed to not improve

Must always move the shorter pointer to have chance of improvement.
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4️⃣ SOLUTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def max_area(height):
    """
    Find maximum water container area.
    
    Approach: Two pointers from ends, move shorter pointer.
    Time: O(n) - single pass
    Space: O(1)
    """
    left, right = 0, len(height) - 1
    max_water = 0
    
    while left < right:
        # Calculate current area
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height
        
        max_water = max(max_water, current_area)
        
        # Move pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water


"""
5️⃣ BAD: O(n²) checking all pairs
6️⃣ KEY: Two pointers, always move shorter one
7️⃣ COMPLEXITY: O(n) time, O(1) space - optimal
8️⃣ TIME OUT: "Two pointers from ends, move shorter height inward"
9️⃣ FOLLOW-UP: "Why move shorter?" → Only way area could improve
🔟 EVALUATION: Must recognize greedy two-pointer approach
"""


# ═══════════════════════════════════════════════════════════════════════
# PROBLEM 6: MERGE INTERVALS
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1️⃣ PROBLEM STATEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Given collection of intervals, merge all overlapping intervals.

Example:
    Input: [[1,3], [2,6], [8,10], [15,18]]
    Output: [[1,6], [8,10], [15,18]]
    Explanation: [1,3] and [2,6] overlap, merge to [1,6]

Intervals represented as [start, end] where start <= end.
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2️⃣ THINK-ALOUD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Merge overlapping intervals.

Key insight: If sorted by start time, overlapping intervals will be adjacent.

Algorithm:
1. Sort intervals by start time
2. Iterate through sorted intervals:
   - If current overlaps with last merged interval: merge them
   - Otherwise: add current to result

Overlap check: current.start <= last.end

Merge: new_end = max(current.end, last.end)

Example: [[1,3], [2,6], [8,10], [15,18]]
Already sorted by start
- Add [1,3] to result
- [2,6] overlaps (2 <= 3): merge to [1,6]
- [8,10] doesn't overlap: add to result
- [15,18] doesn't overlap: add to result
Result: [[1,6], [8,10], [15,18]]"
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3️⃣ TRAP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TRAP: Not sorting first

Without sorting, overlapping intervals might not be adjacent:
[[8,10], [1,3], [2,6], [15,18]]

Can't detect [1,3] and [2,6] overlap when they're separated.

Must sort by start time first!
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4️⃣ SOLUTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def merge_intervals(intervals):
    """
    Merge all overlapping intervals.
    
    Approach: Sort by start, merge adjacent overlapping intervals.
    Time: O(n log n) for sorting
    Space: O(n) for result
    """
    if not intervals:
        return []
    
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        
        # Check if current overlaps with last merged
        if current[0] <= last[1]:
            # Overlap - merge by extending end
            last[1] = max(last[1], current[1])
        else:
            # No overlap - add as new interval
            merged.append(current)
    
    return merged


"""
5️⃣ BAD: O(n²) checking every pair without sorting
6️⃣ KEY: Sort first makes overlaps adjacent
7️⃣ COMPLEXITY: O(n log n) time (sorting dominates)
8️⃣ TIME OUT: "Sort by start time, merge adjacent overlapping intervals"
9️⃣ FOLLOW-UP: "Insert new interval?" → Binary search + merge
🔟 EVALUATION: Must sort first, handle merge logic correctly
"""


# ═══════════════════════════════════════════════════════════════════════
# TESTING FRAMEWORK
# ═══════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # Test Longest Substring
    print("Testing Longest Substring:")
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0
    print("✓ All Longest Substring tests passed\n")
    
    # Test Group Anagrams
    print("Testing Group Anagrams:")
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert len(result) == 3  # Should have 3 groups
    # Flatten and check all words are present
    all_words = []
    for group in result:
        all_words.extend(group)
    assert sorted(all_words) == sorted(["eat", "tea", "tan", "ate", "nat", "bat"])
    print("✓ All Group Anagrams tests passed\n")
    
    # Test Product Except Self
    print("Testing Product Except Self:")
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([0, 1, 2, 3]) == [6, 0, 0, 0]
    print("✓ All Product tests passed\n")
    
    # Test 3Sum
    print("Testing 3Sum:")
    result = three_sum([-1, 0, 1, 2, -1, -4])
    assert len(result) == 2
    assert [-1, -1, 2] in result or [-1, 0, 1] in result
    print("✓ All 3Sum tests passed\n")
    
    # Test Container With Most Water
    print("Testing Container With Most Water:")
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
    assert max_area([4, 3, 2, 1, 4]) == 16
    print("✓ All Container tests passed\n")
    
    # Test Merge Intervals
    print("Testing Merge Intervals:")
    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]
    print("✓ All Merge Intervals tests passed\n")
    
    print("🎉 ALL 6 MEDIUM PROBLEMS TESTED SUCCESSFULLY")
    print("Problems: Longest Substring, Anagrams, Product, 3Sum, Container, Merge Intervals")
