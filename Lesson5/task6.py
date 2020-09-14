import re

with open('test_file6.txt') as test_file:
    my_dict = {}
    for i in test_file.readlines():
        res = re.findall(r'\d+', i)
        discipline = re.findall(r'\w+', i)
        my_dict[discipline[0]] = sum(map(int, res))
print(my_dict)
