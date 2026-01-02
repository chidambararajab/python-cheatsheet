# Python Programming Assessment Cheat Sheet - Guvi Platform

## 🚀 Quick Reference for 45-Minute Coding Assessment

### 1. Input/Output Patterns (Most Common on Guvi)

#### Single Line Input

```python
# Single integer
n = int(input())

# Single float
f = float(input())

# Single string
s = input()

# Multiple integers in one line
a, b, c = map(int, input().split())

# List of integers in one line
numbers = list(map(int, input().split()))

# List of strings in one line
words = input().split()
```

#### Multiple Lines Input

```python
# First line: number of test cases
t = int(input())
for _ in range(t):
    # Process each test case
    n = int(input())
    # Your logic here

# Read n lines of integers
n = int(input())
for i in range(n):
    x = int(input())
    # Process x

# Read matrix/2D array
rows, cols = map(int, input().split())
matrix = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)
```

#### Output Formatting

```python
# Print with space separation
print(*list_name)  # Unpacks list elements
print(a, b, c)     # Multiple variables

# Print without newline
print(value, end="")

# Print with custom separator
print(a, b, c, sep="-")

# Formatted strings
print(f"Result: {value}")
print("%.2f" % float_value)  # 2 decimal places
print("{:.2f}".format(float_value))
```

### 2. Common String Problems

#### String Reversal

```python
# Method 1: Slicing (fastest)
reversed_str = s[::-1]

# Method 2: Using reversed()
reversed_str = ''.join(reversed(s))

# Reverse words in sentence
sentence = "hello world"
reversed_words = ' '.join(sentence.split()[::-1])  # "world hello"
```

#### Palindrome Check

```python
def is_palindrome(s):
    return s == s[::-1]

# Case-insensitive palindrome
def is_palindrome_ignore_case(s):
    s = s.lower()
    return s == s[::-1]

# Alphanumeric palindrome (ignore spaces, punctuation)
def is_palindrome_alphanumeric(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]
```

#### Character Frequency

```python
# Method 1: Using dictionary
def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

# Method 2: Using Counter
from collections import Counter
freq = Counter(s)
```

#### Anagram Check

```python
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

# Using Counter
from collections import Counter
def are_anagrams(s1, s2):
    return Counter(s1) == Counter(s2)
```

### 3. Array/List Manipulation

#### Find Maximum/Minimum

```python
# Basic
max_val = max(arr)
min_val = min(arr)

# Second largest
def second_largest(arr):
    unique = list(set(arr))
    unique.sort()
    return unique[-2] if len(unique) >= 2 else None

# K-th largest/smallest
def kth_largest(arr, k):
    return sorted(arr, reverse=True)[k-1]

def kth_smallest(arr, k):
    return sorted(arr)[k-1]
```

#### Array Rotation

```python
# Left rotation by k positions
def rotate_left(arr, k):
    n = len(arr)
    k = k % n  # Handle k > n
    return arr[k:] + arr[:k]

# Right rotation by k positions
def rotate_right(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]
```

#### Subarray/Subset Problems

```python
# Maximum subarray sum (Kadane's Algorithm)
def max_subarray_sum(arr):
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Find all subarrays
def all_subarrays(arr):
    subarrays = []
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n+1):
            subarrays.append(arr[i:j])
    return subarrays
```

### 4. Number Problems

#### Prime Number Check

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Generate primes up to n (Sieve of Eratosthenes)
def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n + 1, i):
                primes[j] = False

    return [i for i in range(n + 1) if primes[i]]
```

#### GCD and LCM

```python
# Euclidean algorithm for GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Using math module
import math
gcd_val = math.gcd(a, b)

# LCM
def lcm(a, b):
    return (a * b) // gcd(a, b)
```

#### Factorial

```python
# Iterative
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Using math module
import math
fact = math.factorial(n)

# Recursive (careful with stack overflow)
def factorial_recursive(n):
    return 1 if n <= 1 else n * factorial_recursive(n - 1)
```

#### Fibonacci

```python
# First n Fibonacci numbers
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

# N-th Fibonacci number (optimized)
def nth_fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

### 5. Pattern Printing

#### Number Patterns

```python
# Triangle pattern
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# Pyramid pattern
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
# Output:
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
```

#### Character Patterns

```python
# Alphabet triangle
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")  # A=65 in ASCII
    print()
```

### 6. Searching Algorithms

#### Linear Search

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

#### Binary Search

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### 7. Sorting Problems

#### Built-in Sorting

```python
# Sort list in place
arr.sort()  # Ascending
arr.sort(reverse=True)  # Descending

# Create new sorted list
sorted_arr = sorted(arr)

# Sort by custom key
# Sort strings by length
words.sort(key=len)

# Sort by multiple criteria
students = [("Alice", 85), ("Bob", 75), ("Charlie", 85)]
students.sort(key=lambda x: (-x[1], x[0]))  # Sort by score desc, then name asc
```

#### Quick Implementations

```python
# Bubble Sort (simple but slow)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

### 8. Dictionary/HashTable Problems

#### Two Sum Problem

```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

#### Frequency Counting

```python
# Count occurrences
def count_elements(arr):
    count = {}
    for item in arr:
        count[item] = count.get(item, 0) + 1
    return count

# Find most frequent element
def most_frequent(arr):
    count = count_elements(arr)
    return max(count, key=count.get)
```

### 9. Mathematical Formulas

```python
# Sum of first n natural numbers
sum_n = n * (n + 1) // 2

# Sum of squares
sum_squares = n * (n + 1) * (2 * n + 1) // 6

# Sum of cubes
sum_cubes = (n * (n + 1) // 2) ** 2

# Arithmetic progression sum
# first term = a, common difference = d, n terms
ap_sum = n * (2 * a + (n - 1) * d) // 2

# Geometric progression sum
# first term = a, common ratio = r, n terms
gp_sum = a * (r**n - 1) // (r - 1)  # if r != 1

# Distance between two points
import math
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Area of triangle (given 3 sides)
# Heron's formula
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
```

### 10. Common Edge Cases to Remember

```python
# Empty input
if not arr:
    return []  # or appropriate default

# Single element
if len(arr) == 1:
    return arr[0]  # or handle accordingly

# Division by zero
if denominator == 0:
    return float('inf')  # or handle error

# Integer overflow (Python handles automatically)
# But be aware of time limits for large numbers

# Negative numbers
if n < 0:
    # Handle negative case

# String with spaces
s = s.strip()  # Remove leading/trailing spaces
words = s.split()  # Split by any whitespace

# Case sensitivity
s = s.lower()  # or s.upper()
```

### 11. Time Complexity Quick Reference

- **O(1)**: Constant - Direct access, simple math
- **O(log n)**: Logarithmic - Binary search
- **O(n)**: Linear - Single loop
- **O(n log n)**: Linearithmic - Efficient sorting (merge sort, heap sort)
- **O(n²)**: Quadratic - Nested loops
- **O(2ⁿ)**: Exponential - Recursive without memoization

### 12. Object-Oriented Programming (OOP)

#### Basic Class Structure

```python
class Person:
    # Class variable
    species = "Homo sapiens"

    # Constructor
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age

    # Instance method
    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old"

    # String representation
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

    # Static method
    @staticmethod
    def is_adult(age):
        return age >= 18

    # Class method
    @classmethod
    def create_baby(cls, name):
        return cls(name, 0)

# Usage
person = Person("Alice", 25)
print(person.introduce())
baby = Person.create_baby("Bob")
```

#### Inheritance

```python
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self, subject):
        return f"{self.name} is studying {subject}"

# Multiple inheritance
class WorkingStudent(Student, Employee):
    pass
```

### 13. Exception Handling

```python
# Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Multiple exceptions
try:
    value = int(input())
    result = 10 / value
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"Error: {e}")

# Try-except-else-finally
try:
    file = open('data.txt', 'r')
except FileNotFoundError:
    print("File not found")
else:
    content = file.read()
    print("File read successfully")
finally:
    if 'file' in locals():
        file.close()

# Raising exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
```

### 14. File Handling

```python
# Reading files
# Method 1: Using with statement (recommended)
with open('file.txt', 'r') as f:
    content = f.read()  # Read entire file
    # OR
    lines = f.readlines()  # Read all lines into list
    # OR
    for line in f:  # Read line by line
        process(line.strip())

# Writing files
with open('output.txt', 'w') as f:
    f.write("Hello World\n")
    f.writelines(["Line 1\n", "Line 2\n"])

# Append mode
with open('log.txt', 'a') as f:
    f.write("New log entry\n")

# Reading CSV (if allowed to import)
import csv
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

### 15. Regular Expressions

```python
import re

# Basic patterns
# \d - digit, \w - word character, \s - whitespace
# + - one or more, * - zero or more, ? - zero or one
# ^ - start, $ - end

# Find all matches
text = "Contact: 123-456-7890 or 987-654-3210"
phones = re.findall(r'\d{3}-\d{3}-\d{4}', text)

# Search for pattern
match = re.search(r'[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+', email)
if match:
    print(f"Valid email: {match.group()}")

# Replace pattern
text = re.sub(r'\d+', 'X', "Room 123, Floor 4")  # "Room X, Floor X"

# Split by pattern
parts = re.split(r'[,;]', "apple,banana;orange")  # ['apple', 'banana', 'orange']

# Common patterns
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
phone_pattern = r'^\d{10}  # 10 digit phone
url_pattern = r'https?://(?:www\.)?[a-zA-Z0-9./]+'
```

### 16. Data Structure Implementations

#### Stack

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Using list as stack
stack = []
stack.append(1)  # push
top = stack.pop()  # pop
```

#### Queue

```python
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft() if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

# Using deque as queue (efficient)
queue = deque()
queue.append(1)  # enqueue
front = queue.popleft()  # dequeue
```

#### Linked List

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements
```

### 17. Lambda Functions and Functional Programming

```python
# Lambda function
square = lambda x: x ** 2
add = lambda x, y: x + y

# Map function
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))  # [1, 4, 9, 16, 25]

# Filter function
evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]

# Reduce function
from functools import reduce
sum_all = reduce(lambda x, y: x + y, numbers)  # 15
product = reduce(lambda x, y: x * y, numbers)  # 120

# Sorting with lambda
students = [('Alice', 85), ('Bob', 75), ('Charlie', 90)]
students.sort(key=lambda x: x[1])  # Sort by score

# List comprehension vs map/filter
# These are equivalent:
squares = [x**2 for x in numbers]
squares = list(map(lambda x: x**2, numbers))

evens = [x for x in numbers if x % 2 == 0]
evens = list(filter(lambda x: x % 2 == 0, numbers))
```

### 18. Set Operations

```python
# Creating sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Set operations
union = set1 | set2  # or set1.union(set2)  # {1, 2, 3, 4, 5, 6}
intersection = set1 & set2  # or set1.intersection(set2)  # {3, 4}
difference = set1 - set2  # or set1.difference(set2)  # {1, 2}
symmetric_diff = set1 ^ set2  # or set1.symmetric_difference(set2)  # {1, 2, 5, 6}

# Set methods
set1.add(5)
set1.remove(3)  # Raises error if not found
set1.discard(3)  # No error if not found
set1.clear()

# Subset and superset
{1, 2}.issubset({1, 2, 3})  # True
{1, 2, 3}.issuperset({1, 2})  # True

# Remove duplicates from list
unique_list = list(set(my_list))
```

### 19. Tuple Operations

```python
# Creating tuples
tup = (1, 2, 3)
single = (1,)  # Note the comma
empty = ()

# Tuple unpacking
x, y, z = (1, 2, 3)
a, *rest = (1, 2, 3, 4)  # a=1, rest=[2, 3, 4]

# Named tuples
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
print(p.x, p.y)  # 11 22

# Tuple methods
tup.count(2)  # Count occurrences
tup.index(3)  # Find index

# Using tuples as dictionary keys
coordinates = {(0, 0): 'origin', (1, 0): 'right'}
```

### 20. Recursion Problems

```python
# Factorial
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Power
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

# Sum of digits
def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)

# Reverse string
def reverse_string(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])

# Tower of Hanoi
def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n-1, auxiliary, target, source)
```

### 21. Important Built-in Functions

```python
# enumerate() - Get index and value
fruits = ['apple', 'banana', 'orange']
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# Start from custom index
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}: {fruit}")

# zip() - Combine multiple iterables
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# zip with different lengths
from itertools import zip_longest
list1 = [1, 2, 3]
list2 = ['a', 'b']
for x, y in zip_longest(list1, list2, fillvalue='-'):
    print(x, y)  # 1 a, 2 b, 3 -

# range() variations
range(5)          # 0, 1, 2, 3, 4
range(2, 8)       # 2, 3, 4, 5, 6, 7
range(10, 0, -2)  # 10, 8, 6, 4, 2

# all() and any()
all([True, True, False])  # False
any([False, False, True]) # True

# eval() and exec() - Use carefully!
result = eval("2 + 3 * 4")  # 14
exec("x = 5")  # Executes code
```

### 22. Generators and Iterators

```python
# Generator function
def fibonacci_gen(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Using generator
for num in fibonacci_gen(5):
    print(num)  # 0, 1, 1, 2, 3

# Generator expression
squares_gen = (x**2 for x in range(10))
print(next(squares_gen))  # 0
print(next(squares_gen))  # 1

# Memory efficient for large data
sum_of_squares = sum(x**2 for x in range(1000000))
```

### 23. Comprehensions (Advanced)

```python
# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
# Result: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Dictionary comprehension with condition
scores = {'Alice': 85, 'Bob': 72, 'Charlie': 90, 'David': 68}
passed = {name: score for name, score in scores.items() if score >= 70}

# Set comprehension
unique_lengths = {len(word) for word in ['apple', 'banana', 'pear', 'kiwi']}

# Multiple conditions
result = [x for x in range(100) if x % 2 == 0 if x % 3 == 0]
# Same as: [x for x in range(100) if x % 2 == 0 and x % 3 == 0]

# With if-else
result = [x if x > 0 else 0 for x in [-1, 2, -3, 4]]
```

### 24. Collections Module

```python
from collections import defaultdict, Counter, OrderedDict, deque

# defaultdict - No KeyError
dd = defaultdict(list)
dd['key'].append('value')  # No need to check if key exists

# Word grouping by first letter
words = ['apple', 'banana', 'apricot', 'cherry']
grouped = defaultdict(list)
for word in words:
    grouped[word[0]].append(word)

# Counter - Count hashable objects
from collections import Counter
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
count = Counter(colors)
print(count.most_common(2))  # [('blue', 3), ('red', 2)]

# OrderedDict - Maintains insertion order (Python 3.7+ dicts do this too)
from collections import OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2

# ChainMap - Combine multiple dicts
from collections import ChainMap
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
combined = ChainMap(dict1, dict2)
```

### 25. Important Modules for Algorithms

```python
# bisect - Binary search and insertion
import bisect
sorted_list = [1, 3, 4, 7, 9]
pos = bisect.bisect_left(sorted_list, 5)  # Position to insert 5
bisect.insort(sorted_list, 5)  # Insert maintaining order

# heapq - Heap queue (priority queue)
import heapq
heap = [3, 1, 4, 1, 5]
heapq.heapify(heap)  # Convert to heap
heapq.heappush(heap, 2)  # Push item
smallest = heapq.heappop(heap)  # Pop smallest

# Find k largest/smallest
nums = [3, 1, 4, 1, 5, 9, 2, 6]
k_largest = heapq.nlargest(3, nums)  # [9, 6, 5]
k_smallest = heapq.nsmallest(3, nums)  # [1, 1, 2]

# itertools - Powerful iteration tools
from itertools import permutations, combinations, product

# Permutations
perms = list(permutations([1, 2, 3], 2))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# Combinations
combs = list(combinations([1, 2, 3], 2))
# [(1, 2), (1, 3), (2, 3)]

# Cartesian product
prod = list(product([1, 2], ['a', 'b']))
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
```

### 26. String Formatting (All Methods)

```python
# f-strings (Python 3.6+) - Preferred
name = "Alice"
age = 25
print(f"Name: {name}, Age: {age}")
print(f"Pi: {3.14159:.2f}")  # 2 decimal places
print(f"Binary: {10:b}, Hex: {10:x}")  # Binary: 1010, Hex: a

# .format() method
print("Name: {}, Age: {}".format(name, age))
print("Name: {0}, Age: {1}, {0} is {1}".format(name, age))
print("Name: {n}, Age: {a}".format(n=name, a=age))

# % formatting (old style)
print("Name: %s, Age: %d" % (name, age))
print("Pi: %.2f" % 3.14159)

# Padding and alignment
print(f"{'left':<10}|{'center':^10}|{'right':>10}")
print(f"{42:05d}")  # 00042 (zero padding)
```

### 27. Date and Time

```python
from datetime import datetime, timedelta, date

# Current date and time
now = datetime.now()
today = date.today()

# Formatting dates
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # 2024-06-26 14:30:45
print(now.strftime("%B %d, %Y"))  # June 26, 2024

# Parsing dates
date_str = "2024-06-26"
parsed = datetime.strptime(date_str, "%Y-%m-%d")

# Date arithmetic
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
diff = datetime(2024, 12, 31) - now  # Time until year end

# Common date operations
print(now.year, now.month, now.day)
print(now.hour, now.minute, now.second)
print(now.weekday())  # 0=Monday, 6=Sunday
```

### 28. JSON Handling

```python
import json

# Convert Python to JSON
data = {
    'name': 'Alice',
    'age': 25,
    'scores': [85, 90, 92]
}
json_string = json.dumps(data)
json_string_pretty = json.dumps(data, indent=2)

# Convert JSON to Python
parsed = json.loads(json_string)

# Read/Write JSON files
# Write
with open('data.json', 'w') as f:
    json.dump(data, f)

# Read
with open('data.json', 'r') as f:
    loaded = json.load(f)
```

### 29. Function Arguments (\*args, \*\*kwargs)

```python
# *args - Variable positional arguments
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))  # 10

# **kwargs - Variable keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")

# Both together
def process(*args, **kwargs):
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

# Unpacking arguments
def greet(first, last):
    return f"Hello, {first} {last}"

name = ["John", "Doe"]
print(greet(*name))  # Unpacks list

info = {"first": "Jane", "last": "Smith"}
print(greet(**info))  # Unpacks dict
```

### 30. Common Algorithm Patterns

```python
# Sliding window
def max_sum_subarray(arr, k):
    """Find maximum sum of subarray of size k"""
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)

    return max_sum

# Two pointers
def two_sum_sorted(arr, target):
    """Find two numbers that sum to target in sorted array"""
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

# Prefix sum
def range_sum_query(arr):
    """Precompute prefix sums for range queries"""
    prefix = [0]
    for num in arr:
        prefix.append(prefix[-1] + num)

    def query(i, j):
        return prefix[j + 1] - prefix[i]

    return query

# Memoization
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]
```

### 🚨 Last-Minute Checklist:

1. **Input format** - Single line? Multiple lines? Check carefully
2. **Output format** - Space-separated? New lines? Exact format matters
3. **Data types** - Integer division (//) vs float division (/)
4. **Edge cases** - Empty input, single element, negative numbers
5. **Constraints** - Check time/space limits in problem statement
6. **Python version** - Guvi usually uses Python 3.7+

### 📊 Estimated Problem Distribution:

- **Easy (60%)**: Direct implementation, basic loops, simple conditions
- **Medium (35%)**: Algorithms, data structures, optimization needed
- **Hard (5%)**: Complex algorithms, dynamic programming

### 🎯 Time Management Strategy:

- **0-5 min**: Read all problems, start with easiest
- **5-35 min**: Solve problems (aim for 10-15 min each)
- **35-45 min**: Debug, optimize, submit all attempts

Remember: **Partial solutions get partial marks!** Always submit something that runs.

Good luck! You're well-prepared now! 🚀
