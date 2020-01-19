# ----- Python ---------------------------------------- #
# ----- Finding Maximum Subarray by Divide and Conquer  #
# ----- Number of operations:  0.484375*n*log(2,n) ---- #
# ----- Running time T(n) = 0.484375*n*log(2,n) ------- #
# ----------------------------------------------------- #

import random
import sys

listToSort = []

# Generating a list of random numbers
for i in range(1000):
    listToSort.append( random.randint(-10000, 1000))

# listToSort = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]  # alternative input example 
inputSize = len(listToSort)
numOfOperations = 0

def FIND_MAX_CROSSING_SUBARRAY(inputArray, lowIndex, midIndex, highIndex) :
    leftSum = -9999999
    suma = 0
    maxRightIndex = 0
    maxLeftIndex = 0
    for i in range(midIndex, lowIndex - 1, -1):
        suma += inputArray[i]
        if (suma > leftSum):
            leftSum = suma
            maxLeftIndex = i
    
    rightSum = -9999999
    suma = 0
    for j in range(midIndex + 1, highIndex + 1, 1):
        suma += inputArray[j]
        if (suma > rightSum):
            rightSum = suma
            maxRightIndex = j
    return maxLeftIndex, maxRightIndex, leftSum+rightSum


def FIND_MAXIMUM_SUBARRAY(inputArray, lowIndex, highIndex):
    global numOfOperations
    numOfOperations += 1
    if (highIndex == lowIndex):
        return lowIndex, highIndex, inputArray[lowIndex]
    else:
        midIndex = (lowIndex + highIndex)//2
        leftLowIndex, leftHighIndex, leftSum = FIND_MAXIMUM_SUBARRAY(inputArray, lowIndex, midIndex)
        rightLowIndex, rightHighIndex, rightSum = FIND_MAXIMUM_SUBARRAY(inputArray, midIndex+1, highIndex)
        crossLowIndex, crossHighIndex, crossSum = FIND_MAX_CROSSING_SUBARRAY(inputArray, lowIndex, midIndex, highIndex)

        if (leftSum >= rightSum and leftSum >= crossSum):
            return leftLowIndex, leftHighIndex, leftSum
        elif(rightSum >= leftSum and rightSum >= crossSum):
            return rightLowIndex, rightHighIndex, rightSum
        else:
            return crossLowIndex, crossHighIndex, crossSum

print('Process started ...')
maxSubarray_lowIndex, maxSubarray_highIndex, maxSubarray_sum = FIND_MAXIMUM_SUBARRAY(listToSort, 0, inputSize-1)

print('Process finished after ', numOfOperations, ' iterations.')
print('The maximum subarray is: \n', listToSort[maxSubarray_lowIndex:maxSubarray_highIndex+1], '\nAnd the sum of the subarray is: ', maxSubarray_sum)
