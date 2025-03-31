# prompt user to get main string
user_input = str(input("Enter a String of Characters: "))

# initialize a variable to store the uppercase string
converted_uppercase = ""

# reference variable
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# use for loop to check if character is in lowercase
for char in user_input:
    if char in lowercase:
        index = lowercase.index(char)
        converted_uppercase += uppercase[index]

# keep uppercase characters unchanged
    else: 
        converted_uppercase += char

# print string converted to uppercase
print (converted_uppercase)