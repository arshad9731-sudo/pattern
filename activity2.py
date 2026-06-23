rows = int(input("Please enter the total numbers of rows"))
number = 1

print("Floyd's triangle ")
for i in range (1, rows + 1):
    for j in range (1, 1 + i):
        print (number, end = '  ')
        number = number + 1
    print()


