numbers = int(input('enter the number of products: '))
tovar_list = []
name_list = []
price_list = []
quantity_list = []
unit_list = []
my_dict = {}
tovar_turple = ()
for i in range(1, numbers + 1):
    tovar = input('enter the product name: ')
    name_list.append(tovar)
    price = int(input('enter the product price: '))
    price_list.append(price)
    quantity = int(input('enter the product quantity: '))
    quantity_list.append(quantity)
    unit = input("enter the product's units of measurement: ")
    unit_list.append(unit)
    tovar_dict = {'название': tovar, 'цена': price, 'количество': quantity, 'ед': unit}
    tovar_turple = (i, tovar_dict)
    tovar_list.append(tovar_turple)
print(tovar_list)
tovar_dict = {'название': name_list, 'цена': price_list, 'количество': quantity_list, 'ед': unit_list}
print(tovar_dict)