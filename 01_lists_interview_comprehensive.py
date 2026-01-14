"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 PYTHON LISTS - SENIOR ENGINEER INTERVIEW PREPARATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Interviewer: Senior Staff Engineer | Bar-Raiser | Python Expert
Candidate Level: 5+ Years Experience
Purpose: FILTER weak candidates, IDENTIFY strong ones
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

# ═══════════════════════════════════════════════════════════════════════
# 1️⃣ FILE INTERVIEW OVERVIEW
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHY LISTS ARE CRITICAL IN PYTHON INTERVIEWS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Lists appear in 90% of Python interviews. They're the foundation for:
• Array manipulation problems (Two Sum, Three Sum, etc.)
• Two pointers technique
• Sliding window algorithms
• In-place modification challenges
• Stack/Queue implementations
• Dynamic programming state storage

WHAT INTERVIEWERS EXPECT MASTERY OF:
────────────────────────────────────
✓ Slicing syntax (start:end:step) - instant recall required
✓ Mutability implications - reference vs copy behavior
✓ Time complexity of ALL operations (append, insert, pop, etc.)
✓ List comprehensions vs loops - when to use which
✓ Shallow vs deep copy - THIS IS A MAJOR TRAP
✓ In-place modification patterns

MUST-KNOW vs NICE-TO-KNOW:
──────────────────────────
MUST-KNOW (Will be tested):
  • append, extend, insert, pop, remove
  • Slicing and reverse slicing
  • sort() vs sorted()
  • List comprehensions
  • Two pointers pattern
  • In-place modification

NICE-TO-KNOW (Rarely tested directly):
  • clear(), count(), index() with bounds
  • copy.deepcopy() for nested structures

SIGNALS OF STRONG vs WEAK CANDIDATES:
─────────────────────────────────────
STRONG CANDIDATES:
  ✓ Immediately identify when to use list vs set vs dict
  ✓ Explain O(1) amortized append vs O(n) insert
  ✓ Use slicing naturally without hesitation
  ✓ Recognize two-pointer opportunities instantly
  ✓ Handle shallow copy traps correctly
  ✓ Write clean, Pythonic code with list comprehensions

WEAK CANDIDATES:
  ✗ Confuse append() with extend()
  ✗ Use remove() in loops (iterator invalidation)
  ✗ Don't understand that sort() returns None
  ✗ Create 2D arrays with [[0]*n]*m (shallow copy trap)
  ✗ Use O(n) operations when O(1) alternatives exist
  ✗ Silent coding - don't narrate thought process

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
║ Slicing [start:end:step]  HIGH      ║ Core Pythonic idiom             ║
║                        ║             ║ REJECT: Hesitates on [::-1]     ║
╠════════════════════════╬═════════════╬══════════════════════════════════╣
║ append() vs extend()   ║ HIGH        ║ Tests mutability understanding  ║
║                        ║             ║ REJECT: Confuses the two        ║
╠════════════════════════╬═════════════╬══════════════════════════════════╣
║ List comprehension     ║ HIGH        ║ Pythonic vs non-Pythonic code   ║
║                        ║             ║ REJECT: Always uses loops       ║
╠════════════════════════╬═════════════╬══════════════════════════════════╣
║ sort() vs sorted()     ║ HIGH        ║ In-place vs functional style    ║
║                        ║             ║ REJECT: Doesn't know sort()=None║
╠════════════════════════╬═════════════╬══════════════════════════════════╣
║ Shallow vs Deep copy   ║ HIGH        ║ Critical for 2D arrays/matrices ║
║                        ║             ║ REJECT: [[0]*n]*m trap          ║
╠════════════════════════╬═════════════╬══════════════════════════════════╣
║ Two pointers pattern   ║ HIGH        ║ Optimization technique          ║
║                        ║             ║ REJECT: Can't identify pattern  ║
╠════════════════════════╬═════════════╬══════════════════════════════════╣
║ In-place modification  ║ HIGH        ║ Space optimization              ║
║                        ║             ║ REJECT: Creates unnecessary copy║
╠════════════════════════╬═════════════╬══════════════════════════════════╣
║ pop() complexity       ║ MEDIUM      ║ Understands internal structure  ║
║                        ║             ║ REJECT: Says pop() is always O(1)║
╠════════════════════════╬═════════════╬══════════════════════════════════╣
║ remove() in loops      ║ MEDIUM      ║ Iterator invalidation awareness ║
║                        ║             ║ REJECT: Doesn't see the bug     ║
╠════════════════════════╬═════════════╬══════════════════════════════════╣
║ insert() complexity    ║ MEDIUM      ║ Array internals knowledge       ║
║                        ║             ║ REJECT: Claims O(1) for insert  ║
╠════════════════════════╬═════════════╬══════════════════════════════════╣
║ index(), count()       ║ LOW         ║ Basic search operations         ║
║                        ║             ║ REJECT: (Rarely disqualifying)  ║
╠════════════════════════╬═════════════╬══════════════════════════════════╣
║ clear()               ║ LOW         ║ Simple operation                ║
║                        ║             ║ REJECT: (Not tested directly)   ║
╚════════════════════════╩═════════════╩══════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ═══════════════════════════════════════════════════════════════════════
# 3️⃣ INTERVIEW QUESTIONS (CONTROLLED DENSITY)
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 3A: SLICING (HIGH FREQUENCY)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

① WARM-UP QUESTION: Syntax & Awareness
──────────────────────────────────────
Q: Given arr = [0,1,2,3,4,5,6,7,8,9], what does arr[2:7:2] return?
   What about arr[::-1]?

EXPECTED ANSWER:
"arr[2:7:2] starts at index 2, stops before 7, steps by 2, returning [2,4,6].
arr[::-1] reverses the entire list by stepping backwards, giving [9,8,7,6,5,4,3,2,1,0].
The slicing creates a NEW list; original is unchanged. Time: O(k) where k is slice length."

② CORE INTERVIEW QUESTION: Main Use Case
─────────────────────────────────────────
Q: Reverse the first half of an array in-place without using extra space.
   arr = [1,2,3,4,5,6,7,8,9,10]

THINK-ALOUD ANSWER:
"I need to reverse just the first half in-place. I'll use two pointers: left starting
at 0, right at len(arr)//2 - 1. Swap elements and move pointers inward. This is O(n/4)
swaps, O(1) space. Alternative: arr[:len(arr)//2] = arr[:len(arr)//2][::-1], but that
creates temporary list, so two-pointer is better for true in-place."

def reverse_first_half_inplace(arr):
    \"\"\"
    Interviewer expects: Two-pointer approach, O(1) space complexity narration
    \"\"\"
    mid = len(arr) // 2
    left, right = 0, mid - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]  # Pythonic swap
        left += 1
        right -= 1
    
    return arr  # Modified in-place

③ EDGE-CASE / TRAP QUESTION: Common Failure
────────────────────────────────────────────
Q: Debug this code. Why doesn't it work as expected?
   
   matrix = [[0] * 3] * 2
   matrix[0][0] = 1
   # Expected: [[1,0,0], [0,0,0]]
   # Actual: [[1,0,0], [1,0,0]]

EXPECTED ANSWER:
"This is the shallow copy trap. [[0]*3]*2 creates ONE list [0,0,0] and references it
twice. Modifying matrix[0][0] affects both rows because they point to the SAME list.
Correct approach: [[0]*3 for _ in range(2)] creates TWO separate lists."

INTERVIEWER EVALUATION:
✓ STRONG: Immediately identifies shallow copy, mentions object references
✗ WEAK: Says 'it's a bug in Python' or doesn't understand why

④ FOLLOW-UP OPTIMIZATION QUESTION
──────────────────────────────────
Q: Given sorted array, remove all elements less than k in-place. Optimize space.

THINK-ALOUD ANSWER:
"I'll use two pointers. Read pointer scans array, write pointer tracks where to place
next valid element. When arr[read] >= k, copy to arr[write] and increment write. Return
write as new length. This is O(n) time, O(1) space. Better than slicing which creates
new array."

def remove_less_than_k(arr, k):
    \"\"\"
    Interviewer tests: In-place awareness, two-pointer pattern recognition
    \"\"\"
    write = 0
    for read in range(len(arr)):
        if arr[read] >= k:
            arr[write] = arr[read]
            write += 1
    return write  # New length

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 3B: append() vs extend() (HIGH FREQUENCY)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

① WARM-UP QUESTION
──────────────────
Q: What's the difference between append([1,2]) and extend([1,2])?

EXPECTED ANSWER:
"append([1,2]) adds the LIST as a single element: [existing..., [1,2]].
extend([1,2]) adds EACH element: [existing..., 1, 2].
append is O(1), extend is O(k) where k=length of added iterable."

② CORE INTERVIEW QUESTION
─────────────────────────
Q: Flatten a list of lists. Given [[1,2],[3,4],[5,6]], return [1,2,3,4,5,6].

THINK-ALOUD ANSWER:
"I'll iterate through outer list, extend result with each inner list. extend() is
perfect here because it unpacks iterables. Time: O(n*m) where n=outer length, m=avg
inner length. Space: O(n*m) for result."

def flatten(nested):
    \"\"\"
    Interviewer expects: extend() usage, complexity analysis
    \"\"\"
    result = []
    for sublist in nested:
        result.extend(sublist)  # NOT append(sublist)
    return result

# Alternative: List comprehension (even better)
def flatten_pythonic(nested):
    return [item for sublist in nested for item in sublist]

③ EDGE-CASE / TRAP QUESTION
────────────────────────────
Q: Why does this produce unexpected output?
   
   result = []
   for i in range(3):
       result.append([i])
   # Expected one list with 3 elements?

EXPECTED ANSWER:
"This creates [[0], [1], [2]], a list of lists. If you wanted [0,1,2], should use
append(i) not append([i]). Common mistake: treating append like it unpacks iterables.
Only extend() unpacks."

④ FOLLOW-UP OPTIMIZATION
─────────────────────────
Q: Build a list of squares for numbers 0-999. What's the most Pythonic way?

EXPECTED ANSWER:
"List comprehension: [x**2 for x in range(1000)]. More Pythonic than loop with append().
Both are O(n), but comprehension is faster (optimized C loop) and more readable. Avoid:
result = []; for x in range(1000): result.append(x**2) - works but not Pythonic."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 3C: sort() vs sorted() (HIGH FREQUENCY)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

① WARM-UP QUESTION
──────────────────
Q: What does arr.sort() return? What about sorted(arr)?

EXPECTED ANSWER:
"arr.sort() sorts IN-PLACE and returns None. sorted(arr) returns a NEW sorted list,
original unchanged. Both are O(n log n) Timsort. In-place is O(1) space, sorted() is
O(n) space."

RED FLAG: Candidate writes result = arr.sort() and expects a sorted list.

② CORE INTERVIEW QUESTION
─────────────────────────
Q: Sort list of tuples [(1,5), (3,2), (2,8), (3,1)] by second element, then by
   first element if tied. How would you do this?

THINK-ALOUD ANSWER:
"I'll use sorted() with a key function. Python's sort is stable, so I can sort twice
OR use tuple key. Better: sorted(arr, key=lambda x: (x[1], x[0])) sorts by second
element primarily, first element as tiebreaker. Single pass, O(n log n)."

def sort_tuples_custom(arr):
    \"\"\"
    Interviewer expects: lambda usage, understanding of tuple comparison
    \"\"\"
    return sorted(arr, key=lambda x: (x[1], x[0]))
    # Returns: [(3,1), (3,2), (1,5), (2,8)]

③ EDGE-CASE / TRAP QUESTION
────────────────────────────
Q: Debug this code. Why doesn't it work?
   
   arr = [3, 1, 4, 1, 5]
   sorted_arr = arr.sort()
   print(sorted_arr)  # Prints None

EXPECTED ANSWER:
"arr.sort() returns None because it modifies in-place. Two fixes: (1) Use sorted(arr)
and assign result, or (2) Call arr.sort() on one line, use arr on next line. This is
a CLASSIC Python trap that catches non-Python developers."

INTERVIEWER EVALUATION:
✓ STRONG: Immediately says 'sort() returns None'
✗ WEAK: Confused why None appears, doesn't know Python semantics

④ FOLLOW-UP OPTIMIZATION
─────────────────────────
Q: Given unsorted array, find kth largest element. Can you optimize?

THINK-ALOUD ANSWER:
"Three approaches: (1) Sort entire array O(n log n), return arr[-k]. Simple but
overkill. (2) Use heapq.nlargest(k, arr)[-1], O(n log k). Best for small k. (3)
Quickselect O(n) average, but complex to implement. For interview, I'd use
heapq unless asked to optimize further."

import heapq

def kth_largest(arr, k):
    \"\"\"
    Interviewer tests: Knowledge of heapq, trade-off discussion
    \"\"\"
    return heapq.nlargest(k, arr)[-1]  # O(n log k)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 3D: SHALLOW vs DEEP COPY (HIGH FREQUENCY - MAJOR TRAP)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

① WARM-UP QUESTION
──────────────────
Q: What's the difference between arr[:], arr.copy(), and list(arr)?

EXPECTED ANSWER:
"All three create shallow copies. They copy the list structure but not nested objects.
For flat lists like [1,2,3], all are equivalent. For nested lists like [[1,2],[3,4]],
inner lists are still references. Need copy.deepcopy() for true independent copy."

② CORE INTERVIEW QUESTION
─────────────────────────
Q: Modify a 2D matrix without affecting the original. What's the correct approach?

THINK-ALOUD ANSWER:
"For 2D arrays, shallow copy is insufficient. matrix.copy() or matrix[:] only copies
outer list. Inner lists are still shared references. Must use copy.deepcopy(matrix)
OR rebuild with [[cell for cell in row] for row in matrix]. I prefer deepcopy for
clarity, comprehension for performance."

import copy

def modify_matrix_safely(matrix):
    \"\"\"
    Interviewer expects: Deep copy awareness, explaining why needed
    \"\"\"
    # Method 1: deepcopy (clearest)
    new_matrix = copy.deepcopy(matrix)
    
    # Method 2: List comprehension (faster for simple types)
    # new_matrix = [[cell for cell in row] for row in matrix]
    
    # Now safe to modify
    new_matrix[0][0] = 999
    return new_matrix

③ EDGE-CASE / TRAP QUESTION
────────────────────────────
Q: Why does this code have a bug?
   
   def create_board(n):
       row = [0] * n
       board = [row] * n  # Create n x n board
       return board
   
   board = create_board(3)
   board[0][0] = 1  # Set top-left
   # Bug: All rows change!

EXPECTED ANSWER:
"[row] * n creates n references to the SAME row object. Modifying any row affects all.
Correct: [[0]*n for _ in range(n)] creates n DISTINCT rows. This is interview gold -
if candidate misses this, it's a strong rejection signal."

INTERVIEWER EVALUATION:
✓ STRONG: Recognizes immediately, draws memory diagram if needed
✗ WEAK: Doesn't understand object references vs values

④ FOLLOW-UP OPTIMIZATION
─────────────────────────
Q: When is shallow copy sufficient vs when do you need deep copy?

EXPECTED ANSWER:
"Shallow copy is sufficient when: (1) List contains only immutable types (int, str,
tuple). (2) You won't modify nested structures. Deep copy needed when: (1) List
contains mutable nested structures (lists, dicts). (2) You need complete independence.
Trade-off: deepcopy is slower O(n*depth) vs shallow O(n), so use only when necessary."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 3E: LIST COMPREHENSION (HIGH FREQUENCY)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

① WARM-UP QUESTION
──────────────────
Q: Convert this loop to a list comprehension:
   
   result = []
   for x in range(10):
       if x % 2 == 0:
           result.append(x ** 2)

EXPECTED ANSWER:
"result = [x**2 for x in range(10) if x % 2 == 0]. Comprehension is more Pythonic,
often faster, and more readable for simple cases. Same O(n) complexity."

② CORE INTERVIEW QUESTION
─────────────────────────
Q: Given list of strings, create dict mapping each string to its length, but only
   for strings longer than 3 characters.

THINK-ALOUD ANSWER:
"I'll use dict comprehension with filter. {s: len(s) for s in strings if len(s) > 3}.
This is O(n) time, O(k) space where k=number of strings meeting condition. More
Pythonic than manual dict.update() in loop."

def string_length_map(strings):
    \"\"\"
    Interviewer expects: Dict comprehension usage
    \"\"\"
    return {s: len(s) for s in strings if len(s) > 3}

③ EDGE-CASE / TRAP QUESTION
────────────────────────────
Q: When should you NOT use list comprehension?

EXPECTED ANSWER:
"Don't use comprehensions when: (1) Logic is too complex (hurts readability). (2) Need
to break early (comprehensions always complete). (3) Have side effects (like printing,
file I/O). (4) Nested depth > 2 (becomes unreadable). Rule: If explaining takes more
than 10 seconds, use explicit loop."

INTERVIEWER EVALUATION:
✓ STRONG: Mentions readability trade-off, knows when to avoid
✗ WEAK: Says 'always use comprehensions' or 'never use them'

④ FOLLOW-UP OPTIMIZATION
─────────────────────────
Q: Flatten nested list [[1,2],[3,[4,5]],[6]] to [1,2,3,4,5,6]. Any depth.

EXPECTED ANSWER:
"For arbitrary depth, need recursion. List comprehension won't work elegantly here.
I'd write recursive function checking isinstance(item, list). Alternative: use
itertools, but recursion is clearer in interview setting."

def flatten_recursive(nested):
    \"\"\"
    Interviewer tests: Recognizing limits of comprehensions
    \"\"\"
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten_recursive(item))
        else:
            result.append(item)
    return result

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 3F: pop() COMPLEXITY (MEDIUM FREQUENCY)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

① WARM-UP QUESTION
──────────────────
Q: What's the time complexity of arr.pop() vs arr.pop(0)?

EXPECTED ANSWER:
"arr.pop() removes from end, O(1) - just decrement size pointer. arr.pop(0) removes
from front, O(n) - must shift all remaining elements left. For frequent front removals,
use collections.deque with popleft() which is O(1)."

RED FLAG: Saying both are O(1) indicates weak understanding of array internals.

② CORE INTERVIEW QUESTION (Only 1 for MEDIUM frequency)
────────────────────────────────────────────────────────
Q: Implement a stack using Python list. What operations are O(1)?

THINK-ALOUD ANSWER:
"Use list as stack: append() for push (O(1)), pop() for pop (O(1)), arr[-1] for peek
(O(1)). All stack operations are O(1) because we only work with the end. Don't use
insert(0) or pop(0) - those are O(n)."

class Stack:
    \"\"\"
    Interviewer expects: Correct complexity analysis
    \"\"\"
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)  # O(1)
    
    def pop(self):
        if not self.items:
            raise IndexError("Pop from empty stack")
        return self.items.pop()  # O(1)
    
    def peek(self):
        if not self.items:
            raise IndexError("Peek from empty stack")
        return self.items[-1]  # O(1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 3G: remove() IN LOOPS (MEDIUM FREQUENCY)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

① CORE INTERVIEW QUESTION (Only 1 for MEDIUM)
──────────────────────────────────────────────
Q: Debug this code. Why doesn't it remove all even numbers?
   
   nums = [1, 2, 3, 4, 5, 6]
   for num in nums:
       if num % 2 == 0:
           nums.remove(num)
   # Result: [1, 3, 5, 6] - missed 6!

THINK-ALOUD ANSWER:
"Iterator invalidation bug. When we remove 2, list becomes [1,3,4,5,6]. Iterator moves
to next position (now 4), skipping 3. Then removes 4, becomes [1,3,5,6], moves to 6,
skips 5. Classic bug. Fix: Use list comprehension nums = [x for x in nums if x % 2 != 0]
OR iterate backwards with reversed()."

INTERVIEWER EVALUATION:
✓ STRONG: Immediately identifies iterator invalidation, suggests comprehension
✗ WEAK: Doesn't understand why elements are skipped
✗ DISQUALIFYING: Suggests using a flag or try-except

def remove_evens_correct(nums):
    \"\"\"
    Three correct approaches
    \"\"\"
    # Approach 1: List comprehension (best)
    return [x for x in nums if x % 2 != 0]
    
    # Approach 2: Iterate backwards (modifies in-place)
    # for i in range(len(nums)-1, -1, -1):
    #     if nums[i] % 2 == 0:
    #         nums.pop(i)
    
    # Approach 3: New list (explicit)
    # return [x for x in nums if x % 2 != 0]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ═══════════════════════════════════════════════════════════════════════
# 4️⃣ THINK-ALOUD ANSWERS (MANDATORY)
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT STRONG CANDIDATES SAY (verbatim examples)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PROBLEM: Reverse an array in-place
──────────────────────────────────

STRONG CANDIDATE NARRATION:
"I see this is asking for in-place reversal. I'll use two pointers - left at start,
right at end. Swap elements and move pointers inward until they meet. This is O(n/2)
swaps which simplifies to O(n) time, O(1) space since we're not allocating anything
new. I could use arr[::-1] but that creates a new list, violating the in-place
requirement. Let me code this."

[Codes solution while talking]

"Time complexity is O(n) where n is array length. Space is O(1) auxiliary. Edge cases:
empty array returns immediately, single element returns as-is."

INTERVIEWER EVALUATION: ✓ HIRE
- Identified in-place requirement
- Explained algorithm before coding
- Mentioned alternative and why it's wrong
- Stated complexity without being asked
- Thought about edge cases

───────────────────────────────────────────────────────────────────────

WEAK CANDIDATE NARRATION:
"Um, I think I can use reverse()? Or maybe... let me think..."
[Silent for 30 seconds]
"I'll just use arr.reverse()."

INTERVIEWER RESPONSE:
"Can you implement it without using the built-in?"

WEAK CANDIDATE:
[Struggles, eventually writes nested loops or incorrect solution]

INTERVIEWER EVALUATION: ✗ NO HIRE
- Didn't understand problem
- Silent thinking (red flag)
- Tried to use built-in without understanding
- Couldn't implement algorithm

───────────────────────────────────────────────────────────────────────

RED-FLAG PHRASES THAT CAUSE REJECTION:
──────────────────────────────────────
❌ "I don't know Python that well"
❌ "I usually Google this"
❌ "Can I use a library for this?"
❌ "I'm more of a Java person"
❌ [Long silences without narration]
❌ "Is this O(1) or O(n)?" [Should know without asking]
❌ "I'll just try this and see if it works"

STRONG SIGNALS (What interviewers want to hear):
─────────────────────────────────────────────────
✓ "Let me clarify the requirements first..."
✓ "I'll use two pointers here because..."
✓ "This is O(n) time because we touch each element once..."
✓ "I'm choosing X over Y because of the space constraint..."
✓ "Edge cases: empty array, single element, all duplicates..."
✓ "Let me trace through an example: [1,2,3,4]..."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ═══════════════════════════════════════════════════════════════════════
# 5️⃣ LIVE CODING EXPECTATIONS
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROBLEM: Remove Duplicates from Sorted Array (In-Place)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Given sorted array nums, remove duplicates in-place. Return length of unique elements.
Example: [1,1,2,2,3] → return 3, first 3 elements are [1,2,3]

───────────────────────────────────────────────────────────────────────
APPROACH 1: BRUTE FORCE (What interviewers DON'T want)
───────────────────────────────────────────────────────────────────────
\"\"\"
def remove_duplicates_brute(nums):
    # Create new array with unique elements
    unique = []
    for num in nums:
        if num not in unique:  # O(n) lookup!
            unique.append(num)
    
    # Copy back to original
    for i in range(len(unique)):
        nums[i] = unique[i]
    
    return len(unique)

TIME: O(n²) due to 'num not in unique' check
SPACE: O(n) for unique array
INTERVIEWER REACTION: ✗ "Can you optimize this?"
\"\"\"

───────────────────────────────────────────────────────────────────────
APPROACH 2: USING SET (Incorrect - loses sorted property)
───────────────────────────────────────────────────────────────────────
\"\"\"
def remove_duplicates_set(nums):
    unique = list(set(nums))  # Loses order!
    unique.sort()  # Need to re-sort
    for i in range(len(unique)):
        nums[i] = unique[i]
    return len(unique)

TIME: O(n log n) due to sort
SPACE: O(n) for set
INTERVIEWER REACTION: ✗ "You're not leveraging that input is sorted"
\"\"\"

───────────────────────────────────────────────────────────────────────
APPROACH 3: TWO POINTERS (Optimal - What interviewers expect)
───────────────────────────────────────────────────────────────────────
\"\"\"
def remove_duplicates_optimal(nums):
    '''
    Two pointer technique:
    - slow: position to write next unique element
    - fast: scans through array
    - Since array is sorted, duplicates are adjacent
    
    Time: O(n) - single pass
    Space: O(1) - only two pointers
    '''
    if not nums:
        return 0
    
    slow = 1  # Position for next unique element
    
    for fast in range(1, len(nums)):
        if nums[fast] != nums[fast - 1]:  # Found new unique
            nums[slow] = nums[fast]
            slow += 1
    
    return slow

INTERVIEWER EVALUATION: ✓ STRONG HIRE
- Optimal O(n) time, O(1) space
- Leverages sorted property
- Clean, readable code
- Handles edge cases
\"\"\"

───────────────────────────────────────────────────────────────────────
FINAL INTERVIEW-SAFE SOLUTION (With full narration)
───────────────────────────────────────────────────────────────────────
\"\"\"

def remove_duplicates(nums):
    '''
    Remove duplicates from sorted array in-place.
    
    Approach: Two pointers
    - slow pointer: tracks position for next unique element
    - fast pointer: scans array looking for new unique values
    
    Since array is sorted, duplicates are adjacent. We only need to
    compare with previous element.
    
    Time: O(n) - single pass through array
    Space: O(1) - only using two integer pointers
    
    Args:
        nums: List[int], sorted array (modified in-place)
    
    Returns:
        int: length of unique portion
    '''
    # Edge case: empty array
    if not nums:
        return 0
    
    # Start slow at index 1 (first element is always unique)
    slow = 1
    
    # Fast pointer scans from index 1 to end
    for fast in range(1, len(nums)):
        # If current differs from previous, it's a new unique element
        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]  # Place at slow position
            slow += 1
    
    # slow now points to length of unique portion
    return slow


# Test cases (what strong candidates do)
def test_remove_duplicates():
    # Test 1: Normal case
    arr1 = [1, 1, 2, 2, 3]
    length1 = remove_duplicates(arr1)
    assert length1 == 3
    assert arr1[:length1] == [1, 2, 3]
    
    # Test 2: Edge case - empty
    arr2 = []
    assert remove_duplicates(arr2) == 0
    
    # Test 3: Edge case - single element
    arr3 = [1]
    assert remove_duplicates(arr3) == 1
    
    # Test 4: All duplicates
    arr4 = [1, 1, 1, 1]
    assert remove_duplicates(arr4) == 1
    
    # Test 5: No duplicates
    arr5 = [1, 2, 3, 4]
    assert remove_duplicates(arr5) == 4
    
    print("✓ All tests pass")

\"\"\"

───────────────────────────────────────────────────────────────────────
COMMON INCORRECT IMPLEMENTATIONS (Seen in real interviews)
───────────────────────────────────────────────────────────────────────

❌ MISTAKE 1: Using slow = 0
def wrong_slow_start(nums):
    slow = 0  # Should be 1!
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1  # Off-by-one error

❌ MISTAKE 2: Comparing with slow instead of fast-1
def wrong_comparison(nums):
    slow = 1
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:  # Wrong! Compare with nums[fast-1]
            nums[slow] = nums[fast]
            slow += 1
    return slow

❌ MISTAKE 3: Not handling empty array
def no_edge_case(nums):
    slow = 1  # Crashes on empty array!
    for fast in range(1, len(nums)):
        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]
            slow += 1
    return slow

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ═══════════════════════════════════════════════════════════════════════
# 6️⃣ PATTERN RECOGNITION (MANDATORY)
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PATTERN MAPPING: WHEN TO USE WHICH PATTERN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PATTERN 1: TWO POINTERS
════════════════════════

SIGNAL PHRASES IN PROBLEM:
- "sorted array"
- "in-place"
- "two elements that sum to..."
- "remove duplicates"
- "merge two arrays"
- "partition array"

TEMPLATE:
```
def two_pointers_template(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        # Check condition
        if meets_condition(arr[left], arr[right]):
            return (left, right)
        elif need_larger_value:
            left += 1
        else:
            right -= 1
```

INTERVIEWER EXPECTS YOU TO SAY:
"I notice this is a sorted array and we're looking for a pair. This signals two
pointers pattern. I'll start with pointers at opposite ends and move them based on
the comparison. This gives O(n) time, O(1) space."

EXAMPLE PROBLEMS:
• Two Sum II (sorted array)
• Container With Most Water
• Remove Duplicates (slow/fast variant)
• Three Sum
• Trapping Rain Water

───────────────────────────────────────────────────────────────────────

PATTERN 2: SLIDING WINDOW
══════════════════════════

SIGNAL PHRASES IN PROBLEM:
- "subarray" or "substring"
- "maximum/minimum length"
- "consecutive elements"
- "window of size k"
- "longest/shortest..."

TEMPLATE:
```
def sliding_window_template(arr, k):
    window_sum = sum(arr[:k])  # Initialize window
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]  # Slide
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

INTERVIEWER EXPECTS YOU TO SAY:
"This asks for a subarray property, which signals sliding window. I'll maintain a
window and slide it across the array, updating state as elements enter/leave. This
avoids recalculating from scratch each time, giving O(n) instead of O(n*k)."

EXAMPLE PROBLEMS:
• Maximum Sum Subarray of Size K
• Longest Substring Without Repeating Characters
• Minimum Window Substring
• Fruits Into Baskets

───────────────────────────────────────────────────────────────────────

PATTERN 3: IN-PLACE MODIFICATION
══════════════════════════════════

SIGNAL PHRASES IN PROBLEM:
- "in-place"
- "O(1) extra space"
- "modify the array itself"
- "without creating new array"

TEMPLATE:
```
def inplace_template(arr):
    write = 0  # Position to write next valid element
    
    for read in range(len(arr)):
        if is_valid(arr[read]):
            arr[write] = arr[read]
            write += 1
    
    return write  # New length
```

INTERVIEWER EXPECTS YOU TO SAY:
"The O(1) space constraint signals in-place modification. I'll use two pointers: read
scans the array, write tracks where to place next valid element. This lets us filter
or rearrange without allocating new array."

EXAMPLE PROBLEMS:
• Move Zeroes
• Remove Element
• Remove Duplicates
• Sort Colors (Dutch National Flag)

───────────────────────────────────────────────────────────────────────

PATTERN 4: BINARY SEARCH (On sorted arrays)
════════════════════════════════════════════

SIGNAL PHRASES IN PROBLEM:
- "sorted array"
- "find element"
- "O(log n)" hint
- "search in..."

INTERVIEWER EXPECTS YOU TO SAY:
"Sorted array with search requirement signals binary search. O(log n) time by halving
search space each iteration."

───────────────────────────────────────────────────────────────────────

PATTERN 5: STACK (Using list)
═══════════════════════════════

SIGNAL PHRASES IN PROBLEM:
- "valid parentheses"
- "next greater element"
- "evaluate expression"
- "recent first" / "last in, first out"

INTERVIEWER EXPECTS YOU TO SAY:
"This requires tracking most recent elements, which signals stack. I'll use a Python
list with append/pop for O(1) stack operations."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ═══════════════════════════════════════════════════════════════════════
# 7️⃣ COMMON INTERVIEW FAILURE MODES
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PYTHON-SPECIFIC FAILURES (That get candidates rejected)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FAILURE #1: MUTABILITY MISTAKES
════════════════════════════════

❌ WHAT WEAK CANDIDATES DO:
```
def buggy_default_arg(x, arr=[]):
    arr.append(x)
    return arr

print(buggy_default_arg(1))  # [1]
print(buggy_default_arg(2))  # [1, 2] - SURPRISE!
```

INTERVIEWER THINKING: "Doesn't understand mutable default arguments. RED FLAG."

✓ WHAT STRONG CANDIDATES DO:
```
def correct_default_arg(x, arr=None):
    if arr is None:
        arr = []
    arr.append(x)
    return arr
```

SAYS: "Mutable defaults are shared across calls. I'll use None and create new list
inside function."

───────────────────────────────────────────────────────────────────────

FAILURE #2: INCORRECT ASSUMPTIONS ABOUT COMPLEXITY
═══════════════════════════════════════════════════

❌ WHAT WEAK CANDIDATES SAY:
"All list operations are O(1) right?"
"insert() is fast, it's just adding an element"
"Slicing is free since it doesn't copy... oh wait..."

✓ WHAT STRONG CANDIDATES SAY:
"append() is O(1) amortized, but insert(0) is O(n) because we shift all elements.
Slicing creates a shallow copy, so it's O(k) where k is slice length."

INTERVIEWER TEST:
"What's the complexity of arr.remove(x)?"

STRONG: "O(n) - must scan to find x, then shift elements"
WEAK: "O(1) because we know the value"

───────────────────────────────────────────────────────────────────────

FAILURE #3: MODIFYING DATA WHILE ITERATING
═══════════════════════════════════════════

❌ WHAT WEAK CANDIDATES WRITE:
```
for i, val in enumerate(arr):
    if val % 2 == 0:
        arr.pop(i)  # WRONG! Index changes during iteration
```

✓ WHAT STRONG CANDIDATES WRITE:
```
arr = [x for x in arr if x % 2 != 0]  # Create new list
# OR
for i in range(len(arr) - 1, -1, -1):  # Iterate backwards
    if arr[i] % 2 == 0:
        arr.pop(i)
```

───────────────────────────────────────────────────────────────────────

FAILURE #4: MISUSING BUILT-INS
════════════════════════════════

❌ WHAT WEAK CANDIDATES DO:
```
sorted_arr = arr.sort()  # sorted_arr is None!
result = arr.reverse()   # result is None!
```

INTERVIEWER THINKING: "Doesn't know Python semantics. This is basic."

✓ WHAT STRONG CANDIDATES DO:
```
sorted_arr = sorted(arr)  # Returns new list
arr.sort()  # Use this, then reference arr

arr_copy = arr[::-1]  # Returns reversed copy
arr.reverse()  # Modifies in-place, use arr after
```

───────────────────────────────────────────────────────────────────────

FAILURE #5: OVER-ENGINEERING SIMPLE PROBLEMS
══════════════════════════════════════════════

❌ WHAT WEAK CANDIDATES DO:
Problem: "Reverse a list"

```
def reverse_complex(arr):
    # Create stack
    stack = []
    for item in arr:
        stack.append(item)
    
    # Pop into new array
    result = []
    while stack:
        result.append(stack.pop())
    
    return result
```

INTERVIEWER THINKING: "Why not just arr[::-1]? Over-complicated."

✓ WHAT STRONG CANDIDATES DO:
```
def reverse_simple(arr):
    return arr[::-1]  # O(n), clean
```

OR if in-place required:
```
def reverse_inplace(arr):
    arr.reverse()  # O(n), modifies in-place
```

───────────────────────────────────────────────────────────────────────

FAILURE #6: POOR NARRATION / SILENT CODING
════════════════════════════════════════════

❌ WEAK CANDIDATE BEHAVIOR:
[Types code silently for 5 minutes]
[Makes mistake, silently debugs]
[Finishes] "Done"

INTERVIEWER THINKING: "Can't communicate. Red flag for teamwork."

✓ STRONG CANDIDATE BEHAVIOR:
"Let me think through this... I'll use two pointers because the array is sorted.
Left starts at 0, right at length minus 1. If sum is too small, move left up...
Let me code this while explaining..."
[Codes while talking]
"I'm checking if left < right to avoid double-counting middle element..."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ═══════════════════════════════════════════════════════════════════════
# 8️⃣ MOCK INTERVIEW ROUND
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REALISTIC INTERVIEW SIMULATION (45 minutes)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEWER: "Let's start with a warm-up."

───────────────────────────────────────────────────────────────────────
RAPID-FIRE ROUND (5 minutes) - Tests instant recall
───────────────────────────────────────────────────────────────────────

Q1: "What's the time complexity of list.append()?"
EXPECTED: "O(1) amortized"
FOLLOW-UP: "Why amortized?"
EXPECTED: "Occasionally needs to resize underlying array, but infrequent enough that
           average case is constant time."

Q2: "How do you reverse a list in-place?"
EXPECTED: "arr.reverse() or use two pointers with swapping"

Q3: "What does arr.sort() return?"
EXPECTED: "None - it sorts in-place"
FOLLOW-UP: "What if you need the original?"
EXPECTED: "Use sorted(arr) which returns new list"

Q4: "Create a 3x3 matrix of zeros. What's wrong with [[0]*3]*3?"
EXPECTED: "Shallow copy - all rows point to same list. Use [[0]*3 for _ in range(3)]"

Q5: "What's the complexity of list.insert(0, x)?"
EXPECTED: "O(n) - must shift all elements right"

INTERVIEWER SCORING:
- 5/5 instant correct answers: Proceed to medium problem
- 3-4/5: Proceed with caution, may probe deeper
- < 3/5: Strong rejection signal

───────────────────────────────────────────────────────────────────────
MAIN PROBLEM (25 minutes) - Tests algorithm design
───────────────────────────────────────────────────────────────────────

INTERVIEWER: "Given an array of integers, move all zeros to the end while maintaining
relative order of non-zero elements. Do this in-place with O(1) extra space."

Example: [0,1,0,3,12] → [1,3,12,0,0]

[Pause for candidate to ask clarifying questions]

STRONG CANDIDATE ASKS:
- "Can I modify the array in-place?"  → YES
- "What if array is empty or all zeros?" → Should handle gracefully
- "Should I maintain order of non-zero elements?" → YES

WEAK CANDIDATE:
[Starts coding immediately without clarifying]

───────────────────────────────────────────────────────────────────────

INTERVIEWER: "Take a minute to think about your approach."

STRONG CANDIDATE THINKS ALOUD:
"This is an in-place problem with O(1) space. I see two approaches:
1. Count zeros, create new array - but that's O(n) space, violates constraint
2. Two pointers - one tracks position for next non-zero, other scans array

I'll use approach 2: slow pointer for write position, fast pointer to scan. When fast
finds non-zero, swap with slow position and increment slow. This is O(n) time, O(1)
space."

WEAK CANDIDATE:
[Silent, or says] "I'll just try something..."

───────────────────────────────────────────────────────────────────────

INTERVIEWER: "Go ahead and code it."

STRONG CANDIDATE CODES:
```
def move_zeros(nums):
    '''
    Move all zeros to end, maintain order of non-zeros.
    
    Approach: Two pointers
    - slow: position for next non-zero
    - fast: scans array
    
    Time: O(n), Space: O(1)
    '''
    slow = 0
    
    for fast in range(len(nums)):
        if nums[fast] != 0:
            # Swap non-zero to slow position
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
```

INTERVIEWER: "Walk me through an example."

STRONG CANDIDATE:
"Let's use [0,1,0,3,12]:
- Initially slow=0, fast=0
- fast=0: nums[0]=0, skip
- fast=1: nums[1]=1 (non-zero), swap with slow=0 → [1,0,0,3,12], slow=1
- fast=2: nums[2]=0, skip
- fast=3: nums[3]=3 (non-zero), swap with slow=1 → [1,3,0,0,12], slow=2
- fast=4: nums[4]=12 (non-zero), swap with slow=2 → [1,3,12,0,0], slow=3
Result: [1,3,12,0,0] ✓"

───────────────────────────────────────────────────────────────────────
PRESSURE FOLLOW-UPS (Interruptions during coding)
───────────────────────────────────────────────────────────────────────

INTERVIEWER: [While candidate is coding] "What's the time complexity?"
STRONG: "O(n) - single pass through array"
WEAK: "Um... let me finish first..."

INTERVIEWER: "What if array is [1,2,3,4,5]?"
STRONG: "All non-zeros, so we swap each element with itself. Still works, O(n)."
WEAK: [Confused] "I didn't think about that..."

INTERVIEWER: "Can you optimize space further?"
STRONG: "We're already at O(1) auxiliary space - just two pointers."
WEAK: "Maybe use less variables?" [Doesn't understand O(1) already optimal]

───────────────────────────────────────────────────────────────────────
EDGE CASES (Tests thoroughness)
───────────────────────────────────────────────────────────────────────

INTERVIEWER: "What are the edge cases?"

STRONG CANDIDATE LISTS:
1. Empty array: []
2. All zeros: [0,0,0]
3. No zeros: [1,2,3]
4. Single element: [0] or [1]
5. Zeros at start: [0,0,1,2]
6. Zeros at end: [1,2,0,0]

WEAK CANDIDATE:
"Um... empty array?" [Doesn't think of other cases]

───────────────────────────────────────────────────────────────────────
COMPLEXITY CHALLENGE
───────────────────────────────────────────────────────────────────────

INTERVIEWER: "State time and space complexity with explanation."

STRONG:
"Time: O(n) where n=array length - single pass, each element touched once.
Space: O(1) auxiliary - only using slow/fast pointers, no additional data structures.
If we count the input array, space is O(n), but auxiliary space is O(1)."

WEAK:
"O(n)... because of the loop?"
[Doesn't mention space, doesn't explain reasoning]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEWER FINAL DECISION MATRIX:
───────────────────────────────────

STRONG HIRE (Would extend offer):
✓ Asked clarifying questions
✓ Explained approach before coding
✓ Clean, working solution
✓ Handled follow-ups smoothly
✓ Identified all edge cases
✓ Clear complexity analysis
✓ Maintained communication throughout

NO HIRE (Reject):
✗ Silent coding
✗ Didn't handle edge cases
✗ Wrong complexity analysis
✗ Struggled with follow-ups
✗ Unclear explanation
✗ Buggy code with no testing

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ═══════════════════════════════════════════════════════════════════════
# 9️⃣ SELF-ASSESSMENT CHECK
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SELF-ASSESSMENT: ARE YOU INTERVIEW READY?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Test yourself honestly. Can you answer these WITHOUT hesitation?

TIER 1: MUST KNOW (Failure = Not ready)
════════════════════════════════════════
□ Explain arr[start:end:step] with examples
□ Difference between append() and extend()
□ Why arr.sort() returns None
□ Create 2D array without shallow copy trap
□ Time complexity of append, insert, pop
□ Two pointers pattern - when and how
□ Remove elements from list while iterating (correct way)
□ Difference between arr[:] and arr.copy()

TIER 2: SHOULD KNOW (Weak if you can't)
════════════════════════════════════════
□ List comprehension vs loop - when to use
□ Slicing creates shallow or deep copy?
□ Complexity of pop() vs pop(0)
□ How to deep copy nested list
□ Why [[]]*n doesn't create independent lists
□ In-place modification pattern
□ Sliding window pattern on lists

TIER 3: NICE TO KNOW (Bonus points)
════════════════════════════════════
□ Amortized O(1) for append - why?
□ When to use collections.deque over list
□ List internals: dynamic array implementation
□ sort() vs sorted() - implementation differences

───────────────────────────────────────────────────────────────────────
SCORING:
───────────────────────────────────────────────────────────────────────

TIER 1: Can answer 7/8+ → Minimum bar
TIER 1: Can answer < 7/8 → NOT READY - Study more

TIER 2: Can answer 6/7+ → Solid
TIER 2: Can answer < 6/7 → Weak - Review patterns

TIER 3: Can answer 3/4+ → Strong hire signal
TIER 3: Can answer < 3/4 → Average

OVERALL READINESS:
──────────────────
✓ TIER 1: 7/8+ AND TIER 2: 6/7+ → INTERVIEW READY
✗ Any other combination → STUDY MORE

───────────────────────────────────────────────────────────────────────
WHAT SECTIONS TO REVISE:
───────────────────────────────────────────────────────────────────────

If you missed slicing questions → Review Section 3A
If you missed append/extend → Review Section 3B
If you missed sort questions → Review Section 3C
If you missed copy questions → Review Section 3D
If you missed comprehensions → Review Section 3E
If you missed complexity → Review Section 2
If you missed patterns → Review Section 6

───────────────────────────────────────────────────────────────────────
INTERVIEWER CONCLUSION ABOUT YOU:
───────────────────────────────────────────────────────────────────────

Based on your self-assessment:

If TIER 1 < 7/8:
"Candidate lacks fundamental Python list knowledge. This is concerning for a
5+ YOE engineer. Would not proceed to onsite. REJECT."

If TIER 1 >= 7/8, TIER 2 < 5/7:
"Candidate knows basics but weak on patterns and optimization. Might struggle
with medium problems. WEAK HIRE or NO HIRE."

If TIER 1 >= 7/8, TIER 2 >= 6/7:
"Solid fundamentals, good pattern recognition. Would perform well in interviews.
HIRE if communication is also strong."

If All tiers strong:
"Strong technical depth, ready for senior+ roles. STRONG HIRE."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ═══════════════════════════════════════════════════════════════════════
# FINAL NOTES
# ═══════════════════════════════════════════════════════════════════════

"""
This file is designed for INTERVIEW PREPARATION, not learning Python.
If you can't answer Tier 1 questions instantly, you are NOT ready.

Practice the mock interview section out loud.
Time yourself: 45 minutes for the full simulation.

Remember:
- Clarity > Correctness > Performance > Cleverness
- Narrate your thought process
- Ask clarifying questions
- Test your code
- State complexity

Good luck.
"""
