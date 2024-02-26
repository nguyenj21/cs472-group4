#include "sorting.h"
#include <iostream>
#include <utility>

/*
 * @brief Sorts an array of integers using the bubble sort algorithm.
 * @param numbers - The array of integers to be sorted.
 * @param arraySize - The number of elements in the array.
 */
void bubbleSort(int numbers[], int arraySize){
    for(int i = 0; i < arraySize-1; i++){
        for(int j = 0; j < arraySize-i-1; j++){
            if(numbers[j] > numbers[j + 1]){
                std::swap(numbers[j], numbers[j + 1]);
            }
        }
    }
}

/*
 * @brief Prints the elements of an integer array.
 * @details Bubble sort repeatedly steps through the list, compares adjacent elements,
 *          and swaps them if they are in the wrong order until the entire list is sorted.
 * @param numbers - The array of integers to be printed.
 * @param arraySize - The number of elements in the array.
 */
void print(const int numbers[], int arraySize){
    for(int i = 0; i < arraySize; i++){
        std::cout << numbers[i];
        if(i < arraySize - 1){
            std::cout << ", ";
        }
    }
    std::cout << std::endl;
}