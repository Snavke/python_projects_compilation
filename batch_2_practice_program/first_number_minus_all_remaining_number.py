# asks user for the first number to subtract all of the other numbers
first_number = float(input("Enter Number: "))

# create a prompt from 1 - 9 for the other 9 remaining numbers 
for i in range (0, 9):
    remaining_number = float(input("Enter Number: "))
    # subtract first number from remaining number
    first_number -= remaining_number

# print the first number with the subtracted values of the remaining number
print (first_number)
