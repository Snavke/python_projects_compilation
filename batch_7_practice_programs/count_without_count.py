# prompt user to get main string
user_input = str(input("Enter String: "))

# prompt user to enter the substring they want to count
substring_to_count = str(input("Enter Substring to Count: "))

# initialize a variable for counting the substring
count_substring = 0

# for loop for string and substring
for i in range(len(user_input) - len(substring_to_count) + 1):
# count if substring matches current position
    if user_input[i:i+len(substring_to_count)] == substring_to_count:
        count_substring += 1

# print the occurence of substring
print (f"The Substring '{substring_to_count}' occured {count_substring} times.")

