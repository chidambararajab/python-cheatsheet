"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 PYTHON IMPORTS & MODULES - ELIMINATION INTERVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣ OVERVIEW

FILTERS:
• Those who don't understand import execution
• Candidates who can't explain module caching
• Engineers who don't understand circular imports
• People who misuse if __name__ == "__main__"

WEAK:
────
❌ Think imports don't execute code
❌ Don't know modules cached in sys.modules
❌ Can't explain circular import issues
❌ Misunderstand __name__ behavior

STRONG:
──────
✓ Import executes module code once
✓ Modules cached to prevent re-execution
✓ Circular imports fail due to incomplete objects
✓ __name__ is "__main__" only when script run directly

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

2️⃣ CONCEPTS

╔═══════════════════════════╦═══════════╦════════════════════════════════╗
║ CONCEPT                   ║ FREQUENCY ║ WHAT TESTED                    ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ Import execution          ║ HIGH      ║ Code runs on import            ║
║                           ║           ║ REJECT: Thinks it's passive    ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ Module caching            ║ HIGH      ║ sys.modules prevents re-run    ║
║                           ║           ║ REJECT: Doesn't know cached    ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ Circular imports          ║ MEDIUM    ║ Why they fail                  ║
║                           ║           ║ REJECT: Can't explain          ║
╠═══════════════════════════╬═══════════╬════════════════════════════════╣
║ if __name__ == "__main__" ║ HIGH      ║ When it's True                 ║
║                           ║           ║ REJECT: Doesn't understand     ║
╚═══════════════════════════╩═══════════╩════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

3️⃣ QUESTIONS

SECTION 3A: IMPORT EXECUTION (HIGH)
────────────────────────────────────

① WARM-UP
──────────
Q: "What happens when you import a module?"

STRONG: "Python executes the module's code top-to-bottom. Functions/classes are
defined. Module-level code runs. Result is cached in sys.modules. Subsequent imports
use cache, don't re-execute."

WEAK: "It loads the code?" ✗ VAGUE

② CORE
──────
Q: "What prints?"

# module_a.py
print("Loading A")
x = 10

# main.py
import module_a
import module_a

STRONG: "Prints 'Loading A' ONCE. First import executes module, caches in
sys.modules. Second import finds in cache, doesn't re-execute."

③ EDGE-CASE
────────────
Q: "How to force re-import?"

STRONG:
import importlib
import module_a
importlib.reload(module_a)  # Re-executes

"Rarely needed. Usually sign of design issue."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 3B: if __name__ == "__main__" (HIGH)
─────────────────────────────────────────────

① WARM-UP
──────────
Q: "When is __name__ equal to '__main__'?"

STRONG: "When module is run directly as script (python module.py). If imported,
__name__ equals module name ('module'). Use to prevent code from running on import."

WEAK: "When it's the main file?" ✗ IMPRECISE

② CORE
──────
Q: "What prints?"

# script.py
def func():
    print("Func")

print("Top")

if __name__ == "__main__":
    print("Main")
    func()

# Run: python script.py
# vs import script

STRONG:
"Run directly: Prints 'Top', 'Main', 'Func'
Import: Prints only 'Top'

Top-level print always runs. if __name__ block only when script run directly."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 3C: CIRCULAR IMPORTS (MEDIUM)
──────────────────────────────────────

① WARM-UP
──────────
Q: "Why do circular imports cause problems?"

STRONG: "When A imports B which imports A, second import of A gets incomplete A
(not fully executed yet). Attributes defined after import don't exist. Causes
AttributeError."

② CORE
──────
Q: "How to fix circular import?"

STRONG:
"1. Move import inside function (delay until needed)
2. Restructure code to remove cycle
3. Import whole module, not specific names

Option 2 preferred - circular deps indicate design issue."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

4️⃣ THINK-ALOUD

QUESTION: "Why does this fail?"

# a.py
from b import func_b
def func_a():
    pass

# b.py
from a import func_a
def func_b():
    pass

STRONG: "Circular import. When a.py imports b, b.py tries to import func_a from a,
but a hasn't finished executing yet. func_a not defined. Fix: Move imports inside
functions or restructure."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

5️⃣ OUTPUT PREDICTION

PROBLEM:
────────
# mod.py
print(f"__name__ is {__name__}")

# Run: python mod.py
# vs: python -c "import mod"

OUTPUT:
Run directly: "__name__ is __main__"
Import: "__name__ is mod"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

6️⃣ COMMON FAILURES

FAILURE #1: SIDE EFFECTS AT MODULE LEVEL
═════════════════════════════════════════

WRONG:
# module.py
print("Starting server...")  # Runs on import!
start_server()

CORRECT:
def main():
    start_server()

if __name__ == "__main__":
    main()

FAILURE #2: NOT UNDERSTANDING CACHING
══════════════════════════════════════

WRONG BELIEF: "Each import re-executes module"

CORRECT: "First import executes and caches. Subsequent imports use cache."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

7️⃣ MOCK INTERVIEW

Q1: "Does import execute module code?"
EXPECTED: "Yes, once. Cached after" [< 5 sec]

Q2: "When is __name__ == '__main__'?"
EXPECTED: "When run as script directly" [< 5 sec]

Q3: "Why do circular imports fail?"
EXPECTED: "Module not fully defined yet" [< 10 sec]

Q4: "How is module cached?"
EXPECTED: "sys.modules dict" [< 5 sec]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

8️⃣ SELF-ASSESSMENT

CRITICAL (ALL):
───────────────
□ Know import executes code
□ Know modules cached in sys.modules
□ Understand if __name__ == "__main__"
□ Can explain circular import issues
□ Know to avoid module-level side effects

SCORING:
< 5/5: FAIL
5/5: PASS

INTERVIEWER:
IF FAIL: "Doesn't understand Python module system. Would structure code poorly. REJECT."
"""
