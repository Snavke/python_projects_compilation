# get user input
user_input = str(input("Enter String: "))

# check if input is not empty
if user_input:

# convert first letter to uppercase, the rest in lowercase
    capitalized = user_input[0].upper() + user_input[1:].lower()

# ignore empty iput
else:
    capitalized = user_input

# print capitalized input
print (capitalized)
