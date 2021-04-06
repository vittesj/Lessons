def int_func(text):
    counter = 0
    for j in range(len(text)):
        if 97 <= ord(text[j]) <= 122:
            counter += 1
        else:
            break
        if counter == len(text):
            text = text.title()
    return text


text = input('enter a keyword: ')
text_list = text.split()
for i in range(len(text_list)):
    text = text_list[i]
    text_list[i] = int_func(text)
    text = ' '.join(text_list)
print(text)
