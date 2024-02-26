def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Args:
        n (int): The number for which factorial is to be calculated.

    Returns:
        int: The factorial of the input number.

    Raises:
        ValueError: If the input number is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def main():
    """
    Main function to prompt user input for a number and calculate its factorial.
    """
    try:
        num = int(input("Enter a non-negative integer: "))
        result = factorial(num)
        print("Factorial of", num, "is", result)
    except ValueError as ve:
        print("Error:", ve)

if __name__ == "__main__":
    main()
