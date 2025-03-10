# Initializes variable for adding the values from each prompt later on 
total = 0

# loop for entering 10 prompts
for i in range (0, 10):
    num = float(input("Enter Number: "))   
    # starting from 0 we add the values entered assigned to the variable num for each loop
    total += num

# prints the sum of the 10 inputs
print (total)

