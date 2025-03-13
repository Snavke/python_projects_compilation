# lists to store numbers entered by user
number_inputs = []
# a loop that indefinitely asks user for number
while True:
    numbers = (input("Enter Number: "))
# check if input is not a number
    if not numbers.isdigit():
        # terminate if non numerical value
        break
# check input
    if numbers in number_inputs:
# display message if entered number "unique" or "duplicated" after user enters number
        print ("Duplicate")
    else:
        number_inputs.append(numbers)
        print ("Unique")