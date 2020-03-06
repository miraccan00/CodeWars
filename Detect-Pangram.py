"""
A pangram is a sentence that contains every 
single letter of the alphabet at least once. 
For example,the sentence "The quick brown fox jumps over the lazy dog"
is a pangram,because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation."""

import string


def is_pangram(sentence):
    my_lower_alphabet = string.ascii_lowercase
    sentence = sentence.lower()
    counter = 0
    for i in range(len(my_lower_alphabet)):
        if my_lower_alphabet[i] in sentence:
            counter = counter+1
    if counter == 26:
        return True
    else:
        return False


print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
