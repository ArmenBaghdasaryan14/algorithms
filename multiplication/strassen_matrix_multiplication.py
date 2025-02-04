# --------------------------------------------------------- #
# ----- Square Matrix Multiplication - divide and conquer - #
# ----- Strassen's Method --------------------------------- #
# ----- Number of operations:    n**log(2, 7) == n**2.8  -- #
# ----- Running time T(n) =                         ------- #
# --------------------------------------------------------- #

import sys
import numpy as np

sys.path.insert(0, "C:\\Users\\ARMEN\\Desktop\Algorithms")
sys.setrecursionlimit(5000)

numRows = 16
numColumns = 16
numOfOperations = 0

matrixA = np.zeros((numRows, numColumns))
matrixB = np.zeros((numRows, numColumns))
matrixD = np.zeros((numRows, numColumns))

count = 0
for i in range(numRows):
    for j in range(numRows):
        count += 1
        matrixA[i, j] = count
        matrixB[i, j] = count * 10


def SQUARE_MATRIX_MULTIPLY_RECURSIVE(matrixA, matrixB):
    global numOfOperations
    n = len(matrixA)
    matrixC = np.zeros((n, n))

    if n == 0:
        return matrixC
    if n == 1:
        matrixC[0, 0] = matrixA[0, 0] * matrixB[0, 0]
    else:
        m = n // 2

        A11 = matrixA[0:m, 0:m]
        A12 = matrixA[0:m, m:n]
        A21 = matrixA[m:n, 0:m]
        A22 = matrixA[m:n, m:n]

        B11 = matrixB[0:m, 0:m]
        B12 = matrixB[0:m, m:n]
        B21 = matrixB[m:n, 0:m]
        B22 = matrixB[m:n, m:n]

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
        matrixC[0:m, 0:m] = C11
        matrixC[0:m, m:n] = C12
        matrixC[m:n, 0:m] = C21
        matrixC[m:n, m:n] = C22
        n = n // 2
    print(matrixC)
    numOfOperations += 1
    return matrixC


print("Multiplication started")

SQUARE_MATRIX_MULTIPLY_RECURSIVE(matrixA, matrixB)

print("Multiplication finished")
print("Number of operations: ", numOfOperations)
