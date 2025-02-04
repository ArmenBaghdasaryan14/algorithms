# ----------------------------------------------------- #
# ----- Square Matrix Multiplication - simple method -- #
# ----- Number of operations:  n**3             ------- #
# ----- Running time T(n) =                     ------- #
# ----------------------------------------------------- #

import time
import numpy as np


def square_matrix_linear_multiplication(matrix_a, matrix_b):
    matrix_size = len(matrix_a)
    matrix_c = np.zeros((matrix_size, matrix_size))

    for i in range(matrix_size):
        for j in range(matrix_size):
            matrix_c[i][j] = 0
            for k in range(matrix_size):
                matrix_c[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return matrix_c


if __name__ == "__main__":
    matrix_size = 32
    num_rows = matrix_size
    num_columns = matrix_size

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

    result = square_matrix_linear_multiplication(matrix_a, matrix_b)

    print("Multiplication finished")
    elapsed = time.time() - start

    print(f"Elapsed time: {elapsed} seconds")
