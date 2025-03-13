# list to store inputs
number_inputs = []
# indefinite loop asking for number
while True:
    numbers = (input("Enter Number:"))
# check if input is not a number
    if not numbers.isdigit():
# terminates if non numeric value
        break
# convert string inputs to int
    converted_int_number = int(numbers)
    number_inputs.append(converted_int_number)
# arrange list from lowest to highest using .sort function
    number_inputs.sort
# print list arranged from lowest to highest
    print (number_inputs)