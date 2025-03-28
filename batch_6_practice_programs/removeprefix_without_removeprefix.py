# prompt to get main string
user_input = str(input("Enter a String of Characters: "))

# prompt to get prefix
user_input_prefix = str(input("Enter Prefix to Remove: "))

# check if input starts with prefix
if user_input.startswith(user_input_prefix):

# remove prefix
    user_input = user_input[len(user_input_prefix):]
    
# print string without prefix
print (user_input)