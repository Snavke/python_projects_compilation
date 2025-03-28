# prompt user to get main string
user_input = str(input("Enter String: "))

# variable to store swapcased string
swapcase = ""

# for loop to swapcases
for char in user_input:
# if lowercase then convert to uppercase
    if char in "abcdefghijklmnopqrstuvwxyz":
        swapcase += char.upper()
# if uppercase then convert to lowercase
    elif char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        swapcase += char.lower()
# ignore non alphabet characters
    else: 
        swapcase += char

# print swapcased version 
print (swapcase)