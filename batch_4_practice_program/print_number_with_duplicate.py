# list to store inputs
number_inputs = []
# loop for entering 10 numbers
for i in range (0, 10):
# store variable to list
    numbers = int(input("Enter Number: "))
# add numbers to existing list
    number_inputs.append(numbers)
# list to store duplicated inputs
duplicated_inputs = []
# check for duplicate
for item in number_inputs:
    if number_inputs.count(item) == 2:
        duplicated_inputs.append(item)

# print duplicated numbers
print (duplicated_inputs)