# list to store inputs
list_smallest_number = []
# indefinite loop asking for number
while True:
    numbers_input = (input("Enter Number: "))
# check if input is not a number
    if not numbers_input.isdigit():
# exit loop if non numeric value
        break
     # safely convert string inputs to integer for safe comparisons
    converted_int_number = int(numbers_input)
# check for inputs for lowest
    if numbers_input not in list_smallest_number:
        list_smallest_number.append(converted_int_number)
# print smallest number
    print (min(list_smallest_number))