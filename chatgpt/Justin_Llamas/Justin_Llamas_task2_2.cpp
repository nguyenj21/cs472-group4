#include <iostream> 
#include <fstream>
#include <string>
#include "LL.h"

int main(){
    //Prompt the user for a file CHECK
    //Read in the file into the linked list CHECK

    //List to store the doubly linked list 
    LL<int> list;
    //Iterators to keep track of positioning
    LL<int>:: Iterator t1;          //Tracker 1
    LL<int>:: Iterator t2;          //Tracker 2
    LL<int>:: Iterator t3;          //Tracker 3
    LL<int>:: Iterator print;       //Print the outcome

    std::ifstream inFile;                //File reading
    std::string fileName;                //Input File
    int input;                      //Data input from file 
    bool isSorted = false;          //The array is not sorted 

    //No error checking, assume that the correct file name will be put in
    std::cout << "Enter filename:";
    std::cin >> fileName;
    inFile.open(fileName);

    //Read in the integers into the doubly linked list 
    while(inFile >> input){
        list.tailInsert(input);
    }
    inFile.close();

    //Sorting algorithm (Brick Sort aka OddEven Sorting)
    //Brick sort works in pairs 
    while(!isSorted){
        isSorted = true; //List is sorted
        //Even Sort, first cause it looked simpler to convert 
        for(t1 = list.begin(); t1 != t2; t1++){
            t3 = t1;
            t3++;
            //Check to see if t3 is nullptr for out of bounds, if so break out of the loop
            if(t3 == t2){
                break;
            }
            //Check the data and compare then swap if true 
            if(*t1 > *t3){
                list.swapNodes(t1,t3);
                isSorted = false;
            }
            t1++;
            //check if t1 is nullptr for out of bounds, if so break out of the loop
            if(t1 == t2){
                break;
            }
        }
        //Odd Sort, convert the for loop properly 
        t1 = list.begin();      //start of the list, iterator at the first point
        t1++;                   //increment to follow the i = 1 for loop

        //Inner First For Loop
            //keep incrementing t1 as long as t1 != t2 which t2 is nullptr
        for(t1; t1 != t2; t1++){
            t3 = t1;                
            t3++;                   
            
            //Check to see if t3 is nullptr for out of bounds, if so break out of the loop
            if(t3 == t2){
                break;
            }
            
            //Check the data and compare then swap if true 
            if(*t1 > *t3){
                list.swapNodes(t1,t3);
                isSorted = false;
            }

            t1++;
            //check if t1 is nullptr for out of bounds, if so break out of the loop
            if(t1 == t2){
                break;
            }
        }
    }
    //Start of the list 
    print = list.begin();
    //Keep printing until you reach the end of the list 
    while(print != nullptr){
        std::cout << *print << "\n";
        print++;
    }
}