# use lists to store inputs
list_number_input = []
# prompt user to enter 10 inputs using for loop 
for i in range (0, 10):
    numbers_input = int(input("Enter Number: "))
    # use .append to add user inputs to existing list
    list_number_input.append(numbers_input)

# create list to store unique numbers
unique_inputs = []

# determine if a number is duplicated
for item in list_number_input:
    # if values in "number_inputs" is equal to one, we add it to the list "unique_inputs"
    if list_number_input.count(item) == 1:
        unique_inputs.append(item)

# print numbers without duplicate
print (unique_inputs)