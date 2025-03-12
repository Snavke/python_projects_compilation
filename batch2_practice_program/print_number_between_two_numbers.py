# prompt user to initialize the first and last number
first_number = int(input("Enter Number: "))
last_number = int(input("Enter Number: "))

# for loop create range with start as the "first_number" and stop as "last_number" both entered by user
for i in range(first_number, last_number):
# skip first number in range since prompt only need the numbers in between
    if i != first_number:
# print numbers between the two numbers entered
        print (i)