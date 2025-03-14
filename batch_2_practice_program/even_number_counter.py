# initiliaze where to store the amount of even numbers are in the input
count_of_even = 0

# loop for entering 10 numbers
for i in range (0,10):
    number_input = float(input("Enter Number: "))
# condition to determine if number is even
    if number_input % 2 == 0:
# if condition is met, count as +1
        count_of_even += 1
# print the amount of even numbers
print (count_of_even)