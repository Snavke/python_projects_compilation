# prompt user to enter a character with spaces before the characters
user_input = str(input('Enter a String with Left Leading Spaces[Ex: "   Hello World"]: '))

# use index method to track place in string
index = 0

# while loop to find the non-space character
while index < len(user_input) and user_input[index] == " ":

# increment index by 1
    index += 1  

# remove leading spaces
user_input = user_input[index:]

# print user input without left leading spaces
print(user_input)

