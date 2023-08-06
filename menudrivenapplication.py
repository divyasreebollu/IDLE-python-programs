# A simple menu driven application in python

# Define some functions to perform different tasks
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y
# Display a menu with options
print("Welcome to menu driven application!")
print("choose an option from the following list:")
print("1. Add two numbers")
print("2. Subtract two numbers")
print("3. Multiply two numbers")
print("4. Exit")

# Loop until the user chooses to exit
while True:
    # Get the user's choice
    choice = input("Enter your choice: ")

    # Validate the choice
    if choice in ("1", "2", "3", "4"):
        # Perform the corresponding task
        if choice == "1":
            # Get the input numbers
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            # Call the add function and print the result
            sum= add(num1, num2)
            print(f"The sum of {num1} and {num2} is {sum}")
        elif choice == "2":
            # Get the input numbers
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            # Call the subtract function and print the result
            sub = subtract(num1, num2)
            print(f"The difference of {num1} and {num2} is {sub}")
        elif choice == "3":
            # Get the input numbers
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            # Call the multiply function and print the result
            mul = multiply(num1, num2)
            print(f"The product of {num1} and {num2} is {mul}")
        else:
            # Break out of the loop
            break
    else:
        # Print an invalid message
        print("invalid,try again")
