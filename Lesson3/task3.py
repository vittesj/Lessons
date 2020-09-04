def my_func(num1, num2, num3):
    return num1 + num2 + num3 - min(num1, num2, num3)


print(my_func(num1=int(input('Enter num1: ')), num2=int(input('Enter num2: ')), num3=int(input('Enter num3: '))))
