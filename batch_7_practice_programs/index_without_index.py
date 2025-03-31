# prompt user to get main string
user_input = str(input("Enter String: "))

# prompt to ask user to input substring to search for
substring_to_search = str(input("Enter the Substring to Search: "))

# for loop to loop through each character of string
for index_position in range(len(user_input)):

# check if substring matches current position
    if user_input [index_position:index_position+len(substring_to_search)] == substring_to_search:
        print (f"Substring '{substring_to_search}' Located at Index {index_position}")
        break
# prints a message sin case the loops finishes without finding the substring to search
else:
    print(f"'{substring_to_search} nowhere to be found in the string.'")
