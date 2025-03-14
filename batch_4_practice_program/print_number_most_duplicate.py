# list to store inputs
number_inputs = []
duplicated_inputs = []
# indefinitely ask for user input
while True:
    numbers = (input("Enter Number: "))
# check if input is not a number
    if not numbers.isdigit():
# terminate if non numerical value
        break
# convert string inputs to int
    converted_int_number = int(numbers)
# add to list
    number_inputs.append(converted_int_number)
# scan for duplicates
    if number_inputs.count(converted_int_number) == 2:
        # eliminate other number if already in list
        duplicated_inputs.append(converted_int_number)          
# print number with most duplicate
    print (duplicated_inputs)
