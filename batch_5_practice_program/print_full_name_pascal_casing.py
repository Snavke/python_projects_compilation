# Prompt user to enter full name & Convert string input to .title, eliminate spaces with .replace
full_name = str(input("Please Enter Full Name: ")).title().replace(" ", "")

# Print full name in Pascal Casing
print (full_name)