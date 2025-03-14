# dictionary to store inputs
list_number_inputs = {}
# indefinitely ask for user input
while True:
    numbers_input = input("Enter Number: ")
# check if input is not a number
    if not numbers_input.isdigit():
# terminate if non numerical value
        break
# convert string inputs to int
    converted_int_number = int(numbers_input)

# count how many times a number shows up
    if converted_int_number in list_number_inputs:
        list_number_inputs[converted_int_number] += 1
    else:
        list_number_inputs[converted_int_number] = 1

    
# scan for duplicates
    if list_number_inputs:
        most_frequent = max (list_number_inputs, key=list_number_inputs.get)
# print most duplicated 
        print (most_frequent)
