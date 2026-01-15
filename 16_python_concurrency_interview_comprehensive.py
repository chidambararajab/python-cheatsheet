"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 PYTHON CONCURRENCY - ELIMINATION INTERVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣ OVERVIEW

FILTERS:
• Those who don't understand GIL
• Candidates who confuse threading with multiprocessing
• Engineers who can't explain CPU-bound vs IO-bound
• People who don't understand race conditions

WEAK:
────
❌ Think threads provide true parallelism
❌ Don't know what GIL is
❌ Can't explain when to use threading vs multiprocessing
❌ Don't understand race conditions

STRONG:
──────
✓ GIL prevents true parallel CPU execution in CPython
✓ Threading for IO-bound, multiprocessing for CPU-bound
✓ Race conditions occur when shared state accessed concurrently
✓ Locks prevent concurrent access but can deadlock

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

2️⃣ CONCEPTS

╔═══════════════════════════╦═══════════╦════════════════════════════════╗
║ CONCEPT                   ║ FREQUENCY ║ WHAT TESTED                    ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ GIL (Global Interp Lock)  ║ HIGH      ║ Why threads don't parallelize  ║
║                           ║           ║ REJECT: Doesn't know exists    ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ Threading vs multiprocess ║ HIGH      ║ When to use which              ║
║                           ║           ║ REJECT: Confuses them          ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ CPU-bound vs IO-bound     ║ HIGH      ║ Workload classification        ║
║                           ║           ║ REJECT: Can't distinguish      ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ Race conditions           ║ MEDIUM    ║ Concurrent access bugs         ║
║                           ║           ║ REJECT: Doesn't recognize      ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ Locks & deadlocks         ║ MEDIUM    ║ Synchronization                ║
╚═══════════════════════════╩═══════════╩════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

3️⃣ QUESTIONS

SECTION 3A: GIL (HIGH - CRITICAL)
──────────────────────────────────

① WARM-UP
──────────
Q: "What is the GIL?"

STRONG: "Global Interpreter Lock. CPython's mechanism ensuring only one thread
executes Python bytecode at a time. Prevents true parallel CPU execution with threads.
Necessary for memory management safety. Means threading doesn't help for CPU-bound
tasks."

WEAK: "It's about threads?" ✗ VAGUE
"Never heard of it" ✗ DISQUALIFYING for 5+ YOE

② CORE
──────
Q: "Will threading speed up this CPU-intensive task?"

def process():
    # Heavy computation
    for i in range(10_000_000):
        x = i ** 2

STRONG: "No. GIL prevents threads from executing Python code in parallel. All threads
run on one CPU core, taking turns. Threading adds overhead. For CPU-bound, use
multiprocessing or asyncio won't help either. Need separate processes."

WEAK: "Yes, threads make it faster?" ✗ WRONG, fundamental misunderstanding

③ EDGE-CASE
────────────
Q: "When DO threads help?"

STRONG: "IO-bound tasks: network requests, file I/O, database queries. When thread
waits for I/O, it releases GIL so other threads can run. Example: downloading multiple
URLs concurrently. Threading good here."

④ FOLLOW-UP
────────────
Q: "How to get true parallelism for CPU-bound work?"

STRONG: "multiprocessing module. Creates separate Python processes, each with own
GIL. True parallel execution across CPU cores. Trade-off: higher memory, IPC overhead."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 3B: THREADING VS MULTIPROCESSING (HIGH)
────────────────────────────────────────────────

① WARM-UP
──────────
Q: "Threading vs multiprocessing - when to use each?"

STRONG:
"Threading: IO-bound work (network, disk, DB). Shares memory, lightweight.
Multiprocessing: CPU-bound work. Separate processes, true parallelism. Higher overhead.

Rule: IO → threading, CPU → multiprocessing."

② CORE
──────
Q: "Which is better for this?"

# Download 100 URLs
# vs
# Compute fibonacci for 100 large numbers

STRONG:
"Download 100 URLs: Threading. IO-bound, threads can wait concurrently.
Fibonacci computation: Multiprocessing. CPU-bound, need true parallelism."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 3C: RACE CONDITIONS (MEDIUM)
─────────────────────────────────────

① WARM-UP
──────────
Q: "What's a race condition?"

STRONG: "Multiple threads accessing shared state concurrently, at least one writing.
Outcome depends on timing/scheduling. Non-deterministic behavior. Example: two threads
incrementing same counter - final value unpredictable."

② CORE
──────
Q: "Is this thread-safe?"

counter = 0

def increment():
    global counter
    for _ in range(100000):
        counter += 1

# Run in 2 threads

STRONG: "No! counter += 1 is read-modify-write. Not atomic. Both threads might read
same value, increment, write - losing updates. Final counter < 200000. Need lock:

lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1"

③ EDGE-CASE
────────────
Q: "What's a deadlock?"

STRONG: "Two threads each holding lock, waiting for other's lock. Neither can proceed.
Classic: Thread A holds Lock1, waits for Lock2. Thread B holds Lock2, waits for Lock1.
Forever stuck. Fix: consistent lock ordering or use timeouts."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

4️⃣ THINK-ALOUD

QUESTION: "Why doesn't threading speed this up?"

import threading

def heavy_compute():
    result = 0
    for i in range(10_000_000):
        result += i ** 2
    return result

threads = [threading.Thread(target=heavy_compute) for _ in range(4)]
# Slower than single-threaded!

STRONG: "GIL. Only one thread executes Python at a time. Four threads take turns on
one CPU core, adding context-switch overhead. Actually SLOWER than single-threaded.
For CPU-bound, need multiprocessing to use multiple cores."

WEAK: "Threads should make it faster?" ✗ DOESN'T UNDERSTAND GIL

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

5️⃣ OUTPUT PREDICTION

PROBLEM:
────────
import threading

counter = 0
lock = threading.Lock()

def increment_safe():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

threads = [threading.Thread(target=increment_safe) for _ in range(2)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(counter)

OUTPUT: 200000 (deterministic)
REASONING: "Lock ensures atomic access. No race condition. Both increments counted."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

6️⃣ COMMON FAILURES

FAILURE #1: USING THREADING FOR CPU-BOUND
══════════════════════════════════════════

WRONG:
# Heavy computation
import threading
threads = [threading.Thread(target=cpu_intensive) for _ in range(4)]
# Doesn't help! GIL limits to one CPU.

CORRECT:
import multiprocessing
processes = [multiprocessing.Process(target=cpu_intensive) for _ in range(4)]
# True parallelism across cores.

FAILURE #2: SHARED STATE WITHOUT LOCKS
═══════════════════════════════════════

WRONG:
shared_list = []
def append_items():
    for i in range(1000):
        shared_list.append(i)  # Race condition!

CORRECT:
import threading
shared_list = []
lock = threading.Lock()

def append_items():
    for i in range(1000):
        with lock:
            shared_list.append(i)

FAILURE #3: NOT KNOWING WHEN TO USE WHAT
═════════════════════════════════════════

WRONG BELIEFS:
"Threading always makes code faster" ✗
"Multiprocessing for everything" ✗

CORRECT:
- IO-bound (network, disk): threading or asyncio
- CPU-bound (computation): multiprocessing
- Understand GIL limitations

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

7️⃣ MOCK INTERVIEW

Q1: "What is the GIL?"
EXPECTED: "Global Interpreter Lock - one thread executes Python at a time" [< 10 sec]
REJECT IF: "Don't know"

Q2: "Threading for CPU-bound work?"
EXPECTED: "No - GIL prevents parallelism. Use multiprocessing" [< 10 sec]

Q3: "When to use threading?"
EXPECTED: "IO-bound tasks - network, disk, DB" [< 10 sec]

Q4: "What's a race condition?"
EXPECTED: "Concurrent access to shared state, non-deterministic outcome" [< 15 sec]

Q5: "How to prevent race condition?"
EXPECTED: "Use locks to synchronize access" [< 5 sec]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

8️⃣ SELF-ASSESSMENT

CRITICAL (ALL):
───────────────
□ Know what GIL is
□ Know threading doesn't help CPU-bound
□ Distinguish IO-bound from CPU-bound
□ Know when to use threading vs multiprocessing
□ Understand race conditions

SCORING:
< 5/5: FAIL - Missing concurrency fundamentals
5/5: PASS

INTERVIEWER:
IF FAIL: "Doesn't understand Python concurrency. Would use threading incorrectly,
creating race conditions or failing to achieve parallelism. REJECT."
"""
