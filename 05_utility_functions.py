"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 PYTHON UTILITY FUNCTIONS - INTERVIEW MASTERY GUIDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
For 5+ YOE Developer | Interview-Focused | Complete Reference
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

These utility functions separate beginners from experienced Python developers
in interviews. Knowing when and how to use them shows Pythonic thinking.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

# ═══════════════════════════════════════════════════════════════════════
# 1️⃣ TYPE & SAFETY FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════

print("📌 TYPE & SAFETY FUNCTIONS:")

# type(obj) - Get the type of an object
x = 42
print(f"type(42) = {type(x)}")  # <class 'int'>
print(f"type('hello') = {type('hello')}")  # <class 'str'>
print(f"type([1,2,3]) = {type([1, 2, 3])}")  # <class 'list'>

# isinstance(obj, type) - Check if object is instance of type
x = 42
print(f"isinstance(42, int) = {isinstance(x, int)}")  # True
print(f"isinstance(42, (int, float)) = {isinstance(x, (int, float))}")  # True

# 🎤 INTERVIEWER NARRATION:
"""
"I'll use isinstance to check if the input is a list or a single value.
This makes my function more robust."
"""

def process_input(data):
    if isinstance(data, list):
        return sum(data)
    elif isinstance(data, (int, float)):
        return data * 2
    else:
        return None

print(f"process_input([1,2,3]) = {process_input([1, 2, 3])}")
print(f"process_input(5) = {process_input(5)}")

# 🚨 INTERVIEW TIP: Use isinstance(), not type() == 
# isinstance() works with inheritance!


# ═══════════════════════════════════════════════════════════════════════
# 2️⃣ STRING METHODS (HIGH-FREQUENCY)
# ═══════════════════════════════════════════════════════════════════════

print("\n📌 STRING METHODS:")

# join(iterable) - Join with separator (INTERVIEW ESSENTIAL)
words = ["hello", "world", "python"]
result = " ".join(words)
print(f"' '.join(...) = '{result}'")  # "hello world python"

chars = ['a', 'b', 'c']
result = "".join(chars)
print(f"''.join(['a','b','c']) = '{result}'")  # "abc"

# 🎤 INTERVIEWER NARRATION:
"""
"I'll build the result as a list of characters, then join at the end.
This is O(n) versus O(n²) for repeated string concatenation."
"""

# ❌ SLOW: String concatenation in loop
result = ""
for char in "hello":
    result += char  # O(n²) - creates new string each time

# ✅ FAST: Build list, then join
result = []
for char in "hello":
    result.append(char)
final = "".join(result)  # O(n)

# split(sep=None, maxsplit=-1) - Split string
text = "hello world python"
words = text.split()  # Split on whitespace
print(f"split() = {words}")  # ['hello', 'world', 'python']

text = "a,b,c,d"
parts = text.split(",")
print(f"split(',') = {parts}")  # ['a', 'b', 'c', 'd']

parts = text.split(",", 2)  # Limit splits
print(f"split(',', 2) = {parts}")  # ['a', 'b', 'c,d']

# strip() - Remove leading/trailing whitespace
text = "  hello  "
print(f"strip() = '{text.strip()}'")  # "hello"
print(f"lstrip() = '{text.lstrip()}'")  # "hello  "
print(f"rstrip() = '{text.rstrip()}'")  # "  hello"

# Can strip specific characters
text = "!!!hello!!!"
print(f"strip('!') = '{text.strip('!')}'")  # "hello"

# replace(old, new, count=-1) - Replace substrings
text = "hello world"
result = text.replace("world", "python")
print(f"replace('world', 'python') = '{result}'")

result = text.replace("l", "L", 1)  # Replace first occurrence only
print(f"replace('l', 'L', 1) = '{result}'")  # "heLlo world"

# startswith(prefix) / endswith(suffix) - Check prefix/suffix
text = "hello.py"
print(f"startswith('hello') = {text.startswith('hello')}")  # True
print(f"endswith('.py') = {text.endswith('.py')}")  # True

# Can check multiple prefixes
print(f"startswith(('hello', 'hi')) = {text.startswith(('hello', 'hi'))}")

# 🎤 INTERVIEWER NARRATION:
"""
"I'll check if the string ends with '.jpg' or '.png'. The endswith()
method accepts a tuple of suffixes, so I can check multiple at once."
"""

# Other useful string methods
text = "Hello World"
print(f"lower() = '{text.lower()}'")  # "hello world"
print(f"upper() = '{text.upper()}'")  # "HELLO WORLD"
print(f"isalpha() = {text.isalpha()}")  # False (has space)
print(f"isdigit() = {'123'.isdigit()}")  # True
print(f"isalnum() = {'abc123'.isalnum()}")  # True


# ═══════════════════════════════════════════════════════════════════════
# 3️⃣ RANGE (ITERATION ESSENTIAL)
# ═══════════════════════════════════════════════════════════════════════

print("\n📌 RANGE:")

# range(stop) - 0 to stop-1
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4
print()

# range(start, stop) - start to stop-1
for i in range(2, 5):
    print(i, end=" ")  # 2 3 4
print()

# range(start, stop, step) - With custom step
for i in range(0, 10, 2):
    print(i, end=" ")  # 0 2 4 6 8
print()

# Reverse range
for i in range(5, 0, -1):
    print(i, end=" ")  # 5 4 3 2 1
print()

# Create list from range
nums = list(range(5))
print(f"list(range(5)) = {nums}")  # [0, 1, 2, 3, 4]

# 🎤 INTERVIEWER NARRATION:
"""
"I'll iterate backwards from n-1 to 0 using range(n-1, -1, -1).
This lets me modify the array in-place without index issues."
"""

# COMPARE WITH JAVA/JS:
"""
Java: for(int i = 0; i < 5; i++)  →  Python: for i in range(5)
JS:   for(let i = 0; i < 5; i++)  →  Python: for i in range(5)
"""


# ═══════════════════════════════════════════════════════════════════════
# 4️⃣ ENUMERATE (INTERVIEW FAVORITE)
# ═══════════════════════════════════════════════════════════════════════

print("\n📌 ENUMERATE:")

# enumerate(iterable, start=0) - Get index and value
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Custom start index
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")

# 🎤 INTERVIEWER NARRATION:
"""
"I need both the index and value, so I'll use enumerate. This is more
Pythonic than manually tracking an index with a counter variable."
"""

# ❌ UN-PYTHONIC:
i = 0
for fruit in fruits:
    print(f"{i}: {fruit}")
    i += 1

# ✅ PYTHONIC:
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Convert to dict
fruit_indices = dict(enumerate(fruits))
print(f"Dict from enumerate: {fruit_indices}")


# ═══════════════════════════════════════════════════════════════════════
# 5️⃣ ZIP (COMBINE ITERABLES)
# ═══════════════════════════════════════════════════════════════════════

print("\n📌 ZIP:")

# zip(*iterables) - Combine multiple iterables
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, {city}")

# Create dict from two lists
person_dict = dict(zip(names, ages))
print(f"Dict from zip: {person_dict}")

# Create list of tuples
pairs = list(zip(names, ages))
print(f"List of tuples: {pairs}")

# Unzip (using zip with *)
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*pairs)
print(f"Unzipped: {numbers}, {letters}")

# 🎤 INTERVIEWER NARRATION:
"""
"I have two arrays - keys and values. I'll use zip to combine them into
a dictionary in one line: dict(zip(keys, values))."
"""

# ⚠️ zip stops at shortest iterable
short = [1, 2]
long = ['a', 'b', 'c', 'd']
print(f"zip mismatched: {list(zip(short, long))}")  # [(1, 'a'), (2, 'b')]

# For longest: use itertools.zip_longest
from itertools import zip_longest
print(f"zip_longest: {list(zip_longest(short, long, fillvalue=0))}")


# ═══════════════════════════════════════════════════════════════════════
# 6️⃣ MAP, FILTER, LAMBDA (FUNCTIONAL PROGRAMMING)
# ═══════════════════════════════════════════════════════════════════════

print("\n📌 MAP, FILTER, LAMBDA:")

# lambda - Anonymous function
square = lambda x: x ** 2
print(f"lambda x: x**2 → {square(5)}")  # 25

add = lambda x, y: x + y
print(f"lambda x,y: x+y → {add(3, 4)}")  # 7

# map(function, iterable) - Apply function to each element
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, nums))
print(f"map(lambda x: x**2) = {squares}")

# Multiple iterables
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sums = list(map(lambda x, y: x + y, nums1, nums2))
print(f"map(add) = {sums}")

# 🎤 INTERVIEWER NARRATION:
"""
"I need to convert these strings to integers. I'll use map(int, strings)
which is cleaner than a list comprehension here."
"""

strings = ["1", "2", "3"]
numbers = list(map(int, strings))
print(f"map(int, strings) = {numbers}")

# filter(function, iterable) - Keep elements where function returns True
nums = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(f"filter(lambda x: x%2==0) = {evens}")

# ⚠️ INTERVIEW TIP: List comprehension is often clearer!
evens = [x for x in nums if x % 2 == 0]  # More Pythonic

# 🎤 INTERVIEWER NARRATION:
"""
"While map/filter work, I prefer list comprehensions in interviews.
They're more readable and Pythonic:
  [x**2 for x in nums]  instead of  list(map(lambda x: x**2, nums))
"""


# ═══════════════════════════════════════════════════════════════════════
# 7️⃣ ANY, ALL (BOOLEAN AGGREGATION)
# ═══════════════════════════════════════════════════════════════════════

print("\n📌 ANY, ALL:")

# any(iterable) - True if ANY element is True
nums = [0, 0, 1, 0]
print(f"any([0,0,1,0]) = {any(nums)}")  # True

print(f"any([0,0,0]) = {any([0, 0, 0])}")  # False

# Check if any element satisfies condition
nums = [1, 3, 5, 7]
has_even = any(x % 2 == 0 for x in nums)
print(f"Has even number: {has_even}")

# all(iterable) - True if ALL elements are True
nums = [1, 1, 1, 1]
print(f"all([1,1,1,1]) = {all(nums)}")  # True

nums = [1, 1, 0, 1]
print(f"all([1,1,0,1]) = {all(nums)}")  # False

# Check if all elements satisfy condition
nums = [2, 4, 6, 8]
all_even = all(x % 2 == 0 for x in nums)
print(f"All even: {all_even}")

# 🎤 INTERVIEWER NARRATION:
"""
"I need to check if all rows in the matrix are sorted. I'll use all()
with a generator expression: all(is_sorted(row) for row in matrix).
This short-circuits on the first False."
"""

# Short-circuiting example
def check(x):
    print(f"Checking {x}")
    return x > 5

nums = [10, 12, 3, 15]  # Will stop at 3
result = all(check(x) for x in nums)
print(f"Result: {result}")

# COMPARE WITH JAVA:
"""
Java: return Arrays.stream(arr).allMatch(x -> x % 2 == 0);
Python: return all(x % 2 == 0 for x in arr)
"""


# ═══════════════════════════════════════════════════════════════════════
# 8️⃣ SORTED (ADVANCED SORTING)
# ═══════════════════════════════════════════════════════════════════════

print("\n📌 SORTED:")

# sorted(iterable, key=None, reverse=False) - Return new sorted list
nums = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_nums = sorted(nums)
print(f"sorted() = {sorted_nums}")

# Sort in reverse
sorted_desc = sorted(nums, reverse=True)
print(f"sorted(reverse=True) = {sorted_desc}")

# Custom key function - Sort by absolute value
nums = [-5, -2, -8, 3, 1]
by_abs = sorted(nums, key=abs)
print(f"sorted(key=abs) = {by_abs}")  # [1, -2, 3, -5, -8]

# Sort strings by length
words = ["python", "is", "awesome", "a"]
by_length = sorted(words, key=len)
print(f"sorted(key=len) = {by_length}")

# Sort tuples/lists
points = [(1, 5), (3, 2), (2, 8), (3, 1)]
by_x = sorted(points)  # Default: sort by first element, then second
print(f"sorted(points) = {by_x}")

by_y = sorted(points, key=lambda p: p[1])  # Sort by y
print(f"sorted(key=lambda p: p[1]) = {by_y}")

# Multiple sort criteria
by_x_then_y_desc = sorted(points, key=lambda p: (p[0], -p[1]))
print(f"Multi-criteria sort: {by_x_then_y_desc}")

# 🎤 INTERVIEWER NARRATION:
"""
"I need to sort intervals by start time, and if tied, by end time.
Since Python sorts tuples lexicographically, sorted(intervals) does
exactly what I need without a custom key function."
"""

# Sort dictionary by value
freq = {"a": 3, "b": 1, "c": 2}
sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
print(f"Sorted dict by value: {sorted_items}")

# Get top k elements
from heapq import nlargest, nsmallest
nums = [3, 1, 4, 1, 5, 9, 2, 6]
top_3 = nlargest(3, nums)
print(f"Top 3: {top_3}")


# ═══════════════════════════════════════════════════════════════════════
# 9️⃣ MATH & NUMERIC FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════

print("\n📌 MATH & NUMERIC:")

# abs(x) - Absolute value
print(f"abs(-5) = {abs(-5)}")  # 5
print(f"abs(-3.14) = {abs(-3.14)}")  # 3.14

# round(x, digits=0) - Round to n digits
print(f"round(3.14159, 2) = {round(3.14159, 2)}")  # 3.14
print(f"round(42.5) = {round(42.5)}")  # 42 (banker's rounding)

# min(*args) / max(*args) - Min/max of values
print(f"min(3, 1, 4) = {min(3, 1, 4)}")  # 1
print(f"max([1, 2, 3]) = {max([1, 2, 3])}")  # 3

# With key function
words = ["python", "is", "awesome"]
longest = max(words, key=len)
print(f"max(words, key=len) = '{longest}'")

# sum(iterable, start=0) - Sum of elements
nums = [1, 2, 3, 4, 5]
total = sum(nums)
print(f"sum(nums) = {total}")  # 15

total = sum(nums, 100)  # Start from 100
print(f"sum(nums, 100) = {total}")  # 115

# pow(x, y) - x raised to power y
print(f"pow(2, 10) = {pow(2, 10)}")  # 1024
print(f"2 ** 10 = {2 ** 10}")  # Same thing

# divmod(x, y) - (quotient, remainder)
q, r = divmod(17, 5)
print(f"divmod(17, 5) = ({q}, {r})")  # (3, 2)

# 🎤 INTERVIEWER NARRATION:
"""
"I need both quotient and remainder. I'll use divmod() instead of
separate // and % operations."
"""


# ═══════════════════════════════════════════════════════════════════════
# 🔟 ADVANCED: ITERTOOLS (BONUS)
# ═══════════════════════════════════════════════════════════════════════

print("\n📌 ITERTOOLS (Bonus):")

from itertools import (
    combinations, permutations, product,
    accumulate, chain, groupby
)

# combinations - All k-length combinations (order doesn't matter)
nums = [1, 2, 3]
combs = list(combinations(nums, 2))
print(f"combinations([1,2,3], 2) = {combs}")  # [(1,2), (1,3), (2,3)]

# permutations - All k-length permutations (order matters)
perms = list(permutations(nums, 2))
print(f"permutations([1,2,3], 2) = {perms}")

# product - Cartesian product
prod = list(product([1, 2], ['a', 'b']))
print(f"product([1,2], ['a','b']) = {prod}")  # [(1,'a'), (1,'b'), (2,'a'), (2,'b')]

# accumulate - Running totals
nums = [1, 2, 3, 4, 5]
running_sum = list(accumulate(nums))
print(f"accumulate([1,2,3,4,5]) = {running_sum}")  # [1, 3, 6, 10, 15]

# chain - Flatten iterables
flat = list(chain([1, 2], [3, 4], [5, 6]))
print(f"chain([1,2], [3,4], [5,6]) = {flat}")  # [1,2,3,4,5,6]

# groupby - Group consecutive equal elements
from itertools import groupby
data = [1, 1, 2, 2, 2, 3, 1, 1]
groups = [(k, list(g)) for k, g in groupby(data)]
print(f"groupby([1,1,2,2,2,3,1,1]) = {groups}")

# 🎤 INTERVIEWER NARRATION:
"""
"For this combinatorics problem, I'll use itertools.combinations
instead of implementing backtracking manually. It's more efficient
and shows I know the standard library."
"""


# ═══════════════════════════════════════════════════════════════════════
# 📊 QUICK REFERENCE TABLE
# ═══════════════════════════════════════════════════════════════════════

reference = """
╔═══════════════════════════════════════════════════════════════════════╗
║                  UTILITY FUNCTIONS QUICK REFERENCE                    ║
╠═══════════════════════════╦═══════════════════════════════════════════╣
║ CATEGORY                  ║ FUNCTIONS                                 ║
╠═══════════════════════════╬═══════════════════════════════════════════╣
║ Type Checking             ║ isinstance(), type()                      ║
╠═══════════════════════════╬═══════════════════════════════════════════╣
║ String                    ║ join(), split(), strip(),                 ║
║                           ║ replace(), startswith(), endswith()       ║
╠═══════════════════════════╬═══════════════════════════════════════════╣
║ Iteration                 ║ range(), enumerate(), zip()               ║
╠═══════════════════════════╬═══════════════════════════════════════════╣
║ Functional                ║ map(), filter(), lambda                   ║
╠═══════════════════════════╬═══════════════════════════════════════════╣
║ Boolean                   ║ any(), all()                              ║
╠═══════════════════════════╬═══════════════════════════════════════════╣
║ Sorting                   ║ sorted(), min(), max()                    ║
╠═══════════════════════════╬═══════════════════════════════════════════╣
║ Math                      ║ abs(), round(), sum(), pow(), divmod()    ║
╠═══════════════════════════╬═══════════════════════════════════════════╣
║ Itertools                 ║ combinations(), permutations(),           ║
║                           ║ product(), accumulate()                   ║
╚═══════════════════════════╩═══════════════════════════════════════════╝

🔥 MOST IMPORTANT FOR INTERVIEWS:
  1. enumerate() - Always use when you need index + value
  2. zip() - Combine parallel arrays
  3. join() - Build strings efficiently
  4. sorted(key=...) - Custom sorting
  5. any() / all() - Boolean checks
  6. isinstance() - Type checking
"""
print(reference)

print("\n✅ UTILITY FUNCTIONS MASTERY COMPLETE!")
print("🚀 Ready to solve interview problems!")

