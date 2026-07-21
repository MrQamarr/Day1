import random 


guess = random.randint(1, 50)

cond = True 
attempts = 1

while cond and attempts <= 6:
    user_num = int(input("Number hagg: "))
    if user_num == guess:
        print("Sahi jAwABBB, Aap 7 crore rupay jeetliye")
        cond = False
    elif user_num <= guess:
        print('Zyada hagg Bhadwe')
        attempts += 1
    elif user_num >= guess:
        print('Kamm hagg  Bhadwe')
        attempts += 1
else:
    print('Kutriya h tu saala, tere hagne ke attempts khatam hogye, diarrhoea kahika.') 
