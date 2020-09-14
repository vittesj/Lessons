test_file = open('test_file.txt', 'w', encoding='utf-8')

while True:
    line = input('Enter a line of text, or an empty line to complete: ')
    if not line:
        break
    print(line, file=test_file)

test_file.close()