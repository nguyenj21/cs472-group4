/*
  - Alec Him (ChatGPT Lab)
  - BubbleSort Algorithm
*/

#include <iostream>
#include "sorting.h"

int main(){
    int numbers[] = {6, 2, 27, 24, 12, 22, 41, 19, 38, 31, 46, 35, 15, 10, 30};
    int arraySize = sizeof(numbers) / sizeof(numbers[0]);
    
    std::cout << "Unsorted Array" << std::endl;
    print(numbers, arraySize);
    
    bubbleSort(numbers, arraySize);

    std::cout << "Sorted Array" << std::endl;
    print(numbers, arraySize);

    return 0;
}