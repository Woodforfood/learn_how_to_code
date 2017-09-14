# Complete the squareSum/square_sum/SquareSum method so that 
# it squares each number passed into it and then sums the results together.

def square_sum(numbers):
    numbers = [i**2 for i in numbers]
    return sum(numbers)
