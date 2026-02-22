import subprocess
from pathlib import Path
import sys

DIR_BASE = Path.parent
NEXA_DIR = DIR_BASE / "nexa.py"

if __name__ == '__main__':
    if not NEXA_DIR.exists():
        print("nexa.py not found. Please ensure it is in the same directory as this script.")
        sys.exit(1)

    if sys.version_info is not None:
        if sys.version_info < (3, 8):
            print("Python 3.8 or higher is required to run NEXA.")
            sys.exit(1)
    else:
        print("Unable to find Python version information. Please ensure you are installed Python 3.8 or higher.")
        sys.exit(1)

    # Run nexa.py
    try:
        subprocess.run([sys.executable, str(NEXA_DIR)], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running nexa.py: {e}")
        sys.exit(1)