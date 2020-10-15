import os
import sys


libPath = os.path.abspath(os.path.dirname(__file__)) + '../../lib'

sys.path.insert(0, libPath)
# ---------- OR ----------
sys.path.append(libPath)
