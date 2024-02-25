/*
  - Alec Him (ChatGPT Lab)
  - BubbleSort Algorithm
*/

#include <iostream>
#include "sorting.h"

int main(){
    // Array of integers to be sorted
    int numbers[] = {6, 2, 27, 24, 12, 22, 41, 19, 38, 31, 46, 35, 15, 10, 30};
    // Calculate the number of elements in the array
    int arraySize = sizeof(numbers) / sizeof(numbers[0]);
    
    // Print the unsorted array
    std::cout << "Unsorted Array" << std::endl;
    print(numbers, arraySize);
    
    // Sort the array using the bubble sort algorithm
    bubbleSort(numbers, arraySize);

    // Print the sorted array
    std::cout << "Sorted Array" << std::endl;
    print(numbers, arraySize);

    return 0;
}