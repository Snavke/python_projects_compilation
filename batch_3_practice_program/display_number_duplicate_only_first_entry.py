# list to store inputs
list_number_inputs = []
# prompt user to enter 10 inputs using for loop
for i in range (0, 10):
    numbers_input = int(input("Enter Number: "))
    list_number_inputs.append(numbers_input)
# store unique inputs
unique_inputs = []
# eliminate duplicated input using "not in"
for item in list_number_inputs:
# check if already in list, if not add 
    if item not in unique_inputs:
# if not add to unique list
        unique_inputs.append(item)
# print numbers 
print (unique_inputs)