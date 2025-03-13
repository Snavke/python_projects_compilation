# list to store inputs
number_inputs = []
# prompt user to enter 10 inputs using for loop
for i in range (0,10):
    numbers = int(input("Enter Number: "))
# use .append to store inputs to existing list
    number_inputs.append(numbers)
# list to store numbers with duplicate
duplicate_inputs = []
# eliminate duplicated inputs 
for item in number_inputs:
    if number_inputs.count(item) == 2:
        duplicate_inputs.append(item) 
# print numbers 
print (duplicate_inputs)