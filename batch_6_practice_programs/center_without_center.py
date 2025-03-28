# prompt user to get main string
user_input = str(input("Enter String: "))

# prompt to ask user desired width
desired_width = int(input("Enter Total Width: "))

# determine the number of spaces needed through calculations
if len(user_input) < desired_width:
    total_space = desired_width - len(user_input)
    left_space = total_space // 2
    right_space = total_space - left_space 
    user_input = " " * left_space + user_input + " " * right_space

# print adjusted string with visual markers 
print (f"|{user_input}|")