# 📚 Complete Python Interview Prep - Course Index

**Complete guide for experienced developers (5+ YOE) to master Python for technical interviews**

---

## 🎯 Quick Navigation

| You Want To... | Go Here |
|---------------|---------|
| **Start learning** | [START_HERE.md](START_HERE.md) |
| **Quick syntax lookup** | [QUICK_REFERENCE.md](QUICK_REFERENCE.md) |
| **Full curriculum** | [README.md](README.md) |
| **Run all files** | `python3 run_all.py` |

---

## 📖 Course Structure

### **Phase 1: Core Data Structures (6 hours)**

#### 01. Lists - Dynamic Arrays
**File:** `01_lists_comprehensive.py`  
**Duration:** 45 minutes  
**Priority:** 🔴 CRITICAL

**You'll Learn:**
- List creation & comprehension
- Indexing & slicing (`arr[start:end:step]`)
- All list methods (append, extend, insert, remove, pop, sort, etc.)
- Two pointers pattern
- In-place modification
- Time complexity of operations

**Run:** `python3 01_lists_comprehensive.py`

---

#### 02. Tuples - Immutable Sequences
**File:** `02_tuples_comprehensive.py`  
**Duration:** 30 minutes  
**Priority:** 🟠 IMPORTANT

**You'll Learn:**
- Tuple creation & single-element trap
- Immutability & shallow copy behavior
- Tuple unpacking & swapping
- Multiple return values
- Tuples as dict keys & set elements
- When to use tuple vs list

**Run:** `python3 02_tuples_comprehensive.py`

---

#### 03. Sets - Hash Sets
**File:** `03_sets_comprehensive.py`  
**Duration:** 45 minutes  
**Priority:** 🟡 IMPORTANT

**You'll Learn:**
- Set creation & comprehension
- O(1) lookup power
- Set methods (add, remove, discard, pop)
- Set operations (union, intersection, difference)
- Duplicate detection patterns
- Visited tracking for graphs
- Hashability constraints

**Run:** `python3 03_sets_comprehensive.py`

---

#### 04. Dictionaries - Hash Maps
**File:** `04_dictionaries_comprehensive.py`  
**Duration:** 90 minutes  
**Priority:** 🟢 MOST CRITICAL (Study this twice!)

**You'll Learn:**
- Dict creation & comprehension
- get() with defaults (never use `dict[key]` directly!)
- Dict methods (keys, values, items, pop, update)
- Iteration patterns (4 different ways)
- Counter & defaultdict
- All major interview patterns (Two Sum, anagram, frequency)
- Graph adjacency lists
- Memoization for DP

**Run:** `python3 04_dictionaries_comprehensive.py`

**⚠️ This is THE most important file. 70% of interview problems use dicts!**

---

### **Phase 2: Utility Functions & Pythonic Code (2 hours)**

#### 05. Utility Functions
**File:** `05_utility_functions.py`  
**Duration:** 45 minutes  
**Priority:** 🔵 ESSENTIAL

**You'll Learn:**
- **Type checking:** isinstance(), type()
- **String methods:** join(), split(), strip(), replace(), startswith(), endswith()
- **Iteration:** range(), enumerate(), zip()
- **Functional:** map(), filter(), lambda
- **Boolean:** any(), all()
- **Sorting:** sorted() with key parameter
- **Math:** abs(), round(), sum(), min(), max()
- **Itertools:** combinations(), permutations(), product()

**Run:** `python3 05_utility_functions.py`

**💡 These functions separate beginners from experts in interviews!**

---

### **Phase 3: Interview Patterns (3 hours)**

#### 07. Interview Patterns & Techniques
**File:** `07_interview_patterns.py`  
**Duration:** 60 minutes  
**Priority:** ⚫ CRITICAL

**You'll Master:**

**Pattern 1: Two Pointers**
- Opposite ends (Two Sum sorted)
- Same direction (Remove duplicates)
- When to use: Sorted arrays, palindromes

**Pattern 2: Sliding Window**
- Fixed size (Max sum subarray)
- Dynamic size (Longest substring k distinct)
- When to use: Subarray/substring optimization

**Pattern 3: Hash Map**
- Two Sum pattern
- Frequency counting
- When to use: "Find pair that...", counting

**Pattern 4: Fast & Slow Pointers**
- Cycle detection
- Find middle
- When to use: Linked lists, cycles

**Pattern 5: Stack**
- Parentheses matching
- Next greater element
- When to use: LIFO behavior, DFS

**Pattern 6: Binary Search**
- Standard template
- Find first/last occurrence
- When to use: Sorted arrays, O(log n)

**Pattern 7: Dynamic Programming**
- Top-down (memoization)
- Bottom-up (iteration)
- When to use: Optimization, counting

**Run:** `python3 07_interview_patterns.py`

**🎯 Pattern recognition is the key to solving problems fast!**

---

### **Phase 4: Practice & Application (10+ hours)**

#### 06. Practice Problems
**File:** `06_practice_problems.py`  
**Duration:** 2-3 hours (first pass), ongoing practice  
**Priority:** 🟣 ESSENTIAL

**Problems Included:**

**Warm-up (5-10 mins each):**
1. Reverse String
2. Valid Anagram
3. Contains Duplicate

**Medium (15-25 mins each):**
4. Two Sum
5. Group Anagrams
6. Longest Substring Without Repeating Characters
7. Valid Parentheses
8. Product of Array Except Self
9. Maximum Subarray (Kadane's Algorithm)

**Each Problem Includes:**
- ✅ Think-aloud interview narration
- ✅ Brute force solution
- ✅ Optimized solution
- ✅ Time & space complexity
- ✅ Common mistakes
- ✅ Follow-up questions

**Run:** `python3 06_practice_problems.py`

**🎯 Don't just read - code these yourself!**

---

## 📚 Reference Materials

### Quick Reference
**File:** `QUICK_REFERENCE.md`  
**When to Use:** During practice, before interviews

**Contains:**
- All data structure operations (one-liners)
- Time complexity tables
- Pattern templates
- Common mistakes to avoid
- Pythonic tricks
- Interview communication templates

**Keep this open while solving LeetCode!**

---

### Full Guide
**File:** `README.md`  
**When to Use:** Planning your study schedule

**Contains:**
- Complete learning path
- Week-by-week schedule
- Practice strategy
- Success metrics
- Interview day checklist
- Resource recommendations

---

### Getting Started
**File:** `START_HERE.md`  
**When to Use:** First time opening this repo

**Contains:**
- 24-hour crash course
- Full learning path
- Daily checklists
- Troubleshooting guide
- Interview day tips
- Success metrics

---

## 🚀 Tools & Scripts

### Run All Files
**File:** `run_all.py`  
**Purpose:** Execute all training files in sequence

```bash
# Run everything (15 mins)
python3 run_all.py

# Quick mode - core concepts only (5 mins)
python3 run_all.py --quick

# Run specific file
python3 run_all.py --file 1    # Lists
python3 run_all.py --file 4    # Dictionaries
```

**Interactive menu available!**

---

## 📊 Recommended Learning Paths

### Path 1: Thorough Preparation (3 weeks)

**Week 1: Foundations**
- Day 1: Lists (01)
- Day 2: Tuples (02)
- Day 3: Sets (03)
- Day 4: Dictionaries (04) - SPEND EXTRA TIME
- Day 5: Utility Functions (05)
- Day 6-7: Practice Problems (06)

**Week 2: Patterns**
- Day 1-2: Interview Patterns (07)
- Day 3-7: LeetCode practice (5 problems/day)

**Week 3: Mastery**
- Day 1-5: LeetCode practice (10 problems/day)
- Day 6-7: Mock interviews

**Total Time:** ~60 hours  
**Best For:** Thorough preparation

---

### Path 2: Quick Prep (1 week)

**Days 1-2: Core Data Structures**
- Lists, Dictionaries, Sets (01, 04, 03)
- 4-6 hours

**Day 3: Utility Functions**
- Utility Functions (05)
- 2 hours

**Days 4-5: Patterns & Practice**
- Interview Patterns (07)
- Practice Problems (06)
- 6-8 hours

**Days 6-7: LeetCode**
- 20-30 problems
- 10-12 hours

**Total Time:** ~30 hours  
**Best For:** 1 week until interview

---

### Path 3: Emergency Crash Course (24 hours)

**Hour 1-2:** Lists + Dictionaries (01, 04)  
**Hour 3:** Sets + Tuples (03, 02)  
**Hour 4:** Utility Functions (05)  
**Hour 5-8:** Practice Problems (06)  
**Hour 9-12:** Interview Patterns (07)  
**Hour 13-24:** LeetCode top 20 problems

**Total Time:** 24 hours  
**Best For:** Interview tomorrow!

---

## 🎯 Study Tips

### Do's ✅
- **Run every file** - Don't just read
- **Code yourself** - Type out the examples
- **Practice narration** - Speak your thought process aloud
- **Time yourself** - Simulate interview pressure
- **Review mistakes** - Learn from errors
- **Use QUICK_REFERENCE.md** - Keep it open during practice

### Don'ts ❌
- **Don't just read** - You must code!
- **Don't skip basics** - Foundation is critical
- **Don't memorize solutions** - Understand patterns
- **Don't work alone** - Do mock interviews
- **Don't skip edge cases** - Test thoroughly
- **Don't panic** - You've prepared well!

---

## 📈 Progress Tracking

### After Week 1
- [ ] Completed files 01-05
- [ ] Can write Python syntax confidently
- [ ] Understand dict, list, set operations
- [ ] Can use enumerate, zip, join

### After Week 2
- [ ] Completed files 06-07
- [ ] Solved 30+ LeetCode problems
- [ ] Recognize patterns instantly
- [ ] Can explain solutions clearly

### Interview Ready
- [ ] Solved 50+ LeetCode problems
- [ ] 80%+ success on Medium problems
- [ ] Comfortable with think-aloud
- [ ] Know all 7 patterns by heart
- [ ] Can code and talk simultaneously

---

## 🔥 Most Important Files (Priority Order)

1. **04_dictionaries_comprehensive.py** 🟢 - Master this first!
2. **01_lists_comprehensive.py** 🔴 - Second most important
3. **07_interview_patterns.py** ⚫ - Pattern recognition
4. **06_practice_problems.py** 🟣 - Practice, practice, practice
5. **03_sets_comprehensive.py** 🟡 - O(1) lookup power
6. **05_utility_functions.py** 🔵 - Pythonic code
7. **02_tuples_comprehensive.py** 🟠 - Less common but important

---

## 📞 Quick Commands

```bash
# Start learning
python3 01_lists_comprehensive.py

# Review everything quickly
python3 run_all.py --quick

# Practice problems
python3 06_practice_problems.py

# Quick reference
cat QUICK_REFERENCE.md

# Full guide
cat README.md
```

---

## 🎉 You're All Set!

You now have:
- ✅ 7 comprehensive training files
- ✅ 100+ code examples with narration
- ✅ 10+ practice problems with solutions
- ✅ 7 interview patterns mastered
- ✅ Quick reference guide
- ✅ Complete learning path
- ✅ Interactive run script

**Everything you need to clear Python interviews!**

---

## 🚀 Next Steps

1. **First Time Here?**
   - Read [START_HERE.md](START_HERE.md)
   - Run `python3 01_lists_comprehensive.py`

2. **Ready to Practice?**
   - Run `python3 06_practice_problems.py`
   - Solve problems on LeetCode

3. **Need Quick Review?**
   - Open [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
   - Run `python3 run_all.py --quick`

4. **Interview Tomorrow?**
   - Follow 24-hour crash course in [START_HERE.md](START_HERE.md)
   - Review [QUICK_REFERENCE.md](QUICK_REFERENCE.md)

---

**Good luck with your interviews! 🎯**

*Remember: Success = Knowledge × Practice × Communication*

You have the knowledge (these files).  
Now add practice (LeetCode).  
Master communication (think-aloud narration).  
= Interview Success! 🎉

