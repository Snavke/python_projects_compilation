# variable to store highest number
highest_number = None
# indefinite loop asking for number
while True:
    number_input = input("Enter a Number: ")
# check if input is not a number
    if not number_input.isdigit():
# exit loop if non numeric value
        break
# convert input to integer
    converted_int_number = int(number_input)
# update highest number
    if highest_number is None or converted_int_number > highest_number:
        highest_number = converted_int_number
# display highest number
    print (highest_number)