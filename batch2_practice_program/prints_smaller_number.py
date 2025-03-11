# prompts user to enter 2 numbers for comparison
num1 = float(input("Enter Number: "))
num2 = float(input("Enter Number: "))

# compares the value of both values entered
if num1 < num2:
    # prints the lesser number if condition is met.
    print (num1)
else: 
    # prints the other number if condition is not met.
    print (num2)