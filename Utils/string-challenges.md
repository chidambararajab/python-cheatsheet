# 30 String Programming Challenges in Python

## 1. Reverse a String (Easy)

**Problem:** Reverse the given string.

**Sample Input:** `"hello"`  
**Sample Output:** `"olleh"`

```python
def reverse_string(s):
    """
    Time Complexity: O(n) where n is the length of string
    Space Complexity: O(n) for creating new string

    Explanation:
    - Python's slicing [::-1] creates a new string in reverse order
    - Alternative methods: ''.join(reversed(s)) or loop from end
    """
    return s[::-1]

# Test
print(reverse_string("hello"))  # Output: "olleh"
```

## 2. Check Palindrome (Easy)

**Problem:** Check if a string is a palindrome (reads same forwards and backwards).

**Sample Input:** `"racecar"`  
**Sample Output:** `True`

```python
def is_palindrome(s):
    """
    Time Complexity: O(n) where n is the length of string
    Space Complexity: O(n) for creating reversed string

    Explanation:
    - Compare string with its reverse
    - For case-insensitive: s.lower() == s.lower()[::-1]
    - Alternative: Use two pointers from start and end
    """
    return s == s[::-1]

# Test
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False
```

## 3. Count Vowels (Easy)

**Problem:** Count the number of vowels in a string.

**Sample Input:** `"hello world"`  
**Sample Output:** `3`

```python
def count_vowels(s):
    """
    Time Complexity: O(n) where n is the length of string
    Space Complexity: O(1) constant space

    Explanation:
    - Define vowels set for O(1) lookup
    - Iterate through string once
    - Check each character against vowels set
    - Case-insensitive by converting to lower
    """
    vowels = set('aeiouAEIOU')
    return sum(1 for char in s if char in vowels)

# Test
print(count_vowels("hello world"))  # Output: 3
```

## 4. First Non-Repeating Character (Medium)

**Problem:** Find the first non-repeating character in a string.

**Sample Input:** `"leetcode"`  
**Sample Output:** `"l"`

```python
def first_non_repeating(s):
    """
    Time Complexity: O(n) where n is the length of string
    Space Complexity: O(k) where k is unique characters (at most 26 for lowercase)

    Explanation:
    - First pass: Count frequency of each character
    - Second pass: Find first character with frequency 1
    - Using dict maintains insertion order in Python 3.7+
    """
    char_count = {}

    # Count frequencies
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Find first non-repeating
    for char in s:
        if char_count[char] == 1:
            return char

    return ""  # No non-repeating character

# Test
print(first_non_repeating("leetcode"))  # Output: "l"
print(first_non_repeating("aabbcc"))    # Output: ""
```

## 5. Anagram Check (Easy)

**Problem:** Check if two strings are anagrams of each other.

**Sample Input:** `"listen", "silent"`  
**Sample Output:** `True`

```python
def are_anagrams(s1, s2):
    """
    Time Complexity: O(n log n) where n is the length of strings
    Space Complexity: O(n) for sorted strings

    Explanation:
    - Anagrams have same characters in different order
    - Sort both strings and compare
    - Alternative: Use Counter for O(n) time complexity
    """
    return sorted(s1) == sorted(s2)

# Alternative O(n) solution
from collections import Counter
def are_anagrams_v2(s1, s2):
    """
    Time Complexity: O(n) where n is the length of strings
    Space Complexity: O(k) where k is unique characters
    """
    return Counter(s1) == Counter(s2)

# Test
print(are_anagrams("listen", "silent"))  # Output: True
print(are_anagrams("hello", "world"))    # Output: False
```

## 6. String Compression (Medium)

**Problem:** Compress consecutive characters: "aabcccccaaa" → "a2b1c5a3"

**Sample Input:** `"aabcccccaaa"`  
**Sample Output:** `"a2b1c5a3"`

```python
def compress_string(s):
    """
    Time Complexity: O(n) where n is the length of string
    Space Complexity: O(n) for result string

    Explanation:
    - Track current character and its count
    - When character changes, append previous char and count
    - Handle last group after loop
    - Edge case: empty string
    """
    if not s:
        return ""

    result = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append(s[i-1] + str(count))
            count = 1

    # Don't forget the last group
    result.append(s[-1] + str(count))

    return ''.join(result)

# Test
print(compress_string("aabcccccaaa"))  # Output: "a2b1c5a3"
print(compress_string("abc"))         # Output: "a1b1c1"
```

## 7. Longest Common Prefix (Medium)

**Problem:** Find the longest common prefix among an array of strings.

**Sample Input:** `["flower", "flow", "flight"]`  
**Sample Output:** `"fl"`

```python
def longest_common_prefix(strs):
    """
    Time Complexity: O(S) where S is sum of all characters in all strings
    Space Complexity: O(1) constant space

    Explanation:
    - Compare characters at same position across all strings
    - Stop when mismatch found or any string ends
    - Vertical scanning approach
    - Edge case: empty array returns ""
    """
    if not strs:
        return ""

    # Find minimum length to avoid index out of range
    min_len = min(len(s) for s in strs)

    for i in range(min_len):
        char = strs[0][i]
        for s in strs[1:]:
            if s[i] != char:
                return strs[0][:i]

    return strs[0][:min_len]

# Test
print(longest_common_prefix(["flower", "flow", "flight"]))  # Output: "fl"
print(longest_common_prefix(["dog", "racecar", "car"]))    # Output: ""
```

## 8. Valid Parentheses (Medium)

**Problem:** Check if parentheses are balanced.

**Sample Input:** `"({[]})"`  
**Sample Output:** `True`

```python
def is_valid_parentheses(s):
    """
    Time Complexity: O(n) where n is the length of string
    Space Complexity: O(n) for stack in worst case

    Explanation:
    - Use stack to track opening brackets
    - When closing bracket found, check if matches top of stack
    - String is valid if stack is empty at end
    - HashMap for matching pairs
    """
    stack = []
    pairs = {'(': ')', '{': '}', '[': ']'}

    for char in s:
        if char in pairs:  # Opening bracket
            stack.append(char)
        elif char in pairs.values():  # Closing bracket
            if not stack or pairs[stack.pop()] != char:
                return False

    return len(stack) == 0

# Test
print(is_valid_parentheses("({[]})"))   # Output: True
print(is_valid_parentheses("([)]"))     # Output: False
```

## 9. Remove Duplicates (Easy)

**Problem:** Remove duplicate characters from string, keeping first occurrence.

**Sample Input:** `"programming"`  
**Sample Output:** `"progamin"`

```python
def remove_duplicates(s):
    """
    Time Complexity: O(n) where n is the length of string
    Space Complexity: O(k) where k is unique characters

    Explanation:
    - Use set to track seen characters
    - Build result with only first occurrences
    - Maintains original order
    - Alternative: Use dict.fromkeys() for Python 3.7+
    """
    seen = set()
    result = []

    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)

    return ''.join(result)

# Test
print(remove_duplicates("programming"))  # Output: "progamin"
print(remove_duplicates("hello"))       # Output: "helo"
```

## 10. Rotate String (Medium)

**Problem:** Check if string s2 is a rotation of s1.

**Sample Input:** `"abcde", "cdeab"`  
**Sample Output:** `True`

```python
def is_rotation(s1, s2):
    """
    Time Complexity: O(n) where n is the length of strings
    Space Complexity: O(n) for concatenated string

    Explanation:
    - Key insight: s2 is rotation of s1 if s2 is substring of s1+s1
    - Example: "abcde" + "abcde" = "abcdeabcde" contains "cdeab"
    - Check lengths first for quick rejection
    - Handle empty strings
    """
    if len(s1) != len(s2):
        return False

    if not s1:  # Both empty
        return True

    return s2 in s1 + s1

# Test
print(is_rotation("abcde", "cdeab"))  # Output: True
print(is_rotation("abcde", "abced"))  # Output: False
```

## 11. Word Reversal (Medium)

**Problem:** Reverse words in a string while maintaining word order.

**Sample Input:** `"hello world python"`  
**Sample Output:** `"olleh dlrow nohtyp"`

```python
def reverse_words(s):
    """
    Time Complexity: O(n) where n is the length of string
    Space Complexity: O(n) for result

    Explanation:
    - Split string into words
    - Reverse each word individually
    - Join back with spaces
    - Handles multiple spaces with split()
    """
    return ' '.join(word[::-1] for word in s.split())

# Test
print(reverse_words("hello world python"))  # Output: "olleh dlrow nohtyp"
print(reverse_words("The quick brown"))     # Output: "ehT kciuq nworb"
```

## 12. Character Frequency Sort (Medium)

**Problem:** Sort characters by frequency, highest first.

**Sample Input:** `"tree"`  
**Sample Output:** `"eert" or "eetr"`

```python
def frequency_sort(s):
    """
    Time Complexity: O(n log n) where n is the length of string
    Space Complexity: O(k) where k is unique characters

    Explanation:
    - Count frequency of each character
    - Sort by frequency (descending) then by character
    - Build result string with sorted characters
    - Multiple valid outputs possible
    """
    from collections import Counter

    char_count = Counter(s)
    # Sort by frequency (descending), then by character
    sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))

    result = []
    for char, count in sorted_chars:
        result.append(char * count)

    return ''.join(result)

# Test
print(frequency_sort("tree"))      # Output: "eert" or "eetr"
print(frequency_sort("cccaaa"))    # Output: "aaaccc" or "cccaaa"
```

## 13. Substring Search (Easy)

**Problem:** Find all occurrences of a pattern in a string.

**Sample Input:** `"ababcababa", "aba"`  
**Sample Output:** `[0, 5, 7]`

```python
def find_all_occurrences(text, pattern):
    """
    Time Complexity: O(n*m) where n is text length, m is pattern length
    Space Complexity: O(k) where k is number of occurrences

    Explanation:
    - Slide pattern over text
    - Check for match at each position
    - Store starting indices of matches
    - Handle overlapping matches
    """
    if not pattern:
        return []

    occurrences = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            occurrences.append(i)

    return occurrences

# Test
print(find_all_occurrences("ababcababa", "aba"))  # Output: [0, 5, 7]
print(find_all_occurrences("hello", "ll"))        # Output: [2]
```

## 14. String to Integer (atoi) (Medium)

**Problem:** Convert string to integer, handling signs and invalid characters.

**Sample Input:** `"  -42"`  
**Sample Output:** `-42`

```python
def my_atoi(s):
    """
    Time Complexity: O(n) where n is the length of string
    Space Complexity: O(1) constant space

    Explanation:
    - Skip leading whitespace
    - Check for optional sign
    - Convert consecutive digits
    - Handle overflow (32-bit integer limits)
    - Stop at first non-digit
    """
    s = s.strip()  # Remove leading/trailing whitespace

    if not s:
        return 0

    sign = 1
    index = 0

    # Check sign
    if s[0] in '+-':
        sign = -1 if s[0] == '-' else 1
        index = 1

    result = 0
    while index < len(s) and s[index].isdigit():
        result = result * 10 + int(s[index])
        index += 1

    # Apply sign and handle overflow
    result *= sign

    # 32-bit integer limits
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    if result > INT_MAX:
        return INT_MAX
    if result < INT_MIN:
        return INT_MIN

    return result

# Test
print(my_atoi("  -42"))      # Output: -42
print(my_atoi("4193 with"))  # Output: 4193
```

## 15. Longest Substring Without Repeating Characters (Hard)

**Problem:** Find length of longest substring without repeating characters.

**Sample Input:** `"abcabcbb"`  
**Sample Output:** `3` (substring "abc")

```python
def length_of_longest_substring(s):
    """
    Time Complexity: O(n) where n is the length of string
    Space Complexity: O(min(n, k)) where k is size of character set

    Explanation:
    - Use sliding window with two pointers
    - Track characters in current window using set
    - Expand window by moving right pointer
    - Contract window when duplicate found
    - Update max length at each step
    """
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        # Contract window until no duplicate
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length

# Test
print(length_of_longest_substring("abcabcbb"))  # Output: 3
print(length_of_longest_substring("bbbbb"))     # Output: 1
```

## 16. Group Anagrams (Medium)

**Problem:** Group strings that are anagrams of each other.

**Sample Input:** `["eat", "tea", "tan", "ate", "nat", "bat"]`  
**Sample Output:** `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`

```python
def group_anagrams(strs):
    """
    Time Complexity: O(n * k log k) where n is number of strings, k is max length
    Space Complexity: O(n * k) for storing results

    Explanation:
    - Use sorted string as key for anagram groups
    - All anagrams will have same sorted string
    - Use defaultdict to group strings
    - Return values as list of lists
    """
    from collections import defaultdict

    anagram_groups = defaultdict(list)

    for s in strs:
        # Use sorted string as key
        key = ''.join(sorted(s))
        anagram_groups[key].append(s)

    return list(anagram_groups.values())

# Test
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

## 17. Check Permutation (Medium)

**Problem:** Check if s2 contains any permutation of s1.

**Sample Input:** `s1 = "ab", s2 = "eidbaooo"`  
**Sample Output:** `True`

```python
def check_inclusion(s1, s2):
    """
    Time Complexity: O(n) where n is length of s2
    Space Complexity: O(1) - at most 26 lowercase letters

    Explanation:
    - Use sliding window of size len(s1)
    - Compare character frequencies in window with s1
    - Slide window and update frequencies
    - O(1) comparison since limited to 26 characters
    """
    from collections import Counter

    if len(s1) > len(s2):
        return False

    # Count characters in s1
    s1_count = Counter(s1)
    window_count = Counter()

    # Initialize window
    for i in range(len(s1)):
        window_count[s2[i]] += 1

    # Check initial window
    if window_count == s1_count:
        return True

    # Slide window
    for i in range(len(s1), len(s2)):
        # Add new character
        window_count[s2[i]] += 1

        # Remove old character
        old_char = s2[i - len(s1)]
        window_count[old_char] -= 1
        if window_count[old_char] == 0:
            del window_count[old_char]

        # Check if permutation found
        if window_count == s1_count:
            return True

    return False

# Test
print(check_inclusion("ab", "eidbaooo"))  # Output: True
print(check_inclusion("ab", "eidboaoo"))  # Output: False
```

## 18. Minimum Window Substring (Hard)

**Problem:** Find minimum window in s that contains all characters of t.

**Sample Input:** `s = "ADOBECODEBANC", t = "ABC"`  
**Sample Output:** `"BANC"`

```python
def min_window(s, t):
    """
    Time Complexity: O(n) where n is length of s
    Space Complexity: O(k) where k is unique characters in t

    Explanation:
    - Use two pointers to form a window
    - Expand window until all chars of t are included
    - Contract window to find minimum
    - Track character frequencies and required matches
    - Update minimum window when valid window found
    """
    from collections import Counter

    if not s or not t:
        return ""

    # Count characters in t
    t_count = Counter(t)
    required = len(t_count)

    # Sliding window
    left = right = 0
    formed = 0
    window_counts = {}

    # Result
    min_len = float('inf')
    min_left = 0

    while right < len(s):
        # Expand window
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1

        if char in t_count and window_counts[char] == t_count[char]:
            formed += 1

        # Contract window
        while left <= right and formed == required:
            # Update result
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_left = left

            # Remove from left
            char = s[left]
            window_counts[char] -= 1
            if char in t_count and window_counts[char] < t_count[char]:
                formed -= 1

            left += 1

        right += 1

    return "" if min_len == float('inf') else s[min_left:min_left + min_len]

# Test
print(min_window("ADOBECODEBANC", "ABC"))  # Output: "BANC"
print(min_window("a", "a"))                # Output: "a"
```

## 19. Decode String (Medium)

**Problem:** Decode string with pattern k[encoded_string].

**Sample Input:** `"3[a2[c]]"`  
**Sample Output:** `"accaccacc"`

```python
def decode_string(s):
    """
    Time Complexity: O(n) where n is length of decoded string
    Space Complexity: O(n) for stack

    Explanation:
    - Use stack to handle nested patterns
    - When '[' found, push current string and number
    - When ']' found, pop and repeat string
    - Build result character by character
    - Handle multi-digit numbers
    """
    stack = []
    current_string = ""
    current_num = 0

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            # Push current state
            stack.append((current_string, current_num))
            current_string = ""
            current_num = 0
        elif char == ']':
            # Pop and decode
            prev_string, num = stack.pop()
            current_string = prev_string + current_string * num
        else:
            current_string += char

    return current_string

# Test
print(decode_string("3[a2[c]]"))     # Output: "accaccacc"
print(decode_string("2[abc]3[cd]"))  # Output: "abcabccdcdcd"
```

## 20. Edit Distance (Hard)

**Problem:** Find minimum operations to convert word1 to word2.

**Sample Input:** `word1 = "horse", word2 = "ros"`  
**Sample Output:** `3`

```python
def min_distance(word1, word2):
    """
    Time Complexity: O(m*n) where m, n are lengths of words
    Space Complexity: O(m*n) for DP table

    Explanation:
    - Dynamic Programming approach
    - dp[i][j] = min operations to convert word1[:i] to word2[:j]
    - Three operations: insert, delete, replace
    - Base cases: empty string conversions
    - Build solution bottom-up
    """
    m, n = len(word1), len(word2)

    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases
    for i in range(m + 1):
        dp[i][0] = i  # Delete all characters
    for j in range(n + 1):
        dp[0][j] = j  # Insert all characters

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]  # No operation needed
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # Delete
                    dp[i][j-1],    # Insert
                    dp[i-1][j-1]   # Replace
                )

    return dp[m][n]

# Test
print(min_distance("horse", "ros"))       # Output: 3
print(min_distance("intention", "execution"))  # Output: 5
```

## 21. Zigzag Conversion (Medium)

**Problem:** Convert string to zigzag pattern with given rows.

**Sample Input:** `s = "PAYPALISHIRING", numRows = 3`  
**Sample Output:** `"PAHNAPLSIIGYIR"`

```python
def convert_zigzag(s, numRows):
    """
    Time Complexity: O(n) where n is length of string
    Space Complexity: O(n) for storing result

    Explanation:
    - Simulate zigzag pattern by tracking direction
    - Use array of strings for each row
    - Change direction at top and bottom
    - Join all rows at the end
    Pattern for numRows=3:
    P   A   H   N
    A P L S I I G
    Y   I   R
    """
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [''] * numRows
    current_row = 0
    going_down = False

    for char in s:
        rows[current_row] += char

        # Change direction at boundaries
        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down

        current_row += 1 if going_down else -1

    return ''.join(rows)

# Test
print(convert_zigzag("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
print(convert_zigzag("PAYPALISHIRING", 4))  # Output: "PINALSIGYAHRPI"
```

## 22. Word Break (Medium)

**Problem:** Check if string can be segmented into dictionary words.

**Sample Input:** `s = "leetcode", wordDict = ["leet", "code"]`  
**Sample Output:** `True`

```python
def word_break(s, wordDict):
    """
    Time Complexity: O(n²) where n is length of string
    Space Complexity: O(n) for DP array

    Explanation:
    - Dynamic Programming approach
    - dp[i] = True if s[:i] can be segmented
    - For each position, check all possible words ending there
    - Use set for O(1) word lookup
    - Build solution from left to right
    """
    word_set = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True  # Empty string

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[len(s)]

# Test
print(word_break("leetcode", ["leet", "code"]))     # Output: True
print(word_break("applepenapple", ["apple", "pen"]))  # Output: True
```

## 23. String Multiplication (Medium)

**Problem:** Multiply two strings representing non-negative integers.

**Sample Input:** `num1 = "123", num2 = "456"`  
**Sample Output:** `"56088"`

```python
def multiply(num1, num2):
    """
    Time Complexity: O(m*n) where m, n are lengths of numbers
    Space Complexity: O(m+n) for result

    Explanation:
    - Simulate grade school multiplication
    - Multiply each digit and track position
    - Result length is at most m + n
    - Handle carries properly
    - Remove leading zeros
    """
    if num1 == "0" or num2 == "0":
        return "0"

    m, n = len(num1), len(num2)
    result = [0] * (m + n)

    # Reverse for easier processing
    num1 = num1[::-1]
    num2 = num2[::-1]

    # Multiply each digit
    for i in range(m):
        for j in range(n):
            # Multiply digits
            mul = int(num1[i]) * int(num2[j])
            # Add to result
            result[i + j] += mul
            # Handle carry
            result[i + j + 1] += result[i + j] // 10
            result[i + j] %= 10

    # Convert to string and remove leading zeros
    result = result[::-1]
    start = 0
    while start < len(result) - 1 and result[start] == 0:
        start += 1

    return ''.join(map(str, result[start:]))

# Test
print(multiply("123", "456"))  # Output: "56088"
print(multiply("2", "3"))      # Output: "6"
```

## 24. Implement strStr() (Easy)

**Problem:** Find first occurrence of needle in haystack.

**Sample Input:** `haystack = "hello", needle = "ll"`  
**Sample Output:** `2`

```python
def strStr(haystack, needle):
    """
    Time Complexity: O(n*m) where n is haystack length, m is needle length
    Space Complexity: O(1) constant space

    Explanation:
    - Naive approach: check at each position
    - For each position, compare needle characters
    - Return first match position
    - Return -1 if not found
    - Handle edge cases (empty needle)
    """
    if not needle:
        return 0

    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i

    return -1

# KMP Algorithm - O(n+m) solution
def strStr_KMP(haystack, needle):
    """
    Time Complexity: O(n+m) where n is haystack length, m is needle length
    Space Complexity: O(m) for pattern table
    """
    if not needle:
        return 0

    # Build pattern table
    def build_pattern(needle):
        pattern = [0] * len(needle)
        j = 0

        for i in range(1, len(needle)):
            while j > 0 and needle[i] != needle[j]:
                j = pattern[j-1]

            if needle[i] == needle[j]:
                j += 1
            pattern[i] = j

        return pattern

    pattern = build_pattern(needle)
    j = 0

    for i in range(len(haystack)):
        while j > 0 and haystack[i] != needle[j]:
            j = pattern[j-1]

        if haystack[i] == needle[j]:
            j += 1

        if j == len(needle):
            return i - j + 1

    return -1

# Test
print(strStr("hello", "ll"))     # Output: 2
print(strStr("aaaaa", "bba"))    # Output: -1
```

## 25. Longest Palindromic Substring (Medium)

**Problem:** Find the longest palindromic substring.

**Sample Input:** `"babad"`  
**Sample Output:** `"bab" or "aba"`

```python
def longest_palindrome(s):
    """
    Time Complexity: O(n²) where n is length of string
    Space Complexity: O(1) constant space

    Explanation:
    - Expand around center approach
    - For each character, treat as center and expand
    - Consider both odd and even length palindromes
    - Track longest palindrome found
    - Alternative: Dynamic Programming O(n²) space
    """
    if not s:
        return ""

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    start = 0
    max_len = 0

    for i in range(len(s)):
        # Odd length palindromes
        len1 = expand_around_center(i, i)
        # Even length palindromes
        len2 = expand_around_center(i, i + 1)

        curr_len = max(len1, len2)
        if curr_len > max_len:
            max_len = curr_len
            start = i - (curr_len - 1) // 2

    return s[start:start + max_len]

# Test
print(longest_palindrome("babad"))  # Output: "bab" or "aba"
print(longest_palindrome("cbbd"))   # Output: "bb"
```

## 26. Roman to Integer (Easy)

**Problem:** Convert Roman numeral to integer.

**Sample Input:** `"MCMXCIV"`  
**Sample Output:** `1994`

```python
def roman_to_int(s):
    """
    Time Complexity: O(n) where n is length of string
    Space Complexity: O(1) constant space

    Explanation:
    - Map each Roman symbol to its value
    - If current value < next value, subtract (like IV = 4)
    - Otherwise add to result
    - Process from left to right
    - Handle subtractive notation
    """
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    result = 0
    n = len(s)

    for i in range(n):
        # If current value is less than next value, subtract
        if i < n - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
            result -= roman_map[s[i]]
        else:
            result += roman_map[s[i]]

    return result

# Test
print(roman_to_int("MCMXCIV"))  # Output: 1994 (M=1000, CM=900, XC=90, IV=4)
print(roman_to_int("LVIII"))    # Output: 58 (L=50, V=5, III=3)
```

## 27. Text Justification (Hard)

**Problem:** Format text with exact line width, fully justified.

**Sample Input:** `words = ["This", "is", "an", "example"], maxWidth = 16`  
**Sample Output:** `["This    is    an", "example        "]`

```python
def full_justify(words, maxWidth):
    """
    Time Complexity: O(n) where n is total characters in all words
    Space Complexity: O(n) for result

    Explanation:
    - Greedy approach: fit as many words per line
    - Distribute spaces evenly between words
    - Extra spaces go to leftmost gaps
    - Last line is left-justified
    - Handle single word lines
    """
    result = []
    current_line = []
    current_length = 0

    for word in words:
        # Check if word fits in current line
        if current_length + len(word) + len(current_line) > maxWidth:
            # Justify current line
            if len(current_line) == 1:
                # Single word - left justify
                result.append(current_line[0] + ' ' * (maxWidth - len(current_line[0])))
            else:
                # Multiple words - full justify
                total_spaces = maxWidth - current_length
                gaps = len(current_line) - 1
                spaces_per_gap = total_spaces // gaps
                extra_spaces = total_spaces % gaps

                line = ""
                for i, w in enumerate(current_line[:-1]):
                    line += w
                    line += ' ' * spaces_per_gap
                    if i < extra_spaces:
                        line += ' '
                line += current_line[-1]
                result.append(line)

            # Start new line
            current_line = [word]
            current_length = len(word)
        else:
            current_line.append(word)
            current_length += len(word)

    # Handle last line (left-justified)
    last_line = ' '.join(current_line)
    result.append(last_line + ' ' * (maxWidth - len(last_line)))

    return result

# Test
print(full_justify(["This", "is", "an", "example"], 16))
# Output: ["This    is    an", "example        "]
```

## 28. Wildcard Matching (Hard)

**Problem:** Implement wildcard pattern matching with '?' and '\*'.

**Sample Input:** `s = "aa", p = "*"`  
**Sample Output:** `True`

```python
def is_match(s, p):
    """
    Time Complexity: O(m*n) where m, n are lengths of string and pattern
    Space Complexity: O(m*n) for DP table

    Explanation:
    - Dynamic Programming approach
    - dp[i][j] = True if s[:i] matches p[:j]
    - '?' matches any single character
    - '*' matches any sequence (including empty)
    - Build solution bottom-up
    """
    m, n = len(s), len(p)

    # Create DP table
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    # Empty pattern matches empty string
    dp[0][0] = True

    # Handle patterns with * at beginning
    for j in range(1, n + 1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-1]

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j-1] == '*':
                # * can match empty or any sequence
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
            elif p[j-1] == '?' or s[i-1] == p[j-1]:
                # Character match or ?
                dp[i][j] = dp[i-1][j-1]

    return dp[m][n]

# Test
print(is_match("aa", "*"))        # Output: True
print(is_match("aa", "a"))        # Output: False
print(is_match("cb", "?a"))       # Output: False
```

## 29. Find All Palindromes (Medium)

**Problem:** Find all palindromic substrings in a string.

**Sample Input:** `"aaa"`  
**Sample Output:** `["a", "a", "a", "aa", "aa", "aaa"]`

```python
def find_all_palindromes(s):
    """
    Time Complexity: O(n²) where n is length of string
    Space Complexity: O(n²) for storing all palindromes

    Explanation:
    - Expand around center for each possible center
    - Consider both odd and even length palindromes
    - Store all valid palindromes found
    - Alternative: Use DP to check all substrings
    """
    def expand_around_center(left, right):
        palindromes = []
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindromes.append(s[left:right+1])
            left -= 1
            right += 1
        return palindromes

    result = []

    for i in range(len(s)):
        # Odd length palindromes
        result.extend(expand_around_center(i, i))
        # Even length palindromes
        result.extend(expand_around_center(i, i + 1))

    return result

# Alternative: Count palindromic substrings
def count_palindromic_substrings(s):
    """
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    def count_around_center(left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count

    total = 0
    for i in range(len(s)):
        total += count_around_center(i, i)      # Odd length
        total += count_around_center(i, i + 1)  # Even length

    return total

# Test
print(find_all_palindromes("aaa"))  # Output: ["a", "a", "a", "aa", "aa", "aaa"]
print(count_palindromic_substrings("abc"))  # Output: 3
```

## 30. String Interleaving (Hard)

**Problem:** Check if s3 is formed by interleaving s1 and s2.

**Sample Input:** `s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"`  
**Sample Output:** `True`

```python
def is_interleave(s1, s2, s3):
    """
    Time Complexity: O(m*n) where m, n are lengths of s1, s2
    Space Complexity: O(m*n) for DP table

    Explanation:
    - Dynamic Programming approach
    - dp[i][j] = True if s3[:i+j] is interleaving of s1[:i] and s2[:j]
    - Can take character from s1 or s2 at each step
    - Length constraint: len(s1) + len(s2) must equal len(s3)
    - Build solution checking all possibilities
    """
    if len(s1) + len(s2) != len(s3):
        return False

    m, n = len(s1), len(s2)

    # Create DP table
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    # Base case: empty strings
    dp[0][0] = True

    # First row: s1 is empty
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

    # First column: s2 is empty
    for i in range(1, m + 1):
        dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Can we take from s1?
            if s1[i-1] == s3[i+j-1]:
                dp[i][j] |= dp[i-1][j]

            # Can we take from s2?
            if s2[j-1] == s3[i+j-1]:
                dp[i][j] |= dp[i][j-1]

    return dp[m][n]

# Test
print(is_interleave("aabcc", "dbbca", "aadbbcbcac"))  # Output: True
print(is_interleave("aabcc", "dbbca", "aadbbbaccc"))  # Output: False
```

## Summary of Time Complexities:

- **O(n)**: Problems 1-4, 9, 11, 13-15, 17, 21, 24, 26
- **O(n log n)**: Problems 5, 12
- **O(n²)**: Problems 6-8, 16, 20, 22-23, 25, 29
- **O(n\*m)**: Problems 10, 13, 18-19, 24, 28, 30
- **O(S)**: Problem 7 (S = sum of all characters)

## Key Techniques Used:

1. **Two Pointers**: Problems 10, 15, 18
2. **Sliding Window**: Problems 15, 17-18
3. **Dynamic Programming**: Problems 20, 22, 25, 28, 30
4. **Stack**: Problems 8, 19
5. **Hash Map/Set**: Problems 4, 9, 15-17
6. **String Manipulation**: Problems 1-3, 6, 11-14
7. **Pattern Matching**: Problems 13, 24, 28
8. **Greedy**: Problems 27
9. **Expand Around Center**: Problems 25, 29
10. **Mathematical**: Problems 23, 26
