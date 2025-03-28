# prompt user input to get main string
user_input = str(input("Enter String: "))

# split input into words by using .split()
split_word = user_input.split()

# variable to store string converted to title
title_case = ""

# for loop to capitalize first letter of each word and leave the rest in lowercase
for word in split_word:
    title_case += word[0].upper() + word[1:].lower() + " "
# remove spaces at the end
title_case = title_case.strip()

# print string converted to tile case
print (title_case)