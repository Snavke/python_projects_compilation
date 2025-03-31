# prompt user to get main sring
user_input = str(input("Enter String: "))

# prompt to ask user the desired width
desired_width = int(input("Enter Desired Total Widt: "))

# if the string is shorter than the width, add spaces to left
if len(user_input) < desired_width:
    user_input = " " * (desired_width - len(user_input)) + user_input

# print adjusted string with visual markers
print (f"|{user_input}|")