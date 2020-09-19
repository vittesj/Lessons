from itertools import islice, count

test_file = open('test_file2.txt', 'w', encoding='utf-8')

my_list = [i for i in islice(count(1), 20)]
line = ' '.join([str(i) for i in my_list])
print(line, file=test_file)
print(sum(my_list))

test_file.close()
