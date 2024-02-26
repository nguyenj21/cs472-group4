#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

//constant for magic number error
const int TENK = 10000, TWO = 2 , ONEHUNDRED = 100;

int main()
{
    ifstream fin; 
    string fileName;
    int increment = 0;
    int error = 0;
    double array[ONEHUNDRED] = {};
    double fileNumber = 0;
    double sum = 0;
    //asking user for a file name
    cout << "Enter a file name" << "\n" << "**";
    //entering the fileName as a string 
    cin >> fileName;
    //opening the file
    fin.open(fileName);
    cout << endl;
    //If the user puts the wrong file name or invalid name
    cout << setprecision(TWO) << fixed;
    while(!fin.is_open())
    {
        //Ask the user to enter another file name
        cout << "Error: Invalid file name." << endl;
        //Reasking the user to enter a file name
        cout << "Enter a file name" << "\n" << "**";
        //get file name from user
        cin >> fileName;
        //open file name
        fin.open(fileName);
        cout << endl;
    }
    while(!fin.eof())
    {
        //reading in the data from the file and checking
        fin >> fileNumber;
        //if there is an error
        if(fin.fail())
        {
            //clear error
            fin.clear();
            //ignore error
            fin.ignore(TENK,'\n');
            //add 1 to error counter to keep track
            error++;
        }
        else
        {
            array[increment] = fileNumber;
            //finding the sum 
            sum = sum + fileNumber;
            //adding an increment for every time it goes through else
            increment++;
        }
    }
    //closing file
    fin.close();
    for (int i = 1; i < error; i++)
    {
        cout << "Error: Invalid input in file." << endl;
    }
    cout << endl;
    //display the valid inputs
    cout << "Amount of Elements Read In: " << increment << endl;
    //displaying the forwards data
    cout << "Forwards: ";
    for(int i = 0; i < increment; i++)
    {
        //print the value of array
        cout << array[i];
        //printing out the commas
        if(i + 1 != increment)
        {
            cout << ", ";
        }
    }
    cout << endl;
    //displaying the data backwards
    cout << "Backwards: ";
    for(int i = increment - 1; i >= 0; i--)
    {
        //print the value of array
        cout << array[i];
        //printing out the commas 
        if(i > 0)
        {
            cout << ", ";
        }
    }
    cout << endl;
    double minimum = array[0];
    //loop for checking for minimum
    for(int i = 1; i < increment; i++)
    {
        if(array[i] < minimum)
        {
            //setting minimum = the array[i] if
            //the if statement is true
            minimum = array[i];
        }
    }
    cout << "Minimum: " << minimum << endl;
    double maximum = array[0];
    //loop for checking for maximum
    for(int i = 1; i < increment; i++)
    {
        if(array[i] > maximum)
        {
            //setting maximum = array[i] if
            //the if statement is true
            maximum = array[i];
        }
    }
    //show the maximum 
    cout << "Maximum: " << maximum << endl;
    //show the sum
    cout << "Sum: " << sum << endl;
    //show the average, while also finding the average
    cout << "Average: " << sum / increment;
}