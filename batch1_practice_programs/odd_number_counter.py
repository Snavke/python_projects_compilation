# initiliazes where to store the amount of odd numbers are in the input
count = 0

# loop for entering 10 numbers
for i in range (0,10):
    num = float(input("Enter Number: "))
    # condition for determining if number is odd
    if num % 2 != 0:
        # if condition is met, increment by 1
        count += 1

# prints the amount of odd numbers
print (count)
    