# You need to write a function that reverses the words in a given string. A word can also fit an empty string.

def reverse(st):
    return " ".join(st.split(" ")[::-1])
