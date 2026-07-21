
# item = input('please enter your Item:')
# quantity = int(input('please enter the numer of quantity:'))
# unit_price = int(input("Enter the price per single unit: "))
# total = quantity* unit_price
# print(f'The given item is {item} and your  quantity is {quantity} and the unit price for your item is {unit_price}. So, now the total price foe your item is {total}') 

# Movie ticket counter
# item = input('please enter your movie name:')
# quantity = int(input('please enter the numer of tickets:'))
# unit_price = int(input("Enter the single ticket price "))
# total = quantity* unit_price
# print(f'The ticket booking for your {item} has initiated and the number of tickets are {quantity} and the price for your ticket is {unit_price}. So, now the total price for all of your tickets is {total}')  

#Shopping card 

product = [
    {
        'item_name': 'asus rog strix laptop',
        'price': 120000,
        'quantity': 2,
        'tax_rate': 0.10
    }
]

grand_total = 0
print("------------------Shopping Cart--------------------")
for item in product:
    print('Item: ', item.get('item_name'))
    print('price: ', item.get('price'))
    print('quantity', item.get('quantity'))

item['subtotal'] = item['price'] * item['quantity']
item['tax'] = item['subtotal'] * item['tax_rate']
item['before_discount'] = item['subtotal'] + item['tax']

if item['before_discount'] > 1000000:
    item['discount'] = item['before_discount'] * 0.20
    item['final_total'] = item['before_discount'] - item['discount']
    print(item['final_total'])
else:
    item['discount'] = 0
    item['final_total'] = item['before_discount']
    print(item['final_total'])

if item['final_total'] > 50:
    print('True')
