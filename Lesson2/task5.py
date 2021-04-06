rating_list = [7, 5, 3, 3, 2]
numbers = int(input('enter a natural number: '))
rating_list.append(numbers)
rating_list.sort(reverse=True)
print(rating_list)