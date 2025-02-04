# ------------------------------------------------------------------------- #
# ----- Binary Search Algorithm  (divide and conquer, with sorted array) -- #
# ----- Time complexity O(log(2,n)) --------------------------------------- #
# ------------------------------------------------------------------------- #

import sys
from typing import List

sys.setrecursionlimit(2000)


def binary_search(
    desired_number: int,
    input_list: List[int],
    left_index: int = 0,
    right_index: int = None,
):
    if right_index is None:
        right_index = len(input_list) - 1

    if right_index >= left_index:
        mid_index = (left_index + right_index) // 2

        if input_list[mid_index] == desired_number:
            print(desired_number, "found at index", mid_index)
            return mid_index

        elif input_list[mid_index] > desired_number:
            return binary_search(desired_number, input_list, left_index, mid_index - 1)

        else:
            return binary_search(desired_number, input_list, mid_index + 1, right_index)
    else:
        print("Desired number not found...")
        return None


if __name__ == "__main__":
    sample_list = [-2, 2, 5, 5, 10, 11, 32, 100, 111, 3333]
    desired_number = 111
    binary_search(desired_number, sample_list)
