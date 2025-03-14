# list to store inputs
number_inputs = []
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
# list to add duplicated numbers
duplicated_inputs = []
# scan for duplicates

