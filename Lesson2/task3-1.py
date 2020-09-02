month_of_year = (list(range(1, 13)))
month = int(input('enter the month number: '))
while 13 <= month or month <= 0:
    month = int(input('enter a number from 1 to 12: '))
for i in range(len(month_of_year)):
    if month_of_year[i] == month:
        if 3 <= month_of_year[i] <= 5:
            print('this month refers to spring')
        elif 6 <= month_of_year[i] <= 8:
            print('this month refers to summer')
        elif 9 <= month_of_year[i] <= 11:
            print('this month refers to autumn')
        else:
            print('this month refers to winter')
