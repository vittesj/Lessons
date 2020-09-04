def sum_func():
    line_list = line.split()
    global summa
    for i in range(len(line_list)):
        if line_list[i] != 'e':
            summa += int(line_list[i])
        else:
            break
    return print(summa)


summa = 0
while True:
    line = input('Enter numbers separated by spaces, to exit press "e": ')
    sum_func()
    if 'e' in line:
        break
