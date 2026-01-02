# Python Operators and Conditional Statements Reference

This guide covers all Python operators and ways of adding conditions with easy-to-understand examples.

## 1. Arithmetic Operators

### Addition (`+`)

```python
# Numbers
result = 5 + 3          # Output: 8
result = 2.5 + 1.5      # Output: 4.0

# Strings (concatenation)
result = "Hello" + " " + "World"  # Output: "Hello World"

# Lists (concatenation)
result = [1, 2] + [3, 4]  # Output: [1, 2, 3, 4]
```

### Subtraction (`-`)

```python
result = 10 - 3         # Output: 7
result = 5.5 - 2.5      # Output: 3.0
result = -5 - 3         # Output: -8
```

### Multiplication (`*`)

```python
# Numbers
result = 4 * 3          # Output: 12
result = 2.5 * 4        # Output: 10.0

# String repetition
result = "Hi" * 3       # Output: "HiHiHi"

# List repetition
result = [1, 2] * 3     # Output: [1, 2, 1, 2, 1, 2]
```

### Division (`/`)

```python
result = 10 / 2         # Output: 5.0 (always returns float)
result = 7 / 2          # Output: 3.5
result = 10 / 3         # Output: 3.3333...
```

### Floor Division (`//`)

```python
result = 10 // 3        # Output: 3 (rounds down)
result = -10 // 3       # Output: -4 (rounds down)
result = 10.5 // 2      # Output: 5.0
```

### Modulus (`%`)

```python
result = 10 % 3         # Output: 1 (remainder)
result = 20 % 6         # Output: 2
result = 5 % 2          # Output: 1 (odd number check)

# String formatting (old style)
result = "Hello %s, you are %d years old" % ("Alice", 25)
```

### Exponentiation (`**`)

```python
result = 2 ** 3         # Output: 8 (2 to the power of 3)
result = 4 ** 0.5       # Output: 2.0 (square root)
result = 27 ** (1/3)    # Output: 3.0 (cube root)
```

## 2. Comparison Operators

### Equal to (`==`)

```python
print(5 == 5)           # Output: True
print("hello" == "hello")  # Output: True
print([1, 2] == [1, 2])    # Output: True
print(5 == 3)           # Output: False
```

### Not equal to (`!=`)

```python
print(5 != 3)           # Output: True
print("hello" != "world")  # Output: True
print([1, 2] != [1, 2])    # Output: False
```

### Greater than (`>`)

```python
print(5 > 3)            # Output: True
print(2 > 5)            # Output: False
print("b" > "a")        # Output: True (lexicographic)
```

### Less than (`<`)

```python
print(3 < 5)            # Output: True
print(5 < 3)            # Output: False
print("apple" < "banana")  # Output: True
```

### Greater than or equal to (`>=`)

```python
print(5 >= 5)           # Output: True
print(5 >= 3)           # Output: True
print(2 >= 5)           # Output: False
```

### Less than or equal to (`<=`)

```python
print(3 <= 5)           # Output: True
print(5 <= 5)           # Output: True
print(7 <= 5)           # Output: False
```

## 3. Logical Operators

### `and`

Returns True if both conditions are True.

```python
# Basic usage
print(True and True)    # Output: True
print(True and False)   # Output: False
print(False and True)   # Output: False

# With conditions
age = 25
has_license = True
can_drive = age >= 18 and has_license  # Output: True

# Short-circuit evaluation
x = 5
y = 0
result = y != 0 and x/y > 2  # False (doesn't evaluate x/y)
```

### `or`

Returns True if at least one condition is True.

```python
# Basic usage
print(True or False)    # Output: True
print(False or False)   # Output: False

# With conditions
is_weekend = True
is_holiday = False
can_sleep_in = is_weekend or is_holiday  # Output: True

# Short-circuit evaluation
x = 5
result = x > 0 or x/0 > 0  # True (doesn't evaluate x/0)
```

### `not`

Reverses the boolean value.

```python
print(not True)         # Output: False
print(not False)        # Output: True

# With conditions
is_raining = False
is_sunny = not is_raining  # Output: True

# Complex example
age = 15
is_adult = not (age < 18)  # Output: False
```

## 4. Bitwise Operators

### Bitwise AND (`&`)

```python
a = 5   # Binary: 0101
b = 3   # Binary: 0011
result = a & b  # Output: 1 (Binary: 0001)

# Set intersection
set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1 & set2  # Output: {2, 3}
```

### Bitwise OR (`|`)

```python
a = 5   # Binary: 0101
b = 3   # Binary: 0011
result = a | b  # Output: 7 (Binary: 0111)

# Set union
set1 = {1, 2}
set2 = {2, 3}
result = set1 | set2  # Output: {1, 2, 3}
```

### Bitwise XOR (`^`)

```python
a = 5   # Binary: 0101
b = 3   # Binary: 0011
result = a ^ b  # Output: 6 (Binary: 0110)

# Set symmetric difference
set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1 ^ set2  # Output: {1, 4}
```

### Bitwise NOT (`~`)

```python
a = 5   # Binary: 0101
result = ~a  # Output: -6 (inverts all bits)

# Explanation: ~n = -(n + 1)
print(~5)    # Output: -6
print(~(-3)) # Output: 2
```

### Left Shift (`<<`)

```python
a = 5   # Binary: 0101
result = a << 1  # Output: 10 (Binary: 1010)
result = a << 2  # Output: 20 (Binary: 10100)

# Equivalent to multiplying by 2^n
print(3 << 2)  # Output: 12 (3 * 2^2)
```

### Right Shift (`>>`)

```python
a = 20  # Binary: 10100
result = a >> 1  # Output: 10 (Binary: 1010)
result = a >> 2  # Output: 5  (Binary: 0101)

# Equivalent to dividing by 2^n
print(16 >> 2)  # Output: 4 (16 / 2^2)
```

## 5. Assignment Operators

### Basic Assignment (`=`)

```python
x = 5
name = "Alice"
numbers = [1, 2, 3]
```

### Compound Assignment Operators

```python
# Addition assignment
x = 5
x += 3      # Same as: x = x + 3, Result: 8

# Subtraction assignment
x = 10
x -= 4      # Same as: x = x - 4, Result: 6

# Multiplication assignment
x = 3
x *= 4      # Same as: x = x * 4, Result: 12

# Division assignment
x = 20
x /= 4      # Same as: x = x / 4, Result: 5.0

# Floor division assignment
x = 20
x //= 3     # Same as: x = x // 3, Result: 6

# Modulus assignment
x = 20
x %= 7      # Same as: x = x % 7, Result: 6

# Exponentiation assignment
x = 2
x **= 3     # Same as: x = x ** 3, Result: 8

# Bitwise operators assignment
x = 5
x &= 3      # Same as: x = x & 3, Result: 1
x |= 4      # Same as: x = x | 4, Result: 5
x ^= 2      # Same as: x = x ^ 2, Result: 7
x <<= 1     # Same as: x = x << 1, Result: 14
x >>= 2     # Same as: x = x >> 2, Result: 3
```

### Walrus Operator (`:=`) - Python 3.8+

Assigns values within expressions.

```python
# In while loops
while (n := input("Enter number: ")) != "quit":
    print(f"You entered: {n}")

# In if statements
numbers = [1, 2, 3, 4, 5]
if (n := len(numbers)) > 3:
    print(f"List has {n} elements")  # Output: List has 5 elements

# In list comprehensions
data = [1, 2, 3, 4, 5]
filtered = [y for x in data if (y := x * 2) > 5]
print(filtered)  # Output: [6, 8, 10]
```

## 6. Identity Operators

### `is`

Checks if two variables refer to the same object in memory.

```python
# With None
x = None
print(x is None)        # Output: True

# With lists
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a is b)           # Output: False (different objects)
print(a is c)           # Output: True (same object)
print(a == b)           # Output: True (same content)

# With small integers (cached by Python)
x = 256
y = 256
print(x is y)           # Output: True (cached)

x = 257
y = 257
print(x is y)           # Output: False (not cached)
```

### `is not`

Checks if two variables don't refer to the same object.

```python
x = [1, 2]
y = [1, 2]
print(x is not y)       # Output: True

# Common pattern
value = "hello"
if value is not None:
    print(f"Value is: {value}")
```

## 7. Membership Operators

### `in`

Checks if a value exists in a sequence.

```python
# In strings
print("h" in "hello")           # Output: True
print("world" in "hello world") # Output: True

# In lists
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)             # Output: True
print(10 in numbers)            # Output: False

# In dictionaries (checks keys)
person = {"name": "Alice", "age": 25}
print("name" in person)         # Output: True
print("Alice" in person)        # Output: False

# In sets
fruits = {"apple", "banana", "orange"}
print("apple" in fruits)        # Output: True
```

### `not in`

Checks if a value doesn't exist in a sequence.

```python
# In strings
print("x" not in "hello")       # Output: True

# In lists
numbers = [1, 2, 3, 4, 5]
print(10 not in numbers)        # Output: True

# Common pattern
banned_users = ["user1", "user2"]
username = "user3"
if username not in banned_users:
    print("Access granted")
```

## 8. Conditional Statements

### `if` Statement

```python
age = 18
if age >= 18:
    print("You are an adult")
```

### `if-else` Statement

```python
age = 16
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

### `if-elif-else` Statement

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")  # Output: Your grade is: B
```

### Nested Conditions

```python
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You're too young to drive")
```

### Multiple Conditions

```python
# Using and
age = 25
income = 50000
if age >= 21 and income >= 30000:
    print("Loan approved")

# Using or
day = "Saturday"
is_holiday = False
if day in ["Saturday", "Sunday"] or is_holiday:
    print("No work today!")

# Complex conditions
x = 10
if 0 < x < 20 and x % 2 == 0:
    print("x is a positive even number less than 20")
```

## 9. Ternary Operator (Conditional Expression)

```python
# Basic syntax: value_if_true if condition else value_if_false

# Simple example
age = 20
status = "adult" if age >= 18 else "minor"
print(status)  # Output: adult

# With calculation
x = 5
result = x * 2 if x > 0 else 0
print(result)  # Output: 10

# Nested ternary
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
print(grade)  # Output: B

# In list comprehension
numbers = [1, -2, 3, -4, 5]
positive = [x if x > 0 else 0 for x in numbers]
print(positive)  # Output: [1, 0, 3, 0, 5]
```

## 10. Match Statement (Python 3.10+)

```python
# Basic match
def describe_status(status_code):
    match status_code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:
            return "Unknown status"

print(describe_status(404))  # Output: Not Found

# Match with patterns
def process_command(command):
    match command.split():
        case ["quit"]:
            return "Goodbye!"
        case ["hello", name]:
            return f"Hello, {name}!"
        case ["add", x, y]:
            return int(x) + int(y)
        case _:
            return "Unknown command"

print(process_command("hello Alice"))  # Output: Hello, Alice!
print(process_command("add 5 3"))      # Output: 8

# Match with guards
def categorize_number(n):
    match n:
        case x if x < 0:
            return "negative"
        case 0:
            return "zero"
        case x if x < 10:
            return "single digit"
        case x if x < 100:
            return "double digit"
        case _:
            return "large number"

print(categorize_number(-5))   # Output: negative
print(categorize_number(7))    # Output: single digit
```

## 11. Special Conditional Constructs

### List Comprehension with Conditions

```python
# Basic filtering
numbers = [1, 2, 3, 4, 5, 6]
evens = [x for x in numbers if x % 2 == 0]
print(evens)  # Output: [2, 4, 6]

# With if-else
result = [x if x > 0 else 0 for x in [-1, 2, -3, 4]]
print(result)  # Output: [0, 2, 0, 4]

# Multiple conditions
result = [x for x in range(20) if x % 2 == 0 if x % 3 == 0]
print(result)  # Output: [0, 6, 12, 18]
```

### Dictionary Comprehension with Conditions

```python
# Filter dictionary
scores = {"Alice": 85, "Bob": 72, "Charlie": 90, "David": 68}
passed = {name: score for name, score in scores.items() if score >= 70}
print(passed)  # Output: {'Alice': 85, 'Bob': 72, 'Charlie': 90}
```

### Generator Expression with Conditions

```python
# Memory efficient filtering
numbers = range(1000)
evens = (x for x in numbers if x % 2 == 0)
print(sum(evens))  # Sum of even numbers from 0 to 998
```

### `all()` and `any()` Functions

```python
# all() - returns True if all elements are True
numbers = [2, 4, 6, 8]
print(all(x % 2 == 0 for x in numbers))  # Output: True

# any() - returns True if any element is True
numbers = [1, 3, 4, 7]
print(any(x % 2 == 0 for x in numbers))  # Output: True

# Practical example
passwords = ["abc123", "password123", "secure!pass"]
if all(len(p) >= 8 for p in passwords):
    print("All passwords meet length requirement")
```

### `filter()` Function

```python
# Filter with function
def is_positive(x):
    return x > 0

numbers = [-2, -1, 0, 1, 2, 3]
positive = list(filter(is_positive, numbers))
print(positive)  # Output: [1, 2, 3]

# Filter with lambda
evens = list(filter(lambda x: x % 2 == 0, range(10)))
print(evens)  # Output: [0, 2, 4, 6, 8]
```

## 12. Boolean Context

### Truthy and Falsy Values

```python
# Falsy values
falsy_values = [False, None, 0, 0.0, "", [], {}, set(), ()]

for value in falsy_values:
    if not value:
        print(f"{repr(value)} is falsy")

# Truthy values
if "hello":     # Non-empty string is truthy
    print("String is truthy")

if [1, 2, 3]:   # Non-empty list is truthy
    print("List is truthy")

if 42:          # Non-zero number is truthy
    print("Number is truthy")
```

### Short-Circuit Evaluation

```python
# With 'and' - returns first falsy or last value
result = "" and "hello"    # Output: ""
result = "hi" and "hello"  # Output: "hello"
result = 5 and 10          # Output: 10

# With 'or' - returns first truthy or last value
result = "" or "default"   # Output: "default"
result = "value" or "default"  # Output: "value"
result = 0 or 5 or 10      # Output: 5

# Practical usage
name = input("Enter name: ") or "Anonymous"
config = user_config or default_config
```

## Summary

### Arithmetic Operators (7)

`+`, `-`, `*`, `/`, `//`, `%`, `**`

### Comparison Operators (6)

`==`, `!=`, `>`, `<`, `>=`, `<=`

### Logical Operators (3)

`and`, `or`, `not`

### Bitwise Operators (6)

`&`, `|`, `^`, `~`, `<<`, `>>`

### Assignment Operators (13)

`=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`, `&=`, `|=`, `^=`, `<<=`, `>>=`

### Special Assignment (1)

`:=` (walrus operator)

### Identity Operators (2)

`is`, `is not`

### Membership Operators (2)

`in`, `not in`

### Conditional Constructs

- `if`, `elif`, `else` statements
- Ternary operator: `value_if_true if condition else value_if_false`
- `match` statement (Python 3.10+)
- List/dict/set comprehensions with conditions
- `all()`, `any()`, `filter()` functions
- Boolean context and short-circuit evaluation

**Total**: 40+ operators and multiple ways to implement conditional logic in Python!
