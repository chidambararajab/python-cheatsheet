"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 PYTHON ASYNCIO - ELIMINATION INTERVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣ OVERVIEW

FILTERS:
• Those who confuse async with threading/multiprocessing
• Candidates who don't understand event loop
• Engineers who block the event loop
• People who don't know when asyncio is WRONG choice

WEAK:
────
❌ Think async provides parallelism like threads
❌ Don't understand event loop
❌ Mix blocking and non-blocking calls
❌ Use asyncio for CPU-bound work

STRONG:
──────
✓ async is cooperative concurrency, not parallelism
✓ Event loop schedules coroutines
✓ await yields control, doesn't block
✓ asyncio for IO-bound, NOT CPU-bound
✓ Blocking calls kill performance

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

2️⃣ CONCEPTS

╔═══════════════════════════╦═══════════╦════════════════════════════════╗
║ CONCEPT                   ║ FREQUENCY ║ WHAT TESTED                    ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ async vs sync mental model║ HIGH      ║ Cooperative vs preemptive      ║
║                           ║           ║ REJECT: Thinks it's threading  ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ Event loop basics         ║ HIGH      ║ How coroutines are scheduled   ║
║                           ║           ║ REJECT: Doesn't understand     ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ async / await semantics   ║ HIGH      ║ What await actually does       ║
║                           ║           ║ REJECT: Can't explain          ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ Blocking vs non-blocking  ║ HIGH      ║ time.sleep vs asyncio.sleep    ║
║                           ║           ║ REJECT: Uses blocking calls    ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ When asyncio is WRONG     ║ MEDIUM    ║ CPU-bound work                 ║
╚═══════════════════════════╩═══════════╩════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

3️⃣ QUESTIONS

SECTION 3A: async vs sync MENTAL MODEL (HIGH)
──────────────────────────────────────────────

① WARM-UP
──────────
Q: "What's the difference between async and threading?"

STRONG: "asyncio is COOPERATIVE concurrency. Coroutines explicitly yield control
with await. Single-threaded event loop. Threading is PREEMPTIVE - OS schedules
threads, can switch anytime. asyncio avoids race conditions easier, but requires
all code to be async-aware. Both run on single CPU core (due to GIL)."

WEAK: "They're both for concurrency?" ✗ DOESN'T EXPLAIN MECHANISM
"Async is faster?" ✗ WRONG, depends on workload

② CORE
──────
Q: "Does asyncio provide true parallelism?"

STRONG: "No. Runs on single thread. Coroutines take turns, yielding at await points.
No parallel CPU execution. Good for IO-bound (waiting for network/disk), not CPU-bound.
For CPU parallelism, need multiprocessing."

WEAK: "Yes, async functions run in parallel?" ✗ FUNDAMENTAL MISUNDERSTANDING

③ EDGE-CASE
────────────
Q: "What's wrong with this?"

async def process():
    result = expensive_computation()  # Blocks!
    await asyncio.sleep(1)
    return result

STRONG: "expensive_computation() is synchronous/blocking. Freezes entire event loop.
No other coroutines can run while it computes. asyncio is single-threaded - blocking
one blocks all. Fix: Use await asyncio.to_thread(expensive_computation) or
multiprocessing."

④ FOLLOW-UP
────────────
Q: "When should you NOT use asyncio?"

STRONG:
"Don't use for:
1. CPU-bound work - blocks event loop
2. Libraries that are sync-only - blocks loop
3. Simple scripts - adds complexity
4. When team doesn't understand async

Use for: Many concurrent IO operations (APIs, databases, file I/O)."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 3B: EVENT LOOP (HIGH)
──────────────────────────────

① WARM-UP
──────────
Q: "What does the event loop do?"

STRONG: "Schedules and runs coroutines. When coroutine awaits, loop suspends it,
runs another ready coroutine. Continues until all complete. Single-threaded
cooperative multitasking."

② CORE
──────
Q: "What happens when you call async function?"

STRONG: "Returns coroutine object, doesn't execute. Must await it or run with
asyncio.run() or event loop. Example:

async def func():
    return 1

coro = func()  # Coroutine object, hasn't run
result = await coro  # Now it runs"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 3C: BLOCKING vs NON-BLOCKING (HIGH - CRITICAL)
───────────────────────────────────────────────────────

① WARM-UP
──────────
Q: "time.sleep() vs asyncio.sleep()?"

STRONG:
"time.sleep(1): BLOCKS entire thread/event loop. Nothing else runs.
asyncio.sleep(1): YIELDS control. Other coroutines can run.

In async code, ALWAYS use asyncio.sleep, never time.sleep."

② CORE
──────
Q: "Fix this performance killer:"

async def fetch_all(urls):
    results = []
    for url in urls:
        response = requests.get(url)  # BLOCKS!
        results.append(response.text)
    return results

STRONG:
import aiohttp

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [session.get(url) for url in urls]
        responses = await asyncio.gather(*tasks)
        return [await r.text() for r in responses]

"Use async library (aiohttp). requests.get() blocks - defeats purpose of async.
gather() runs all requests concurrently."

③ EDGE-CASE
────────────
Q: "Can you call synchronous function from async?"

STRONG: "Yes, but it blocks. If sync function is fast (<1ms), okay. If slow, wraps
in executor:

import asyncio

async def async_func():
    result = await asyncio.to_thread(slow_sync_func)
    # Runs in thread pool, doesn't block loop"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

4️⃣ THINK-ALOUD

QUESTION: "Why is this async code slower than sync?"

import asyncio
import requests

async def fetch(url):
    response = requests.get(url)  # Blocking!
    return response.text

async def main():
    urls = [f"http://api.com/{i}" for i in range(10)]
    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)

STRONG: "Uses blocking requests library in async code. requests.get() blocks event
loop. All requests run SEQUENTIALLY on blocked loop. Async overhead makes it slower
than plain sync. Fix: Use async library like aiohttp. Blocking calls defeat asyncio."

WEAK: "Async is just slower?" ✗ DOESN'T IDENTIFY BLOCKING

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

5️⃣ OUTPUT PREDICTION

PROBLEM:
────────
import asyncio

async def task(n):
    print(f"Start {n}")
    await asyncio.sleep(1)
    print(f"End {n}")

async def main():
    await asyncio.gather(task(1), task(2), task(3))

asyncio.run(main())

OUTPUT:
Start 1
Start 2
Start 3
(1 second pause)
End 1
End 2
End 3

REASONING: "gather() starts all tasks. Each prints 'Start', hits await, yields.
After all start, they all sleep concurrently. After 1 second, all print 'End'."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

6️⃣ COMMON FAILURES

FAILURE #1: BLOCKING THE EVENT LOOP
════════════════════════════════════

WRONG:
async def process():
    time.sleep(1)  # BLOCKS EVERYTHING!
    result = requests.get(url)  # BLOCKS!
    data = expensive_compute()  # BLOCKS!

CORRECT:
async def process():
    await asyncio.sleep(1)
    async with aiohttp.ClientSession() as session:
        result = await session.get(url)
    data = await asyncio.to_thread(expensive_compute)

FAILURE #2: NOT AWAITING COROUTINES
════════════════════════════════════

WRONG:
async def fetch():
    result = async_func()  # Returns coroutine, doesn't run!
    return result

CORRECT:
async def fetch():
    result = await async_func()  # Actually runs
    return result

FAILURE #3: USING ASYNCIO FOR CPU-BOUND
════════════════════════════════════════

WRONG:
async def compute():
    # Heavy computation
    for i in range(10_000_000):
        x = i ** 2
    return x

# Blocks event loop! async adds overhead, no benefit.

CORRECT: Use multiprocessing for CPU-bound, not asyncio.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

7️⃣ MOCK INTERVIEW

Q1: "Does asyncio provide parallelism?"
EXPECTED: "No - single-threaded cooperative concurrency" [< 10 sec]
REJECT IF: "Yes"

Q2: "time.sleep vs asyncio.sleep?"
EXPECTED: "time.sleep blocks loop, asyncio.sleep yields" [< 10 sec]

Q3: "When NOT to use asyncio?"
EXPECTED: "CPU-bound work, sync-only libraries" [< 10 sec]

Q4: "What does await do?"
EXPECTED: "Yields control to event loop, suspends coroutine" [< 10 sec]

Q5: "Why is blocking bad in async code?"
EXPECTED: "Freezes entire event loop, defeats purpose" [< 10 sec]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

8️⃣ SELF-ASSESSMENT

CRITICAL (ALL):
───────────────
□ Know asyncio is single-threaded, not parallel
□ Understand event loop schedules coroutines
□ Know await yields control
□ Never use blocking calls in async code
□ Know when asyncio is wrong choice

SCORING:
< 5/5: FAIL
5/5: PASS

INTERVIEWER:
IF FAIL: "Doesn't understand asyncio fundamentals. Would block event loop, create
slow async code. Doesn't know when to use it. REJECT."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FINAL NOTE:
asyncio is COOPERATIVE. You must explicitly yield. Blocking kills performance.
Only use for IO-bound work with async libraries. CPU-bound? Use multiprocessing.
Understanding this distinction is MANDATORY for 5+ YOE Python engineers.
"""
