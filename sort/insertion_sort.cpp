#include <iostream>
#include <string>

int main()
{

	int min = -1000;
	int max = 1000;
	const int INPUT_SIZE = 10;
	int numOfOperations = 0;
	int arrayToSort[INPUT_SIZE];

	for (size_t i = 0; i < INPUT_SIZE; i++)
	{
		arrayToSort[i] = rand() % (max - min + 1) + min;
	}

	std::cout << "Sorting process started ..." << std::endl;

	for (int j = 0; j < INPUT_SIZE; j++)
	{
		int key = arrayToSort[j];
		int i = j - 1;
		while (i > 0 & arrayToSort[i] > key)
		{
			arrayToSort[i + 1] = arrayToSort[i];
			i -= 1;
			numOfOperations++;
		}
		arrayToSort[i + 1] = key;
	}

	std::cout << "Sorting process finished after " << numOfOperations << " operations." << std::endl;

	for (size_t i = 0; i < INPUT_SIZE; i++)
	{
		std::cout << arrayToSort[i];
	}

	return 0;
}