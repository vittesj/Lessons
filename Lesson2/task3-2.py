month_dict = {1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer', 7: 'summer', 8: 'summer',
              9: 'autumn', 10: 'autumn', 11: 'autumn', 12: 'winter'}
month = int(input('enter the month number: '))
while 13 <= month or month <= 0:
    month = int(input('enter a number from 1 to 12: '))
print('this month refers to', month_dict[month])
