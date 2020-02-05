# ------------------------------------------------- #
# ----- Remove duplicates from an unsorted array/list -- #
# ------------------------------------------------- #

def remove_duplicate(inputList):
    someset = set()

    for i in inputList:
        print(i)
        someset.add(i)

    return print(someset)



sampleList = [-2, 2, 5, 5, 10, 11, 32, 100, 111, 3333]
remove_duplicate(sampleList)