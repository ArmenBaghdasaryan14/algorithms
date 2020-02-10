# Remove duplicates from an unsorted array/list #

# The following method consists in iterating over the list and
# adding each element to a set. By definition, a set consists of
# unique values, therefore, duplicates won't be added.


def remove_duplicate(inputList):
    filterSet = set()

    for i in inputList:
        filterSet.add(i)
    return list(filterSet)


sampleList = [-2, 2, 5, 5, 10, 11, 32, 100, 111, 3333]
filteredList = remove_duplicate(sampleList)
