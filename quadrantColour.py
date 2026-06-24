User = input('''enter the direction in which you want to go? is it S1, S2, S3, or S4?
Depending on your choice, you will be assigned a color and you can move in that direction: ''').lower()
a = False
while User != "Exit":

    if User == 's1':
        print('You have chosen S1, your color is Red')
        a = True
    elif User == 's2':
        print('You have chosen S2, your color is Blue')
        a = True
    elif User == 's3':
        print('You have chosen S3, your color is Green')
        a = True
    elif User == 's4':
        print('You have chosen S4, your color is Yellow')
        a = True
    elif User == 'exit':
        print('Exiting the program...')
        a = True
    else:
        print('Invalid input, please enter S1, S2, S3, or S4')  
        User = input('Please enter the direction again: ').lower() 
    break    
# a = False
# while a == False:
#     print(a)