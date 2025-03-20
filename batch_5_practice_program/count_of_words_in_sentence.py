# Prompt user to enter a sentence
sentence = str(input("Please Enter a Sentence: "))

# Count words using .split as argument of len method
count_of_words = len(sentence.split())

# Print count of words
print (count_of_words)
