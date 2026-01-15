"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 HARD LIVE CODING CHALLENGES - REAL INTERVIEW SIMULATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Interviewer: Staff Engineer | Hiring Bar-Raiser
Target: 3-7 YOE | Python Engineers
Time: 45-60 minutes per problem
Focus: Complex State Management, Multiple Constraints, Trade-offs
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

HARD EXPECTATIONS:
──────────────────
• Multiple constraints to balance
• State management across operations
• Deep algorithmic thinking
• Clear trade-off articulation
• Partial solutions acceptable
• Communication more important than perfect code

ELIMINATION TRIGGERS:
─────────────────────
• Gives up without attempting → REJECT
• Can't break problem into parts → REJECT
• No trade-off awareness → BORDERLINE
• Silent for >5 minutes → REJECT
• Defensive about hints → RED FLAG
"""

# ═══════════════════════════════════════════════════════════════════════
# PROBLEM 1: LRU CACHE
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1️⃣ PROBLEM STATEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Design and implement an LRU (Least Recently Used) Cache.

Operations:
- get(key): Return value if key exists, else -1
- put(key, value): Insert or update key-value pair

Constraints:
- Fixed capacity
- When capacity reached, evict least recently used item
- Both operations must be O(1)

Example:
    cache = LRUCache(2)  # capacity = 2
    cache.put(1, 1)      # cache: {1=1}
    cache.put(2, 2)      # cache: {1=1, 2=2}
    cache.get(1)         # returns 1, cache: {2=2, 1=1}
    cache.put(3, 3)      # evicts 2, cache: {1=1, 3=3}
    cache.get(2)         # returns -1 (not found)
    cache.put(4, 4)      # evicts 1, cache: {3=3, 4=4}

Requirements:
- O(1) time for get and put
- Track access order for eviction
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2️⃣ THINK-ALOUD FLOW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STRONG CANDIDATE:

"LRU cache - need O(1) get and put, with eviction of least recently used.

Let me think about data structures:
- Need fast lookup: Hash map for O(1) get
- Need to track order: Some ordered structure
- Need to move items to front on access: Doubly linked list!

Why doubly linked list?
- Add/remove from ends: O(1)
- Remove from middle: O(1) if we have node reference
- Hash map stores: key → node reference

Data structures:
1. Hash map: key → DoublyLinkedListNode
2. Doubly linked list: maintains order (most recent at head, LRU at tail)

Operations:
- get(key): 
  * If in cache: move to head (most recent), return value
  * If not: return -1
- put(key, value):
  * If exists: update value, move to head
  * If new and at capacity: remove tail (LRU), add new at head
  * If new and not full: add at head

Example trace with capacity=2:
put(1,1): add 1 at head → List: 1
put(2,2): add 2 at head → List: 2 → 1
get(1): move 1 to head → List: 1 → 2
put(3,3): at capacity, remove tail (2), add 3 at head → List: 3 → 1

Implementation challenges:
- Maintain both hash map and linked list
- Correctly update pointers when moving nodes
- Handle edge cases (empty, single element)

I'll need:
- Node class with prev, next, key, value
- Dummy head and tail for easier edge handling
- Helper methods: _remove_node, _add_to_head"
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3️⃣ TRAP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TRAP 1: Using OrderedDict without understanding it
Python's OrderedDict could work, but interviewers want to see you understand
the data structure mechanics, not just use a library.

TRAP 2: Forgetting to update both hash map AND linked list
When moving a node, must:
1. Remove from current position in list
2. Add to head of list
3. Keep hash map pointing to same node (no update needed if node object persists)

TRAP 3: Not storing key in node
When evicting LRU (tail), need key to delete from hash map.
Node must store both key and value.

TRAP 4: Pointer bugs when removing nodes
Common mistake: forgetting to update both prev and next pointers,
leading to broken list.
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4️⃣ SOLUTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

class Node:
    """
    Doubly linked list node.
    Stores key (for eviction), value (for get), and prev/next pointers.
    """
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """
    LRU Cache with O(1) get and put operations.
    
    Data structures:
    - Hash map: key → Node (for O(1) lookup)
    - Doubly linked list: tracks order (most recent at head, LRU at tail)
    
    List structure:
    dummy_head ↔ most_recent ↔ ... ↔ least_recent ↔ dummy_tail
    
    Using dummy head/tail simplifies edge case handling.
    """
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key → Node
        
        # Dummy head and tail for easier node manipulation
        self.head = Node()  # Dummy head
        self.tail = Node()  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove_node(self, node: Node) -> None:
        """
        Remove node from linked list (doesn't remove from hash map).
        """
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _add_to_head(self, node: Node) -> None:
        """
        Add node right after dummy head (most recently used position).
        """
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def _move_to_head(self, node: Node) -> None:
        """
        Move existing node to head (mark as recently used).
        """
        self._remove_node(node)
        self._add_to_head(node)
    
    def _evict_lru(self) -> None:
        """
        Remove least recently used item (node before dummy tail).
        """
        lru_node = self.tail.prev
        self._remove_node(lru_node)
        # Also remove from hash map
        del self.cache[lru_node.key]
    
    def get(self, key: int) -> int:
        """
        Get value for key. Mark as recently used.
        Time: O(1)
        
        Args:
            key: Key to lookup
        
        Returns:
            Value if found, -1 otherwise
        """
        if key not in self.cache:
            return -1
        
        # Found - move to head (most recently used)
        node = self.cache[key]
        self._move_to_head(node)
        return node.value
    
    def put(self, key: int, value: int) -> None:
        """
        Insert or update key-value pair. Mark as recently used.
        If at capacity, evict LRU before adding.
        Time: O(1)
        
        Args:
            key: Key to insert/update
            value: Value to store
        """
        if key in self.cache:
            # Update existing - move to head
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            # New key - add to cache
            if len(self.cache) >= self.capacity:
                # At capacity - evict LRU
                self._evict_lru()
            
            # Create new node and add to head
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)


"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5️⃣ BAD SOLUTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

class LRUCacheBad:
    """
    ❌ Using list to track order - O(n) operations
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.order = []  # Track access order
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move key to end (most recent)
        self.order.remove(key)  # ❌ O(n)
        self.order.append(key)
        return self.cache[key]
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.order.remove(key)  # ❌ O(n)
        elif len(self.cache) >= self.capacity:
            lru = self.order.pop(0)  # ❌ O(n) for pop(0)
            del self.cache[lru]
        
        self.cache[key] = value
        self.order.append(key)

"""
WHY BAD:
- list.remove(key) is O(n) - searches for key
- list.pop(0) is O(n) - shifts all elements
- Doesn't meet O(1) requirement
- Shows lack of understanding of time complexity

SIGNALS: Can solve functionally but can't optimize to requirements.
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
6️⃣ EXPLANATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHY THIS DESIGN WORKS:

HASH MAP:
- Provides O(1) lookup by key
- Stores reference to linked list node
- Allows fast access to any element

DOUBLY LINKED LIST:
- Maintains access order
- O(1) add/remove from any position (if we have node reference)
- Head = most recently used
- Tail = least recently used (candidate for eviction)

DUMMY HEAD/TAIL:
- Simplifies edge cases (empty list, single element)
- Never need to check for None
- Consistent pointer operations

OPERATIONS:
- get(): Hash map lookup + move to head = O(1) + O(1) = O(1)
- put(): Hash map insert + list operations = O(1)
- evict(): Remove from tail + hash map delete = O(1) + O(1) = O(1)

KEY INSIGHT:
Combining two data structures (hash map + doubly linked list) gives us
fast lookup (hash map) and fast order management (linked list).
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
7️⃣ COMPLEXITY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TIME:
- get(): O(1) - hash map lookup + list pointer updates
- put(): O(1) - hash map insert + list pointer updates
- All helper methods: O(1) - just pointer manipulation

SPACE: O(capacity)
- Hash map stores at most capacity entries
- Linked list stores at most capacity nodes
- Each node stores constant data (key, value, 2 pointers)

This meets the O(1) requirement for both operations.
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
8️⃣ IF TIME RUNS OUT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT TO SAY:
"I'm implementing LRU cache with hash map for O(1) lookup and doubly linked
list for O(1) order management. Most recent items at head, LRU at tail. On
get, move to head. On put, add to head and evict tail if at capacity. Would
need helper methods for pointer manipulation."

PARTIAL CREDIT FOR:
✓ Identified need for hash map + linked list
✓ Explained why doubly linked list (not singly)
✓ Described operations even without complete implementation
✓ Understood O(1) requirement drives design

WHAT NOT TO DO:
❌ Give up: "This is too hard"
❌ Use OrderedDict without explaining: "Python has this built-in"
❌ Propose O(n) solution and call it done

RECOVERY:
"If time's short, I can implement with Python's OrderedDict to show functionality,
then discuss how I'd implement the underlying doubly linked list for a real
production system."
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
9️⃣ FOLLOW-UP QUESTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEWER: "How would you make this thread-safe?"

ANSWER:
"Add locking around operations:
- Lock on get() to prevent race conditions
- Lock on put() to ensure atomic eviction + insertion
- Could use threading.Lock() or RLock()
- Trade-off: Locks serialize access, reduce throughput
- For high concurrency, could use read-write lock or sharding"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEWER: "What if you needed to support TTL (time-to-live)?"

ANSWER:
"Add timestamp to each node. On get(), check if expired:
- If expired, treat as cache miss, remove from cache
- Alternatively, background thread periodically sweeps expired entries
- Trade-off: More complex, requires time tracking"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERVIEWER: "How would you handle distributed caching?"

ANSWER:
"LRU per node would cause inconsistency. Options:
1. Consistent hashing to route requests to same node
2. Central cache (Redis) with LRU eviction policy
3. Hybrid: Local LRU + distributed invalidation
Each has trade-offs in consistency, latency, complexity"
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔟 EVALUATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ HIRE SIGNALS:
- Immediately recognized need for hash map + linked list
- Explained why doubly linked (bi-directional traversal)
- Correctly implemented pointer manipulation
- Used dummy nodes to simplify edge cases
- Clean code with helper methods
- Handled edge cases (empty, at capacity)
- Achieved O(1) for both operations

⚠️ BORDERLINE:
- Needed hints to arrive at doubly linked list
- Pointer bugs fixed after testing
- Got partial implementation working
- Understood approach but struggled with details

❌ NO-HIRE:
- Couldn't identify data structures needed
- Proposed O(n) solution and couldn't optimize
- Pointer bugs broke functionality
- Used OrderedDict without understanding
- Gave up or silent for long periods
- Can't explain time complexity

DECISION FACTORS:
Hard problems test problem decomposition, data structure knowledge, and
persistence. Not expecting perfect code, but expect:
1. Right approach (even if not fully implemented)
2. Clear communication of thinking
3. Awareness of trade-offs
4. Ability to work through complexity

LRU Cache is a classic system design component. Senior engineers should
recognize it and know the standard implementation pattern.
"""


# ═══════════════════════════════════════════════════════════════════════
# PROBLEM 2: WORD LADDER (Shortest Transformation Sequence)
# ═══════════════════════════════════════════════════════════════════════

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1️⃣ PROBLEM STATEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Given a start word, end word, and dictionary of valid words, find the length
of shortest transformation sequence from start to end.

Rules:
- Change only one letter at a time
- Each transformed word must exist in dictionary
- All words same length
- All words lowercase

Example:
    start = "hit"
    end = "cog"
    dict = ["hot", "dot", "dog", "lot", "log", "cog"]
    
    Output: 5
    Explanation: "hit" → "hot" → "dot" → "dog" → "cog"

Return 0 if no transformation possible.
"""

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2-10 SECTIONS (ABBREVIATED FOR SPACE)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

2️⃣ THINK-ALOUD:
"This is a graph problem. Each word is a node. Edge between words that differ
by one letter. Need shortest path → BFS!

Build graph, run BFS from start to end."

3️⃣ TRAP: Trying to generate all possible words instead of checking dictionary.
For word "hit", checking 26^3 possibilities vs checking dictionary membership.

4️⃣ SOLUTION: BFS with level tracking
"""

from collections import deque, defaultdict

def word_ladder_length(start, end, word_list):
    """
    Find shortest transformation sequence length using BFS.
    
    Approach:
    1. Build adjacency list using wildcard patterns
    2. BFS from start word, tracking level (distance)
    3. Return level when end word reached
    
    Time: O(N * L^2) where N = words, L = word length
    Space: O(N * L^2) for adjacency list
    """
    if end not in word_list:
        return 0
    
    # Add start to word list if not present
    word_list = set(word_list)
    word_list.add(start)
    
    # Build adjacency list using wildcard patterns
    # "hit" → "*it", "h*t", "hi*"
    neighbors = defaultdict(list)
    for word in word_list:
        for i in range(len(word)):
            pattern = word[:i] + '*' + word[i+1:]
            neighbors[pattern].append(word)
    
    # BFS
    queue = deque([(start, 1)])  # (word, level)
    visited = {start}
    
    while queue:
        word, level = queue.popleft()
        
        if word == end:
            return level
        
        # Check all patterns for this word
        for i in range(len(word)):
            pattern = word[:i] + '*' + word[i+1:]
            for neighbor in neighbors[pattern]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, level + 1))
    
    return 0  # No transformation found


"""
5️⃣ BAD SOLUTION: Generate all one-letter variations - O(26*L*N) per word
6️⃣ KEY: Recognize as BFS shortest path problem. Wildcard pattern optimization.
7️⃣ COMPLEXITY: O(N*L^2) where N=words, L=length. Space O(N*L^2) for graph.
8️⃣ TIME OUT: "BFS from start, check all one-letter differences, track level"
9️⃣ FOLLOW-UP: "Return actual path?" → Store parent pointers
🔟 EVALUATION: Must recognize BFS pattern. Graph building shows sophistication.
"""


# ═══════════════════════════════════════════════════════════════════════
# TESTING FRAMEWORK
# ═══════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # Test LRU Cache
    print("Testing LRU Cache:")
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1  # Evicted
    cache.put(4, 4)
    assert cache.get(1) == -1  # Evicted
    assert cache.get(3) == 3
    assert cache.get(4) == 4
    print("✓ LRU Cache tests passed\n")
    
    # Test Word Ladder
    print("Testing Word Ladder:")
    word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
    assert word_ladder_length("hit", "cog", word_list) == 5
    word_list2 = ["hot", "dot", "dog", "lot", "log"]
    assert word_ladder_length("hit", "cog", word_list2) == 0  # No path
    print("✓ Word Ladder tests passed\n")
    
    print("🎉 ALL HARD PROBLEMS TESTED SUCCESSFULLY")
    print("\n" + "="*70)
    print("CONGRATULATIONS! You've completed all live coding challenges.")
    print("These problems represent real interview difficulty levels.")
    print("Practice explaining your thinking process out loud!")
    print("="*70)
