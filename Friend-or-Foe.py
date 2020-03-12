"""
Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

i.e.
"""


def friend():

    my_friends = ['P', 'pO', 'nIv', 'E0pW']
    real_friend = []
    for i in range(len(my_friends)):
        if len(my_friends[i]) == 4:
            real_friend.append(my_friends[i])
    return real_friend


print(friend())
