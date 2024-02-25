/*
  - Alec Him (ChatGPT Lab)
  - BubbleSort Algorithm
*/

#include <iostream>

using namespace std;

// Function Prototypes
void swap(int&, int&);
void bubbleSort(int[], int);
void print(int[], int);

// Function Declarations
void swap(int &a, int &b){
    int tmp = a;
    a = b;
    b = tmp;
}
void bubbleSort(int num[], int size){
    for(int i = 0; i < size-1; i++){
        for(int j = 0; j < size-i-1; j++){
            if(num[j] > num[j + 1]){
                swap(num[j], num[j + 1]);
            }
        }
    }
}
void print(int num[], int size){
    for(int i = 0; i < size; i++){
       cout << num[i];
       if(i < size - 1){
            cout << ", ";
       }
    }
    cout << endl;
}

int main(){
    int num[] = {6, 2, 27, 24, 12, 22, 41, 19, 38, 31, 46, 35, 15, 10, 30};
    int numSize = sizeof(num) / sizeof(num[0]);
    cout << "Unsorted Array" << endl;
    print(num, numSize);
    bubbleSort(num, numSize);
    cout << "Sorted Array" << endl;
    print(num, numSize);

    return 0;
}