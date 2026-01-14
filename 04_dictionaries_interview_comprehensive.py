"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 PYTHON DICTIONARIES - SENIOR ENGINEER INTERVIEW PREPARATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Interviewer: Staff Engineer | Bar-Raiser | Python Expert
Candidate Level: 5+ Years Experience  
Purpose: THE MOST CRITICAL DATA STRUCTURE - 70% of problems need this
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

# ═══════════════════════════════════════════════════════════════════════
# 1️⃣ FILE INTERVIEW OVERVIEW
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHY DICTIONARIES ARE THE MOST CRITICAL FOR PYTHON INTERVIEWS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Dictionaries appear in 70% of Python interviews. Master this, master interviews.

THE GOLDEN RULE:
"If you see 'find two elements that...'" → THINK DICTIONARY IMMEDIATELY

Dicts are used for:
• Two Sum pattern (THE most common interview question)
• Frequency counting (anagrams, character counts, etc.)
• Caching/Memoization (DP problems)
• Graph adjacency lists
• Prefix sum patterns
• Grouping operations
• O(n²) → O(n) optimization

WHAT INTERVIEWERS EXPECT MASTERY OF:
────────────────────────────────────
✓ get() with default - NEVER use dict[key] directly!
✓ Iteration: for k,v in d.items() (most common)
✓ defaultdict and Counter from collections
✓ Hash table internals - O(1) average case
✓ Two Sum pattern - must code in under 2 minutes
✓ Frequency counting pattern
✓ When dict beats list/set

MUST-KNOW (Will be tested):
───────────────────────────
• get(key, default)
• items(), keys(), values()
• Iteration patterns (4 types)
• defaultdict(int), defaultdict(list)
• Counter and most_common()
• Two Sum pattern
• Anagram grouping pattern
• Hash collisions (theory)

NICE-TO-KNOW (Rarely tested):
──────────────────────────────
• setdefault()
• popitem()
• Dictionary view objects
• OrderedDict (obsolete in Python 3.7+)

SIGNALS OF STRONG vs WEAK CANDIDATES:
─────────────────────────────────────
STRONG CANDIDATES:
  ✓ Immediately suggest dict for "find pair" problems
  ✓ Use d.get(key, 0) + 1 pattern instantly
  ✓ Explain O(n²) → O(n) optimization with hash map
  ✓ Recognize when Counter is cleaner than manual dict
  ✓ Handle KeyError gracefully with get()
  ✓ Know when keys must be hashable

WEAK CANDIDATES:
  ✗ Use nested loops for Two Sum (O(n²))
  ✗ Write if key in dict: dict[key] += 1 else: dict[key] = 1
  ✗ Don't know defaultdict exists
  ✗ Use d[key] instead of d.get(key, default)
  ✗ Iterate with for key in d: value = d[key] (inefficient)
  ✗ Don't understand hash table complexity

AUTOMATIC REJECTION SIGNALS:
────────────────────────────
❌ Can't code Two Sum with dict in 3 minutes
❌ Doesn't know what O(1) lookup means
❌ Uses list when dict is clearly better
❌ Doesn't handle KeyError
❌ Can't explain why dict is faster than list for search

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ═══════════════════════════════════════════════════════════════════════
# 2️⃣ METHOD / CONCEPT EXTRACTION & CLASSIFICATION
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONCEPT CLASSIFICATION BY INTERVIEW FREQUENCY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

╔════════════════════════╦═════════════╦══════════════════════════════════╗
║ CONCEPT                ║ FREQUENCY   ║ WHY TESTED / REJECTION REASONS   ║
╠════════════════════════╬═════════════╬══════════════════════════════════╣
║ get(key, default)      ║ HIGH        ║ Prevents KeyError - critical     ║
║                        ║             ║ REJECT: Uses d[key] unsafely     ║
╠════════════════════════╬═════════════╬══════════════════════════════════╣
║ d.items() iteration    ║ HIGH        ║ Most Pythonic iteration          ║
║                        ║             ║ REJECT: for k in d: v = d[k]     ║
╠════════════════════════╬═════════════╬══════════════════════════════════╣
║ defaultdict            ║ HIGH        ║ Cleaner than manual checking     ║
║                        ║             ║ REJECT: Doesn't know it exists   ║
╠════════════════════════╬═════════════╬══════════════════════════════════╣
║ Counter                ║ HIGH        ║ Frequency counting standard      ║
║                        ║             ║ REJECT: Manual freq counting     ║
╠════════════════════════╬═════════════╬══════════════════════════════════╣
║ Two Sum pattern        ║ HIGH        ║ THE interview question           ║
║                        ║             ║ REJECT: Can't code in 3 mins     ║
╠════════════════════════╬═════════════╬══════════════════════════════════╣
║ O(1) lookup            ║ HIGH        ║ Hash table fundamentals          ║
║                        ║             ║ REJECT: Doesn't understand why   ║
╠════════════════════════╬═════════════╬══════════════════════════════════╣
║ Hashable keys          ║ MEDIUM      ║ Understands immutability         ║
║                        ║             ║ REJECT: Tries to use list as key ║
╠════════════════════════╬═════════════╬══════════════════════════════════╣
║ Modifying while iterate║ MEDIUM      ║ Iterator invalidation            ║
║                        ║             ║ REJECT: Doesn't see the bug      ║
╠════════════════════════╬═════════════╬══════════════════════════════════╣
║ pop(key, default)      ║ MEDIUM      ║ Safe removal                     ║
║                        ║             ║ REJECT: (Minor if missed)        ║
╠════════════════════════╬═════════════╬══════════════════════════════════╣
║ update()               ║ LOW         ║ Dictionary merging               ║
║                        ║             ║ REJECT: (Rarely tested)          ║
╠════════════════════════╬═════════════╬══════════════════════════════════╣
║ setdefault()           ║ LOW         ║ get+set combo                    ║
║                        ║             ║ REJECT: (Nice to know only)      ║
╚════════════════════════╩═════════════╩══════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ═══════════════════════════════════════════════════════════════════════
# 3️⃣ INTERVIEW QUESTIONS (CONTROLLED DENSITY)
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 3A: get() WITH DEFAULT (HIGH FREQUENCY - CRITICAL)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

① WARM-UP QUESTION
──────────────────
Q: What's the difference between dict[key] and dict.get(key, 0)?

EXPECTED ANSWER:
"dict[key] raises KeyError if key doesn't exist. dict.get(key, 0) returns 0 (the
default) if key is missing. In interviews, ALWAYS use get() for safety unless you're
certain the key exists. Time complexity: both O(1)."

RED FLAG: "They're the same" or "I always use dict[key]"

② CORE INTERVIEW QUESTION
─────────────────────────
Q: Count frequency of each character in a string. Write the code.

THINK-ALOUD ANSWER:
"I'll use a dictionary to map character to count. For each character, I'll use
d.get(char, 0) + 1 to increment. This handles missing keys gracefully. Alternative:
use Counter from collections, which is cleaner."

def count_chars_manual(s):
    \"\"\"
    Interviewer expects: get() usage, clean code
    \"\"\"
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

def count_chars_pythonic(s):
    \"\"\"
    Better: use Counter (what strong candidates do)
    \"\"\"
    from collections import Counter
    return Counter(s)

INTERVIEWER EVALUATION:
✓ STRONG: Uses get() or Counter immediately
✗ WEAK: Writes if char in freq: freq[char] += 1 else: freq[char] = 1

③ EDGE-CASE / TRAP QUESTION
────────────────────────────
Q: Debug this code. What's wrong?

```
def count_words(words):
    freq = {}
    for word in words:
        freq[word] += 1  # Bug here!
    return freq
```

EXPECTED ANSWER:
"KeyError on first occurrence of each word. Should use freq[word] = freq.get(word, 0) + 1
OR use defaultdict(int) which auto-initializes to 0."

INTERVIEWER EVALUATION:
✓ STRONG: Immediately identifies KeyError
✗ WEAK: Doesn't see the bug
✗ DISQUALIFYING: Suggests try-except (massive red flag)

④ FOLLOW-UP OPTIMIZATION
─────────────────────────
Q: What's the most Pythonic way to implement the frequency counter?

EXPECTED ANSWER:
"from collections import Counter; return Counter(words). Counter is purpose-built for
this, more readable, and has useful methods like most_common(). Only write manual dict
if interviewer specifically asks or Counter is unavailable."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 3B: ITERATION PATTERNS (HIGH FREQUENCY)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

① WARM-UP QUESTION
──────────────────
Q: What are the 4 ways to iterate over a dictionary? Which is most common?

EXPECTED ANSWER:
"1. for key in d: (keys only)
 2. for key in d.keys(): (keys explicitly)
 3. for value in d.values(): (values only)
 4. for key, value in d.items(): (key-value pairs) ← Most common in interviews

items() is most common because you usually need both key and value."

② CORE INTERVIEW QUESTION
─────────────────────────
Q: Given dict of student grades, return list of students with grades above 90.

THINK-ALOUD ANSWER:
"I'll iterate with items() to get both name and grade. Filter grades > 90. Can use
list comprehension for clean one-liner."

def students_above_90(grades):
    \"\"\"
    Interviewer expects: items() usage, list comprehension
    \"\"\"
    return [name for name, grade in grades.items() if grade > 90]

INTERVIEWER EVALUATION:
✓ STRONG: Uses items() with comprehension
✗ WEAK: for name in grades: if grades[name] > 90: ... (inefficient)

③ EDGE-CASE / TRAP QUESTION
────────────────────────────
Q: Debug this. Why does it cause RuntimeError?

```
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    if d[key] == 2:
        del d[key]  # RuntimeError!
```

EXPECTED ANSWER:
"Modifying dictionary during iteration invalidates the iterator. Fix: iterate over
list(d.keys()) to create a copy of keys first, or build new dict with comprehension.
This is similar to modifying list while iterating - same bug class."

CORRECT SOLUTION:
```
for key in list(d.keys()):  # list() creates copy
    if d[key] == 2:
        del d[key]
```

④ FOLLOW-UP OPTIMIZATION
─────────────────────────
Q: What's more efficient: for k in d: v = d[k] OR for k, v in d.items()?

EXPECTED ANSWER:
"items() is more efficient. First approach does two lookups per iteration (checking
key exists, then fetching value). items() returns pairs directly, single lookup.
Always use items() when you need both key and value."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 3C: TWO SUM PATTERN (HIGH FREQUENCY - THE INTERVIEW KILLER)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This is THE most important pattern. If you can't code this in 2-3 minutes, you FAIL.

① WARM-UP QUESTION
──────────────────
Q: Why does Two Sum need a dictionary? Why not use two loops?

EXPECTED ANSWER:
"Two loops is O(n²) - for each element, scan entire array for complement. Dictionary
gives O(1) lookup, reducing to O(n) total. We store seen numbers with indices, check
if complement exists in constant time. This is the hash table advantage."

RED FLAG: Can't explain why dict is faster than nested loops

② CORE INTERVIEW QUESTION (MUST MASTER THIS)
─────────────────────────────────────────────
Q: Given array of integers and target, return indices of two numbers that sum to target.
   Example: nums = [2,7,11,15], target = 9 → return [0,1]

THINK-ALOUD ANSWER (Must say this confidently):
"This is Two Sum, classic hash map problem. I'll iterate through array once. For each
number, calculate complement = target - num. Check if complement exists in hash map
using O(1) lookup. If yes, found pair. If no, add current number to map. This is O(n)
time, O(n) space, better than O(n²) brute force."

def two_sum(nums, target):
    \"\"\"
    THE interview question. Must code this in under 3 minutes.
    
    Interviewer expects:
    - Use dictionary
    - One pass solution
    - Handle indices correctly
    - Mention complexity without being asked
    \"\"\"
    seen = {}  # value -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return None  # Or raise exception

INTERVIEWER EVALUATION:
✓ STRONG HIRE: Codes correctly in < 3 minutes, explains complexity
✓ HIRE: Codes correctly with minor hints
✗ NO HIRE: Can't code this, uses nested loops, takes > 5 minutes

③ EDGE-CASE / TRAP QUESTION
────────────────────────────
Q: What if the same element can't be used twice? How does your solution handle it?

EXPECTED ANSWER:
"My solution already handles this correctly. We check if complement exists BEFORE adding
current element to map. This ensures we don't use the same element twice. Example:
nums=[3,3], target=6 works because first 3 isn't in map when we check."

INTERVIEWER EVALUATION:
✓ STRONG: Explains why code already handles this
✗ WEAK: Modifies working code unnecessarily

④ FOLLOW-UP OPTIMIZATION
─────────────────────────
Q: Return ALL pairs that sum to target, not just first one.

THINK-ALOUD ANSWER:
"Need to collect all pairs. I'll still use hash map but continue iteration instead of
returning early. Store (seen[complement], i) in result list. Handle duplicates by using
set of tuples or sorting pairs."

def two_sum_all_pairs(nums, target):
    \"\"\"
    Find all pairs (distinct indices)
    \"\"\"
    seen = {}
    pairs = []
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            pairs.append([seen[complement], i])
        seen[num] = i
    
    return pairs

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 3D: DEFAULTDICT (HIGH FREQUENCY)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

① WARM-UP QUESTION
──────────────────
Q: What's the advantage of defaultdict over regular dict?

EXPECTED ANSWER:
"defaultdict auto-initializes missing keys with default value based on type. 
defaultdict(int) initializes to 0, defaultdict(list) to []. Avoids manual checking
'if key in dict' or using get(). Cleaner code, same O(1) complexity."

② CORE INTERVIEW QUESTION
─────────────────────────
Q: Group anagrams: ["eat","tea","tan","ate","nat","bat"] → [["eat","tea","ate"],["tan","nat"],["bat"]]

THINK-ALOUD ANSWER:
"Anagrams have same characters when sorted. I'll use sorted(word) as key, defaultdict(list)
as container. For each word, append to list at sorted key. This groups anagrams
automatically. O(n * k log k) where n=number words, k=max word length."

def group_anagrams(words):
    \"\"\"
    Interviewer expects: defaultdict usage, sorted as key
    \"\"\"
    from collections import defaultdict
    
    groups = defaultdict(list)
    for word in words:
        key = tuple(sorted(word))  # Sorted chars as key
        groups[key].append(word)
    
    return list(groups.values())

INTERVIEWER EVALUATION:
✓ STRONG: Uses defaultdict(list) immediately
✗ WEAK: Manual if key in groups: groups[key].append() else: groups[key] = []

③ EDGE-CASE / TRAP QUESTION
────────────────────────────
Q: Why use tuple(sorted(word)) instead of sorted(word) as key?

EXPECTED ANSWER:
"sorted() returns a list, which is unhashable - can't be dict key. tuple() makes it
immutable and hashable. This is a common trap. Keys must be immutable: int, str, tuple
work. List, dict, set don't."

④ FOLLOW-UP OPTIMIZATION
─────────────────────────
Q: Can you avoid sorting (O(k log k)) per word?

EXPECTED ANSWER:
"Yes, use character count as key instead of sorted chars. Create tuple of 26 counts
(a-z). This is O(k) per word instead of O(k log k). Trade-off: more complex key
creation vs faster runtime. For short words, sorting is fine. For long words or many
words, counting is better."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 3E: Counter (HIGH FREQUENCY)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

① WARM-UP QUESTION
──────────────────
Q: What does Counter.most_common(k) return? What's the complexity?

EXPECTED ANSWER:
"Returns list of (element, count) tuples, k most frequent elements. Complexity: O(n log k)
using heap internally. Common interview use: find top k frequent elements."

② CORE INTERVIEW QUESTION
─────────────────────────
Q: Find k most frequent elements in array. nums = [1,1,1,2,2,3], k = 2 → [1,2]

THINK-ALOUD ANSWER:
"I'll use Counter to count frequencies, then most_common(k) to get top k. This is
O(n) to count, O(n log k) to find top k. Total O(n log k). Could optimize to O(n)
with bucket sort, but Counter is cleaner for interviews unless asked to optimize."

def top_k_frequent(nums, k):
    \"\"\"
    Interviewer expects: Counter + most_common
    \"\"\"
    from collections import Counter
    
    freq = Counter(nums)
    # most_common returns [(element, count), ...]
    return [element for element, count in freq.most_common(k)]

③ EDGE-CASE / TRAP QUESTION
────────────────────────────
Q: What if k is larger than number of unique elements?

EXPECTED ANSWER:
"most_common(k) returns all elements if k exceeds unique count. No error. Example:
Counter([1,2,3]).most_common(10) returns all 3 elements. This is safe behavior."

④ FOLLOW-UP OPTIMIZATION
─────────────────────────
Q: Can you get O(n) time for top k frequent?

EXPECTED ANSWER:
"Yes, bucket sort. Create list of size n+1, where index = frequency. Place elements
in buckets by frequency. Iterate buckets backwards to get most frequent. O(n) time,
O(n) space. But Counter is cleaner and O(n log k) is usually acceptable in interviews."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 3F: HASHABLE KEYS (MEDIUM FREQUENCY)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

① CORE INTERVIEW QUESTION (Only 1 for MEDIUM)
──────────────────────────────────────────────
Q: You need to use a list as dictionary key. How do you handle this?

THINK-ALOUD ANSWER:
"Lists are unhashable - can't be dict keys. Convert to tuple: tuple(my_list). Tuples
are immutable and hashable. Common in problems with coordinates (row, col) or when
sorting creates a hashable signature."

EXAMPLE:
```
# ❌ Won't work
coordinates = {}
coordinates[[1, 2]] = "value"  # TypeError: unhashable type: 'list'

# ✅ Correct
coordinates = {}
coordinates[(1, 2)] = "value"  # Works!
```

INTERVIEWER EVALUATION:
✓ STRONG: Immediately mentions tuple conversion
✗ WEAK: Doesn't know why it fails or suggests workarounds

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ═══════════════════════════════════════════════════════════════════════
# 4️⃣ THINK-ALOUD ANSWERS (MANDATORY)
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT STRONG CANDIDATES SAY (verbatim examples)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PROBLEM: Two Sum
────────────────

STRONG CANDIDATE NARRATION (EXACTLY WHAT TO SAY):
"This is a classic hash map problem. The brute force would be nested loops - for each
element, check if target minus element exists in rest of array. That's O(n²).

Better approach: use dictionary to track seen numbers. As I iterate, for each number I
calculate complement equals target minus current number. I check if complement exists
in the hash map - that's O(1) lookup. If yes, I found my pair, return the indices. If
no, I add current number with its index to the map.

This is a single pass through array, O(n) time. Space is O(n) for the hash map. Much
better than O(n²) brute force. Let me code this."

[Codes while explaining]

"Time: O(n) - one pass. Space: O(n) - hash map stores at most n elements. Edge case:
if no solution, return None or empty list depending on requirements."

INTERVIEWER EVALUATION: ✓ STRONG HIRE
- Explained brute force and why it's bad
- Justified hash map choice with complexity
- Coded correctly while talking
- Mentioned complexity without prompt
- Thought about edge cases

───────────────────────────────────────────────────────────────────────

WEAK CANDIDATE NARRATION:
"Um, I think I need to find two numbers that add up to target. So... I'll use two for
loops to check all pairs?"

[Writes nested loops]

INTERVIEWER: "Can you optimize this?"

WEAK CANDIDATE:
"Maybe... sort the array first?"

INTERVIEWER EVALUATION: ✗ NO HIRE
- Went straight to O(n²) solution
- Didn't consider hash map
- Suggested sorting (doesn't help for indices problem)
- Lacks fundamental algorithm knowledge

───────────────────────────────────────────────────────────────────────

RED-FLAG PHRASES THAT CAUSE IMMEDIATE REJECTION:
─────────────────────────────────────────────────
❌ "Why would I use a dictionary for this?"
❌ "Can I just use nested loops?"
❌ "I don't know what O(1) lookup means"
❌ [Doesn't mention hash map for Two Sum]
❌ "Dict and list are the same speed, right?"
❌ [Takes > 5 minutes to code Two Sum]

STRONG SIGNALS (Gets you hired):
─────────────────────────────────
✓ "Hash map gives O(1) lookup, so..."
✓ "I'll use dict.get(key, 0) to avoid KeyError..."
✓ "This reduces complexity from O(n²) to O(n)..."
✓ "defaultdict(list) is cleaner than manual checking..."
✓ "Counter.most_common() simplifies this..."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ═══════════════════════════════════════════════════════════════════════
# 5️⃣ LIVE CODING EXPECTATIONS
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROBLEM: Longest Substring Without Repeating Characters
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Given string, find length of longest substring without repeating characters.
Example: "abcabcbb" → 3 (substring "abc")

───────────────────────────────────────────────────────────────────────
APPROACH 1: BRUTE FORCE (What weak candidates do)
───────────────────────────────────────────────────────────────────────
def longest_substring_brute(s):
    '''
    Check all substrings, verify no duplicates
    
    TIME: O(n³) - O(n²) substrings, O(n) to check each
    SPACE: O(min(n, m)) where m = charset size
    
    INTERVIEWER REACTION: ✗ "Can you do better?"
    '''
    max_len = 0
    n = len(s)
    
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            if len(substring) == len(set(substring)):  # No dups
                max_len = max(max_len, j - i + 1)
    
    return max_len

───────────────────────────────────────────────────────────────────────
APPROACH 2: SLIDING WINDOW WITH SET (What strong candidates do)
───────────────────────────────────────────────────────────────────────
def longest_substring_sliding_window(s):
    '''
    Sliding window + hash set for O(1) duplicate checking
    
    KEY INSIGHT: When we find duplicate, shrink window from left
    until duplicate is removed.
    
    TIME: O(n) - each character visited at most twice
    SPACE: O(min(n, m)) - set stores unique chars in window
    
    INTERVIEWER REACTION: ✓ "Good, any optimization?"
    '''
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

───────────────────────────────────────────────────────────────────────
APPROACH 3: OPTIMIZED SLIDING WINDOW WITH DICT (What senior candidates do)
───────────────────────────────────────────────────────────────────────
def longest_substring_optimized(s):
    '''
    Use dict to store last seen index of each character.
    When duplicate found, jump left pointer directly.
    
    TIME: O(n) - single pass, no inner while loop
    SPACE: O(min(n, m))
    
    INTERVIEWER REACTION: ✓ STRONG HIRE "Perfect!"
    '''
    char_index = {}  # char -> last seen index
    left = 0
    max_len = 0
    
    for right, char in enumerate(s):
        # If char seen and within current window, move left past it
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        
        char_index[char] = right
        max_len = max(max_len, right - left + 1)
    
    return max_len

───────────────────────────────────────────────────────────────────────
FINAL INTERVIEW-SAFE SOLUTION (Complete with narration)
───────────────────────────────────────────────────────────────────────

def longest_unique_substring(s):
    '''
    Find length of longest substring without repeating characters.
    
    Approach: Sliding window with hash map
    - right pointer expands window
    - left pointer shrinks when duplicate found
    - hash map tracks last seen index of each character
    
    When we encounter a character we've seen before within current window,
    we move left pointer just past previous occurrence.
    
    Time: O(n) - single pass through string
    Space: O(min(n, m)) - m is charset size (26 for lowercase, 128 for ASCII)
    
    Args:
        s: str, input string
    
    Returns:
        int: length of longest substring with unique characters
    '''
    if not s:
        return 0
    
    char_index = {}  # Maps character to its last seen index
    left = 0
    max_length = 0
    
    for right, char in enumerate(s):
        # If character seen before AND within current window
        if char in char_index and char_index[char] >= left:
            # Move left pointer just past previous occurrence
            left = char_index[char] + 1
        
        # Update last seen index
        char_index[char] = right
        
        # Update max length
        max_length = max(max_length, right - left + 1)
    
    return max_length


# Test cases (what strong candidates do unprompted)
def test_longest_unique():
    assert longest_unique_substring("abcabcbb") == 3  # "abc"
    assert longest_unique_substring("bbbbb") == 1  # "b"
    assert longest_unique_substring("pwwkew") == 3  # "wke"
    assert longest_unique_substring("") == 0  # empty
    assert longest_unique_substring("a") == 1  # single char
    assert longest_unique_substring("abcdef") == 6  # all unique
    print("✓ All tests pass")

───────────────────────────────────────────────────────────────────────
COMMON MISTAKES (Seen in real interviews)
───────────────────────────────────────────────────────────────────────

❌ MISTAKE 1: Not handling char_index[char] < left case
```
# Wrong: Doesn't check if char is in current window
if char in char_index:
    left = char_index[char] + 1  # Bug! Might jump left backwards
```

❌ MISTAKE 2: Using set instead of dict for optimization
```
# Less optimal: Still needs while loop to find char to remove
while s[right] in char_set:
    char_set.remove(s[left])
    left += 1
```

❌ MISTAKE 3: Not handling empty string
```
# Crashes on empty input
char_index = {}
for right, char in enumerate(s):  # Works fine on ""
    ...
# Actually this is fine, but candidate should explicitly check
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ═══════════════════════════════════════════════════════════════════════
# 6️⃣ PATTERN RECOGNITION (MANDATORY)
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PATTERN MAPPING FOR DICTIONARIES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PATTERN 1: HASH MAP FOR COMPLEMENT FINDING
═══════════════════════════════════════════

SIGNAL PHRASES:
- "find two elements that sum/multiply to..."
- "pair of elements"
- "check if complement exists"

TEMPLATE:
```
def hash_complement_template(arr, target):
    seen = {}
    for i, val in enumerate(arr):
        complement = target - val  # or target / val, etc.
        if complement in seen:
            return (seen[complement], i)
        seen[val] = i
```

INTERVIEWER EXPECTS YOU TO SAY:
"I see we need to find pairs that satisfy a condition. Instead of nested loops (O(n²)),
I'll use a hash map to store values we've seen. For each element, I check if its
complement exists in the map in O(1) time. Total: O(n) time, O(n) space."

EXAMPLE PROBLEMS:
• Two Sum
• Four Sum
• Pair with Given Difference
• Check if pair exists

───────────────────────────────────────────────────────────────────────

PATTERN 2: FREQUENCY COUNTING
══════════════════════════════

SIGNAL PHRASES:
- "count occurrences"
- "frequency of..."
- "most frequent"
- "anagram"

TEMPLATE:
```
from collections import Counter

def frequency_template(items):
    freq = Counter(items)
    # OR manual: freq = {}; for item in items: freq[item] = freq.get(item, 0) + 1
    return freq
```

INTERVIEWER EXPECTS YOU TO SAY:
"This requires counting frequencies. I'll use Counter from collections, which is
purpose-built for this. It's a specialized dict that counts hashable objects. O(n)
time to build, O(1) to query."

EXAMPLE PROBLEMS:
• Valid Anagram
• Group Anagrams
• Top K Frequent Elements
• First Unique Character
• Sort Characters By Frequency

───────────────────────────────────────────────────────────────────────

PATTERN 3: SLIDING WINDOW + FREQUENCY MAP
══════════════════════════════════════════

SIGNAL PHRASES:
- "substring with..."
- "contiguous subarray where..."
- "window of..."
- "at most k distinct..."

TEMPLATE:
```
from collections import defaultdict

def sliding_window_template(s, k):
    char_freq = defaultdict(int)
    left = 0
    result = 0
    
    for right in range(len(s)):
        char_freq[s[right]] += 1
        
        while window_invalid(char_freq, k):
            char_freq[s[left]] -= 1
            if char_freq[s[left]] == 0:
                del char_freq[s[left]]
            left += 1
        
        result = max(result, right - left + 1)
    
    return result
```

INTERVIEWER EXPECTS YOU TO SAY:
"Substring problem signals sliding window. I'll maintain a frequency map of characters
in current window. Expand right to grow window, shrink left when condition violated.
Dict tracks character counts for O(1) validity checks. Time: O(n), Space: O(k) where
k is distinct chars."

EXAMPLE PROBLEMS:
• Longest Substring Without Repeating Characters
• Longest Substring with At Most K Distinct Characters
• Minimum Window Substring
• Permutation in String
• Find All Anagrams

───────────────────────────────────────────────────────────────────────

PATTERN 4: GROUPING / BUCKETING
════════════════════════════════

SIGNAL PHRASES:
- "group by..."
- "categorize..."
- "partition based on..."

TEMPLATE:
```
from collections import defaultdict

def grouping_template(items):
    groups = defaultdict(list)
    for item in items:
        key = compute_key(item)  # Define grouping criteria
        groups[key].append(item)
    return list(groups.values())
```

INTERVIEWER EXPECTS YOU TO SAY:
"Need to group items by some property. I'll use defaultdict(list) which auto-initializes
empty lists for new keys. Compute a hashable key for each item (like sorted string for
anagrams), use as dict key. O(n*k) time where k is key computation cost."

EXAMPLE PROBLEMS:
• Group Anagrams
• Group Shifted Strings
• Group Numbers by Sign

───────────────────────────────────────────────────────────────────────

PATTERN 5: PREFIX SUM / SUBARRAY SUM
═════════════════════════════════════

SIGNAL PHRASES:
- "subarray that sums to..."
- "continuous subarray"
- "cumulative sum"

TEMPLATE:
```
def subarray_sum_template(nums, target):
    prefix_sum = 0
    sum_freq = {0: 1}  # Base case: empty prefix
    count = 0
    
    for num in nums:
        prefix_sum += num
        if prefix_sum - target in sum_freq:
            count += sum_freq[prefix_sum - target]
        sum_freq[prefix_sum] = sum_freq.get(prefix_sum, 0) + 1
    
    return count
```

INTERVIEWER EXPECTS YOU TO SAY:
"This is prefix sum pattern. Key insight: if prefix_sum[i] - prefix_sum[j] = target,
then subarray from j+1 to i sums to target. I'll store prefix sums in hash map, check
if (current_sum - target) exists. O(n) time, O(n) space."

EXAMPLE PROBLEMS:
• Subarray Sum Equals K
• Continuous Subarray Sum
• Maximum Size Subarray Sum Equals k

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ═══════════════════════════════════════════════════════════════════════
# 7️⃣ COMMON INTERVIEW FAILURE MODES
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DICTIONARY-SPECIFIC FAILURES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FAILURE #1: NOT USING get() WITH DEFAULT
═════════════════════════════════════════

❌ WHAT WEAK CANDIDATES WRITE:
```
freq = {}
for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
```

INTERVIEWER THINKING: "Doesn't know basic Python idioms. This is verbose and slow."

✓ WHAT STRONG CANDIDATES WRITE:
```
freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1

# OR even better
from collections import Counter
freq = Counter(s)
```

───────────────────────────────────────────────────────────────────────

FAILURE #2: USING NESTED LOOPS FOR TWO SUM
═══════════════════════════════════════════

❌ WHAT WEAK CANDIDATES DO:
```
def two_sum_slow(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
```

INTERVIEWER THINKING: "Doesn't understand hash tables. Basic algorithm failure."

✓ WHAT STRONG CANDIDATES DO:
```
def two_sum_fast(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
```

CRITICAL: If candidate can't optimize this to O(n), it's a NO HIRE.

───────────────────────────────────────────────────────────────────────

FAILURE #3: INCORRECT COMPLEXITY CLAIMS
════════════════════════════════════════

❌ WEAK CANDIDATE SAYS:
"Hash maps are O(1) for everything, right? So my solution is O(1)."

INTERVIEWER: "What if you're iterating through the map?"

WEAK CANDIDATE: "Oh... then it's O(n)? But the lookups are still O(1)..."

✓ STRONG CANDIDATE SAYS:
"Dictionary lookup is O(1) average case. My solution iterates through n elements,
doing O(1) lookup for each, so total time is O(n). Space is O(n) for the dictionary
storing up to n key-value pairs."

───────────────────────────────────────────────────────────────────────

FAILURE #4: TRYING TO USE UNHASHABLE TYPES AS KEYS
═══════════════════════════════════════════════════

❌ WHAT WEAK CANDIDATES TRY:
```
cache = {}
cache[[1, 2, 3]] = "value"  # TypeError: unhashable type: 'list'
```

INTERVIEWER: "Why doesn't this work?"

WEAK CANDIDATE: "I don't know, Python is weird?"

✓ STRONG CANDIDATE EXPLAINS:
"Lists are mutable and unhashable - can't be dict keys. I'll convert to tuple which
is immutable: cache[tuple([1,2,3])] = 'value'. Only immutable types can be keys:
int, str, tuple work. List, dict, set don't."

───────────────────────────────────────────────────────────────────────

FAILURE #5: NOT KNOWING WHEN TO USE DICT VS SET VS LIST
════════════════════════════════════════════════════════

❌ WEAK CANDIDATE:
Problem: "Check if array contains duplicates"
```
def has_duplicates(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False
```

INTERVIEWER THINKING: "O(n²) for a problem that should be O(n). Doesn't understand
data structures."

✓ STRONG CANDIDATE:
```
def has_duplicates(arr):
    return len(arr) != len(set(arr))  # O(n)
    # OR: seen = set(); check if num in seen for each num
```

───────────────────────────────────────────────────────────────────────

FAILURE #6: NOT KNOWING COLLECTIONS MODULE
═══════════════════════════════════════════

❌ WEAK CANDIDATE:
Writes 10 lines of manual frequency counting, grouping, etc.

✓ STRONG CANDIDATE:
"I'll use Counter from collections for frequency counting."
"I'll use defaultdict(list) for grouping."

INTERVIEWER THINKING: If candidate doesn't know collections module for 5+ YOE
position, that's concerning.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ═══════════════════════════════════════════════════════════════════════
# 8️⃣ MOCK INTERVIEW ROUND
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REALISTIC INTERVIEW: DICTIONARIES FOCUS (45 minutes)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEWER: "Let's assess your Python fundamentals."

───────────────────────────────────────────────────────────────────────
RAPID-FIRE ROUND (3 minutes) - MUST get all correct
───────────────────────────────────────────────────────────────────────

Q1: "What's the average time complexity of dict lookup?"
EXPECTED: "O(1) average case, O(n) worst case with collisions"

Q2: "How do you safely increment a counter for a key that might not exist?"
EXPECTED: "dict[key] = dict.get(key, 0) + 1"

Q3: "What's wrong with using a list as a dictionary key?"
EXPECTED: "Lists are unhashable - only immutable types can be keys"

Q4: "Name two specialized dictionary types from collections module."
EXPECTED: "Counter and defaultdict" [OrderedDict also acceptable]

Q5: "Code Two Sum in 30 seconds." [Timer starts]
EXPECTED: [Must produce working code in < 1 minute]

SCORE: < 4/5 correct = STRONG REJECTION SIGNAL

───────────────────────────────────────────────────────────────────────
MAIN PROBLEM (30 minutes)
───────────────────────────────────────────────────────────────────────

INTERVIEWER: "Given an array of integers and an integer k, return the k most frequent
elements. You may return the answer in any order."

Example: nums = [1,1,1,2,2,3], k = 2 → [1,2]

[Pause for clarifying questions]

STRONG CANDIDATE ASKS:
- "Can k be larger than number of unique elements?"
- "What if multiple elements have same frequency?"
- "Any constraints on array size?"

WEAK CANDIDATE:
[Starts coding immediately]

───────────────────────────────────────────────────────────────────────

STRONG CANDIDATE THINKS ALOUD:
"This is a frequency counting + top k problem. I see three approaches:

1. Count frequencies, sort by frequency, return top k: O(n log n)
2. Count frequencies, use heap to maintain top k: O(n log k)
3. Count frequencies, use bucket sort: O(n)

For interview, I'll use Counter with most_common() - clean and O(n log k). Unless you
want me to optimize to O(n) with bucket sort?"

INTERVIEWER: "Counter with most_common is fine. Go ahead."

STRONG CANDIDATE CODES:
```
def top_k_frequent(nums, k):
    '''
    Find k most frequent elements.
    
    Approach: Counter + most_common()
    - Counter counts in O(n)
    - most_common(k) uses heap, O(n log k)
    - Total: O(n log k)
    
    Time: O(n log k)
    Space: O(n) for counter
    '''
    from collections import Counter
    
    # Count frequencies
    freq = Counter(nums)
    
    # Get top k
    # most_common returns [(element, count), ...]
    top_k = freq.most_common(k)
    
    # Extract just elements
    return [element for element, count in top_k]
```

───────────────────────────────────────────────────────────────────────
PRESSURE FOLLOW-UPS (While coding)
───────────────────────────────────────────────────────────────────────

INTERVIEWER: [Interrupts] "What if k is larger than unique elements?"
STRONG: "most_common(k) returns all elements if k exceeds count. No error."

INTERVIEWER: "Can you optimize to O(n) time?"
STRONG: "Yes, bucket sort. Create array of size n+1, where index = frequency.
Place elements in buckets. Iterate from end to collect top k. But Counter solution
is cleaner for interviews unless specifically asked."

INTERVIEWER: "What's space complexity?"
STRONG: "O(n) for Counter storing up to n unique elements. Bucket sort would also
be O(n) space."

───────────────────────────────────────────────────────────────────────
OPTIMIZATION CHALLENGE
───────────────────────────────────────────────────────────────────────

INTERVIEWER: "Code the O(n) bucket sort solution."

STRONG CANDIDATE:
```
def top_k_frequent_optimal(nums, k):
    '''
    O(n) time using bucket sort
    '''
    from collections import Counter
    
    freq = Counter(nums)
    
    # Bucket sort: index = frequency
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, count in freq.items():
        buckets[count].append(num)
    
    # Collect top k from highest frequency
    result = []
    for i in range(len(buckets) - 1, 0, -1):
        result.extend(buckets[i])
        if len(result) >= k:
            return result[:k]
    
    return result
```

WEAK CANDIDATE:
[Struggles, can't implement bucket sort correctly]

───────────────────────────────────────────────────────────────────────
FINAL DECISION
───────────────────────────────────────────────────────────────────────

STRONG HIRE:
✓ Aced rapid-fire (5/5)
✓ Proposed multiple approaches with trade-offs
✓ Clean working solution
✓ Handled all follow-ups
✓ Could code O(n) optimization when asked

HIRE:
✓ Good rapid-fire (4/5)
✓ Working solution with Counter
✓ Explained complexity correctly
✓ Struggled with bucket sort but got there with hints

NO HIRE:
✗ Rapid-fire < 4/5
✗ Didn't think of Counter
✗ Used nested loops or inefficient sorting
✗ Couldn't optimize when asked

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ═══════════════════════════════════════════════════════════════════════
# 9️⃣ SELF-ASSESSMENT CHECK
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SELF-ASSESSMENT: DICTIONARY MASTERY CHECK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TIER 1: CRITICAL (Must get 8/8 or you're NOT ready)
════════════════════════════════════════════════════
□ Can code Two Sum with dict in under 3 minutes
□ Explain why dict is O(1) lookup vs list O(n)
□ Know when to use get(key, default) vs direct access
□ Understand defaultdict and when to use it
□ Know Counter and most_common()
□ Iterate with items() for key-value pairs
□ Explain why lists can't be dict keys
□ Recognize "find pair that..." signals hash map

TIER 2: IMPORTANT (Should get 6/7+)
════════════════════════════════════
□ Use dict to optimize O(n²) to O(n)
□ Group anagrams with dict + sorted key
□ Handle modifying dict during iteration
□ Know difference between keys(), values(), items()
□ Understand hash collisions conceptually
□ Use sliding window + dict for substring problems
□ Know when Counter is cleaner than manual dict

TIER 3: ADVANCED (Bonus for 3/4+)
══════════════════════════════════
□ Explain dict insertion order (Python 3.7+)
□ Know when to use OrderedDict vs regular dict
□ Understand dict comprehensions
□ Optimize with bucket sort for frequency problems

───────────────────────────────────────────────────────────────────────
CRITICAL CHECKPOINT:
───────────────────────────────────────────────────────────────────────

Can you code these in under 5 minutes each?
1. Two Sum
2. Group Anagrams
3. Top K Frequent Elements

If NO to any of these → NOT READY FOR INTERVIEWS

───────────────────────────────────────────────────────────────────────
INTERVIEWER CONCLUSION:
───────────────────────────────────────────────────────────────────────

TIER 1 < 8/8:
"Critical failure. Can't code Two Sum or doesn't understand hash tables. This is
disqualifying for 5+ YOE. STRONG REJECT."

TIER 1 = 8/8, TIER 2 < 5/7:
"Knows basics but weak on patterns. Might struggle with medium problems. LEAN NO HIRE."

TIER 1 = 8/8, TIER 2 >= 6/7:
"Solid dictionary knowledge. Can solve most hash map problems. HIRE."

All tiers strong + can code 3 critical problems quickly:
"Excellent hash map mastery. Ready for senior+ roles. STRONG HIRE."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

HARSH TRUTH:
If you can't code Two Sum with a dictionary in 3 minutes, you will FAIL 70% of
Python interviews. This is THE gateway problem. Master it or don't bother applying.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ═══════════════════════════════════════════════════════════════════════
# FINAL MANDATE
# ═══════════════════════════════════════════════════════════════════════

"""
Dictionaries are THE most important Python data structure for interviews.
If you only master one file, master this one.

70% of problems become trivial with correct hash map usage.

Review until you can:
- Code Two Sum instantly
- Recognize hash map opportunities immediately
- Use Counter and defaultdict naturally
- Explain O(n²) → O(n) optimization confidently

This is not negotiable for 5+ YOE positions.
"""
