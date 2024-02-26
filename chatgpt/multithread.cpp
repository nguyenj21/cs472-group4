#include <iostream>
#include <string>
#include <vector>
#include <thread>
#include <mutex>

std::vector<short> num1;
std::vector<short> num2;
std::vector<std::vector<short>> partialproduct;
std::vector<std::thread> threadPool;
std::mutex door;

bool fillVector(std::vector<short>& vec, const std::string& number);

void fillThreadPool(int num2_index);

void threadFunc(int num2_index);

void multiply(const std::vector<short>& num1, short digit, std::vector<short>& result);

std::string add(const std::vector<std::vector<short>>& partialproduct);

int main() {
    std::string num;

    bool valid = false;
    while (!valid) {
        std::cout << "Enter number1: ";
        std::getline(std::cin, num);
        valid = fillVector(num1, num);
    }

    valid = false;
    while (!valid) {
        std::cout << "Enter number2: ";
        std::getline(std::cin, num);
        valid = fillVector(num2, num);
    }

    auto maxthreads = std::thread::hardware_concurrency();
    for (int i = 0; i < num2.size(); i++) {
        fillThreadPool(i);
        if (threadPool.size() >= maxthreads) {
            for (auto& thread : threadPool) {
                thread.join();
            }
            threadPool.clear();
        }
    }

    for (auto& thread : threadPool) {
        thread.join();
    }
    threadPool.clear();

    for (int i = 0; i < partialproduct.size(); i++) {
        while (partialproduct[i].size() < partialproduct[partialproduct.size() - 1].size()) {
            partialproduct[i].push_back(0);
        }
    }

    std::string sum = add(partialproduct);
    std::cout << "the product is: " << sum << std::endl;

    num1.clear();
    num2.clear();
    threadPool.clear();
    partialproduct.clear();

    return 0;
}

bool fillVector(std::vector<short>& vec, const std::string& number) {
    bool valid = true;
    for (int i = number.length() - 1; i >= 0; i--) {
        if (!(number[i] >= '0' && number[i] <= '9')) {
            valid = false;
            vec.clear();
            break;
        } else {
            vec.push_back(number[i] - '0');
        }
    }
    return valid;
}

void fillThreadPool(int num2_index) {
    threadPool.push_back(std::thread(threadFunc, num2_index));
}

void threadFunc(int num2_index) {
    std::vector<short> result;
    for (int i = 0; i < num2_index; i++) {
        result.push_back(0);
    }
    int carry = 0;
    for (int i = 0; i < num1.size(); i++) {
        std::vector<short> temp;
        multiply(num1, num2[num2_index], temp);
        short part1 = temp[i] + carry;
        short to_push = part1 % 10;
        result.push_back(to_push);
        carry = part1 / 10;
    }
    if (carry > 0)
        result.push_back(carry);

    door.lock();
    partialproduct.push_back(result);
    door.unlock();
}

void multiply(const std::vector<short>& num1, short digit, std::vector<short>& result) {
    int carry = 0;
    for (auto n : num1) {
        int prod = n * digit + carry;
        result.push_back(prod % 10);
        carry = prod / 10;
    }
    if (carry > 0)
        result.push_back(carry);
}

std::string add(const std::vector<std::vector<short>>& partialproduct) {
    std::string sum = "";
    int carry = 0;
    for (int i = 0; i < partialproduct[0].size(); i++) {
        int tempSum = carry;
        for (const auto& vec : partialproduct) {
            if (i < vec.size()) {
                tempSum += vec[i];
            }
        }
        sum.insert(sum.begin(), '0' + tempSum % 10);
        carry = tempSum / 10;
    }
    while (carry > 0) {
        sum.insert(sum.begin(), '0' + carry % 10);
        carry /= 10;
    }
    return sum;
}