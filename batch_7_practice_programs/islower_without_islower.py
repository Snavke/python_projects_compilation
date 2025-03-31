# prompt user to get main string
user_input = str(input("Enter a String: "))

# boolean that assumes string is already in lowercase
lowercase = True

# for loop to check for uppercase characters
for char in user_input:
    if 'A' <= char <= 'Z':
        lowercase = False

# exit loop if uppercase is found
        break

# returns true or false for lowercase according to user input
print ("Characters in Lowercase?", lowercase)