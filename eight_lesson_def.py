# 1. Написати функції калькулятора. Приймають 2 змінні, повертають результат

# def calculator(a, b, choice):
#     match choice:
#         case "+":
#             result = a+b
#         case "-":
#             result = a-b
#         case "*":
#             result = a*b
#         case "/":
#             try:
#                 result = a/b
#             except ZeroDivisionError:
#                 print("You cannot devide on 0")
#     return result


# number_1 = int(input("Enter first number: "))
# number_2 = int(input("Enter second number: "))
# choice = input("Select + - * /: ")
# print(f"Result of {number_1} {choice} {number_2} is: ", end=" ")
# print(result := calculator(number_1, number_2, choice))


# 2. Написати функція, яка приймає ПІБ ті вік та виводить на екран привітання

# def ShowUserData(first_name, last_name, age):
#     print(f"Hello, {first_name + " " + last_name}. Your age is {age}")


# first_name = input("Enter First Name: ")
# last_name = input("Enter Last Name: ")
# age = int(input("Enter user age: "))
# ShowUserData(first_name, last_name, age)


# 3. Написати функція, яка приймає коордінати точки та перевіряє - в який чтверті знаходиться точка на площіні


def CheckCoordinates(x, y):
    if x > 0 and y > 0:
        result = 1
    elif x > 0 and y < 0:
        result = 4
    elif x < 0 and y > 0:
        result = 2
    elif x < 0 and y < 0:
        result = 3
    return result


def PrintCoordinates(result):
    if result == 1:
        print("I quadrant")
    if result == 4:
        print("IV quadrant")
    if result == 2:
        print("II quadrant")
    if result == 3:
        print("III quadrant")


coordinate_x = int(input("Enter X coordinate: "))
coordinate_y = int(input("Enter Y coordinate: "))
check = CheckCoordinates(coordinate_x, coordinate_y)
PrintCoordinates(check)


# def Sum(a, b):
#     return a + b

# a = float(input("Enter first variable\n"))
# b = float(input("Enter second variable\n"))
# result = Sum(a, b)
# print(f"{a} + {b} = {result}")
# print(f"{a} + {b} = {Sum(a,b)}")
# //////////////////////////////////////////////////////////////////////////////////
# def MinMax(ls):
#     max = ls[0]
#     for i in ls:
#         if max < i:
#             max = i
#         elif min > i:
#             min = i
#     return min, max

# ls = [1,2,3,4,5,67,8,9]
# result = MinMax(ls) #у змінну result запишемо кортеж
# #з результатом пошуку мынымального та максимального
# print(f"Min = {result[0]}\nMax = {result[1]}")

# #трохи гірший варіант - функція викликається 2 рази
# print(f"Min = {MinMax(ls)[0]}\nMax = {MinMax(ls)[1]}")

# ///////////////////////////////////////////////////////////////////////////////////
# import random #модуль,який выдповідає за випадкові числа
# import time #модуль, в якому є функція паузи sleep

# def Show(dice):#функція виводу кубіка на екран яка приймає поточне значення
#     if dice == 1: print("-----\n|   |\n| * |\n|   |\n-----\n")
#     elif dice == 2: print("-----\n|*  |\n|   |\n|  *|\n-----\n")
#     elif dice == 3: print("-----\n|*  |\n| * |\n|  *|\n-----\n")
#     elif dice == 4: print("-----\n|* *|\n|   |\n|* *|\n-----\n")
#     elif dice == 5: print("-----\n|* *|\n| * |\n|* *|\n-----\n")
#     else: print("-----\n|* *|\n|* *|\n|* *|\n-----\n")

# def Winner(user, bot):#функція, яка приймає аргументи та
#     #виводить переможця на екран
#     if bot == user: print("Draw")
#     elif bot > user: print("Bot win")
#     else: print("User win")
#     time.sleep(2)

# game = int(input("Enter number of game\n"))#отримали кількіть ігор
# if game < 0:
#     print("Wrong game number")
# else:
#     while game:
#         user = random.randint(1, 6)#гравець кидає кубік
#         print("User = ")
#         Show(user)#передаємо значення кубіка у функцію
#         time.sleep(2)#пауза 2 секунди
#         bot = random.randint(1, 6)#бот кидає кубік
#         print("Bot = ")
#         Show(bot)#передаємо його значення у функцію
#         Winner(user, bot)#передаємо значення 2 кубіків
#         #у функцію, яка виводить переможця
#         time.sleep(2)
#         game -= 1
# //////////////////////////////////////////////////////////////////////////////////////////////
# import random

# def Show(ls):#Функція виводу на екран поля
#     for row in ls:
#         for column in row:
#             if column == 0:
#                 print(" |", end="")
#             elif column == 1:
#                 print("x|", end="")
#             else:
#                 print("o|", end="")
#         print()

# def Winner(ls):#функція перевірки переможних комбінацій
#     if ls[0][0]==1 and ls[0][1] == 1 and ls[0][2]==1 or ls[1][0] ==1 and ls[1][1]==1 and ls[1][2]==1 or ls[2][0] == 1 and ls[2][1]==1 and ls[2][2] ==1 or ls[0][0] == 1 and ls[1][0]==1 and ls[2][0] == 1 or ls[0][1] == 1 and ls[1][1]==1 and ls[2][1]==1 or ls[0][2] == 1 and ls[1][2]==1 and ls[2][2]==1 or ls[0][0]==1 and ls[1][1]==1 and ls[2][2] ==1 or ls[0][2]==1 and ls[1][1] == 1 and ls[2][0] == 1:
#         return 1#повертає 1 якщо є переможна комбінація у гравця
#     elif ls[0][0]==2 and ls[0][1] == 2 and ls[0][2]==2 or ls[1][0] ==2 and ls[1][1]==2 and ls[1][2]==2 or ls[2][0] == 2 and ls[2][1]==2 and ls[2][2] ==2 or ls[0][0] == 2 and ls[1][0]==2 and ls[2][0] == 2 or ls[0][1] == 2 and ls[1][1]==2 and ls[2][1]==2 or ls[0][2] == 2 and ls[1][2]==2 and ls[2][2]==2 or ls[0][0]==2 and ls[1][1]==2 and ls[2][2] ==2 or ls[0][2]==2 and ls[1][1] == 2 and ls[2][0] == 2:
#         return 2#повертає 2 якщо є переможна комбінація у бота
#     else: #якщо немає переможної комбінації
#         return 0#повертаємо 0

# def Game():
#     game = 9#кількість кроків
#     while game:
#         while True:#цикл для отримання хода гравця
#             #приймаємо знмінні, доки клітина, на яку
#             #хоче поставити свій марке гравець не зберігає 0
#             x = int(input("Enter row: "))
#             y = int(input("Enter column: "))
#             if ls[x][y] == 0:
#                 break
#         ls[x][y] = 1#ставимо маркер гравця
#         Show(ls)#виводимо поле на екран
#         if Winner(ls) == 1:#перевіряємо - чи є перемога
#             print("User win")
#             break#якщо є - виходимо з циклу
#         game -= 1#якщо ні - крок -1
#         if game == 0:#якщо кроків не закінчилось
#             print("Draw")#нічія
#             break
#         while True:#цикл для отримання хода від бота
#             x = random.randint(0,2)
#             y = random.randint(0, 2)
#             if ls[x][y] == 0:
#                 break
#         ls[x][y] = 2
#         Show(ls)
#         if Winner(ls) == 2:
#             print("Bot win")
#             break
#         game -= 1
#         if game == 0:
#             print("Draw")
#             break

# ls = [[0,0,0],[0,0,0],[0,0,0]]
# Show(ls)
# Game()
