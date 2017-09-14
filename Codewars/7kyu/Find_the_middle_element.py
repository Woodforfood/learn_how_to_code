# As a part of this Kata, you need to create a function that when provided with a triplet, 
# returns the index of the numerical element that lies between the other two elements.
# The input to the function will be an array of three distinct numbers (Haskell: a tuple).

import numpy as np
def gimme(input_array):
    mid = np.median(input_array)
    indexes = np.where(input_array == mid)[0]
    return indexes
