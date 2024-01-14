# Гра вгадай число:
# Створіть просту гру, в якій комп'ютер "загадує" число, а користувач повинен вгадати його. Використовуйте цикл while.

import random
attempts = 3
print("Try to guess the number")
randomNumber = random.randint(1, 5)
while attempts:
    number = int(input("Try your luck:"))
    if number == randomNumber:
        print("Congrats!!!")
    else:
        print("Failure")
        attempts -= 1
