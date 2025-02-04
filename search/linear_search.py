# ------------------------------------------------- #
# ----- Linear Search Algorithm  ------------------ #
# ----- Time complexity O(n) ---------------------- #
# ------------------------------------------------- #

from typing import List


def linear_search(desired_number: int, input_list: List[int]):
    for index, number in enumerate(input_list):
        if number == desired_number:
            print(desired_number, "has been found at index ", index)
            return index

    print(desired_number, "has not been found")
    return None


if __name__ == "__main__":
    sample_list = [11, 10, 2, 5, 111, 100, -2, 5, 6, 3333, 32]
    desired_number = 3333
    linear_search(desired_number, sample_list)
