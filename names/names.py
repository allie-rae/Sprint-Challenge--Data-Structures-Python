import time
from binary_search_tree import BSTNode
import math

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# I'm sorting the second file so I can
# check for duplicates more efficiently
# names_2 = sorted(names_2)
# for name_1 in names_1:
#     names = names_2
#     while len(names):
#         start = 0
#         end = len(names) - 1
#         middle = math.ceil((end - start) / 2)
#         if names[middle] == name_1:
#             duplicates.append(name_1)
#             break
#         elif name_1 > names[middle]:
#             start = middle + 1
#             names = names[start:]
#         elif name_1 < names[middle]:
#             end = middle - 1
#             names = names[:middle]

# just remembered binary search tree would
# probably be the better answer to this Q

# root node
bstree = BSTNode(names_2[0])
for name in names_2:
    if name != name[0]:
        bstree.insert(name)

for name in names_1:
    if bstree.contains(name):
        duplicates.append(name)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
