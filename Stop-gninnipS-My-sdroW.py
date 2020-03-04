"""Write a function that takes in a string of one or more words, 
and returns the same string, but with all five or more letter words reversed 
(Just like the name of this Kata). Strings passed in will consist of only
 letters and spaces. Spaces will be included only when more than one word is present.

Examples: 
spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test
"""


def spin_words(sentence):

    sentence_list = sentence.split()
    # print(sentence_list)
    my_new_sentence = ''
    for i in range(len(sentence_list)):
        # print(len(sentence_list[i]))
        if (len(sentence_list[i])) > 5:
            my_new_sentence = my_new_sentence + ' ' + sentence_list[i][::-1]
        else:

            my_new_sentence += ' '+sentence_list[i]

    return my_new_sentence.lstrip()


print(spin_words('Hey fellow warriors'))
print(spin_words('Welcome'))
print(spin_words('This is another test'))
print(spin_words(
    'gnirts more is is words when one dessap gnirts but more will noitcnuf than five tneserp'))

# should equal 'gnirts more is is sdrow when one dessap gnirts but more will noitcnuf than five tneserp'
