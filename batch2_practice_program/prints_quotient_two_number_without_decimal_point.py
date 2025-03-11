# prompts user to enter 2 numbers for comparison
num1 = int(input("Enter Number: "))
num2 = int(input("Enter Number: "))

# divides the value of both variables using floor division to eliminate decimal point
quotient_floor = num1 // num2

# prints quotient without decimal points.
print (quotient_floor)