# Given a string str, reverse it omitting all non-alphabetic characters.

def reverse_letter(string):
    value = []
    for i in string:
        if i.isalpha():
            value.append(i)
    return "".join(value[::-1]) 
