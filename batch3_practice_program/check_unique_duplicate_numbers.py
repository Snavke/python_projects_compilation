# lists to store numbers entered by user
number_inputs = []
# a loop that indefinitely asks user for number
while True:
    numbers = int(input("Enter Number: "))

# exit loop

# check input
    if numbers in number_inputs:
# display message if entered number "unique" or "duplicated" after user enters number
        print ("Duplicate")
        break
    else:
        number_inputs.append(numbers)
        print ("Unique")

# terminate if non numerical value