# Python Array-like Structures: Complete Methods Reference

This guide covers all built-in methods for Python's array-like data structures including lists, array module, bytearray, memoryview, and collections.deque with easy-to-understand examples.

## 1. Adding Elements Methods

### `append(x)`
Adds a single element to the end of the list.
```python
fruits = ['apple', 'banana']
fruits.append('orange')
print(fruits)  # Output: ['apple', 'banana', 'orange']

# Appending a list creates a nested list
fruits.append(['grape', 'mango'])
print(fruits)  # Output: ['apple', 'banana', 'orange', ['grape', 'mango']]
```

### `extend(iterable)`
Adds all elements from an iterable (list, tuple, string, etc.) to the end of the list.
```python
fruits = ['apple', 'banana']
fruits.extend(['orange', 'grape'])
print(fruits)  # Output: ['apple', 'banana', 'orange', 'grape']

# Extending with a string adds each character
numbers = [1, 2, 3]
numbers.extend('45')
print(numbers)  # Output: [1, 2, 3, '4', '5']
```

### `insert(i, x)`
Inserts an element at a specific position.
```python
fruits = ['apple', 'banana', 'orange']
fruits.insert(1, 'grape')
print(fruits)  # Output: ['apple', 'grape', 'banana', 'orange']

# Insert at beginning
fruits.insert(0, 'mango')
print(fruits)  # Output: ['mango', 'apple', 'grape', 'banana', 'orange']

# Insert at end (same as append)
fruits.insert(len(fruits), 'kiwi')
print(fruits)  # Output: ['mango', 'apple', 'grape', 'banana', 'orange', 'kiwi']
```

## 2. Removing Elements Methods

### `remove(x)`
Removes the first occurrence of the specified value. Raises ValueError if not found.
```python
fruits = ['apple', 'banana', 'orange', 'banana']
fruits.remove('banana')
print(fruits)  # Output: ['apple', 'orange', 'banana'] (only first 'banana' removed)

# Trying to remove non-existent item
# fruits.remove('grape')  # Raises ValueError
```

### `pop(i=-1)`
Removes and returns the element at the specified position (default is last element).
```python
fruits = ['apple', 'banana', 'orange']
last = fruits.pop()
print(last)    # Output: 'orange'
print(fruits)  # Output: ['apple', 'banana']

# Pop at specific index
first = fruits.pop(0)
print(first)   # Output: 'apple'
print(fruits)  # Output: ['banana']

# Pop from empty list raises IndexError
# empty = []
# empty.pop()  # Raises IndexError
```

### `clear()`
Removes all elements from the list.
```python
fruits = ['apple', 'banana', 'orange']
fruits.clear()
print(fruits)  # Output: []
```

## 3. Ordering Methods

### `sort(*, key=None, reverse=False)`
Sorts the list in place.
```python
# Basic sorting
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(numbers)  # Output: [1, 1, 2, 3, 4, 5, 9]

# Reverse sorting
numbers.sort(reverse=True)
print(numbers)  # Output: [9, 5, 4, 3, 2, 1, 1]

# Sort with custom key
fruits = ['banana', 'pie', 'Washington', 'book']
fruits.sort(key=len)
print(fruits)  # Output: ['pie', 'book', 'banana', 'Washington']

# Case-insensitive sorting
words = ['Apple', 'banana', 'Cherry', 'date']
words.sort(key=str.lower)
print(words)  # Output: ['Apple', 'banana', 'Cherry', 'date']
```

### `reverse()`
Reverses the list in place.
```python
fruits = ['apple', 'banana', 'orange']
fruits.reverse()
print(fruits)  # Output: ['orange', 'banana', 'apple']

numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # Output: [5, 4, 3, 2, 1]
```

## 4. Searching Methods

### `index(x, start=0, end=len(list))`
Returns the index of the first occurrence of the specified value.
```python
fruits = ['apple', 'banana', 'orange', 'banana']
idx = fruits.index('banana')
print(idx)  # Output: 1

# Search in a specific range
idx = fruits.index('banana', 2)  # Start from index 2
print(idx)  # Output: 3

# Value not found raises ValueError
# idx = fruits.index('grape')  # Raises ValueError
```

### `count(x)`
Returns the number of occurrences of the specified value.
```python
numbers = [1, 2, 3, 2, 2, 4, 2]
count = numbers.count(2)
print(count)  # Output: 4

fruits = ['apple', 'banana', 'orange']
count = fruits.count('grape')
print(count)  # Output: 0
```

## 5. Copying Method

### `copy()`
Returns a shallow copy of the list.
```python
original = ['apple', 'banana', 'orange']
copied = original.copy()
print(copied)  # Output: ['apple', 'banana', 'orange']

# Modifying copy doesn't affect original
copied.append('grape')
print(original)  # Output: ['apple', 'banana', 'orange']
print(copied)    # Output: ['apple', 'banana', 'orange', 'grape']

# Shallow copy warning: nested objects are still referenced
nested = [[1, 2], [3, 4]]
shallow = nested.copy()
shallow[0].append(3)
print(nested)   # Output: [[1, 2, 3], [3, 4]] (original also changed!)
```

## 6. List Operators and Other Operations

### Using `+` for Concatenation
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)  # Output: [1, 2, 3, 4, 5, 6]
```

### Using `*` for Repetition
```python
numbers = [1, 2, 3]
repeated = numbers * 3
print(repeated)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

### Using `in` for Membership Testing
```python
fruits = ['apple', 'banana', 'orange']
print('banana' in fruits)  # Output: True
print('grape' in fruits)   # Output: False
```

### Using `len()` for List Length
```python
fruits = ['apple', 'banana', 'orange']
print(len(fruits))  # Output: 3
```

### Using `del` for Deletion
```python
fruits = ['apple', 'banana', 'orange', 'grape']
del fruits[1]
print(fruits)  # Output: ['apple', 'orange', 'grape']

# Delete a slice
del fruits[1:3]
print(fruits)  # Output: ['apple']
```

## 7. List Comprehensions

A powerful way to create lists:
```python
# Basic list comprehension
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# With condition
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]

# Nested list comprehension
matrix = [[i+j for j in range(3)] for i in range(3)]
print(matrix)  # Output: [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
```

## 8. Special Methods (Magic Methods)

Lists also have special methods that work behind the scenes:

### `__len__()`
Called by `len()` function.
```python
fruits = ['apple', 'banana', 'orange']
print(len(fruits))          # Output: 3
print(fruits.__len__())     # Output: 3 (direct call)
```

### `__getitem__(index)`
Called for indexing and slicing.
```python
fruits = ['apple', 'banana', 'orange']
print(fruits[1])            # Output: 'banana' (calls __getitem__)
print(fruits.__getitem__(1)) # Output: 'banana' (direct call)
```

### `__setitem__(index, value)`
Called for item assignment.
```python
fruits = ['apple', 'banana', 'orange']
fruits[1] = 'grape'         # Calls __setitem__
print(fruits)               # Output: ['apple', 'grape', 'orange']
```

### `__delitem__(index)`
Called by `del` statement.
```python
fruits = ['apple', 'banana', 'orange']
del fruits[1]               # Calls __delitem__
print(fruits)               # Output: ['apple', 'orange']
```

### `__contains__(item)`
Called by `in` operator.
```python
fruits = ['apple', 'banana', 'orange']
print('banana' in fruits)   # Output: True (calls __contains__)
```

### `__add__(other)`
Called by `+` operator.
```python
list1 = [1, 2]
list2 = [3, 4]
print(list1 + list2)        # Output: [1, 2, 3, 4] (calls __add__)
```

### `__mul__(n)`
Called by `*` operator.
```python
numbers = [1, 2]
print(numbers * 3)          # Output: [1, 2, 1, 2, 1, 2] (calls __mul__)
```

## 9. Python Array Module (Complete Methods)

Python's `array` module provides memory-efficient arrays for basic numeric types:

### Creating Arrays
```python
from array import array

# Type codes: 'b'(signed char), 'B'(unsigned char), 'h'(short), 'H'(unsigned short),
# 'i'(int), 'I'(unsigned int), 'l'(long), 'L'(unsigned long), 'f'(float), 'd'(double)
int_array = array('i', [1, 2, 3, 4, 5])
float_array = array('d', [1.1, 2.2, 3.3])
```

### Array Methods (Similar to Lists)

#### `append(x)`
```python
arr = array('i', [1, 2, 3])
arr.append(4)
print(arr)  # Output: array('i', [1, 2, 3, 4])
```

#### `extend(iterable)`
```python
arr = array('i', [1, 2])
arr.extend([3, 4, 5])
print(arr)  # Output: array('i', [1, 2, 3, 4, 5])
```

#### `insert(i, x)`
```python
arr = array('i', [1, 3])
arr.insert(1, 2)
print(arr)  # Output: array('i', [1, 2, 3])
```

#### `remove(x)`
```python
arr = array('i', [1, 2, 3, 2])
arr.remove(2)
print(arr)  # Output: array('i', [1, 3, 2])
```

#### `pop(i=-1)`
```python
arr = array('i', [1, 2, 3])
val = arr.pop()
print(val)  # Output: 3
print(arr)  # Output: array('i', [1, 2])
```

#### `index(x)`
```python
arr = array('i', [1, 2, 3, 2])
idx = arr.index(2)
print(idx)  # Output: 1
```

#### `count(x)`
```python
arr = array('i', [1, 2, 3, 2, 2])
cnt = arr.count(2)
print(cnt)  # Output: 3
```

#### `reverse()`
```python
arr = array('i', [1, 2, 3])
arr.reverse()
print(arr)  # Output: array('i', [3, 2, 1])
```

### Array-Specific Methods

#### `buffer_info()`
Returns (address, length) tuple giving current memory info.
```python
arr = array('i', [1, 2, 3])
info = arr.buffer_info()
print(info)  # Output: (address, 3)
```

#### `byteswap()`
Swaps the byte order of all items (useful for reading data from different endianness).
```python
arr = array('i', [1, 256])
arr.byteswap()
# Byte order is swapped for each element
```

#### `tolist()`
Converts array to ordinary list.
```python
arr = array('i', [1, 2, 3])
lst = arr.tolist()
print(lst)  # Output: [1, 2, 3]
print(type(lst))  # Output: <class 'list'>
```

#### `tobytes()`
Converts array to bytes object.
```python
arr = array('i', [1, 2, 3])
bytes_obj = arr.tobytes()
print(bytes_obj)  # Output: b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00'
```

#### `frombytes(bytes)`
Appends items from bytes object.
```python
arr = array('i')
arr.frombytes(b'\x01\x00\x00\x00\x02\x00\x00\x00')
print(arr)  # Output: array('i', [1, 2])
```

#### `tofile(file)`
Writes array to a file object.
```python
arr = array('i', [1, 2, 3])
with open('array.bin', 'wb') as f:
    arr.tofile(f)
```

#### `fromfile(file, n)`
Reads n items from file object and appends.
```python
arr = array('i')
with open('array.bin', 'rb') as f:
    arr.fromfile(f, 3)  # Read 3 integers
print(arr)  # Output: array('i', [1, 2, 3])
```

#### `fromlist(list)`
Appends items from list.
```python
arr = array('i', [1, 2])
arr.fromlist([3, 4, 5])
print(arr)  # Output: array('i', [1, 2, 3, 4, 5])
```

### Array Attributes

#### `typecode`
The type code character used to create the array.
```python
arr = array('i', [1, 2, 3])
print(arr.typecode)  # Output: 'i'
```

#### `itemsize`
The size in bytes of one array item.
```python
arr = array('i', [1, 2, 3])
print(arr.itemsize)  # Output: 4 (on most systems)

arr_double = array('d', [1.0])
print(arr_double.itemsize)  # Output: 8
```

## 10. Other Built-in Array-like Structures

### bytearray
Mutable sequence of bytes.
```python
# Create bytearray
ba = bytearray(b'hello')
ba = bytearray('hello', 'utf-8')
ba = bytearray([72, 101, 108, 108, 111])

# Methods similar to lists
ba.append(33)           # Append byte value
ba.extend(b' world')    # Extend with bytes
ba.insert(0, 72)        # Insert byte
ba.remove(108)          # Remove first occurrence
ba.pop()                # Remove and return last
ba.reverse()            # Reverse in place
ba.clear()              # Remove all

# Additional methods
ba.decode('utf-8')      # Convert to string
ba.hex()                # Convert to hex string
ba.count(108)           # Count occurrences
ba.index(101)           # Find index

# Bytearray is mutable
ba[0] = 74              # Change individual bytes
```

### memoryview
Creates a view of another object's memory without copying.
```python
# Create memoryview from bytes
data = bytearray(b'hello world')
mv = memoryview(data)

# Access and modify through view
print(mv[0])            # Output: 104 (ASCII 'h')
mv[0] = 72              # Modify original data
print(data)             # Output: bytearray(b'Hello world')

# Slicing creates new view
mv_slice = mv[0:5]
print(bytes(mv_slice))  # Output: b'Hello'

# Methods
mv.tobytes()            # Convert to bytes
mv.tolist()             # Convert to list
mv.hex()                # Convert to hex string
```

### collections.deque
Double-ended queue optimized for appends/pops from both ends.
```python
from collections import deque

# Create deque
dq = deque([1, 2, 3])
dq = deque([1, 2, 3], maxlen=5)  # Fixed size

# Methods
dq.append(4)            # Add to right
dq.appendleft(0)        # Add to left
dq.extend([5, 6])       # Extend right
dq.extendleft([-2, -1]) # Extend left
dq.pop()                # Remove from right
dq.popleft()            # Remove from left
dq.rotate(2)            # Rotate right by 2
dq.rotate(-1)           # Rotate left by 1
dq.reverse()            # Reverse in place
dq.clear()              # Remove all
dq.count(2)             # Count occurrences
dq.index(3)             # Find index
dq.remove(2)            # Remove first occurrence

# Deque example
dq = deque([1, 2, 3, 4])
dq.rotate(1)
print(dq)  # Output: deque([4, 1, 2, 3])
```

## Summary

### Python List Methods (11 core methods):
- **Adding**: `append()`, `extend()`, `insert()`
- **Removing**: `remove()`, `pop()`, `clear()`
- **Ordering**: `sort()`, `reverse()`
- **Searching**: `index()`, `count()`
- **Copying**: `copy()`

### Array Module Methods (17 methods + 2 attributes):
- **List-like methods** (8): `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `index()`, `count()`, `reverse()`
- **Conversion methods** (6): `tolist()`, `tobytes()`, `tofile()`, `fromlist()`, `frombytes()`, `fromfile()`
- **Special methods** (2): `buffer_info()`, `byteswap()`
- **Attributes** (2): `typecode`, `itemsize`

### Bytearray Methods (20+ methods):
- **List-like**: `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `reverse()`, `clear()`, `count()`, `index()`
- **Byte-specific**: `decode()`, `hex()`, `fromhex()`, `translate()`, `maketrans()`
- **And more**: Similar to both lists and bytes objects

### Memoryview Methods (10+ methods):
- **Conversion**: `tobytes()`, `tolist()`, `hex()`
- **Properties**: `format`, `itemsize`, `ndim`, `shape`, `strides`
- **Methods**: `cast()`, `release()`, and more

### collections.deque Methods (16 methods):
- **Double-ended**: `append()`, `appendleft()`, `pop()`, `popleft()`
- **Extension**: `extend()`, `extendleft()`
- **Special**: `rotate()`, `reverse()`, `maxlen` property
- **List-like**: `clear()`, `count()`, `index()`, `remove()`

**Total**: Python provides 75+ methods across various array-like structures, each optimized for different use cases:
- **Lists**: General-purpose, dynamic arrays
- **array.array**: Memory-efficient for numeric types
- **bytearray**: Mutable byte sequences
- **memoryview**: Zero-copy views of data
- **collections.deque**: Efficient double-ended operations