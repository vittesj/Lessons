text = input('entered string: ')
text_list = text.split()
for i in range(len(text_list)):
    if len(text_list[i]) <= 10:
        print(text_list[i])
    else:
        text = text_list[i]
        print(text[:10])
