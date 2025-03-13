# list to store inputs
smallest_number = []
# indefinite loop asking for number
while True:
    numbers = (input("Enter Number: "))
# check if input is not a number
    if not numbers.isdigit():
# exit loop if non numeric value
        break
     # safely convert string inputs to integer for safe comparisons
    converted_int_number = int(numbers)
# check for inputs for lowest
    if numbers not in smallest_number:
        smallest_number.append(converted_int_number)
# print smallest number
    print (min(smallest_number))