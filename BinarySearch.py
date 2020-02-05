# ------------------------------------------------------------------------- #
# ----- Binary Search Algorithm  (divide and conquer, with sorted array) -- #
# ----- Time complexity O(log(2,n)) --------------------------------------- #
# ------------------------------------------------------------------------- #
import sys
sys.setrecursionlimit(2000)

def binary_search(numToFind, inputList, leftIndex, rightIndex):
    if rightIndex >= leftIndex:
        midIndex = (leftIndex + rightIndex) // 2
        print(midIndex)

        if inputList[midIndex] == numToFind:
            return print(numToFind, "found at index", midIndex)

        elif inputList[midIndex] > numToFind:
            return binary_search(numToFind, inputList, leftIndex, midIndex-1)

        else:
            return binary_search(numToFind, inputList, midIndex+1, rightIndex)
    else:
        return print('not found...')


sampleList = [-2, 2, 5, 5, 10, 11, 32, 100, 111, 3333]
numToFind = 111
binary_search(numToFind, sampleList, 0, len(sampleList)-1)
