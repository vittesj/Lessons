def my_func(x, y):
    cikl = 1
    y *= -1
    for i in range(y):
        cikl *= 1 / x
    return cikl


x = float(input('Enter real positive number: '))
y = int(input('Enter negative integer: '))

print(my_func(x, y))
