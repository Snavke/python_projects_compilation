# prompts users to enter first number
num1 = float(input("Enter Number: "))
# prompts user to enter second number
num2 = float(input("Enter Number: "))

# compares variables "num1" & "num2"
if num1 > num2:
    # prints the value of variable num1 if value is bigger than num2
    print (num1)
    # prints the value of variable num2 if condition is not met
else: 
    print (num2)