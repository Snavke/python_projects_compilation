# prompt user to get main string
user_input = str(input("Enter String: "))

# prompt to ask user the desired width
desired_width = int(input("Enter Desired Total Width: "))

# if the string is shorter than the width, add spaces to right
if len(user_input) < desired_width:
    user_input = user_input + " " * (desired_width - len(user_input))

# print adjusted string with visual markers |  | to show visually tell if spaces are added 
print (f"|{user_input}|")