import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.myapp import calculator, developer, numbers, requests
from scripts.my_script import get_my_name
