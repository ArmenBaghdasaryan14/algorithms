# --------------------------------------------------------- #
# ----- Square Matrix Multiplication - divide and conquer - #
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

# matrixA = [[1]*numColumns for row in range(numRows)]
# matrixB = [[2]*numColumns for row in range(numRows)]
# matrixC = [[0]*numColumns for row in range(numRows)]

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
    print("A = ", matrixA)
    print("B = ", matrixB)
    n = len(matrixA)
    matrixC = np.zeros((n, n))
    print(len(matrixA), "....", len(matrixB), ".....", len(matrixC))

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

        print(".................A-s")
        print(A11)
        print(A12)
        print(A21)
        print(A22)
        print(".................B-s")
        print(B11)
        print(B12)
        print(B21)
        print(B22)
        matrixC[0:m, 0:m] = SQUARE_MATRIX_MULTIPLY_RECURSIVE(
            A11, B11
        ) + SQUARE_MATRIX_MULTIPLY_RECURSIVE(A12, B21)
        matrixC[0:m, m:n] = SQUARE_MATRIX_MULTIPLY_RECURSIVE(
            A11, B12
        ) + SQUARE_MATRIX_MULTIPLY_RECURSIVE(A12, B22)
        matrixC[m:n, 0:m] = SQUARE_MATRIX_MULTIPLY_RECURSIVE(
            A21, B11
        ) + SQUARE_MATRIX_MULTIPLY_RECURSIVE(A22, B21)
        matrixC[m:n, m:n] = SQUARE_MATRIX_MULTIPLY_RECURSIVE(
            A21, B12
        ) + SQUARE_MATRIX_MULTIPLY_RECURSIVE(A22, B22)
        n = n // 2
    print(matrixC)
    numOfOperations += 1
    return matrixC


print("Multiplication started")

SQUARE_MATRIX_MULTIPLY_RECURSIVE(matrixA, matrixB)

print("Multiplication finished")
print("Number of operations: ", numOfOperations)
