"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 PYTHON UTILITY FUNCTIONS - SENIOR INTERVIEW PREPARATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Interviewer: Staff Engineer | Pythonic Code Expert
Level: 5+ YOE | Focus: Write CLEAN, IDIOMATIC Python
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣ OVERVIEW
Utility functions separate Pythonic from non-Pythonic code.
Interviewers judge CODE QUALITY through these.

CRITICAL FOR 5+ YOE:
✓ enumerate() over range(len())
✓ zip() for parallel iteration
✓ join() for string building
✓ sorted(key=...) for custom sorts
✓ any()/all() for boolean checks
✓ List comprehensions over loops

REJECTION SIGNALS:
❌ for i in range(len(arr)): val = arr[i]  # Not Pythonic
❌ result = ""; for c in s: result += c     # O(n²) string building
❌ Always uses loops instead of comprehensions
❌ Doesn't know enumerate, zip exist

2️⃣ CONCEPT CLASSIFICATION
╔═══════════════════╦═══════════╦════════════════════════════╗
║ CONCEPT           ║ FREQUENCY ║ REJECTION REASON           ║
╠═══════════════════╬═══════════╬════════════════════════════╣
║ enumerate()       ║ HIGH      ║ Uses range(len()) instead  ║
║ join()            ║ HIGH      ║ String concat in loop O(n²)║
║ List comprehension║ HIGH      ║ Always uses verbose loops  ║
║ zip()             ║ MEDIUM    ║ Manual parallel iteration  ║
║ sorted(key=...)   ║ HIGH      ║ Can't sort with custom key ║
║ any()/all()       ║ MEDIUM    ║ Manual loop for boolean    ║
╚═══════════════════╩═══════════╩════════════════════════════╝

3️⃣ INTERVIEW QUESTIONS

ENUMERATE() - CRITICAL
① WARM-UP: What's wrong with this?
for i in range(len(arr)):
    print(i, arr[i])

EXPECTED: "Not Pythonic. Use enumerate():
for i, val in enumerate(arr):
    print(i, val)"

② CORE: Find indices of all target values.
def find_all_indices(arr, target):
    return [i for i, val in enumerate(arr) if val == target]

INTERVIEWER EXPECTS: enumerate in comprehension
✓ STRONG: One-liner with enumerate
✗ WEAK: Manual index tracking

③ EDGE-CASE: Start enumerate from 1.
for i, val in enumerate(arr, start=1):
    print(f"Item {i}: {val}")  # 1-indexed

④ FOLLOW-UP: Enumerate with filtering.
# Get indices of evens
evens = [i for i, x in enumerate(arr) if x % 2 == 0]

JOIN() - CRITICAL  
① WARM-UP: Why is this slow?
result = ""
for char in "hello":
    result += char  # O(n²)!

EXPECTED: "String concat in loop creates new string each time. O(n²) total.
Use join(): ''.join(chars) for O(n)."

② CORE: Build string from list of words.
words = ['hello', 'world', 'python']
sentence = ' '.join(words)  # O(n)

INTERVIEWER EXPECTS: join() immediately
✓ STRONG: Uses join() 
✗ WEAK: Loop with concat

③ EDGE-CASE: Join with custom separator.
csv_line = ','.join(map(str, numbers))
path = '/'.join(['home', 'user', 'docs'])

④ FOLLOW-UP: When is concat acceptable?
EXPECTED: "For small fixed number of strings (<5), concat is fine:
name = first + ' ' + last. For loops or many strings, use join()."

SORTED(KEY=...) - CRITICAL
① WARM-UP: Sort list of tuples by second element.
points = [(1,5), (3,2), (2,8)]
sorted_points = sorted(points, key=lambda p: p[1])

EXPECTED: lambda for tuple element

② CORE: Sort words by length, then alphabetically.
words = ['apple', 'pie', 'a', 'cherry']
sorted_words = sorted(words, key=lambda w: (len(w), w))

INTERVIEWER EXPECTS: Multiple sort criteria in tuple
✓ STRONG: Uses tuple key for multi-level sort
✗ WEAK: Sorts twice or doesn't know how

③ EDGE-CASE: Sort descending by one criteria.
# Sort by length desc, then alpha asc
sorted(words, key=lambda w: (-len(w), w))

④ FOLLOW-UP: Custom sort without lambda.
def get_length(word):
    return len(word)

sorted(words, key=get_length)

LIST COMPREHENSION - CRITICAL
① WARM-UP: Convert loop to comprehension.
# ❌ Verbose
result = []
for x in range(10):
    if x % 2 == 0:
        result.append(x**2)

# ✅ Pythonic
result = [x**2 for x in range(10) if x % 2 == 0]

② CORE: Nested comprehension for matrix.
matrix = [[j for j in range(cols)] for i in range(rows)]

INTERVIEWER EXPECTS: Correct nesting order
✓ STRONG: [inner-expr for outer for inner]
✗ WEAK: Reverses order or uses loops

③ EDGE-CASE: When NOT to use comprehension.
EXPECTED: "Don't use if:
1. Logic too complex (hurts readability)
2. Need to break early
3. Have side effects (print, file I/O)
4. Nested depth > 2"

④ FOLLOW-UP: Dict comprehension.
{k: v**2 for k, v in d.items() if v > 0}

ZIP() - MEDIUM
① CORE: Combine two lists.
names = ['Alice', 'Bob']
ages = [25, 30]
people = list(zip(names, ages))  # [('Alice', 25), ('Bob', 30)]

② Follow-Up: Create dict from parallel lists.
person_dict = dict(zip(names, ages))

③ Edge-Case: Unzip tuples.
pairs = [(1, 'a'), (2, 'b')]
nums, letters = zip(*pairs)  # Unzip with *

ANY()/ALL() - MEDIUM
① CORE: Check if any element satisfies condition.
has_negative = any(x < 0 for x in nums)
all_positive = all(x > 0 for x in nums)

INTERVIEWER EXPECTS: Generator expression
✓ STRONG: any(condition for x in iter)
✗ WEAK: Manual loop with flag

② EDGE-CASE: Short-circuiting behavior.
# any() stops at first True
# all() stops at first False
# Both are lazy - don't evaluate entire sequence

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

4️⃣ THINK-ALOUD ANSWERS

PROBLEM: Get word lengths for words > 5 chars

STRONG: "I'll use list comprehension with filter:
lengths = [len(w) for w in words if len(w) > 5]
One-liner, O(n), Pythonic."

WEAK: "lengths = []
for word in words:
    if len(word) > 5:
        lengths.append(len(word))"

INTERVIEWER: "More Pythonic?"
WEAK: [Doesn't know comprehension] ✗ RED FLAG for 5+ YOE

PROBLEM: Build CSV line from list

STRONG: "I'll use join():
csv = ','.join(map(str, values))
This is O(n). String concat in loop would be O(n²)."

WEAK: "result = ''
for val in values:
    result += str(val) + ','
return result[:-1]"

INTERVIEWER: ✗ Doesn't understand performance

5️⃣ LIVE CODING

PROBLEM: Sort students by grade DESC, then name ASC

students = [('Alice', 85), ('Bob', 90), ('Charlie', 85)]
Expected: [('Bob', 90), ('Alice', 85), ('Charlie', 85)]

OPTIMAL SOLUTION:
sorted_students = sorted(students, key=lambda s: (-s[1], s[0]))
# Negative for descending grade, positive for ascending name

INTERVIEWER TESTS:
✓ Knows to negate for desc sort
✓ Uses tuple for multi-key
✓ One-liner solution

COMMON MISTAKES:
❌ Sorts twice (inefficient)
❌ Doesn't know how to mix asc/desc
❌ Uses if-else in key function (overcomplicated)

6️⃣ PATTERN RECOGNITION

PATTERN: INDEX + VALUE ITERATION
Signal: "Need both index and element"
Template: for i, val in enumerate(items)
Never: for i in range(len(items)): val = items[i]

PATTERN: STRING BUILDING IN LOOP
Signal: "Concatenate many strings"
Template: ''.join(parts)
Never: result = ''; for p in parts: result += p

PATTERN: BOOLEAN AGGREGATION
Signal: "Check if any/all satisfy..."
Template: any(condition for x in items)
Never: flag = False; for x in items: if condition: flag = True

PATTERN: PARALLEL ITERATION
Signal: "Iterate two lists together"
Template: for a, b in zip(list1, list2)
Never: for i in range(len(list1)): a, b = list1[i], list2[i]

7️⃣ COMMON FAILURES

FAILURE #1: NOT USING ENUMERATE
❌ for i in range(len(arr)):
       print(i, arr[i])
✓ for i, val in enumerate(arr):
       print(i, val)

FAILURE #2: STRING CONCAT IN LOOP
❌ s = ""; for c in chars: s += c  # O(n²)!
✓ s = "".join(chars)  # O(n)

FAILURE #3: VERBOSE LOOPS
❌ result = []; for x in arr: if cond: result.append(f(x))
✓ result = [f(x) for x in arr if cond]

FAILURE #4: MANUAL ZIP
❌ for i in range(len(a)):
       combine(a[i], b[i])
✓ for x, y in zip(a, b):
       combine(x, y)

8️⃣ MOCK INTERVIEW

RAPID-FIRE (2 minutes):

Q1: "Get index and value from list?"
A: "enumerate(list)"

Q2: "Join list of strings with comma?"
A: "','.join(strings)"

Q3: "Check if any element is negative?"
A: "any(x < 0 for x in nums)"

Q4: "Sort by length descending?"
A: "sorted(words, key=len, reverse=True)"

Q5: "Iterate two lists together?"
A: "zip(list1, list2)"

MAIN PROBLEM (15 minutes):

"Given list of transactions [(date, amount), ...], 
return total amount for dates matching pattern."

STRONG CANDIDATE:
def sum_matching(transactions, date_pattern):
    return sum(amt for date, amt in transactions 
               if date.startswith(date_pattern))

USES: List iteration, unpacking, generator, built-in sum
INTERVIEWER: ✓ STRONG HIRE - Clean, Pythonic code

WEAK CANDIDATE:
total = 0
for i in range(len(transactions)):
    if transactions[i][0].startswith(date_pattern):
        total += transactions[i][1]
return total

USES: range(len), manual indexing, verbose
INTERVIEWER: ✗ Not Pythonic for 5+ YOE

9️⃣ SELF-ASSESSMENT

TIER 1: MUST KNOW (7/7)
□ enumerate() instead of range(len())
□ join() for string building
□ List comprehension syntax
□ sorted(key=lambda ...)
□ zip() for parallel iteration
□ any()/all() for boolean checks
□ Generator expressions

TIER 2: SHOULD KNOW (5/6)
□ Dict/set comprehensions
□ Extended unpacking with *
□ map()/filter() vs comprehensions
□ itertools basics
□ When NOT to use comprehension
□ str.split(), str.strip()

SCORING:
TIER 1 < 7/7: NOT READY - Code won't be Pythonic
TIER 1 = 7/7, TIER 2 >= 4/6: READY

CRITICAL: Can you use enumerate naturally?
NO → Will write non-Pythonic code → REJECT

INTERVIEWER CONCLUSION:
< 7/7 TIER 1: "Code style not Pythonic. Concerning for 5+ YOE. REJECT."
7/7 TIER 1: "Writes clean, idiomatic Python. Good code quality. HIRE."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FINAL: These utilities aren't "nice to have" - they're EXPECTED for senior engineers.
Use them naturally or your code will look junior-level.
"""
