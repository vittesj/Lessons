n = int(input('enter the length of the list: '))
while n <= 0:
    n = int(input('enter an integer value greater than zero: '))
list = []
for i in range(n):
    x = input('enter a list item: ')
    list.append(x)
    if i % 2 != 0:
        list[i], list[i - 1] = list[i - 1], list[i]
print(list)
