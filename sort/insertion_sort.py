# ----- Python ----------------------------------------- #
# ----- Sorting Algorithm by Insertion Method ---------- #
# ----- Approximate number of iterations 0.25*n*n ------ #
# ------------------------------------------------------ #
import time
import copy
import random
from typing import List


def insertion_sort(list_to_sort: List[int]):
    temp_list = copy.deepcopy(list_to_sort)

    size = len(temp_list)

    for j in range(1, size, 1):
        key = temp_list[j]
        i = j - 1
        while key < temp_list[i] and i >= 0:
            temp_list[i + 1] = temp_list[i]
            i -= 1
        temp_list[i + 1] = key

    return temp_list


if __name__ == "__main__":
    # Generating a list of random numbers
    list_to_sort = [random.randint(-10000, 10000) for i in range(2000)]
    print(f"List to sort: {list_to_sort}")

    start = time.time()

    sorted_list = insertion_sort(list_to_sort)

    elapsed = time.time() - start
    print(f"Sorted list: {sorted_list}")
    print(f"Size of input list: {len(list_to_sort)}")
    print(f"Elapsed time: {elapsed} seconds")
