# prompt user to enter a character with spaces after the characters
user_input = str(input('Enter a String with Right Leading Spaces [Ex: "Hello World      "]: '))

# use index method to track place in string but start at last character
index = len(user_input) - 1

# while loop to find non-space character
while index >= 0 and user_input[index] == " ":

# move left in the string by reduction of index by 1
    index -= 1

# remove trailing spaces
user_input = user_input[:index + 1]

# print user input without left leading spaces with visual markers
print (f"|{user_input}|")