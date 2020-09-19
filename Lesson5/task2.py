test_file = open('test_file.txt', 'r', encoding='utf-8')

counter = 0
for i in test_file:
    counter += 1
    print('number of words per line', i.count(' '))
print('number of lines in the file', counter)

test_file.close()
