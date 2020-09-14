test_file = open('test_file.txt', 'r', encoding='utf-8')

average_wage = 0
counter = 0
for i in test_file:
    my_list = i.split()
    if float(my_list[1]) < 20000:
        print(my_list[0])
    average_wage += float(my_list[1])
    counter += 1
print('average salary of all employees', average_wage / counter)

test_file.close()
