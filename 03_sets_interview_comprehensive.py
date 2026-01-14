"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 PYTHON SETS - SENIOR ENGINEER INTERVIEW PREPARATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Interviewer: Senior Engineer | Bar-Raiser
Candidate Level: 5+ Years Experience
Purpose: O(1) Lookup Mastery - Critical for Optimization
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣ FILE INTERVIEW OVERVIEW
═══════════════════════════════════════════════════════════════════════

WHY SETS ARE CRITICAL:
Sets appear when you need O(1) membership testing. Key use cases:
• Duplicate detection
• Visited tracking (graphs, grids)
• Intersection/Union problems
• Optimizing O(n) → O(1) lookups
• Set theory operations

WHAT INTERVIEWERS EXPECT:
✓ Know O(1) lookup vs list's O(n)
✓ Use sets for "seen" tracking
✓ Understand hashability constraints
✓ Set operations (union, intersection, difference)
✓ Recognize when set beats list

MUST-KNOW:
• add(), remove(), discard()
• x in set → O(1)
• Union (|), Intersection (&), Difference (-)
• Hashable types only
• Set comprehension

STRONG vs WEAK SIGNALS:
STRONG: Uses set for duplicate detection immediately
WEAK: Nested loops or list.count() for membership

AUTOMATIC REJECTION:
❌ Uses list when set clearly better
❌ Doesn't know O(1) vs O(n) lookup
❌ Tries to add unhashable types
❌ Can't code "contains duplicate" in 1 minute

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

2️⃣ CONCEPT CLASSIFICATION
═══════════════════════════════════════════════════════════════════════

╔════════════════════╦═════════════╦══════════════════════════════════╗
║ CONCEPT            ║ FREQUENCY   ║ WHY TESTED / REJECTION REASONS   ║
╠════════════════════╬═════════════╬══════════════════════════════════╣
║ x in set (O(1))    ║ HIGH        ║ Core optimization technique      ║
║                    ║             ║ REJECT: Uses list for membership ║
╠════════════════════╬═════════════╬══════════════════════════════════╣
║ Duplicate detection║ HIGH        ║ len(arr) != len(set(arr))        ║
║                    ║             ║ REJECT: Nested loops O(n²)       ║
╠════════════════════╬═════════════╬══════════════════════════════════╣
║ Visited tracking   ║ HIGH        ║ Graph BFS/DFS, grid problems     ║
║                    ║             ║ REJECT: Uses list, O(n) checks   ║
╠════════════════════╬═════════════╬══════════════════════════════════╣
║ Set operations     ║ MEDIUM      ║ Union, intersection, difference  ║
║                    ║             ║ REJECT: Manual loops             ║
╠════════════════════╬═════════════╬══════════════════════════════════╣
║ Hashability        ║ MEDIUM      ║ Can't add lists/dicts            ║
║                    ║             ║ REJECT: Doesn't understand why   ║
╠════════════════════╬═════════════╬══════════════════════════════════╣
║ remove vs discard  ║ LOW         ║ Safe removal pattern             ║
╚════════════════════╩═════════════╩══════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

3️⃣ INTERVIEW QUESTIONS
═══════════════════════════════════════════════════════════════════════

SECTION 3A: O(1) LOOKUP (HIGH FREQUENCY - CRITICAL)
────────────────────────────────────────────────────

① WARM-UP: Why set over list for membership?
EXPECTED: "List membership is O(n) - scans entire list. Set uses hash table for O(1)
average case. For 'if x in container' checks, always use set."

② CORE: Contains Duplicate. Return True if any value appears twice.
def contains_duplicate(nums):
    return len(nums) != len(set(nums))  # O(n) time, O(n) space

INTERVIEWER TESTS: Can you code this in 30 seconds?
✓ STRONG: Instant one-liner
✗ WEAK: Nested loops O(n²)

③ EDGE-CASE: What if input has unhashable types like lists?
EXPECTED: "Can't create set of lists - TypeError. Would need to convert to tuples or
use different approach. Sets require hashable (immutable) elements."

④ FOLLOW-UP: Find if any value appears exactly k times.
def has_k_frequency(nums, k):
    from collections import Counter
    return k in Counter(nums).values()

SECTION 3B: VISITED TRACKING (HIGH FREQUENCY)
─────────────────────────────────────────────

① WARM-UP: Why use set for visited cells in grid?
EXPECTED: "Need O(1) lookup to check if cell visited. Set of (row, col) tuples gives
this. List would be O(n) per check."

② CORE: Number of Islands (BFS with visited set)
def num_islands(grid):
    if not grid: return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    count = 0
    
    def bfs(r, c):
        queue = [(r, c)]
        visited.add((r, c))
        
        while queue:
            row, col = queue.pop(0)
            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                nr, nc = row+dr, col+dc
                if (0 <= nr < rows and 0 <= nc < cols and 
                    grid[nr][nc] == '1' and (nr,nc) not in visited):
                    queue.append((nr, nc))
                    visited.add((nr, nc))
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r,c) not in visited:
                bfs(r, c)
                count += 1
    
    return count

INTERVIEWER EXPECTS: Set of tuples, O(1) membership check
✓ STRONG: Uses set((r,c))
✗ WEAK: Modifies grid or uses list

③ EDGE-CASE: Can you use list instead of set here?
EXPECTED: "Could use list, but (r,c) in visited would be O(n) per check. For large
grids, this degrades to O(n²) total. Set keeps it O(n)."

④ FOLLOW-UP: What if coordinates are 3D (x,y,z)?
EXPECTED: "Same approach - set of 3-tuples (x,y,z). Still O(1) per check."

SECTION 3C: SET OPERATIONS (MEDIUM FREQUENCY)
──────────────────────────────────────────────

① WARM-UP: What are the 4 main set operations?
EXPECTED: "Union (A|B), Intersection (A&B), Difference (A-B), Symmetric Diff (A^B)"

② CORE: Find intersection of two arrays.
def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))  # O(n+m)

INTERVIEWER EXPECTS: Use & operator or intersection()
✓ STRONG: One-liner with & 
✗ WEAK: Nested loops

③ EDGE-CASE: Array intersection WITH duplicates counted.
EXPECTED: "Set loses count. Need Counter or dict instead:
from collections import Counter
c1, c2 = Counter(nums1), Counter(nums2)
return [x for x in c1 if x in c2] * min(c1[x], c2[x])"

④ FOLLOW-UP: Union of k arrays.
def union_k_arrays(arrays):
    result = set()
    for arr in arrays:
        result |= set(arr)  # Union update
    return list(result)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

4️⃣ THINK-ALOUD ANSWERS
═══════════════════════════════════════════════════════════════════════

PROBLEM: Contains Duplicate

STRONG CANDIDATE:
"This asks if any value appears twice. I could use nested loops to check all pairs -
that's O(n²). Better: convert to set and compare lengths. If array has duplicates,
set will be smaller because sets only store unique values. This is O(n) time to create
set, O(1) to compare lengths. One-liner: return len(nums) != len(set(nums))"

INTERVIEWER: ✓ HIRE - Explained optimization, coded instantly

WEAK CANDIDATE:
"I'll use two for loops to check every pair..."
[Codes O(n²) solution]

INTERVIEWER: "Can you optimize?"
WEAK: "Um... sort first?" [Still O(n log n), misses O(n) solution]

INTERVIEWER: ✗ NO HIRE - Doesn't understand hash table advantage

RED FLAGS:
❌ "Why not just use a list?"
❌ Can't code in 1 minute
❌ Suggests O(n²) or O(n log n) first

STRONG SIGNALS:
✓ "Set for O(1) lookup..."
✓ Mentions hash table advantage
✓ Instant one-liner solution

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

5️⃣ LIVE CODING EXPECTATIONS
═══════════════════════════════════════════════════════════════════════

PROBLEM: Longest Consecutive Sequence
Given unsorted array, find length of longest consecutive sequence.
[100, 4, 200, 1, 3, 2] → 4 (sequence [1, 2, 3, 4])

BRUTE FORCE (❌ O(n log n)):
def longest_consecutive_brute(nums):
    if not nums: return 0
    nums.sort()  # O(n log n)
    longest = 1
    current = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            current += 1
        elif nums[i] != nums[i-1]:
            longest = max(longest, current)
            current = 1
    return max(longest, current)

OPTIMAL (✓ O(n) with set):
def longest_consecutive_optimal(nums):
    '''
    Use set for O(1) lookup. Key insight: only start counting from
    sequence START (when num-1 not in set). This avoids recounting.
    
    Time: O(n) - each number visited at most twice
    Space: O(n) - set storage
    '''
    if not nums: return 0
    
    num_set = set(nums)
    longest = 0
    
    for num in num_set:
        # Only count from sequence start
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            
            longest = max(longest, current_streak)
    
    return longest

INTERVIEWER EVALUATION:
✓ STRONG HIRE: Codes O(n) solution with set immediately
✓ HIRE: Gets to O(n) with hints
✗ NO HIRE: Only codes O(n log n) solution

COMMON MISTAKES:
❌ Forgets "only start from sequence beginning" optimization
❌ Uses list instead of set → O(n²)
❌ Doesn't handle edge cases (empty, single element)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

6️⃣ PATTERN RECOGNITION
═══════════════════════════════════════════════════════════════════════

PATTERN: MEMBERSHIP TESTING OPTIMIZATION
─────────────────────────────────────────

SIGNAL: "Check if X exists", "Find if...", "Contains..."

TEMPLATE:
seen = set()
for item in items:
    if item in seen:  # O(1) with set
        return True
    seen.add(item)

PROBLEMS:
• Contains Duplicate
• Two Sum (complement in seen)
• Linked List Cycle
• Happy Number

PATTERN: VISITED TRACKING (GRAPHS/GRIDS)
─────────────────────────────────────────

SIGNAL: "Explore grid", "Traverse graph", "Mark visited"

TEMPLATE:
visited = set()
def dfs(node):
    if node in visited: return
    visited.add(node)
    for neighbor in graph[node]:
        dfs(neighbor)

PROBLEMS:
• Number of Islands
• Surrounded Regions
• Word Search
• Graph Valid Tree

PATTERN: SET THEORY OPERATIONS
───────────────────────────────

SIGNAL: "Common elements", "Unique to...", "Union/Intersection"

TEMPLATE:
set_a = set(list_a)
set_b = set(list_b)
intersection = set_a & set_b
union = set_a | set_b
difference = set_a - set_b

PROBLEMS:
• Intersection of Two Arrays
• Find Missing Number
• Single Number

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

7️⃣ COMMON FAILURES
═══════════════════════════════════════════════════════════════════════

FAILURE #1: USING LIST FOR MEMBERSHIP
❌ if x in my_list:  # O(n) each check!
✓ if x in my_set:   # O(1)

FAILURE #2: NOT RECOGNIZING SET OPPORTUNITY  
❌ for i in range(len(arr)):
       for j in range(i+1, len(arr)):
           if arr[i] == arr[j]: return True
✓ return len(arr) != len(set(arr))

FAILURE #3: TRYING TO ADD UNHASHABLE
❌ my_set.add([1, 2])  # TypeError!
✓ my_set.add((1, 2))  # Use tuple

FAILURE #4: EXPECTING ORDER
❌ Assuming sets maintain insertion order
✓ Sets are unordered (use list if order matters)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

8️⃣ MOCK INTERVIEW
═══════════════════════════════════════════════════════════════════════

RAPID-FIRE (2 minutes):

Q1: "Time complexity of x in set?"
A: "O(1) average, O(n) worst case with collisions"

Q2: "How to check for duplicates in O(n)?"
A: "len(arr) != len(set(arr))"

Q3: "Can you add a list to a set?"
A: "No, lists are unhashable. Use tuple."

Q4: "Set vs list for 'visited' tracking?"
A: "Set - O(1) lookup vs list's O(n)"

Q5: "Code contains duplicate NOW."
[Must code in < 30 seconds]

MAIN PROBLEM (20 minutes):

"Given two arrays, return their intersection. Each element must appear as many times
as it shows in both arrays."

Example: nums1 = [1,2,2,1], nums2 = [2,2] → [2,2]

STRONG CANDIDATE:
"Sets lose count info. Need Counter:
from collections import Counter
c1, c2 = Counter(nums1), Counter(nums2)
result = []
for num in c1:
    if num in c2:
        result.extend([num] * min(c1[num], c2[num]))
return result"

DECISION:
✓ 4/5 rapid-fire + working solution = HIRE
✗ <3/5 rapid-fire or no solution = NO HIRE

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

9️⃣ SELF-ASSESSMENT
═══════════════════════════════════════════════════════════════════════

TIER 1: MUST KNOW (7/7 required)
─────────────────────────────────
□ Explain O(1) vs O(n) lookup
□ Code contains duplicate in 30 seconds
□ Use set for visited tracking
□ Know hashability constraint
□ Set comprehension syntax
□ When set beats list/dict
□ Union, intersection, difference operators

TIER 2: SHOULD KNOW (5/6)
──────────────────────────
□ Longest consecutive sequence with set
□ remove() vs discard()
□ Set operations with multiple sets
□ issubset(), issuperset()
□ Frozen set for dict keys
□ Set vs dict - when to use which

SCORING:
────────
TIER 1 < 7/7: NOT READY - Critical gaps
TIER 1 = 7/7, TIER 2 < 5/6: WEAK - Study more
TIER 1 = 7/7, TIER 2 >= 5/6: READY - Can interview

CRITICAL CHECKPOINT:
Can you code "Contains Duplicate" in under 30 seconds?
NO → Not ready for interviews

INTERVIEWER CONCLUSION:
TIER 1 < 7/7: "Doesn't understand O(1) lookup advantage. Basic DS failure. REJECT."
TIER 1 = 7/7: "Knows when to use sets. Can optimize membership checks. HIRE."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FINAL MANDATE:
If you don't immediately think "use a set" when you see membership testing,
you will lose performance points in 50% of interviews.

O(1) lookup is THE advantage. Master it or fail.
"""
