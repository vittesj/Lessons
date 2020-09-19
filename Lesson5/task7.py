import json

with open('test7_file.txt', 'r+', encoding='utf-8') as test_file:
    average_profit = 0
    counter = 0
    my_dict = dict()
    for i in test_file:
        my_list = i.split()
        profit = int(my_list[2]) - int(my_list[3])
        if profit > 0:
            average_profit += profit
            counter += 1
        my_dict[my_list[0]] = profit
    my_list = [my_dict, {"average_profit": average_profit / counter}]
    with open('my_fyle.json', 'w', encoding='utf-8') as test1_file:
        json.dump(my_list, test1_file, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
