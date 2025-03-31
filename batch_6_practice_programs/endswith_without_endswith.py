# prompt to get main string
user_input = str(input("Enter a String of Characters: ")).lower()

# prompt to get suffix
user_input_suffix = str(input("Enter Suffix to Check: ")).lower()

# compare last characters of text with suffix
if user_input[-len(user_input_suffix):] == user_input_suffix:
    print ("String ENDS with the given suffix.")

# print to tell if string ends or does not end with given suffix
else: 
    print ("String does NOT END with the given suffix.")