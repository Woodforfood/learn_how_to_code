# Mr. Scrooge has a sum of money 'P' that wants to invest, and he wants to know how many years 'Y' 
# this sum has to be kept in the bank in order for this sum of money to amount to 'D'.
# The sum is kept for 'Y' years in the bank where interest 'I' is paid yearly, 
# and the new sum is re-invested yearly after paying tax 'T'
# Thus Mr. Scrooge has to wait for 3 years for the initial pricipal to ammount to the desired sum.
# Your task is to complete the method provided and return the number of years 'Y' as a whole in order 
# for Mr. Scrooge to get the desired sum.

def calculate_years(principal, interest, tax, desired):
    years = 0
    result = principal
    while result < desired:
        years += 1
        result_after = result * interest
        result_after -= result_after * tax
        result += result_after
    return years
