# list to store inputs
list_number_inputs = []
# loop for entering 10 numbers
for i in range (0, 10):
# store variable to list
    numbers_input = int(input("Enter Number: "))
# add numbers to existing list
    list_number_inputs.append(numbers_input)
# list to store duplicated inputs
duplicated_inputs = []
# check for duplicate
for item in list_number_inputs:
    if list_number_inputs.count(item) == 2:
        duplicated_inputs.append(item)

# print duplicated numbers
print (duplicated_inputs)