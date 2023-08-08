import os
import sys
MAX = 2
print(sys.getdefaultencoding())
print(os.path.basename(ps.getcwd()))
for i in range(3):
    print(i, end=" ")
    if MAX > 1:
        print(MAX)
    else:
        print("#")

