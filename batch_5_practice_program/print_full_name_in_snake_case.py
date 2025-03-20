# Prompt user to enter full name & Convert string input to .lower, change spaces to _ with .replace
full_name = str(input("Please Enter Full Name: ")).lower().replace(" ", "_")
# Print full name in Snake Case
print (full_name)