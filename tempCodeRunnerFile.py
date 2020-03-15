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
