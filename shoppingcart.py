item_name = input('Please enter item name: ')
price = float(input('Please enter item price: '))
quantity = int(input('please enter item quantity: '))
tax_rate = float(input('please enter tax_rate: '))

subtotal = price * quantity
tax_amount = subtotal * tax_rate
total_before_discount = subtotal + tax_amount
if total_before_discount > 100:
    discount = total_before_discount * 0.20 
    final_total = total_before_discount - discount
    print(f'The Final total after discount is {final_total} ')
else:
    discount = 0
    final_total = total_before_discount
    print(f'Final total is {final_total}')

#Comparison operators

if final_total > 50:
    print(f'Final total is greater than 50: True')
else:
    print(False)

if quantity == 3:
    print(f'Quantity is equal to 3: True')
else:
    print(False)

if price != 0:
    print(True)
else:
    print(False)

if subtotal >= total_before_discount:
    print(True)
else:
    print(False)

#Logical Operators

if quantity > 3 and total_before_discount > 100:
    print("Bulk Order")
    
elif final_total > 40 or quantity >= 5:
    print('Eligible for free shipping')

elif not(quantity > 0):
    print('Invalid Order')

#Modulus Operator

if quantity % 2 == 0:
    print('Even')
else:
    print("Odd")

#Floor division and Exponent


