"""
Lambda Function:
accpet two values from user and perform all arithmetic operations and return all
"""
def main():
    """
    get 2 numbers as input and applying all arithmatic operations
    """
    try:
        a = float(input("Enter first no:"))
        b = float(input("enter second no:"))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    arithmatic = lambda x, y: (x + y, x - y, x * y, x / y if y != 0 else "division by zero")

    addition, subtraction, multiplication, division = arithmatic(a, b)
    print(f"\nResults of arithmetic operations on {a} and {b}:")
    print(f"Addition: {addition}")
    print(f"Subtraction: {subtraction}")
    print(f"Multiplication: {multiplication}")
    print(f"Division: {division}")

if __name__ == "__main__":
    main()
