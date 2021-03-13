import os
from decouple import config
from unipath import Path

BASE_DIR = Path(__file__).parent
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(f"BASE_DIR: {BASE_DIR}")
print(f"CORE_DIR: {CORE_DIR}")