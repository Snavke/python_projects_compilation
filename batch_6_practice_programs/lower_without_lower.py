# prompt user to get main string
user_input = str(input("Enter a String of Characters: "))

# initialize a variable to store the lowercase string
converted_lowercase = ""

# reference variable
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
# use for loop to check if character is in uppercase
for char in user_input: 
    if char in uppercase:
        index = uppercase.index(char)
        converted_lowercase += lowercase[index]
# keep lowercase characters unchanged
    else: 
        converted_lowercase += char
# print string converted to lowercase
print (converted_lowercase)
 