/*
  - Alec Him (ChatGPT Lab)
  - Complex Algorithm - Matrix Multiplication
*/

#include <iostream>
#include <array>

template <size_t rows, size_t cols>
void matrixMult(const std::array<std::array<int, cols>, rows>& mat1, const std::array<std::array<int, cols>, rows>& mat2, std::array<std::array<int, cols>, rows>& result){
    for(size_t i = 0; i < rows; i++){
        for(size_t j = 0; j < cols; j++){
            result[i][j] = 0;
            for(size_t k = 0; k < cols; k++){
                result[i][j] += mat1[i][k] * mat2[k][j];
            }
        }
    }
}

template <size_t rows, size_t cols>
void display(const std::array<std::array<int, cols>, rows>& matrix){
    std::cout << "---------" << std::endl;
    for(int i = 0; i < rows; i++){
        std::cout << "|";
        for(int j = 0; j < cols; j++){
            std::cout << " " << matrix[i][j] << " |";
        }
        std::cout << std::endl;
    }
    std::cout << "---------" << std::endl;
}

int main(){
    std::array<std::array<int, 2>, 2> matrix1 = {{{2, 3}, {3, 5}}};
    std::array<std::array<int, 2>, 2> matrix2 = {{{2, 3}, {3, 5}}};

    constexpr size_t col1 = matrix1.size();
    constexpr size_t row2 = matrix2[0].size();
                           
    // Check if the number of columns in matrix1 is equal to the number of rows in matrix2
    if (col1 != row2) {
        std::cout << "The number of columns in matrix 1 is not equal to the number of rows in matrix 2. Unable to perform multiplication" << std::endl;
    } else {
        std::array<std::array<int, col1>, row2> result;
        std::cout << "Performing Calculation..." << std::endl;
        matrixMult(matrix1, matrix2, result);
        std::cout << "The value of the multiplication is: " << std::endl;
        display(result);
    }

    return 0;
}