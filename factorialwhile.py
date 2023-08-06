# Python program to find the factorial of a number

#Define a factorial and loop variable
fact = 1
i = 1

# To take input from the user
num = int(input("Enter a number: "))

# check if the number is negative or positive
if num < 0:
    print("factorial does not exist for negative numbers")
else:
    while i <= num:
        fact = fact*i
        i = i + 1
    print("The factorial of", num, "is", fact)
