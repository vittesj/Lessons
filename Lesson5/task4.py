from googletrans import Translator

test_file = open('test_file.txt', 'r', encoding='utf-8')
test1_file = open('test1_file.txt', 'w', encoding='utf-8')

translator = Translator()
for i in test_file:
    my_list = i.split()
    the_translation_result = translator.translate(my_list[0], src='en', dest='ru')
    my_list[0] = the_translation_result.text
    i = ''.join(my_list)
    print(i, file=test1_file)

test_file.close()
test1_file.close()
