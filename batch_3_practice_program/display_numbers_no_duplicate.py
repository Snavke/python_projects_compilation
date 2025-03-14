# use lists to store inputs
number_inputs = []
# prompt user to enter 10 inputs using for loop 
for i in range (0, 10):
    numbers = int(input("Enter Number: "))
    # use .append to add user inputs to existing list
    number_inputs.append(numbers)

# create list to store unique numbers
unique_inputs = []

# determine if a number is duplicated
for item in number_inputs:
    # if values in "number_inputs" is equal to one, we add it to the list "unique_inputs"
    if number_inputs.count(item) == 1:
        unique_inputs.append(item)

# print numbers without duplicate
print (unique_inputs)