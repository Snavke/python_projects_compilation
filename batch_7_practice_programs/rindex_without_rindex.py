# prompt user to get main string
user_input = str(input("Enter String: "))

# prompt to ask user to input substring to search for
substring_to_search = str(input("Enter the Substring to Search: "))

# loop through each character of string from the end
for index_position in range(len(user_input) - len(substring_to_search), -1, -1):

# check if substring matches at current 
    if user_input[index_position:index_position + len(substring_to_search)] == substring_to_search:
        print (f"Substring '{substring_to_search}' Located at Index {index_position}")
        break

# prints a message in case the loop finishes without finding a substring
else:
    print(f"'{substring_to_search} nowhere to be found in the string.'")
