def to_camel_case(text):
    text = text.replace(' ', '-').replace('_', '-')
    if '-' in text:
        my_splitted_text = text.split('-')
        new_text = ''
        for i in range(len(my_splitted_text)):
            for j in range(len(my_splitted_text[i])):
                if j == 0:
                    new_text += my_splitted_text[i][j].upper()
                else:
                    new_text += my_splitted_text[i][j]
    return new_text


print(to_camel_case("Testing function to_camel_case"))
