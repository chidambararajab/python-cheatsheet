#!/usr/bin/env python3
"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚀 RUN ALL PYTHON INTERVIEW PREP FILES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This script runs all training files in sequence.
Use this to review all concepts quickly.

Usage:
    python3 run_all.py              # Run all files
    python3 run_all.py --file 1     # Run specific file (01_lists_comprehensive.py)
    python3 run_all.py --quick      # Run only core data structures

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

import os
import sys
import time
import subprocess

# Define all training files in order
FILES = [
    ("01_lists_comprehensive.py", "Lists (Dynamic Arrays)", "🔴"),
    ("02_tuples_comprehensive.py", "Tuples (Immutable Sequences)", "🟠"),
    ("03_sets_comprehensive.py", "Sets (Hash Sets)", "🟡"),
    ("04_dictionaries_comprehensive.py", "Dictionaries (Hash Maps) - MOST IMPORTANT!", "🟢"),
    ("05_utility_functions.py", "Utility Functions & Pythonic Code", "🔵"),
    ("06_practice_problems.py", "Practice Problems with Solutions", "🟣"),
    ("07_interview_patterns.py", "Interview Patterns & Techniques", "⚫"),
]

QUICK_FILES = [0, 3, 2]  # Lists, Dicts, Sets (core for interviews)


def print_banner(text, color="="):
    width = 70
    print("\n" + color * width)
    print(f"{text:^{width}}")
    print(color * width + "\n")


def run_file(filepath, description, emoji):
    """Run a single Python file and show output"""
    print_banner(f"{emoji} {description}", "━")
    print(f"📄 Running: {filepath}\n")
    
    start_time = time.time()
    
    try:
        # Run the file
        result = subprocess.run(
            [sys.executable, filepath],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # Print output
        if result.stdout:
            print(result.stdout)
        
        if result.stderr:
            print("⚠️  Errors/Warnings:", file=sys.stderr)
            print(result.stderr, file=sys.stderr)
        
        # Show execution time
        elapsed = time.time() - start_time
        print(f"\n✅ Completed in {elapsed:.2f} seconds")
        
        return result.returncode == 0
        
    except subprocess.TimeoutExpired:
        print("❌ Timeout: File took too long to execute")
        return False
    except FileNotFoundError:
        print(f"❌ Error: File not found: {filepath}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def show_menu():
    """Show interactive menu"""
    print_banner("🐍 PYTHON INTERVIEW PREP - TRAINING MENU", "═")
    
    print("Choose what to run:\n")
    print("  [0] 🚀 Run ALL files (full training - ~15 minutes)")
    print("  [1] ⚡ Quick mode - Core data structures only (~5 minutes)")
    print()
    
    for i, (filename, description, emoji) in enumerate(FILES, 1):
        print(f"  [{i+1}] {emoji} {description}")
    
    print("\n  [q] Quit")
    print("\n" + "─" * 70)
    
    choice = input("\nEnter your choice: ").strip().lower()
    return choice


def main():
    """Main function"""
    
    # Check if files exist
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Parse command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "--quick":
            # Quick mode - run core files
            files_to_run = [FILES[i] for i in QUICK_FILES]
            print_banner("⚡ QUICK MODE - CORE DATA STRUCTURES", "═")
        elif sys.argv[1] == "--file" and len(sys.argv) > 2:
            # Run specific file
            try:
                file_num = int(sys.argv[2]) - 1
                if 0 <= file_num < len(FILES):
                    files_to_run = [FILES[file_num]]
                else:
                    print(f"❌ Invalid file number. Choose 1-{len(FILES)}")
                    return 1
            except ValueError:
                print("❌ Invalid file number")
                return 1
        else:
            # Run all files
            files_to_run = FILES
    else:
        # Interactive mode
        choice = show_menu()
        
        if choice == 'q':
            print("Goodbye! Happy learning! 🎉")
            return 0
        elif choice == '0':
            files_to_run = FILES
        elif choice == '1':
            files_to_run = [FILES[i] for i in QUICK_FILES]
        else:
            try:
                file_num = int(choice) - 2
                if 0 <= file_num < len(FILES):
                    files_to_run = [FILES[file_num]]
                else:
                    print(f"❌ Invalid choice. Choose 0-{len(FILES)+1} or q")
                    return 1
            except ValueError:
                print("❌ Invalid choice")
                return 1
    
    # Run selected files
    total_start = time.time()
    results = []
    
    for filename, description, emoji in files_to_run:
        if not os.path.exists(filename):
            print(f"❌ File not found: {filename}")
            continue
        
        success = run_file(filename, description, emoji)
        results.append((filename, success))
        
        # Wait a bit between files for readability
        time.sleep(0.5)
    
    # Show summary
    total_time = time.time() - total_start
    print_banner("📊 SUMMARY", "═")
    
    print(f"Total execution time: {total_time:.2f} seconds\n")
    print("Results:")
    
    success_count = 0
    for filename, success in results:
        status = "✅" if success else "❌"
        print(f"  {status} {filename}")
        if success:
            success_count += 1
    
    print(f"\n{success_count}/{len(results)} files completed successfully")
    
    if success_count == len(results):
        print("\n🎉 All files completed! You're ready for interviews!")
    
    print_banner("🚀 NEXT STEPS", "─")
    print("""
1. Review README.md for learning path
2. Check QUICK_REFERENCE.md for quick lookups
3. Practice problems on LeetCode
4. Use the narration style in real interviews
5. Time yourself solving problems

Good luck! 💪
    """)
    
    return 0 if success_count == len(results) else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
        sys.exit(1)

