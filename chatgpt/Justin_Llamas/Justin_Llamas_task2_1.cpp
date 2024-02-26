#include <iostream>
#include <fstream>
#include <iomanip>
#include <vector>

using namespace std;

const int MAX_ELEMENTS = 100;

int main() {
    ifstream fin; 
    string fileName;
    double fileNumber;
    vector<double> dataArray;
    double sum = 0;
    int error = 0;

    // Asking user for a file name
    cout << "Enter a file name: ";
    cin >> fileName;
    cout << endl;

    // Opening the file
    fin.open(fileName);

    // Checking if the file is opened successfully
    while (!fin.is_open()) {
        cout << "Error: Invalid file name." << endl;
        cout << "Enter a file name: ";
        cin >> fileName;
        cout << endl;
        fin.open(fileName);
    }

    // Reading data from the file
    while (fin >> fileNumber) {
        dataArray.push_back(fileNumber);
        sum += fileNumber;
    }

    // Closing the file
    fin.close();

    // Displaying error if any
    error = MAX_ELEMENTS - dataArray.size();
    if (error > 0) {
        cout << "Error: " << error << " invalid input(s) in file." << endl;
    }

    // Displaying the number of elements read in
    cout << "Amount of Elements Read In: " << dataArray.size() << endl;

    // Displaying data forwards
    cout << "Forwards: ";
    for (size_t i = 0; i < dataArray.size(); ++i) {
        cout << dataArray[i];
        if (i + 1 != dataArray.size()) {
            cout << ", ";
        }
    }
    cout << endl;

    // Displaying data backwards
    cout << "Backwards: ";
    for (int i = dataArray.size() - 1; i >= 0; --i) {
        cout << dataArray[i];
        if (i != 0) {
            cout << ", ";
        }
    }
    cout << endl;

    // Finding and displaying minimum
    double minimum = dataArray[0];
    for (size_t i = 1; i < dataArray.size(); ++i) {
        if (dataArray[i] < minimum) {
            minimum = dataArray[i];
        }
    }
    cout << "Minimum: " << minimum << endl;

    // Finding and displaying maximum
    double maximum = dataArray[0];
    for (size_t i = 1; i < dataArray.size(); ++i) {
        if (dataArray[i] > maximum) {
            maximum = dataArray[i];
        }
    }
    cout << "Maximum: " << maximum << endl;

    // Displaying sum and average
    cout << "Sum: " << sum << endl;
    cout << "Average: " << fixed << setprecision(2) << sum / dataArray.size() << endl;

    return 0;
}
