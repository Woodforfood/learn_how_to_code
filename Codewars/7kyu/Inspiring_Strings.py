# When given a string of space separated words, return the word with the longest length.
# If there are multiple words with the longest length, return the last instance of the word with the longest length.

def longest_word(string_of_words):
    longest = max(reversed(string_of_words.split()), key=len)
    return longest
