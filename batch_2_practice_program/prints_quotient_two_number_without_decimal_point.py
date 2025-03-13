# prompt user to to initialize first and second number
first_number = int(input("Enter Number: "))
second_number = int(input("Enter Number: "))

# divide the value of both variables with floor division to eliminate decimal point
quotient_floor = first_number // second_number

# print quotient without decimal points.
print (quotient_floor)