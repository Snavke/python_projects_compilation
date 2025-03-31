# prompt to get main string
user_input = str(input("Enter a String of Characters: "))

# prompt to get suffix
user_input_suffix = str(input("Enter Suffix to Remove: "))

# check if input ends with suffix
if user_input.endswith(user_input_suffix):

# remove suffix
    user_input = user_input[:-len(user_input_suffix):]

# print string without suffix
print (user_input)