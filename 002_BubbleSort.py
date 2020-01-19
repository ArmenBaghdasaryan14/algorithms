# ----- Python ---------------------------------------- #
# ----- Sorting Algorithm by Bubble Sort  ------------- #
# ----- Approximate number of operations: 0.75*n*n  --- #
# ----------------------------------------------------- #
import random

listToSort = []

# Generating a list of random numbers
for i in range(10000):
    listToSort.append( random.randint(-10000, 10000))

inputSize = len(listToSort)
numOfOperations = 0


print('Sorting started')

for i in range(inputSize-1):
    for j in range(inputSize-1, i, -1):
        numOfOperations += 1  #counting comparisons
        if (listToSort[j] < listToSort[j-1]):
            key = listToSort[j] 
            listToSort[j] = listToSort[j-1]
            listToSort[j-1] = key
            numOfOperations += 1  #counting swaps

print('Sorting finished after ', numOfOperations, ' iterations.')
        
print(listToSort)
