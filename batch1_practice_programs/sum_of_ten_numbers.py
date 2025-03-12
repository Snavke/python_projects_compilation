# initalize variable for adding the values from each prompt later on 
total_of_ten = 0

# loop for entering 10 prompts
for i in range (0, 10):
    numbers = float(input("Enter Number: "))   
    # starting from 0 we add the values entered assigned to the variable num for each loop
    total_of_ten += numbers

# prints the sum of the 10 inputs
print (total_of_ten)

