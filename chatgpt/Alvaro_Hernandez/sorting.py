# Basic Python program to sort numbers in a file (inefficiently)

def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        numbers = file.readlines()
    return [int(number.strip()) for number in numbers]

def bubble_sort(numbers):
    # Purposefully inefficient sorting algorithm: Bubble Sort
    for i in range(len(numbers)):
        for j in range(0, len(numbers)-i-1):
            if numbers[j] > numbers[j+1]:
                # Swap if the element found is greater than the next element
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

def write_numbers_to_file(filename, numbers):
    with open(filename, 'w') as file:
        for number in numbers:
            file.write(f"{number}\n")

def main():
    input_filename = 'input.txt'
    output_filename = 'sorted_numbers.txt'
    
    # Reading numbers from file
    numbers = read_numbers_from_file(input_filename)
    
    # Sorting numbers (inefficiently)
    sorted_numbers = bubble_sort(numbers)
    
    # Writing sorted numbers back to a file
    write_numbers_to_file(output_filename, sorted_numbers)
    
    # Redundant: Reading and printing sorted numbers (for demonstration)
    sorted_numbers_again = read_numbers_from_file(output_filename)
    print("Sorted Numbers:", sorted_numbers_again)

if __name__ == "__main__":
    main()
