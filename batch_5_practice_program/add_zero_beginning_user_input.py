# Prompt user to enter a number from 1-1000
number = (input("Enter a Number from (1-1000): "))
# Use .zfill string method and set to 6
add_zero = number.zfill(6)
# Print with zeros at front
print (add_zero)