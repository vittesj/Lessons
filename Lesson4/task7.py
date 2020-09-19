def fact_(n):
    number = 1
    for i in range(1, n + 1):
        number *= i
        yield number


try:
    n = int(input('Enter a natural integer: '))
    for el in fact_(n):
        print(el)
except ValueError:
    print('Enter a natural integer:')
except TypeError:
    print('enter a numeric value')
