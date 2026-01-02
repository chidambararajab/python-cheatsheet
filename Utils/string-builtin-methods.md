# Python String Built-in Methods Reference

This guide covers **all** built-in string methods in Python with easy-to-understand examples. It includes both regular methods that you call directly and special "magic" methods that Python uses behind the scenes.

**Note**: Some methods like `removeprefix()`, `removesuffix()`, and `isascii()` require Python 3.7+ or 3.9+.

## 1. Case Conversion Methods

### `capitalize()`

Returns a string with the first character capitalized and the rest lowercased.

```python
text = "hello world"
print(text.capitalize())  # Output: "Hello world"
```

### `casefold()`

Returns a casefolded string (more aggressive than `lower()`, useful for case-insensitive comparisons).

```python
text = "HELLO WORLD"
print(text.casefold())  # Output: "hello world"

# Useful for special characters
german = "ß"
print(german.casefold())  # Output: "ss"
```

### `lower()`

Returns a string with all characters converted to lowercase.

```python
text = "HELLO World"
print(text.lower())  # Output: "hello world"
```

### `upper()`

Returns a string with all characters converted to uppercase.

```python
text = "hello world"
print(text.upper())  # Output: "HELLO WORLD"
```

### `swapcase()`

Returns a string with uppercase characters converted to lowercase and vice versa.

```python
text = "Hello WORLD"
print(text.swapcase())  # Output: "hELLO world"
```

### `title()`

Returns a string with the first character of each word capitalized.

```python
text = "hello world python"
print(text.title())  # Output: "Hello World Python"
```

## 2. Alignment and Padding Methods

### `center(width, fillchar=' ')`

Returns a centered string of specified width, padded with fillchar.

```python
text = "Python"
print(text.center(10))      # Output: "  Python  "
print(text.center(10, '*'))  # Output: "**Python**"
```

### `ljust(width, fillchar=' ')`

Returns a left-justified string of specified width.

```python
text = "Python"
print(text.ljust(10))      # Output: "Python    "
print(text.ljust(10, '-'))  # Output: "Python----"
```

### `rjust(width, fillchar=' ')`

Returns a right-justified string of specified width.

```python
text = "Python"
print(text.rjust(10))      # Output: "    Python"
print(text.rjust(10, '-'))  # Output: "----Python"
```

### `zfill(width)`

Pads a string with zeros on the left to reach specified width.

```python
text = "42"
print(text.zfill(5))    # Output: "00042"

# Works with signs
text = "-42"
print(text.zfill(5))    # Output: "-0042"
```

## 3. Trimming Methods

### `strip(chars=None)`

Removes leading and trailing characters (whitespace by default).

```python
text = "  Hello World  "
print(text.strip())         # Output: "Hello World"

text = "***Hello***"
print(text.strip('*'))      # Output: "Hello"
```

### `lstrip(chars=None)`

Removes leading characters (whitespace by default).

```python
text = "  Hello World  "
print(text.lstrip())        # Output: "Hello World  "

text = "***Hello***"
print(text.lstrip('*'))     # Output: "Hello***"
```

### `rstrip(chars=None)`

Removes trailing characters (whitespace by default).

```python
text = "  Hello World  "
print(text.rstrip())        # Output: "  Hello World"

text = "***Hello***"
print(text.rstrip('*'))     # Output: "***Hello"
```

### `removeprefix(prefix)`

Removes the specified prefix if present (Python 3.9+).

```python
text = "HelloWorld"
print(text.removeprefix("Hello"))  # Output: "World"
print(text.removeprefix("Hi"))     # Output: "HelloWorld"
```

### `removesuffix(suffix)`

Removes the specified suffix if present (Python 3.9+).

```python
text = "HelloWorld"
print(text.removesuffix("World"))  # Output: "Hello"
print(text.removesuffix("Earth"))  # Output: "HelloWorld"
```

## 4. Searching Methods

### `count(sub, start=0, end=len)`

Returns the number of non-overlapping occurrences of substring.

```python
text = "hello hello world"
print(text.count("hello"))     # Output: 2
print(text.count("l"))         # Output: 5
print(text.count("hello", 6))  # Output: 1 (starts from index 6)
```

### `find(sub, start=0, end=len)`

Returns the lowest index where substring is found, or -1 if not found.

```python
text = "hello world"
print(text.find("world"))    # Output: 6
print(text.find("python"))   # Output: -1
print(text.find("o", 5))     # Output: 7 (starts from index 5)
```

### `rfind(sub, start=0, end=len)`

Returns the highest index where substring is found, or -1 if not found.

```python
text = "hello world hello"
print(text.rfind("hello"))   # Output: 12
print(text.rfind("o"))       # Output: 15
```

### `index(sub, start=0, end=len)`

Like `find()`, but raises ValueError if substring not found.

```python
text = "hello world"
print(text.index("world"))   # Output: 6
# text.index("python")       # Raises ValueError
```

### `rindex(sub, start=0, end=len)`

Like `rfind()`, but raises ValueError if substring not found.

```python
text = "hello world hello"
print(text.rindex("hello"))  # Output: 12
```

## 5. Testing Methods

### `startswith(prefix, start=0, end=len)`

Returns True if string starts with the specified prefix.

```python
text = "hello world"
print(text.startswith("hello"))     # Output: True
print(text.startswith("world"))     # Output: False
print(text.startswith(("hi", "hello")))  # Output: True (tuple of prefixes)
```

### `endswith(suffix, start=0, end=len)`

Returns True if string ends with the specified suffix.

```python
text = "hello world"
print(text.endswith("world"))       # Output: True
print(text.endswith("hello"))       # Output: False
print(text.endswith(("earth", "world")))  # Output: True (tuple of suffixes)
```

### `isalnum()`

Returns True if all characters are alphanumeric (a-z, A-Z, 0-9).

```python
print("Hello123".isalnum())    # Output: True
print("Hello 123".isalnum())   # Output: False (contains space)
print("Hello!".isalnum())      # Output: False (contains !)
```

### `isalpha()`

Returns True if all characters are alphabetic (a-z, A-Z).

```python
print("Hello".isalpha())       # Output: True
print("Hello123".isalpha())    # Output: False
print("Hello World".isalpha()) # Output: False (contains space)
```

### `isascii()`

Returns True if all characters are ASCII (Python 3.7+).

```python
print("Hello".isascii())       # Output: True
print("Hello123".isascii())    # Output: True
print("Héllo".isascii())       # Output: False (é is not ASCII)
```

### `isdecimal()`

Returns True if all characters are decimal numbers (0-9).

```python
print("123".isdecimal())       # Output: True
print("123.45".isdecimal())    # Output: False (contains .)
print("①②③".isdecimal())       # Output: False (not decimal digits)
```

### `isdigit()`

Returns True if all characters are digits (includes superscript digits).

```python
print("123".isdigit())         # Output: True
print("①②③".isdigit())         # Output: True (unicode digits)
print("123.45".isdigit())      # Output: False (contains .)
```

### `isidentifier()`

Returns True if string is a valid Python identifier.

```python
print("variable".isidentifier())      # Output: True
print("_private".isidentifier())      # Output: True
print("2variable".isidentifier())     # Output: False (starts with digit)
print("my-var".isidentifier())        # Output: False (contains -)
```

### `islower()`

Returns True if all cased characters are lowercase.

```python
print("hello".islower())       # Output: True
print("Hello".islower())       # Output: False
print("hello123".islower())    # Output: True (digits are ignored)
```

### `isnumeric()`

Returns True if all characters are numeric (includes digit characters from other languages).

```python
print("123".isnumeric())       # Output: True
print("①②③".isnumeric())       # Output: True
print("½".isnumeric())         # Output: True (fraction character)
print("123.45".isnumeric())    # Output: False (contains .)
```

### `isprintable()`

Returns True if all characters are printable or string is empty.

```python
print("Hello World".isprintable())    # Output: True
print("Hello\nWorld".isprintable())   # Output: False (contains newline)
print("Hello\tWorld".isprintable())   # Output: False (contains tab)
```

### `isspace()`

Returns True if all characters are whitespace.

```python
print("   ".isspace())         # Output: True
print("\t\n".isspace())        # Output: True
print(" hello ".isspace())     # Output: False
```

### `istitle()`

Returns True if string is in title case.

```python
print("Hello World".istitle())     # Output: True
print("Hello world".istitle())     # Output: False
print("HELLO WORLD".istitle())     # Output: False
```

### `isupper()`

Returns True if all cased characters are uppercase.

```python
print("HELLO".isupper())       # Output: True
print("Hello".isupper())       # Output: False
print("HELLO123".isupper())    # Output: True (digits are ignored)
```

## 6. Splitting and Joining Methods

### `split(sep=None, maxsplit=-1)`

Splits string into a list using separator.

```python
text = "hello world python"
print(text.split())            # Output: ['hello', 'world', 'python']
print(text.split(' ', 1))      # Output: ['hello', 'world python']

text = "apple,banana,orange"
print(text.split(','))         # Output: ['apple', 'banana', 'orange']
```

### `rsplit(sep=None, maxsplit=-1)`

Splits string from the right.

```python
text = "hello world python programming"
print(text.rsplit(' ', 2))     # Output: ['hello world', 'python', 'programming']
```

### `splitlines(keepends=False)`

Splits string at line boundaries.

```python
text = "Hello\nWorld\rPython\r\nProgramming"
print(text.splitlines())       # Output: ['Hello', 'World', 'Python', 'Programming']
print(text.splitlines(True))   # Output: ['Hello\n', 'World\r', 'Python\r\n', 'Programming']
```

### `partition(sep)`

Splits string into three parts: before separator, separator, after separator.

```python
text = "hello-world-python"
print(text.partition('-'))     # Output: ('hello', '-', 'world-python')
print(text.partition('*'))     # Output: ('hello-world-python', '', '')
```

### `rpartition(sep)`

Like `partition()` but searches from the right.

```python
text = "hello-world-python"
print(text.rpartition('-'))    # Output: ('hello-world', '-', 'python')
```

### `join(iterable)`

Joins elements of an iterable with the string as separator.

```python
separator = ", "
words = ["apple", "banana", "orange"]
print(separator.join(words))   # Output: "apple, banana, orange"

print("-".join("HELLO"))       # Output: "H-E-L-L-O"
```

## 7. Replacement Methods

### `replace(old, new, count=-1)`

Returns string with occurrences of old replaced by new.

```python
text = "hello hello world"
print(text.replace("hello", "hi"))      # Output: "hi hi world"
print(text.replace("hello", "hi", 1))   # Output: "hi hello world"
```

### `expandtabs(tabsize=8)`

Replaces tabs with spaces.

```python
text = "Hello\tWorld\tPython"
print(text.expandtabs())       # Output: "Hello   World   Python"
print(text.expandtabs(4))      # Output: "Hello   World   Python"
```

### `translate(table)`

Returns string translated using translation table.

```python
# Create translation table
text = "Hello World"
translation = str.maketrans("lo", "12")
print(text.translate(translation))  # Output: "He112 W2r1d"

# Remove characters
translation = str.maketrans("", "", "aeiou")
print(text.translate(translation))  # Output: "Hll Wrld"
```

## 8. Formatting Methods

### `format(*args, **kwargs)`

Formats string using placeholders.

```python
text = "Hello {}, you are {} years old"
print(text.format("Alice", 25))     # Output: "Hello Alice, you are 25 years old"

text = "Hello {name}, you are {age} years old"
print(text.format(name="Bob", age=30))  # Output: "Hello Bob, you are 30 years old"
```

### `format_map(mapping)`

Like `format()` but takes a single mapping object.

```python
data = {'name': 'Charlie', 'age': 35}
text = "Hello {name}, you are {age} years old"
print(text.format_map(data))    # Output: "Hello Charlie, you are 35 years old"
```

## 9. Encoding Methods

### `encode(encoding='utf-8', errors='strict')`

Returns encoded version of string as bytes.

```python
text = "Hello World"
print(text.encode())            # Output: b'Hello World'
print(text.encode('ascii'))     # Output: b'Hello World'

text = "Héllo"
print(text.encode('utf-8'))     # Output: b'H\xc3\xa9llo'
```

## 10. Special Methods and Operators

### `__len__()`

Returns the length of the string (called by `len()` function).

```python
text = "Hello World"
print(len(text))                # Output: 11
print(text.__len__())           # Output: 11 (same as len())
```

### `maketrans(x, y=None, z=None)`

Static method that creates a translation table for `translate()`.

```python
# Simple character mapping
trans = str.maketrans("aeiou", "12345")
print("hello".translate(trans)) # Output: "h2ll4"

# With deletion characters
trans = str.maketrans("ab", "12", "xyz")
print("abcxyz".translate(trans))  # Output: "12c"
```

### Magic Methods (Used Behind the Scenes)

These methods are called automatically by Python operators and functions:

#### `__contains__(item)`

Used by the `in` operator to check if substring exists.

```python
text = "Hello World"
print("World" in text)          # Output: True (calls __contains__)
print(text.__contains__("World")) # Output: True (direct call)
```

#### `__getitem__(index)`

Used for indexing and slicing.

```python
text = "Hello"
print(text[1])                  # Output: "e" (calls __getitem__)
print(text[1:4])                # Output: "ell" (calls __getitem__)
print(text.__getitem__(1))      # Output: "e" (direct call)
```

#### `__add__(other)`

Used for string concatenation with `+`.

```python
text1 = "Hello"
text2 = " World"
print(text1 + text2)            # Output: "Hello World" (calls __add__)
print(text1.__add__(text2))     # Output: "Hello World" (direct call)
```

#### `__mul__(n)`

Used for string repetition with `*`.

```python
text = "Hi"
print(text * 3)                 # Output: "HiHiHi" (calls __mul__)
print(text.__mul__(3))          # Output: "HiHiHi" (direct call)
```

#### `__mod__(values)`

Used for old-style string formatting with `%`.

```python
text = "Hello %s, you are %d years old"
print(text % ("Alice", 25))     # Output: "Hello Alice, you are 25 years old"
print(text.__mod__(("Alice", 25))) # Same output (direct call)
```

#### `__format__(format_spec)`

Used by the `format()` built-in function and f-strings.

```python
text = "Hello"
print(format(text, '^10'))      # Output: "  Hello   " (centered)
print(f"{text:>10}")            # Output: "     Hello" (right-aligned)
```

#### Comparison Methods

Used for string comparisons:

- `__eq__(other)`: equality (==)
- `__ne__(other)`: inequality (!=)
- `__lt__(other)`: less than (<)
- `__le__(other)`: less than or equal (<=)
- `__gt__(other)`: greater than (>)
- `__ge__(other)`: greater than or equal (>=)

```python
text1 = "apple"
text2 = "banana"
print(text1 < text2)            # Output: True (calls __lt__)
print(text1.__lt__(text2))      # Output: True (direct call)
```

#### Other Special Methods

- `__repr__()`: returns string representation for debugging
- `__str__()`: returns string representation for end users
- `__hash__()`: returns hash value for use in dictionaries/sets
- `__iter__()`: returns iterator for the string

```python
text = "Hello"
print(repr(text))               # Output: "'Hello'" (calls __repr__)
print(str(text))                # Output: "Hello" (calls __str__)
print(hash(text))               # Output: (some hash value)
for char in text:               # Uses __iter__
    print(char, end="-")        # Output: H-e-l-l-o-
```

## Summary

Python provides a rich set of string methods for various operations:

### Regular Methods (47 methods):

- **Case conversion** (6): `upper()`, `lower()`, `capitalize()`, `title()`, `swapcase()`, `casefold()`
- **Alignment** (4): `center()`, `ljust()`, `rjust()`, `zfill()`
- **Trimming** (5): `strip()`, `lstrip()`, `rstrip()`, `removeprefix()`, `removesuffix()`
- **Searching** (5): `find()`, `rfind()`, `index()`, `rindex()`, `count()`
- **Testing** (16): `startswith()`, `endswith()`, `isalpha()`, `isdigit()`, `isspace()`, `isalnum()`, `isascii()`, `isdecimal()`, `isidentifier()`, `islower()`, `isnumeric()`, `isprintable()`, `istitle()`, `isupper()`
- **Splitting/Joining** (6): `split()`, `rsplit()`, `splitlines()`, `partition()`, `rpartition()`, `join()`
- **Replacement** (3): `replace()`, `translate()`, `expandtabs()`
- **Formatting** (2): `format()`, `format_map()`
- **Encoding** (1): `encode()`
- **Static method** (1): `maketrans()`

### Magic Methods (Special Methods):

- **Operator support**: `__contains__()`, `__getitem__()`, `__add__()`, `__mul__()`, `__mod__()`, `__format__()`
- **Comparison**: `__eq__()`, `__ne__()`, `__lt__()`, `__le__()`, `__gt__()`, `__ge__()`
- **Representation**: `__repr__()`, `__str__()`, `__len__()`
- **Other**: `__hash__()`, `__iter__()`

Total: **60+ string methods** make string manipulation in Python powerful and convenient!
