def function_of_dividing(*args):
    try:
        return num1 / num2
    except ArithmeticError:
        return 'division by zero is prohibited'


num1 = int(input('Enter number1: '))
num2 = int(input('Enter number2: '))

print(function_of_dividing())
