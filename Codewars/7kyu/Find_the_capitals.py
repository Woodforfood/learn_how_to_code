# Write a function that takes a single string (word) as argument. 
# The function must return an ordered list containing the indexes of all capital letters in the string.

def capitals(word):
    return [i for i, letter in enumerate(word) if letter.isupper()]
