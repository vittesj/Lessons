from itertools import islice, count, cycle

my_list = [i for i in range(intcount(), 20)]

iterable = cycle(my_list)
counter = 0
while counter != 30:
    print(next(iterable))
    counter += 1
