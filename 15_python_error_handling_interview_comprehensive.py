"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 PYTHON ERROR HANDLING - ELIMINATION INTERVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣ OVERVIEW

FILTERS:
• Those who use bare except everywhere
• Candidates who don't know exception hierarchy
• Engineers who can't explain raise vs return
• People who catch and ignore exceptions improperly

WEAK:
────
❌ Use bare except: catching everything
❌ Don't know BaseException vs Exception
❌ Catch exceptions and do nothing
❌ Don't understand exception chaining

STRONG:
──────
✓ Use specific exception types
✓ Know BaseException is root, Exception for normal errors
✓ Understand raise vs return for error signaling
✓ Use exception chaining (raise from)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

2️⃣ CONCEPTS

╔═══════════════════════════╦═══════════╦════════════════════════════════╗
║ CONCEPT                   ║ FREQUENCY ║ WHAT TESTED                    ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ Bare except anti-pattern  ║ HIGH      ║ Catches too much               ║
║                           ║           ║ REJECT: Uses everywhere        ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ Exception hierarchy       ║ MEDIUM    ║ BaseException vs Exception     ║
║                           ║           ║ REJECT: Doesn't know           ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ raise vs return           ║ HIGH      ║ Error signaling                ║
║                           ║           ║ REJECT: Returns error codes    ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ Exception chaining        ║ MEDIUM    ║ raise from                     ║
╚═══════════════════════════╩═══════════╩════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

3️⃣ QUESTIONS

SECTION 3A: BARE EXCEPT (HIGH)
───────────────────────────────

① WARM-UP
──────────
Q: "What's wrong with bare except?"

STRONG: "Catches EVERYTHING including SystemExit, KeyboardInterrupt. Can't Ctrl+C
to stop program. Masks bugs. Should use 'except Exception:' to catch normal errors
only."

WEAK: "It's less specific?" ✗ UNDERSTATES THE ISSUE

② CORE
──────
Q: "Fix this:"

try:
    risky()
except:
    pass  # Silent failure!

STRONG:
try:
    risky()
except Exception as e:
    logger.error(f"Failed: {e}")
    raise  # Re-raise after logging

"Never silently catch. Log and re-raise, or handle specifically."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 3B: raise vs return (HIGH)
───────────────────────────────────

① WARM-UP
──────────
Q: "When to use raise vs return for errors?"

STRONG:
"raise: For exceptional conditions. Caller must handle or propagate.
return: For expected outcomes, including None or error codes.

Use raise for errors. Don't return None/-1/False for errors - that's C-style, not
Pythonic."

② CORE
──────
Q: "Which is better?"

# Option 1
def divide(a, b):
    if b == 0:
        return None
    return a / b

# Option 2
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

STRONG: "Option 2. raise makes error explicit. Caller can't accidentally use None
as valid result. Python way is exceptions, not error codes."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 3C: EXCEPTION CHAINING (MEDIUM)
────────────────────────────────────────

Q: "What does 'raise from' do?"

STRONG: "Exception chaining. Preserves original exception as __cause__. Shows full
error chain in traceback. Use when catching one exception and raising another:

try:
    process()
except KeyError as e:
    raise ValueError('Invalid config') from e

Shows both ValueError and original KeyError in traceback."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

4️⃣ THINK-ALOUD

QUESTION: "What's wrong?"

try:
    data = fetch_data()
    result = process(data)
except:
    result = None

STRONG: "Bare except catches everything - even KeyboardInterrupt. If user presses
Ctrl+C, this catches it. Program won't stop. Also silently fails - no logging. Fix:

try:
    data = fetch_data()
    result = process(data)
except Exception as e:
    logging.error(f'Failed: {e}')
    raise  # Or handle specifically"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

5️⃣ OUTPUT PREDICTION

PROBLEM:
────────
try:
    try:
        raise ValueError("Inner")
    except ValueError as e:
        raise TypeError("Outer") from e
except TypeError as e:
    print(e.__cause__)

OUTPUT: Inner

REASONING: "raise from chains exceptions. __cause__ is original ValueError."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

6️⃣ COMMON FAILURES

FAILURE #1: BARE EXCEPT
═══════════════════════

WRONG:
try:
    work()
except:  # Catches KeyboardInterrupt, SystemExit!
    pass

CORRECT:
try:
    work()
except Exception as e:  # Normal errors only
    handle(e)

FAILURE #2: SILENT FAILURE
══════════════════════════

WRONG:
try:
    critical_operation()
except Exception:
    pass  # Error disappeared!

CORRECT:
try:
    critical_operation()
except Exception as e:
    logger.error(f"Failed: {e}")
    raise  # Propagate

FAILURE #3: RETURNING ERROR CODES
══════════════════════════════════

WRONG (C-style):
def get_user(id):
    user = db.find(id)
    if user is None:
        return -1  # Error code
    return user

CORRECT (Pythonic):
def get_user(id):
    user = db.find(id)
    if user is None:
        raise UserNotFoundError(f"User {id} not found")
    return user

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

7️⃣ MOCK INTERVIEW

Q1: "What's wrong with bare except?"
EXPECTED: "Catches SystemExit, KeyboardInterrupt" [< 10 sec]

Q2: "What should you catch instead?"
EXPECTED: "Exception - normal errors only" [< 5 sec]

Q3: "raise vs return for errors?"
EXPECTED: "raise - exceptions are Pythonic" [< 10 sec]

Q4: "What does 'raise from' do?"
EXPECTED: "Exception chaining, preserves cause" [< 10 sec]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

8️⃣ SELF-ASSESSMENT

CRITICAL (ALL):
───────────────
□ Never use bare except
□ Know to catch Exception, not everything
□ Use raise for errors, not return codes
□ Never silently catch exceptions
□ Understand exception chaining

SCORING:
< 5/5: FAIL
5/5: PASS

INTERVIEWER:
IF FAIL: "Would write code that silently fails and can't be interrupted. REJECT."
"""
