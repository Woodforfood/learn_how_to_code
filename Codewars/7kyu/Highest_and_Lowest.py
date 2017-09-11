# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

def high_and_low(numbers):
    numbers = numbers.split()
    numbers = [int(i) for i in numbers]
    return str(max(numbers))+' '+str(min(numbers)) 
