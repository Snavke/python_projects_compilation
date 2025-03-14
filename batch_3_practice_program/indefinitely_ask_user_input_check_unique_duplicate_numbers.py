# lists to store numbers entered by user
list_number_input = []
# a loop that indefinitely asks user for number
while True:
    numbers_input = (input("Enter Number: "))
# check if input is not a number
    if not numbers_input.isdigit():
        # terminate if non numerical value
        break
# check input
    if numbers_input in list_number_input:
# display message if entered number "unique" or "duplicated" after user enters number
        print ("Duplicate")
    else:
        list_number_input.append(numbers_input)
        print ("Unique")