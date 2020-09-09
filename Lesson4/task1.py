from sys import argv

try:
    name, output_in_hours, rate_per_hour, prize = argv
    print(int(output_in_hours) * int(rate_per_hour) + int(prize))
except ValueError:
    print('Enter a natural integer:')
except TypeError:
    print('enter a numeric value')
