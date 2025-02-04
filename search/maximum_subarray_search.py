# ----- Python ---------------------------------------- #
# ----- Finding Maximum Subarray by Divide and Conquer  #
# ----- Number of operations:  0.484375*n*log(2,n) ---- #
# ----- Running time T(n) = 0.484375*n*log(2,n) ------- #
# ----------------------------------------------------- #

import time
import random
from typing import List


def find_max_crossing_subarray(input_list, low_index, mid_index, high_index):
    left_sum = -9999999
    suma = 0
    max_right_index = 0
    max_left_index = 0
    for i in range(mid_index, low_index - 1, -1):
        suma += input_list[i]
        if suma > left_sum:
            left_sum = suma
            max_left_index = i

    right_sum = -9999999
    suma = 0
    for j in range(mid_index + 1, high_index + 1, 1):
        suma += input_list[j]
        if suma > right_sum:
            right_sum = suma
            max_right_index = j
    return max_left_index, max_right_index, left_sum + right_sum


def find_maximum_subarray(
    input_list: List[int],
    low_index: int = 0,
    high_index: int = None,
) -> List[int]:
    if high_index is None:
        high_index = len(input_list) - 1

    if high_index == low_index:
        return low_index, high_index, input_list[low_index]

    else:
        mid_index = (low_index + high_index) // 2
        leftlow_index, lefthigh_index, left_sum = find_maximum_subarray(
            input_list, low_index, mid_index
        )
        rightlow_index, righthigh_index, right_sum = find_maximum_subarray(
            input_list, mid_index + 1, high_index
        )
        crosslow_index, crosshigh_index, crossSum = find_max_crossing_subarray(
            input_list, low_index, mid_index, high_index
        )

        if left_sum >= right_sum and left_sum >= crossSum:
            return leftlow_index, lefthigh_index, left_sum

        elif right_sum >= left_sum and right_sum >= crossSum:
            return rightlow_index, righthigh_index, right_sum

        else:
            return crosslow_index, crosshigh_index, crossSum


if __name__ == "__main__":
    input_list = [random.randint(-10000, 10000) for i in range(20)]
    print(f"Input list: {input_list}")

    start = time.time()

    max_subarray_low_index, max_subarray_high_index, max_subarray_sum = (
        find_maximum_subarray(input_list)
    )

    max_subarray = input_list[max_subarray_low_index : max_subarray_high_index + 1]

    elapsed = time.time() - start
    print(f"Max subarray: {max_subarray}")
    print(f"Max subarray sum: {max_subarray_sum}")
