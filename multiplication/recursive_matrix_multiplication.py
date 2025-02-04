# --------------------------------------------------------- #
# ----- Square Matrix Multiplication - divide and conquer - #
# ----- Number of operations:    n**log(2, 7) == n**2.8  -- #
# ----- Running time T(n) =                         ------- #
# --------------------------------------------------------- #

import sys
import time
import numpy as np

sys.setrecursionlimit(5000)


def multiply_square_matrix_recursively(matrix_a, matrix_b):
    n = len(matrix_a)
    matrix_c = np.zeros((n, n))

    if n == 0:
        return matrix_c
    if n == 1:
        matrix_c[0, 0] = matrix_a[0, 0] * matrix_b[0, 0]
    else:
        m = n // 2

        A11 = matrix_a[0:m, 0:m]
        A12 = matrix_a[0:m, m:n]
        A21 = matrix_a[m:n, 0:m]
        A22 = matrix_a[m:n, m:n]

        B11 = matrix_b[0:m, 0:m]
        B12 = matrix_b[0:m, m:n]
        B21 = matrix_b[m:n, 0:m]
        B22 = matrix_b[m:n, m:n]

        matrix_c[0:m, 0:m] = multiply_square_matrix_recursively(
            A11, B11
        ) + multiply_square_matrix_recursively(A12, B21)

        matrix_c[0:m, m:n] = multiply_square_matrix_recursively(
            A11, B12
        ) + multiply_square_matrix_recursively(A12, B22)

        matrix_c[m:n, 0:m] = multiply_square_matrix_recursively(
            A21, B11
        ) + multiply_square_matrix_recursively(A22, B21)

        matrix_c[m:n, m:n] = multiply_square_matrix_recursively(
            A21, B12
        ) + multiply_square_matrix_recursively(A22, B22)

        n = n // 2

    return matrix_c


if __name__ == "__main__":
    num_rows = 32
    num_columns = 32

    matrix_a = np.zeros((num_rows, num_columns))
    matrix_b = np.zeros((num_rows, num_columns))

    count = 0
    for i in range(num_rows):
        for j in range(num_rows):
            count += 1
            matrix_a[i, j] = count
            matrix_b[i, j] = count * 10

    start = time.time()
    print("Multiplication started")

    result = multiply_square_matrix_recursively(matrix_a, matrix_b)

    print("Multiplication finished")
    elapsed = time.time() - start

    print(f"Elapsed time: {elapsed} seconds")
