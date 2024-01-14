# Шахова дошка:
# Створіть програму, яка виводить шахову дошку (8x8) за допомогою символів.

matrix = 8
number = 65
for i in range(matrix+1):
    if i != 0:
        print(i, end=" ")
    for j in range(matrix):
        if i == 0:
            print("   ", chr(number), end=" ")
            number += 1
        else:
            print(" ", "[ ]", end=" ")
    print("\n")
