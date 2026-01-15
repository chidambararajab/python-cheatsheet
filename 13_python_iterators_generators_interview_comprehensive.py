"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 PYTHON ITERATORS & GENERATORS - ELIMINATION INTERVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣ OVERVIEW

FILTERS:
• Those who confuse iterable with iterator
• Candidates who don't understand generator lifecycle
• Engineers who think generators return values
• People who don't understand lazy evaluation

WEAK CANDIDATES:
───────────────
❌ Think iterables and iterators are same
❌ Don't know yield creates generator
❌ Think next() on exhausted generator returns None
❌ Don't understand memory benefits

STRONG MODEL:
────────────
✓ Iterable: has __iter__(), returns iterator
✓ Iterator: has __iter__() (returns self) and __next__()
✓ Generator: special iterator created by yield
✓ StopIteration signals exhaustion
✓ Generators are lazy - produce values on demand

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

2️⃣ CONCEPTS

╔═══════════════════════════╦═══════════╦════════════════════════════════╗
║ CONCEPT                   ║ FREQUENCY ║ WHAT TESTED                    ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ Iterable vs Iterator      ║ HIGH      ║ Protocol difference            ║
║                           ║           ║ REJECT: Confuses them          ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ Generator lifecycle       ║ HIGH      ║ Creation, execution, exhaust   ║
║                           ║           ║ REJECT: Thinks it runs eagerly ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ yield execution model     ║ HIGH      ║ Suspension, not return         ║
║                           ║           ║ REJECT: Confuses with return   ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ Generator exhaustion      ║ MEDIUM    ║ StopIteration behavior         ║
║                           ║           ║ REJECT: Expects None           ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ Memory implications       ║ MEDIUM    ║ Lazy vs eager                  ║
╚═══════════════════════════╩═══════════╩════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

3️⃣ QUESTIONS

SECTION 3A: ITERABLE VS ITERATOR (HIGH)
────────────────────────────────────────

① WARM-UP
──────────
Q: "What's the difference between iterable and iterator?"

STRONG:
"Iterable: Object with __iter__() that returns iterator. Can iterate multiple times.
         Examples: list, str, dict, file
Iterator: Object with __iter__() (returns self) and __next__(). Single-pass.
         Examples: returned by iter(list), generator, file object

List is iterable but not iterator. iter(list) returns iterator."

WEAK: "They're the same?" ✗ WRONG

② CORE
──────
Q: "What prints?"

lst = [1, 2, 3]
it = iter(lst)
print(next(it))
print(next(it))
print(next(iter(lst)))

STRONG: "1, 2, 1. First two next() calls advance iterator. Third creates NEW
iterator from list, starts fresh."

③ EDGE-CASE
────────────
Q: "Why does this fail second time?"

def process(iterator):
    for item in iterator:
        print(item)

gen = (x for x in range(3))
process(gen)
process(gen)  # Nothing prints!

STRONG: "Generators (and iterators) are exhausted after one pass. Second process()
sees empty iterator. Need to recreate generator or convert to list if reusing."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 3B: GENERATOR LIFECYCLE (HIGH)
───────────────────────────────────────

① WARM-UP
──────────
Q: "When does generator function body execute?"

STRONG: "Not when called. Calling returns generator object without executing body.
Body executes on first next() call, runs until yield, suspends. Each next() resumes
where it left off."

WEAK: "When you call it?" ✗ WRONG

② CORE
──────
Q: "Trace execution:"

def gen():
    print("Start")
    yield 1
    print("Middle")
    yield 2
    print("End")

g = gen()
print("Created")
x = next(g)
print(f"Got {x}")
y = next(g)

STRONG: Prints:
Created
Start
Got 1
Middle

"gen() returns generator, doesn't execute. First next() runs to first yield.
Second next() resumes at 'Middle'."

③ EDGE-CASE
────────────
Q: "What happens on third next()?"

STRONG: "Raises StopIteration. Generator resumes, prints 'End', function exits
naturally. No more yields, so StopIteration raised."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 3C: MEMORY IMPLICATIONS (MEDIUM)
─────────────────────────────────────────

Q: "Which is more memory efficient?"

# Option 1
def get_numbers():
    return [x**2 for x in range(1000000)]

# Option 2
def get_numbers():
    return (x**2 for x in range(1000000))

STRONG: "Option 2 (generator expression). Creates values on demand, one at a time.
O(1) memory vs O(n) for list. List creates all million numbers immediately."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

4️⃣ THINK-ALOUD

QUESTION: "Why doesn't this work?"

gen = (x for x in range(5))
print(len(gen))  # TypeError!

STRONG: "Generators don't have length - they're lazy. Values not computed yet.
Length unknown until fully consumed. Would need list(gen) to get length, but that
defeats purpose of generator (defeats memory efficiency)."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

5️⃣ OUTPUT PREDICTION

PROBLEM:
────────
def countdown(n):
    while n > 0:
        yield n
        n -= 1

gen = countdown(3)
print(next(gen))
print(list(gen))

OUTPUT:
3
[2, 1]

REASONING: "First next() yields 3. list() consumes rest, collecting [2, 1]."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

6️⃣ COMMON FAILURES

FAILURE #1: TREATING GENERATOR LIKE LIST
═════════════════════════════════════════

WRONG:
gen = (x for x in range(10))
print(len(gen))  # TypeError!
print(gen[0])    # TypeError!

GENERATORS:
- No len()
- No indexing
- Single-pass only
- Lazy evaluation

FAILURE #2: REUSING EXHAUSTED GENERATOR
════════════════════════════════════════

WRONG:
gen = (x for x in range(3))
list(gen)  # [0, 1, 2]
list(gen)  # [] - exhausted!

CORRECT: Recreate or convert to list once.

FAILURE #3: THINKING yield RETURNS
═══════════════════════════════════

WRONG BELIEF: "yield returns value like return"

CORRECT: "yield suspends function, produces value. Function resumes on next()."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

7️⃣ MOCK INTERVIEW

Q1: "List is iterable or iterator?"
EXPECTED: "Iterable. iter(list) returns iterator" [< 5 sec]

Q2: "When does generator body execute?"
EXPECTED: "On next() call, not when created" [< 10 sec]

Q3: "What does yield do?"
EXPECTED: "Suspends function, produces value" [< 5 sec]

Q4: "Exhausted generator next() call?"
EXPECTED: "Raises StopIteration" [< 5 sec]

Q5: "Generator vs list - memory?"
EXPECTED: "Generator O(1), list O(n)" [< 10 sec]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

8️⃣ SELF-ASSESSMENT

CRITICAL (ALL):
───────────────
□ Distinguish iterable from iterator
□ Know generator body doesn't execute on creation
□ Understand yield suspends, doesn't return
□ Know generators are single-pass
□ Understand StopIteration

SCORING:
< 5/5: FAIL
5/5: PASS

INTERVIEWER:
IF FAIL: "Doesn't understand iterators/generators. Would misuse them. REJECT."
"""
