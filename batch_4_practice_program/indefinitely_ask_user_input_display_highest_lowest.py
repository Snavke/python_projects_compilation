# list to store inputs
list_number_inputs = []
# indefinite loop asking for number
while True:
    number_inputs = input("Enter a Number: ")
# check if input is non a number
    if not number_inputs.isdigit(): 
# terminate if non numeric value
        break
# convert string input to int
    converted_int_number = int(number_inputs)
# add to list
    list_number_inputs.append(converted_int_number)
# arrange from highest to lowest using .sort function, reversed
    list_number_inputs.sort(reverse = True)
# print list ararnged from lowest to highest
    print (list_number_inputs)