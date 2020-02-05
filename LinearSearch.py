# ------------------------------------------------- #
# ----- Linear Search Algorithm  ------------------ #
# ----- Time complexity O(n) ---------------------- #
# ------------------------------------------------- #

def linear_search(numToFind, inputList):
    index = 0
    for i in inputList:
        if i == numToFind:
            return print(numToFind, 'has been found at index ', index)
        else:
            index += 1

    if index == len(inputList):
        return print(numToFind, 'has not been found')


sampleList = [11, 10, 2, 5, 111, 100, -2, 5, 6, 3333, 32]
numToFind = 333
linear_search(numToFind, sampleList)






