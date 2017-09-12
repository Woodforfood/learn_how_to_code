# Write a function that returns both the minimum and maximum number of the given list/array.

def min_max(lst):
    new_list = []
    x = min(float(i) for i in lst)
    new_list.append(x)
    a = max(float(i) for i in lst)
    new_list.append(a)
    return new_list
