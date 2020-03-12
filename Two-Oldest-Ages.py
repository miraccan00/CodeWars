def two_oldest_ages(ages):
    # first i sorted mylist
    my_sorted_ages = sorted(ages)
    # and i chosed from my list most bigger number
    for i in range(len(my_sorted_ages)):
        print(i, ". element", my_sorted_ages[i])
    my_oldest_ages = [my_sorted_ages[i-1], my_sorted_ages[i]]
    print(my_oldest_ages)
    return my_oldest_ages


"""
def two_oldest_ages2(ages):

    my_sorted_ages = sorted(ages)
    i = len(my_sorted_ages)
    my_oldest_ages = [my_sorted_ages[i-2], my_sorted_ages[i-1]]
    return my_oldest_ages
"""


two_oldest_ages([10, 1])
