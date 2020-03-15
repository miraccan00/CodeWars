"""
The two oldest ages function/method needs to be completed. It should take an array of numbers as its argument and return the two highest numbers within the array. The returned value should be an array in the format [second oldest age, oldest age].

The order of the numbers passed in could be any order. The array will always include at least 2 items.

For example:
"""


def two_oldest_ages(ages):
    # first i sorted mylist
    my_sorted_ages = sorted(ages)
    # and i chosed from my list most bigger number
    for i in range(len(my_sorted_ages)):
        print(i, ". element", my_sorted_ages[i])
    my_oldest_ages = [my_sorted_ages[i-1], my_sorted_ages[i]]
    print(my_oldest_ages)
    return my_oldest_ages


two_oldest_ages([10, 1])
