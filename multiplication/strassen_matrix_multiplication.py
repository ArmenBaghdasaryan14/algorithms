# --------------------------------------------------------- #
# ----- Square Matrix Multiplication - divide and conquer - #
# ----- Strassen's Method --------------------------------- #
# ----- Number of operations:    n**log(2, 7) == n**2.8  -- #
# ----- Running time T(n) =                         ------- #
# --------------------------------------------------------- #

import sys
import time
import numpy as np

sys.setrecursionlimit(5000)


def multiply_square_matrix_strassen(matrix_a, matrix_b):
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

        S1 = B12 - B22
        S2 = A11 + A12
        S3 = A21 + A22
        S4 = B21 - B11
        S5 = A11 + A22
        S6 = B11 + B22
        S7 = A12 - A22
        S8 = B21 + B22
        S9 = A11 - A21
        S10 = B11 + B12

        P1 = A11 * S1
        P2 = S2 * B22
        P3 = S3 * B11
        P4 = A22 * S4
        P5 = S5 * S6
        P6 = S7 * S8
        P7 = S9 * S10

        C11 = P5 + P4 - P2 + P6
        C12 = P1 + P2
        C21 = P3 + P4
        C22 = P5 + P1 - P3 - P7
        matrix_c[0:m, 0:m] = C11
        matrix_c[0:m, m:n] = C12
        matrix_c[m:n, 0:m] = C21
        matrix_c[m:n, m:n] = C22
        n = n // 2

    return matrix_c


if __name__ == "__main__":
    numRows = 32
    numColumns = 32

    matrix_a = np.zeros((numRows, numColumns))
    matrix_b = np.zeros((numRows, numColumns))

    count = 0
    for i in range(numRows):
        for j in range(numRows):
            count += 1
            matrix_a[i, j] = count
            matrix_b[i, j] = count * 10

    start = time.time()
    print("Multiplication started")

    result = multiply_square_matrix_strassen(matrix_a, matrix_b)

    print("Multiplication finished")
    elapsed = time.time() - start

    print(f"Elapsed time: {elapsed} seconds")
