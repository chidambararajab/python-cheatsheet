"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 PYTHON CONTROL FLOW - ELIMINATION INTERVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Interviewer: Staff Engineer | Elimination Round
Target: 5+ YOE | Purpose: Filter those who don't understand Python's control flow
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣ OVERVIEW

WHY CONTROL FLOW QUESTIONS:
───────────────────────────
Control flow reveals if candidates understand Python's unique features vs just
memorizing syntax. for-else and while-else separate pretenders from experts.

FILTERS:
• Those who don't know for-else/while-else exist
• Candidates who confuse pass/continue/break
• Engineers who misuse try-except-else-finally
• People who don't understand exception flow

WEAK CANDIDATES:
───────────────
❌ Never heard of for-else
❌ Think pass and continue are same
❌ Don't know try-except-else-finally order
❌ Use bare except everywhere
❌ Don't understand when exceptions propagate

STRONG MENTAL MODEL:
───────────────────
✓ Knows for-else executes when loop completes normally
✓ Distinguishes pass (do nothing) from continue (next iteration)
✓ Understands try-except-else-finally execution order
✓ Knows when to use raise vs return
✓ Uses specific exception types, not bare except

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

2️⃣ CONCEPT BREAKDOWN

╔═══════════════════════════╦═══════════╦════════════════════════════════╗
║ CONCEPT                   ║ FREQUENCY ║ WHAT TESTED                    ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ for-else / while-else     ║ HIGH      ║ Unique Python feature          ║
║                           ║           ║ REJECT: Never heard of it      ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ pass vs continue vs break ║ HIGH      ║ Loop control                   ║
║                           ║           ║ REJECT: Confuses them          ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ try-except-else-finally   ║ HIGH      ║ Exception handling order       ║
║                           ║           ║ REJECT: Wrong order            ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ Bare except anti-pattern  ║ MEDIUM    ║ Catching too much              ║
║                           ║           ║ REJECT: Uses everywhere        ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ raise vs return           ║ MEDIUM    ║ Error signaling                ║
╚═══════════════════════════╩═══════════╩════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

3️⃣ INTERVIEW QUESTIONS

SECTION 3A: for-else (HIGH - PYTHON-SPECIFIC)
──────────────────────────────────────────────

① WARM-UP
──────────
Q: "What does else do after a for loop?"

STRONG: "Executes if loop completes normally (not broken). If break executes, else
skipped. Useful for search patterns where else handles 'not found' case."

WEAK: "Never heard of for-else" ✗ RED FLAG for Python experience

② CORE
──────
Q: "Predict output:"

for i in range(3):
    if i == 5:
        break
else:
    print("Completed")

STRONG: "Prints 'Completed'. Loop never breaks (i never equals 5), so completes
normally. else executes."

③ EDGE-CASE
────────────
Q: "Rewrite this without for-else:"

for item in items:
    if predicate(item):
        result = item
        break
else:
    raise ValueError("Not found")

STRONG: 
found = False
for item in items:
    if predicate(item):
        result = item
        found = True
        break
if not found:
    raise ValueError("Not found")

"for-else avoids the found flag pattern."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 3B: pass/continue/break (HIGH)
───────────────────────────────────────

① WARM-UP
──────────
Q: "Difference between pass, continue, and break?"

STRONG:
"pass: Do nothing, placeholder for syntax
continue: Skip rest of current iteration, go to next
break: Exit loop entirely"

② CORE
──────
Q: "What prints?"

for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)

STRONG: "Prints 0, 1, 3. Skips 2 (continue), never reaches 4 (break before print)."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 3C: try-except-else-finally (HIGH)
───────────────────────────────────────────

① WARM-UP
──────────
Q: "Execution order of try-except-else-finally?"

STRONG:
"1. try block executes
2. If exception: matching except block
3. If NO exception: else block (if present)
4. finally ALWAYS executes (cleanup)

else only runs if try succeeds. finally runs regardless."

② CORE
──────
Q: "When does else execute?"

try:
    risky()
except ValueError:
    handle()
else:
    success()
finally:
    cleanup()

STRONG: "else runs ONLY if try completes without exception. If ValueError raised,
else skipped. finally always runs last."

③ EDGE-CASE
────────────
Q: "Does finally run if return in try?"

def func():
    try:
        return 1
    finally:
        return 2

STRONG: "Returns 2. finally executes even after return. If finally has return, it
overrides try's return. This is confusing - avoid return in finally."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

4️⃣ THINK-ALOUD

QUESTION: "Explain for-else"

STRONG: "else block after for executes when loop completes normally - meaning no
break. If break executes, else skipped. Typical use: searching. If found, break.
If not found (loop completes), else handles it. Cleaner than flag variables."

WEAK: "It runs after the loop?" ✗ INCOMPLETE - doesn't mention break condition

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

5️⃣ OUTPUT PREDICTION

PROBLEM 1:
──────────
def search(items, target):
    for item in items:
        if item == target:
            return item
    else:
        return None

print(search([1, 2, 3], 5))

OUTPUT: None
REASONING: "Loop completes without return, so else executes, returns None."

PROBLEM 2:
──────────
try:
    x = 1 / 0
except ZeroDivisionError:
    print("A")
else:
    print("B")
finally:
    print("C")

OUTPUT: A, C
REASONING: "Exception raised, except runs (prints A). else skipped because exception.
finally always runs (prints C)."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

6️⃣ COMMON FAILURES

FAILURE #1: NOT KNOWING for-else
═════════════════════════════════

QUESTION: "How to handle 'not found' after search loop?"

WEAK: Use flag variable

STRONG: Use for-else:
for item in items:
    if matches(item):
        found_item = item
        break
else:
    raise NotFoundError()

FAILURE #2: CONFUSING continue WITH pass
═════════════════════════════════════════

continue: Skips to next iteration
pass: Does nothing, continues to next statement

FAILURE #3: BARE except
═══════════════════════

WRONG:
try:
    risky()
except:  # Catches EVERYTHING including KeyboardInterrupt!
    pass

CORRECT:
try:
    risky()
except Exception as e:  # Catches normal exceptions only
    log(e)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

7️⃣ MOCK INTERVIEW

Q1: "What is for-else?"
EXPECTED: "else runs if loop completes without break" [< 10 sec]
REJECT IF: "Never heard of it"

Q2: "pass vs continue?"
EXPECTED: "pass does nothing, continue skips to next iteration" [< 5 sec]

Q3: "When does try-else run?"
EXPECTED: "Only if try completes without exception" [< 10 sec]

Q4: "What's wrong with bare except?"
EXPECTED: "Catches too much - even system exits" [< 10 sec]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

8️⃣ SELF-ASSESSMENT

CRITICAL (ALL required):
────────────────────────
□ Know for-else and when it executes
□ Distinguish pass/continue/break
□ Understand try-except-else-finally order
□ Know else runs only if no exception
□ Know finally always runs

SCORING:
< 5/5: FAIL - Missing control flow basics
5/5: PASS - Understands Python control flow

INTERVIEWER:
IF PASS: "Knows Python-specific control flow features"
IF FAIL: "Lacks Python fundamentals. REJECT."
"""
