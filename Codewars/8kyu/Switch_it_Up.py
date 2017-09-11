# When provided with a number between 0-9, return it in words.
# Input :: 1
# Output :: "One".
# Try using "Switch" statements.
# This kata is meant for beginners. Rank and upvote to bring it out of beta

def switch_it_up(number):
    num = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return " ".join(num[int(i)] for i in str(number))
