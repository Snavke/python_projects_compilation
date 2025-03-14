# list to store inputs
list_number_input = []
# indefinite loop asking for number
while True:
    numbers_input = (input("Enter Number: "))
# check if input is not a number
    if not numbers_input.isdigit():
# terminates if non numeric value
        break
# convert string inputs to int
    converted_int_number = int(numbers_input)
# add to lists
    list_number_input.append(converted_int_number)
# arrange list from lowest to highest using .sort function
    list_number_input.sort()
# print list arranged from lowest to highest
    print (list_number_input)