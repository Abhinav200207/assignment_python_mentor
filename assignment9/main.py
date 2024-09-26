from arithmetic import add, subtract, multiply, divide
from csv_pretty import display_csv
from dotline_decorator import display_data

def main():
    # Using the arithmetic module
    print("Arithmetic Module:")
    x = 10
    y = 5
    print("Addition:", add(x, y))
    print("Subtraction:", subtract(x, y))
    print("Multiplication:", multiply(x, y))
    print("Division:", divide(x, y))

    print("\n")

    # Using the CSV Pretty Table module
    print("CSV Pretty Table Module:")
    csv_file_path = 'sample.csv'  # Make sure to have this CSV file in the correct location
    display_csv(csv_file_path)

    print("\n")

    # Using the dotline decorator module
    print("Dotline Decorator Module:")
    display_data("My name", "is abihinav", "whats you name", 123, True)

if __name__ == "__main__":
    main()
