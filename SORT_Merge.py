# ----- Python -------------------------------------------------- #
# ----- Sorting Algorithm by Merge Sort  ------------------------ #
# ----- Approximate number of operations:  1.0056*n*log(2,n) ---- #
# --------------------------------------------------------------- #
import random
import sys

listToSort = []

# Generating a list of random numbers
for i in range(10000):
    listToSort.append( random.randint(-10000, 10000))


inputSize = len(listToSort)
numOfOperations = 0

def merge(inputArray, indexLeft, indexRight, indexLast):
    global numOfOperations
    lengthLeftArray = indexRight - indexLeft + 1    # the '+1' is for including the element at indexRight
    lengthRightArray = indexLast - indexRight

    leftArray = ['']*(lengthLeftArray + 1)          # the '+1' position is for the sentinel
    rightArray = ['']*(lengthRightArray + 1)        # the '+1' position is for the sentinel

    for i in range(lengthLeftArray):
        leftArray[i] = inputArray[indexLeft + i]
    for j in range(lengthRightArray):
        rightArray[j] = inputArray[indexRight + j + 1]

    leftArray[lengthLeftArray] = 99999999999        #sentinel
    rightArray[lengthRightArray] = 99999999999      #sentinel
    
    i = 0
    j = 0

    for k in range(indexLeft, indexLast+1, 1):
        if (leftArray[i] <= rightArray[j]):
            inputArray[k] = leftArray[i]
            i += 1
            numOfOperations += 1
        else:
            inputArray[k] = rightArray[j]
            j += 1     
            numOfOperations += 1
    return inputArray



def merge_sort(inputArray, indexLeft, indexLast):
    if (indexLeft < indexLast):
        indexRight = (indexLeft + indexLast)//2
        merge_sort(inputArray, indexLeft, indexRight)
        merge_sort(inputArray, indexRight+1, indexLast)
        merge(inputArray, indexLeft, indexRight, indexLast)  
    return inputArray



# Print the original list
print(listToSort)   

print('Sorting started...')

sys.setrecursionlimit(5000)
listToSort = merge_sort(listToSort, 0, inputSize-1)

print('Sorting finished after ', numOfOperations, ' iterations.')

# Print the sorted list
print(listToSort)
