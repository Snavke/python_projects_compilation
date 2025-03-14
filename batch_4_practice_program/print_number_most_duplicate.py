# dictionary to store inputs
number_inputs = {}
# indefinitely ask for user input
while True:
    numbers = input("Enter Number: ")
# check if input is not a number
    if not numbers.isdigit():
# terminate if non numerical value
        break
# convert string inputs to int
    converted_int_number = int(numbers)

# count how many times a number shows up
    if converted_int_number in number_inputs:
        number_inputs[converted_int_number] += 1
    else:
        number_inputs[converted_int_number] = 1

    
# scan for duplicates
    if number_inputs:
        most_frequent = max (number_inputs, key=number_inputs.get)
# print most duplicated 
        print (most_frequent)
