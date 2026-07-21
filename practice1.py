Username = input('Enter your username:').lower
password = input('Enter your password:').lower
email = input('Enter Your mail: ').lower
upper = 0
lower = 0
digit = 0
special = 0

#First we will check the length of the password
if len(password) >= 10:

#now we will check for the presence of uppercase, lowercase, digits, and special characters
    for char in password:
        if char >= 'A' and char <= 'Z':
            upper += 1

        elif char >= 'a' and char <= 'z':
            lower += 1

        elif char >= '0' and char <= '9':
            digit += 1

        else:
            special += 1

#Now we will check if the password meets all the requirements
    if upper == 0:
        print('Password must contain at least one uppercase letter.')

    if lower == 0:
        print('Password must contain at least one lowercase letter.')

    if digit == 0:
        print('Password must contain at least one digit.')

    if special == 0:
        print('Password must contain at least one special character.')

    #Now we will say that the account has been created successfully and you have been logged in into your ne account.

    if upper > 0 and lower > 0 and digit > 0 and special > 0:
        print(f'login successful, welcome {Username}')
    
    else:
        print('login failed')

    if email.endswith('@gmail.com') or email.endswith('@hotmail.com') or email.endswith('@outlook.com'):
        print(f'''you have entered the right mail
you'll be redirected to your profile soon...''')
    
    else:
        print(f"You've entered the wrong mail. Acche email enter karna bhadwe.")

else:
    print('Password must be at least 10 characters long.')

