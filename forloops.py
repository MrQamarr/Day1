# a = int(input("Enter a number to create a star pattern right angled Triangle: "))
# for i in range(1, a + 1):
#     print((" " * (a - i)) + "* " * i)
# for i in range((a - 1), 0, -1):
#     print((" " * (a - i)) + "* "* i)

# for i in range(1, a + 1):
#     print((" " * (a - i)) + "* " * i)
# for i in range((a - 1), 0, -1):
#     print((" " * (a - i)) + "* "* i)

# for i in range(1, a + 1):
#     print("* " * i + "  " * ((a - i) * 2) + "* " * i)
# for i in range(a - 1, 0 , -1):
#     print("* " * i + "  " * ((a - i) * 2) + "* " * i)
# print(" " * (a - 1) +"*")

# for i in range(2, a):
#     hollowL = " " * (a - i)
#     hollowC = "  " * (i - 2) 
#     print(hollowL + "* " + hollowC + "*")

# print("* " * a)

a = int(input("Enter a number to print and practice nested forloops: "))

for i in range(1, a + 1):
    for j in range(i):
        print("* ", end = " " )
    print(" ")