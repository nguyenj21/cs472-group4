#include <iostream>

void printRectangleInformation(double length, double width, double height) {
    double area = length * width;
    double perimeter = 2 * (length + width);
    double volume = length * width * height;

    std::cout << "Rectangle Area: " << area << std::endl;
    std::cout << "Rectangle Perimeter: " << perimeter << std::endl;
    std::cout << "Rectangle Volume: " << volume << std::endl;
}

int main() {
    // Define the dimensions of the first rectangle
    double length1 = 5;
    double width1 = 4;
    double height1 = 3;

    // Print information about the first rectangle
    std::cout << "First Rectangle:" << std::endl;
    printRectangleInformation(length1, width1, height1);

    // Define the dimensions of the second rectangle
    double length2 = 6;
    double width2 = 9;
    double height2 = 10;

    // Print information about the second rectangle
    std::cout << "Second Rectangle:" << std::endl;
    printRectangleInformation(length2, width2, height2);

    return 0;
}
