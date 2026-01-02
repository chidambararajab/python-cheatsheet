"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 PYTHON DICTIONARIES - INTERVIEW MASTERY GUIDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
For 5+ YOE Developer | Interview-Focused | Complete Reference
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 WHAT IS IT?
-------------
Dictionary = Hash Map / Hash Table
- Key-value pairs with O(1) average lookup
- Keys must be hashable (immutable types)
- Maintains insertion order (Python 3.7+)

📌 WHY IT EXISTS?
----------------
✓ THE MOST IMPORTANT DATA STRUCTURE IN PYTHON INTERVIEWS
✓ 70% of interview problems become easier with a dict
✓ Fast lookup: O(1) average case
✓ Frequency counting (most common pattern!)
✓ Memoization for DP problems
✓ Graph adjacency lists

📌 WHEN INTERVIEWERS EXPECT IT?
------------------------------
✓ Two Sum → dict for O(n) solution
✓ Anagrams → dict for character counts
✓ Frequency counting → Counter (defaultdict)
✓ Caching/memoization → LRU cache
✓ Graph problems → adjacency list
✓ "Find pair/triplet" → dict to store complements

🚨 COMMON MISTAKES THAT FAIL INTERVIEWS
---------------------------------------
❌ Not using get() with default (causes KeyError)
❌ Iterating wrong: for k in d vs for k,v in d.items()
❌ Modifying dict while iterating (causes RuntimeError)
❌ Not knowing about defaultdict, Counter
❌ Using list as key (unhashable!)
❌ Forgetting dict is ordered (Python 3.7+)

🎤 INTERVIEW NARRATION TEMPLATE:
"I'll use a dictionary to map X to Y. This gives me O(1) lookup,
so my overall solution is O(n) instead of O(n²)."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

# ═══════════════════════════════════════════════════════════════════════
# 1️⃣ CREATION & BASIC OPERATIONS
# ═══════════════════════════════════════════════════════════════════════

# Basic creation
person = {"name": "Alice", "age": 30, "city": "NYC"}
print(f"Person: {person}")

# Empty dict
empty = {}
empty2 = dict()

# From key-value pairs
pairs = [("a", 1), ("b", 2), ("c", 3)]
from_pairs = dict(pairs)
print(f"From pairs: {from_pairs}")

# Dict comprehension (INTERVIEW FAVORITE)
squares = {x: x**2 for x in range(5)}
print(f"Squares: {squares}")  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Conditional dict comprehension
evens = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"Even squares: {evens}")

# From two lists (zip pattern)
keys = ["a", "b", "c"]
values = [1, 2, 3]
combined = dict(zip(keys, values))
print(f"Zipped dict: {combined}")

# 🎤 INTERVIEWER NARRATION:
"""
"I'll create a frequency map using a dict comprehension. For each unique
character, I'll count its occurrences. This is O(n) time."
"""


# ═══════════════════════════════════════════════════════════════════════
# 2️⃣ ACCESSING & MODIFYING
# ═══════════════════════════════════════════════════════════════════════

print("\n📌 ACCESSING & MODIFYING:")

d = {"a": 1, "b": 2, "c": 3}

# Access with bracket notation
value = d["a"]
print(f"d['a'] = {value}")

# ❌ TRAP: KeyError if key doesn't exist
try:
    value = d["z"]
except KeyError:
    print("❌ d['z'] raises KeyError")

# ✅ BETTER: Use get() with default
value = d.get("z", 0)  # Returns 0 if key doesn't exist
print(f"d.get('z', 0) = {value}")

# This pattern is EVERYWHERE in interviews!
count = d.get("key", 0) + 1  # Increment with default

# Add/Update
d["d"] = 4  # Add new key
d["a"] = 10  # Update existing key
print(f"After updates: {d}")

# Delete
del d["d"]  # Remove key-value pair
print(f"After del d['d']: {d}")

# 🎤 INTERVIEWER NARRATION:
"""
"I'll use get() with a default of 0. This avoids checking if the key
exists first. If it's new, we start at 0. If it exists, we get the
current count."
"""


# ═══════════════════════════════════════════════════════════════════════
# 3️⃣ DICTIONARY METHODS (INTERVIEW ESSENTIAL)
# ═══════════════════════════════════════════════════════════════════════

print("\n📌 DICTIONARY METHODS:")

d = {"a": 1, "b": 2, "c": 3}

# get(key, default=None) - Safe access
value = d.get("a")      # 1
value = d.get("z", 0)   # 0 (default)
print(f"get('z', 0) = {value}")

# keys() - Get all keys
keys = d.keys()
print(f"keys(): {keys}")  # dict_keys(['a', 'b', 'c'])
print(f"List of keys: {list(keys)}")

# values() - Get all values
values = d.values()
print(f"values(): {values}")  # dict_values([1, 2, 3])

# items() - Get key-value pairs (MOST USED!)
items = d.items()
print(f"items(): {items}")  # dict_items([('a', 1), ('b', 2), ('c', 3)])

# pop(key, default=None) - Remove and return value
d = {"a": 1, "b": 2, "c": 3}
value = d.pop("b")  # Returns 2, removes key "b"
print(f"Popped 'b': {value}, remaining: {d}")

value = d.pop("z", 0)  # Returns 0 (default), no error
print(f"Pop non-existent with default: {value}")

# popitem() - Remove and return last inserted (k,v) pair
d = {"a": 1, "b": 2, "c": 3}
item = d.popitem()  # Returns ('c', 3) in Python 3.7+
print(f"Popped item: {item}, remaining: {d}")

# update(other) - Merge dictionaries
d = {"a": 1, "b": 2}
d.update({"c": 3, "d": 4})
print(f"After update: {d}")

d.update({"a": 10})  # Overwrites existing keys
print(f"After overwrite: {d}")

# Python 3.9+: Merge operator
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
merged = d1 | d2  # Creates new dict
print(f"Merged with |: {merged}")

d1 |= d2  # In-place merge
print(f"After |=: {d1}")

# setdefault(key, default=None) - Get value, set if missing
d = {"a": 1}
value = d.setdefault("a", 0)  # Returns 1 (exists)
value = d.setdefault("b", 0)  # Returns 0 (creates "b": 0)
print(f"After setdefault: {d}")

# clear() - Remove all items
d.clear()
print(f"After clear: {d}")


# ═══════════════════════════════════════════════════════════════════════
# 4️⃣ ITERATION (CRITICAL - GET THIS RIGHT!)
# ═══════════════════════════════════════════════════════════════════════

print("\n📌 ITERATION PATTERNS:")

d = {"a": 1, "b": 2, "c": 3}

# Iterate over keys (DEFAULT)
print("Keys only:")
for key in d:
    print(f"  {key}")

# Same as:
for key in d.keys():
    print(f"  {key}")

# Iterate over values
print("Values only:")
for value in d.values():
    print(f"  {value}")

# Iterate over key-value pairs (MOST COMMON!)
print("Key-value pairs:")
for key, value in d.items():
    print(f"  {key}: {value}")

# 🎤 INTERVIEWER NARRATION:
"""
"I'll iterate through the dictionary using items() to get both keys and
values. This is O(n) time where n is the number of entries."
"""

# With enumerate (when you need index)
for i, (key, value) in enumerate(d.items()):
    print(f"  Index {i}: {key}={value}")

# ⚠️ DON'T modify dict while iterating
d = {"a": 1, "b": 2, "c": 3}
# ❌ BAD: RuntimeError
try:
    for key in d:
        if d[key] == 2:
            del d[key]  # Modifying during iteration!
except RuntimeError as e:
    print(f"❌ Error modifying during iteration: {e}")

# ✅ CORRECT: Create list of keys first
d = {"a": 1, "b": 2, "c": 3}
for key in list(d.keys()):  # list() creates copy
    if d[key] == 2:
        del d[key]
print(f"Safely removed: {d}")


# ═══════════════════════════════════════════════════════════════════════
# 5️⃣ DEFAULTDICT & COUNTER (INTERVIEW POWER TOOLS)
# ═══════════════════════════════════════════════════════════════════════

print("\n📌 DEFAULTDICT & COUNTER:")

from collections import defaultdict, Counter

# defaultdict - Auto-initializes missing keys
word_indices = defaultdict(list)  # Default is empty list
words = ["apple", "banana", "apple", "cherry", "banana"]

for i, word in enumerate(words):
    word_indices[word].append(i)  # No need to check if key exists!

print(f"Word indices: {dict(word_indices)}")

# Common patterns:
freq = defaultdict(int)    # Default 0 for counting
graph = defaultdict(list)  # Default [] for adjacency lists
groups = defaultdict(set)  # Default set() for grouping

# 🎤 INTERVIEWER NARRATION:
"""
"I'll use defaultdict(list) for the adjacency list. This way I don't need
to check if a node exists before appending neighbors."
"""

# Counter - Frequency counting made easy
text = "hello world"
char_count = Counter(text)
print(f"Character count: {char_count}")

nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
num_count = Counter(nums)
print(f"Number count: {num_count}")

# Most common elements
most_common = num_count.most_common(2)  # Top 2
print(f"Most common 2: {most_common}")  # [(4, 4), (3, 3)]

# Counter arithmetic
c1 = Counter(['a', 'b', 'c', 'a'])
c2 = Counter(['a', 'b', 'b', 'd'])
print(f"c1 + c2: {c1 + c2}")  # Combine counts
print(f"c1 - c2: {c1 - c2}")  # Subtract counts
print(f"c1 & c2: {c1 & c2}")  # Intersection (min)
print(f"c1 | c2: {c1 | c2}")  # Union (max)


# ═══════════════════════════════════════════════════════════════════════
# 6️⃣ INTERVIEW PATTERNS WITH DICTIONARIES
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("🔥 INTERVIEW PATTERNS")
print("="*70)

# ────────────────────────────────────────────────────────────────────────
# PATTERN 1: TWO SUM (THE CLASSIC)
# ────────────────────────────────────────────────────────────────────────

def two_sum(nums, target):
    """
    🎤 INTERVIEWER NARRATION:
    "I'll use a dictionary to store numbers I've seen along with their indices.
    For each number, I check if (target - num) exists in the dict. This gives
    me O(n) time instead of O(n²) brute force, with O(n) space."
    """
    seen = {}  # value -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return None

print("\n▶ TWO SUM PATTERN:")
result = two_sum([2, 7, 11, 15], 9)
print(f"Two sum indices: {result}")


# ────────────────────────────────────────────────────────────────────────
# PATTERN 2: FREQUENCY COUNTING / ANAGRAMS
# ────────────────────────────────────────────────────────────────────────

def group_anagrams(words):
    """
    🎤 INTERVIEWER NARRATION:
    "I'll use a dictionary where the key is a sorted tuple of characters,
    and the value is a list of anagrams. Since anagrams have the same
    characters when sorted, they'll map to the same key."
    """
    from collections import defaultdict
    
    anagram_groups = defaultdict(list)
    
    for word in words:
        # Sorted tuple as key (hashable!)
        key = tuple(sorted(word))
        anagram_groups[key].append(word)
    
    return list(anagram_groups.values())

print("\n▶ FREQUENCY/ANAGRAM PATTERN:")
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = group_anagrams(words)
print(f"Anagram groups: {groups}")


# Alternative: Character count as key
def group_anagrams_v2(words):
    """
    🎤 INTERVIEWER NARRATION:
    "Alternative approach: use character frequency as the key. I'll create
    a tuple of (char, count) pairs. This is actually O(n) per word instead
    of O(n log n) for sorting."
    """
    from collections import defaultdict, Counter
    
    anagram_groups = defaultdict(list)
    
    for word in words:
        # Frozenset of (char, count) pairs won't work - need tuple
        key = tuple(sorted(Counter(word).items()))
        anagram_groups[key].append(word)
    
    return list(anagram_groups.values())


# ────────────────────────────────────────────────────────────────────────
# PATTERN 3: CACHING / MEMOIZATION
# ────────────────────────────────────────────────────────────────────────

def fibonacci(n, memo=None):
    """
    🎤 INTERVIEWER NARRATION:
    "I'll use memoization to cache results. Without it, this would be O(2^n).
    With memoization, it's O(n) because we compute each value once."
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

print("\n▶ MEMOIZATION PATTERN:")
print(f"Fibonacci(10): {fibonacci(10)}")

# Python decorator for automatic memoization
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_cached(n):
    """
    🎤 INTERVIEWER NARRATION:
    "In production, I'd use @lru_cache decorator. But in interviews, I often
    implement memoization manually to show I understand the concept."
    """
    if n <= 1:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)


# ────────────────────────────────────────────────────────────────────────
# PATTERN 4: GRAPH ADJACENCY LIST
# ────────────────────────────────────────────────────────────────────────

def build_graph(edges):
    """
    🎤 INTERVIEWER NARRATION:
    "I'll build an adjacency list using defaultdict(list). For each edge,
    I'll add the neighbor to the node's list. This is the standard way to
    represent graphs in Python interviews."
    """
    from collections import defaultdict
    
    graph = defaultdict(list)
    
    for u, v in edges:
        graph[u].append(v)
        # For undirected: graph[v].append(u)
    
    return graph

print("\n▶ GRAPH ADJACENCY LIST:")
edges = [(0, 1), (0, 2), (1, 2), (2, 3)]
graph = build_graph(edges)
print(f"Graph: {dict(graph)}")


# ────────────────────────────────────────────────────────────────────────
# PATTERN 5: PREFIX SUM / SUBARRAY SUM
# ────────────────────────────────────────────────────────────────────────

def subarray_sum(nums, k):
    """
    🎤 INTERVIEWER NARRATION:
    "I'll use a dictionary to store prefix sums we've seen. If
    (current_sum - k) exists in the dict, we've found a subarray that
    sums to k. This is O(n) time."
    """
    count = 0
    current_sum = 0
    sum_freq = {0: 1}  # Base case: empty prefix
    
    for num in nums:
        current_sum += num
        
        # Check if (current_sum - k) exists
        if current_sum - k in sum_freq:
            count += sum_freq[current_sum - k]
        
        # Add current sum to frequency map
        sum_freq[current_sum] = sum_freq.get(current_sum, 0) + 1
    
    return count

print("\n▶ PREFIX SUM PATTERN:")
nums = [1, 1, 1]
k = 2
print(f"Subarrays with sum {k}: {subarray_sum(nums, k)}")


# ────────────────────────────────────────────────────────────────────────
# PATTERN 6: SLIDING WINDOW + FREQUENCY MAP
# ────────────────────────────────────────────────────────────────────────

def longest_substring_k_distinct(s, k):
    """
    🎤 INTERVIEWER NARRATION:
    "I'll use a sliding window with a frequency map. The map tracks
    character counts in the current window. When we have more than k
    distinct chars, we shrink from the left."
    """
    from collections import defaultdict
    
    char_freq = defaultdict(int)
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        char_freq[s[right]] += 1
        
        # Shrink window if too many distinct chars
        while len(char_freq) > k:
            char_freq[s[left]] -= 1
            if char_freq[s[left]] == 0:
                del char_freq[s[left]]
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length

print("\n▶ SLIDING WINDOW + DICT:")
result = longest_substring_k_distinct("eceba", 2)
print(f"Longest substring with 2 distinct chars: {result}")


# ────────────────────────────────────────────────────────────────────────
# PATTERN 7: INDEX MAPPING
# ────────────────────────────────────────────────────────────────────────

def find_pairs_with_difference(nums, k):
    """
    🎤 INTERVIEWER NARRATION:
    "I'll create a set for O(1) lookup, then for each number, check if
    num+k or num-k exists. This beats the O(n log n) sorting approach."
    """
    num_set = set(nums)
    pairs = set()
    
    for num in nums:
        if num + k in num_set:
            pairs.add((num, num + k))
        if num - k in num_set:
            pairs.add((num - k, num))
    
    return list(pairs)

print("\n▶ INDEX MAPPING:")
pairs = find_pairs_with_difference([1, 5, 3, 4, 2], 2)
print(f"Pairs with difference 2: {pairs}")


# ═══════════════════════════════════════════════════════════════════════
# 7️⃣ COMPARISON WITH JAVA/JAVASCRIPT
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("📊 LANGUAGE COMPARISON")
print("="*70)

comparison = """
╔═══════════════════════════╦═══════════════════════╦═══════════════════════╗
║ OPERATION                 ║ PYTHON                ║ JAVA / JAVASCRIPT     ║
╠═══════════════════════════╬═══════════════════════╬═══════════════════════╣
║ Create                    ║ {"a": 1, "b": 2}      ║ new HashMap<>()       ║
║                           ║                       ║ {a: 1, b: 2} (JS)     ║
╠═══════════════════════════╬═══════════════════════╬═══════════════════════╣
║ Get value                 ║ d["key"]              ║ map.get("key")        ║
║                           ║ d.get("key", def)     ║ map.get("key") (JS)   ║
╠═══════════════════════════╬═══════════════════════╬═══════════════════════╣
║ Set value                 ║ d["key"] = val        ║ map.put("key", val)   ║
║                           ║                       ║ map.set("key",val) JS ║
╠═══════════════════════════╬═══════════════════════╬═══════════════════════╣
║ Check key exists          ║ "key" in d            ║ map.containsKey()     ║
║                           ║                       ║ map.has("key") (JS)   ║
╠═══════════════════════════╬═══════════════════════╬═══════════════════════╣
║ Remove key                ║ del d["key"]          ║ map.remove("key")     ║
║                           ║ d.pop("key")          ║ map.delete("key") JS  ║
╠═══════════════════════════╬═══════════════════════╬═══════════════════════╣
║ Size                      ║ len(d)                ║ map.size()            ║
║                           ║                       ║ map.size (JS)         ║
╠═══════════════════════════╬═══════════════════════╬═══════════════════════╣
║ Iterate keys              ║ for k in d:           ║ for(K k : map.keySet║
║                           ║                       ║ for(let k of map.keys║
╠═══════════════════════════╬═══════════════════════╬═══════════════════════╣
║ Iterate key-values        ║ for k,v in d.items()  ║ for(Entry e:entrySet║
║                           ║                       ║ for(let [k,v] of map) ║
╠═══════════════════════════╬═══════════════════════╬═══════════════════════╣
║ Get with default          ║ d.get(k, default)     ║ map.getOrDefault()    ║
║                           ║                       ║ map.get(k) || def (JS║
╠═══════════════════════════╬═══════════════════════╬═══════════════════════╣
║ Merge dicts               ║ d1 | d2  (Python 3.9+)║ map.putAll(map2)      ║
║                           ║ d1.update(d2)         ║ {...d1, ...d2} (JS)   ║
╚═══════════════════════════╩═══════════════════════╩═══════════════════════╝

KEY ADVANTAGES IN PYTHON:
  - Clean syntax: d[k] = v
  - get() with default is elegant
  - dict comprehensions
  - items() returns pairs directly (no Entry object)
  - Guaranteed insertion order (3.7+)
"""
print(comparison)


# ═══════════════════════════════════════════════════════════════════════
# 8️⃣ INTERVIEW CHECKLIST - DICTIONARIES
# ═══════════════════════════════════════════════════════════════════════

checklist = """
┌─────────────────────────────────────────────────────────────────────┐
│ ✅ BEFORE USING DICTIONARIES IN AN INTERVIEW                        │
├─────────────────────────────────────────────────────────────────────┤
│ □ Do I need O(1) lookup? (Dict is perfect!)                        │
│ □ Am I counting frequencies? (Use Counter or defaultdict(int))     │
│ □ Am I grouping items? (Use defaultdict(list))                     │
│ □ Do I need to check if key exists? (Use get() with default)       │
│ □ Am I building a graph? (Use defaultdict(list) for adj list)      │
│ □ Can I reduce time from O(n²) to O(n)? (Dict often enables this!) │
│ □ Am I implementing memoization? (Dict for cache)                  │
│ □ Am I iterating correctly? (Use .items() for key-value pairs)     │
│ □ Are my keys hashable? (No lists/dicts as keys!)                  │
│ □ Will I modify while iterating? (Create list of keys first)       │
└─────────────────────────────────────────────────────────────────────┘

💡 GOLDEN RULE:
If you see "find two elements that..." → Think Dictionary!
"""
print(checklist)


# ═══════════════════════════════════════════════════════════════════════
# 🔥 TIME COMPLEXITY SUMMARY
# ═══════════════════════════════════════════════════════════════════════

complexity_table = """
╔═══════════════════════════════════════════════════════════════════════╗
║              DICTIONARY TIME COMPLEXITY CHEAT SHEET                   ║
╠═══════════════════════════╦══════════════════╦════════════════════════╣
║ OPERATION                 ║ AVERAGE CASE     ║ WORST CASE             ║
╠═══════════════════════════╬══════════════════╬════════════════════════╣
║ d[key] (access)           ║ O(1)             ║ O(n) [rare collision]  ║
║ d[key] = value            ║ O(1)             ║ O(n)                   ║
║ del d[key]                ║ O(1)             ║ O(n)                   ║
║ key in d                  ║ O(1)             ║ O(n)                   ║
║ d.get(key, default)       ║ O(1)             ║ O(n)                   ║
║ d.pop(key)                ║ O(1)             ║ O(n)                   ║
║ d.popitem()               ║ O(1)             ║ O(1)                   ║
║ d.clear()                 ║ O(n)             ║ O(n)                   ║
║ len(d)                    ║ O(1)             ║ O(1)                   ║
║ d.keys()                  ║ O(1) [view]      ║ O(1)                   ║
║ d.values()                ║ O(1) [view]      ║ O(1)                   ║
║ d.items()                 ║ O(1) [view]      ║ O(1)                   ║
║ d.update(other)           ║ O(len(other))    ║ O(len(other))          ║
║ Iterate all items         ║ O(n)             ║ O(n)                   ║
╠═══════════════════════════╩══════════════════╩════════════════════════╣
║ 💡 For interviews, assume O(1) operations - collisions are rare      ║
║ 💡 Space complexity: O(n) where n = number of key-value pairs        ║
╚═══════════════════════════════════════════════════════════════════════╝
"""
print(complexity_table)

print("\n✅ DICTIONARY MASTERY COMPLETE!")
print("🎉 Core data structures done! Moving to utility functions next.")

