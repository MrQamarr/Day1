a = int(input("Enter a number to create a star pattern right angled Triangle: "))
# for i in range(1, a + 1):
#     print((" " * (a - i)) + "* " * i)
# for i in range((a - 1), 0, -1):
#     print((" " * (a - i)) + "* "* i)

# for i in range(1, a + 1):
#     print((" " * (a - i)) + "* " * i)
# for i in range((a - 1), 0, -1):
#     print((" " * (a - i)) + "* "* i)

for i in range(1, a + 1):
    print("* " * i + "  " * ((a - i) * 2) + "* " * i)
for i in range(a - 1, 0 , -1):
    print("* " * i + "  " * ((a - i) * 2) + "* " * i)