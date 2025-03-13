# list to store inputs
number_inputs = []
# prompt user to enter 10 inputs using for loop
for i in range (0, 10):
    numbers = int(input("Enter Number: "))
    number_inputs.append(numbers)
# store unique inputs
unique_inputs = []
# eliminate duplicated input using "not in"
for item in number_inputs:
# check if already in list, if not add 
    if item not in unique_inputs:
# if not add to unique list
        unique_inputs.append(item)
# print numbers 
print (unique_inputs)