#include <iostream>
#include <string>

int main(){
	
	int min = -1000;
	int max =  1000;
	int inputSize = 10;
	int numOfOperations = 0;
	int arrayToSort[inputSize];

	for(size_t i = 0; i < inputSize; i++){
		arrayToSort[i] = rand()%(max-min + 1) + min;
	}

	std::cout << "Sorting process started ..." << std::endl;
	
	for (int j=0; j<inputSize; j++){
		int key = arrayToSort[j];
		int i = j - 1;
		while(i > 0 & arrayToSort[i] > key){
			arrayToSort[i+1] = arrayToSort[i];
			i -= 1;
			numOfOperations++;
		}
		arrayToSort[i+1] = key;
	}

	std::cout << "Sorting process finished after "<< numOfOperations << " operations."<< std::endl;

	for(size_t i = 0; i < inputSize; i++){
		std::cout << arrayToSort[i];
	}


	return 0;
}