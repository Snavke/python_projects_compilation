# prompt user to get main string
user_input = str(input("Enter String: "))

# prompt to ask user the desired width 
desired_width = int(input("Enter Desired Total Width: "))

# if the string is shorter than the width, add zeros to the left
if len(user_input):
    user_input = "0" * (desired_width - len(user_input)) + user_input

# print string filled with zeros
print (user_input)