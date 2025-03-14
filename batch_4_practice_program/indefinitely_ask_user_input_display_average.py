# variable to store sum of numbers
sum_of_numbers = 0
# variable to store count of numbers entered
count_of_numbers = 0
# indefinite loop asking for number
while True:
    number_inputs = input("Enter a Number: ")
# check if input is not a number
    if not number_inputs.isdigit():
# terminates if non numeric value
        break
# convert string inputs to int
    converted_int_number = int(number_inputs)
# add numbers to the sum
    sum_of_numbers += converted_int_number
# increase count
    count_of_numbers += 1
# calculate average
    if count_of_numbers > 0:
        average_of_numbers = sum_of_numbers / count_of_numbers
# print average 
        print (average_of_numbers)