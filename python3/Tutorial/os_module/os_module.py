import os
import time

# -------------------------------------
presentDir = os.path.abspath(os.path.dirname(__file__))
print(presentDir)
# -------------------------------------
curDir = os.getcwd()
print(curDir)

os.mkdir('newDir')

time.sleep(5)

os.rename('newDir', 'newDir2')

time.sleep(3)

os.rmdir('newDir2')
