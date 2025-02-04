/* ---- C++ ----------------------------------------------
------- Sorting Algorithm by Bubble sort -----------------
------- Approximate number of operations 0.75*n*n --------
------------------------------------------------------- */

#include <iostream>

int bubbleSort(int *arrayToSort, size_t inputSize)
{
    int numOfOperations = 0;
    for (int i = 1; i < inputSize; i++)
    {
        for (int j = inputSize - 1; j > i; j--)
        {
            numOfOperations++; // counting comparisons
            if (arrayToSort[j] < arrayToSort[j - 1])
            {
                int key = arrayToSort[j];
                arrayToSort[j] = arrayToSort[j - 1];
                arrayToSort[j - 1] = key;
                numOfOperations++; // counting swaps
            }
        }
        return numOfOperations;
    }
}

void initializeRandomArray(int *arrayToInitialize, size_t inputSize, int min, int max)
{
    for (size_t i = 0; i < inputSize; i++)
    {
        arrayToInitialize[i] = rand() % (max - min + 1) + min;
    }
}

void printArray(int *arrayToPrint, size_t inputSize)
{
    for (size_t i = 0; i < inputSize; i++)
    {
        std::cout << arrayToPrint[i] << "  ";
    }
    std::cout << std::endl;
}

int main()
{

    int min = -1000;
    int max = 1000;
    const int INPUT_SIZE = 1000;
    int inputArray[INPUT_SIZE];

    initializeRandomArray(inputArray, INPUT_SIZE, min, max);

    std::cout << "The original array is: " << std::endl;
    printArray(inputArray, INPUT_SIZE);

    std::cout << "Sorting process started ..." << std::endl;

    std::cout << "Sorting process finished after " << bubbleSort(inputArray, INPUT_SIZE) << " operations." << std::endl;
    std::cout << "The sorted array is: " << std::endl;
    printArray(inputArray, INPUT_SIZE);

    return 0;
}