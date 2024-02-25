/*
  - Alec Him (ChatGPT Lab)
  - Complex Algorithm - Sum of Array
*/

#include <iostream>

/* @brief Takes an array of numbers, squares the elements, and then returns the sum of the values.
 * @param numbers - The array of integers to be used.
 * @param arraySize - The number of elements in the array.
 */
int sumOfSquares(int numbers[], int arraySize){
    int tmp[arraySize];
    for(int i = 0; i < arraySize; i++){
        tmp[i] = numbers[i] * numbers[i];
    }
    int sum = 0;
    for(int i = 0; i < arraySize; i++){
        sum += tmp[i];
    }

    return sum;
}

int main(){
    // Array of integers to be sorted
    int numbers[] = {6, 2, 27, 24, 12, 22, 41, 19, 38, 31, 46, 35, 15, 10, 30};
    // Calculate the number of elements in the array
    int arraySize = sizeof(numbers) / sizeof(numbers[0]);

    std::cout << "The sum of squares for the array is " << sumOfSquares(numbers, arraySize) << std::endl;

    return 0;
}