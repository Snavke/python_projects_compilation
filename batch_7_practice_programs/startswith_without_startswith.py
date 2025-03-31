# prompt to get main string
user_input = str(input("Enter a String of Characters: ")).lower()

# prompt to get prefix
user_input_prefix = str(input("Enter Prefix to Check: ")).lower()

# compare first character of text with prefix
if user_input[:len(user_input_prefix)] == user_input_prefix:
    print ("String STARTS with the given prefix.")

# print to tell if string starts or does not start with given prefix
else:
    print ("String does NOT START with the given prefix.")