# ----- Python -------------------------------------------------- #
# ----- Sorting Algorithm by Merge Sort  ------------------------ #
# ----- Approximate number of operations:  1.0056*n*log(2,n) ---- #
# --------------------------------------------------------------- #

import sys
import time
import random
from typing import List


def merge(list_to_sort: List[int], index_left: int, index_right: int, index_last: int):
    length_left_array = (
        index_right - index_left + 1
    )  # the '+1' is for including the element at index_right
    length_right_array = index_last - index_right

    leftArray = [""] * (length_left_array + 1)  # the '+1' position is for the sentinel
    rightArray = [""] * (
        length_right_array + 1
    )  # the '+1' position is for the sentinel

    for i in range(length_left_array):
        leftArray[i] = list_to_sort[index_left + i]
    for j in range(length_right_array):
        rightArray[j] = list_to_sort[index_right + j + 1]

    leftArray[length_left_array] = 99999999999  # sentinel
    rightArray[length_right_array] = 99999999999  # sentinel

    i = 0
    j = 0

    for k in range(index_left, index_last + 1, 1):
        if leftArray[i] <= rightArray[j]:
            list_to_sort[k] = leftArray[i]
            i += 1
        else:
            list_to_sort[k] = rightArray[j]
            j += 1
    return list_to_sort


def merge_sort(list_to_sort, index_left=0, index_last=None):
    if index_last is None:
        index_last = len(list_to_sort) - 1

    if index_left < index_last:
        index_right = (index_left + index_last) // 2
        merge_sort(list_to_sort, index_left, index_right)
        merge_sort(list_to_sort, index_right + 1, index_last)
        merge(list_to_sort, index_left, index_right, index_last)
    return list_to_sort


if __name__ == "__main__":
    list_to_sort = [random.randint(-10000, 10000) for i in range(20000)]
    print(f"List to sort: {list_to_sort}")

    start = time.time()
    sys.setrecursionlimit(5000)

    sorted_list = merge_sort(list_to_sort)

    elapsed = time.time() - start
    print(f"Sorted list: {sorted_list}")
    print(f"Size of input list: {len(list_to_sort)}")
    print(f"Elapsed time: {elapsed} seconds")
