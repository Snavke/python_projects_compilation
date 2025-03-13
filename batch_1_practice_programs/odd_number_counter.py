# initiliaze where to store the amount of odd numbers are in the input
count_of_odd = 0

# loop for entering 10 numbers
for i in range (0,10):
    num = float(input("Enter Number: "))
    # condition to determine if number is odd
    if num % 2 != 0:
        # if condition is met, count as +1
        count_of_odd += 1

# print the amount of odd numbers
print (count_of_odd)
    