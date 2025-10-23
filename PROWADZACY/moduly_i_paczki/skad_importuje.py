from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


import sys
print(sys.path)

sys.path.insert(0,str(BASE_DIR))