# You are going to be given a word. Your job is to return the middle character of the word. 
# If the word's length is odd, return the middle character. 
# If the word's length is even, return the middle 2 characters.

def get_middle(s):
    if len(s) > 2:
        if len(s) % 2 == 0:
            x = round(len(s) / 2)
            return s[int(x - 1):int(x + 1)]
        else:
            return s[int(len(s) / 2)]
    else:
        return s
