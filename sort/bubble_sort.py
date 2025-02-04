# ----- Python ---------------------------------------- #
# ----- Sorting Algorithm by Bubble Sort  ------------- #
# ----- Approximate number of operations: 0.75*n*n  --- #
# ----------------------------------------------------- #
import time
import copy
import random
from typing import List


def bubble_sort(list_to_sort: List[int]):
    temp_list = copy.deepcopy(list_to_sort)
    size = len(temp_list)

    for i in range(size - 1):
        for j in range(size - 1, i, -1):
            if temp_list[j] < temp_list[j - 1]:
                key = temp_list[j]
                temp_list[j] = temp_list[j - 1]
                temp_list[j - 1] = key

    return temp_list


if __name__ == "__main__":
    list_to_sort = [random.randint(-10000, 10000) for i in range(2000)]
    print(f"List to sort: {list_to_sort}")

    start = time.time()

    sorted_list = bubble_sort(list_to_sort)

    elapsed = time.time() - start
    print(f"Sorted list: {sorted_list}")
    print(f"Size of input list: {len(list_to_sort)}")
    print(f"Elapsed time: {elapsed} seconds")
