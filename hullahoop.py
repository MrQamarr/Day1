a = input("Enter your word so that we can find the unrepeated word: ")
# for i in a:
#     if a.count(i) == 1:
#         print("The unrepeated word is:", i)
#         break


for i in a:
    if a[a.index(i)] == i and a.count(i) == 1:
        print("The unrepeated word is:", i)
        