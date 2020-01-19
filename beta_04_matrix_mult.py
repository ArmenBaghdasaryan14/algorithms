# ----------------------------------------------------- #
# ----- Square Matrix Multiplication - simple method -- #
# ----- Number of operations:  n**3             ------- #   
# ----- Running time T(n) =                     ------- #
# ----------------------------------------------------- #

import numpy as np
import sys

sys.path.insert(0, 'C:\\Users\\ARMEN\\Desktop\\Algorithms')

numRows = 16
numColumns = 16
numOfOperations = 0
if(numRows == numColumns):
    matrixSize = numRows
else:
    print('Not a square matrix')
    
#matrixA = [[1]*numColumns for row in range(numRows)]
#matrixB = [[2]*numColumns for row in range(numRows)]
#matrixC = [[0]*numColumns for row in range(numRows)]
#matrixNP = np.zeros((numRows,numColumns))
    
matrixA = np.zeros((numRows, numColumns))
matrixB = np.zeros((numRows, numColumns))
matrixC = np.zeros((numRows, numColumns))     

count = 0
for i in range(numRows):
    for j in range(numRows):
        count += 1
        matrixA[i, j] = count
        matrixB[i, j] = count*10
        
def SQUARE_MATRIX_MULTIPLY(matrixA, matrixB):
    global numOfOperations
    for i in range(matrixSize):
        for j in range(matrixSize):
            matrixC[i][j] = 0
            for k in range(matrixSize):
                matrixC[i][j] += matrixA[i][k]*matrixB[k][j]
                numOfOperations += 1
    return matrixC
        

print('Multiplication started')

SQUARE_MATRIX_MULTIPLY(matrixA, matrixB)

print('Multiplication finished')
print(matrixA)
print(matrixB)
print(matrixC)
print('Number of operations: ', numOfOperations)

