# ----- Python ----------------------------------------- #
# ----- Sorting Algorithm by Insertion Method ---------- #
# ----- Approximate number of iterations 0.25*n*n ------ #
# ------------------------------------------------------ #
import random

listToSort = []

# Generating a list of random numbers
for i in range(10000):
    listToSort.append( random.randint(-10000, 10000))

inputSize = len(listToSort)
numOfIterations = 0

print(listToSort)

print('Sorting started')

for j in range(1, inputSize, 1):
    key = listToSort[j]
    i = j-1
    while ( key < listToSort[i] and i >= 0):
        listToSort[i+1] = listToSort[i]
        i -= 1
        numOfIterations += 1
    listToSort[i+1] = key

print('Sorting finished after ', numOfIterations, ' iterations.')

print(listToSort)
