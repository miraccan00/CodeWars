"""
if you want to read more

https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python

"""


def disemvowel(string):
    sesli = ["a", "e", "ı", "i", "o", "u"]
    for i in range(len(sesli)):
        if sesli[i] in string or sesli[i].upper() in string:
            string = string.replace(sesli[i], "")
            string = string.replace(sesli[i].upper(), "")
    return string


print(disemvowel("This website is for losers LOL!"))
