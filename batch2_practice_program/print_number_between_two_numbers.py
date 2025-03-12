# prompt user to initialize the first and last number

# 

# print numbers between the two numbers entered

first_number = int(input("Enter Number: "))
last_number = int(input("Enter Number: "))
for i in range(first_number, last_number):
    if i != first_number:
        print (i)