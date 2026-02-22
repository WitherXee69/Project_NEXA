import subprocess
from pathlib import Path
import sys
import nexa

if getattr(sys, 'frozen', False):
    DIR_BASE = Path(sys.executable).parent
else:
    DIR_BASE = Path(__file__).parent

NEXA_DIR = DIR_BASE / "nexa.py"

if __name__ == '__main__':
    if not NEXA_DIR.exists():
        print("nexa.py not found. Please ensure it is in the same directory as this script.")
        sys.exit(1)

    # Run nexa.py
    try:
        nexa.main()
    except Exception as e:
        print(f"An error occurred while running nexa.py: {e}")
        sys.exit(1)