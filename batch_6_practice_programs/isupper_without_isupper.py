# prompt user to get main string
user_input = str(input("Enter a String: "))

# boolean that assumes string is already in uppercase
uppercase = True

# for loop to check for lowercase characters
for char in user_input:
    if 'a' <= char <= 'z':
        uppercase = False
# exit loop if lowercase is found
        break

# returns true or false value for uppercase according to user input
print ("Characters in Uppercase?", uppercase)