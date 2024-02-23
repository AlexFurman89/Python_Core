# 1. Користувач вводить рядок, порахувати кількість слів, в яких є літера "а"

# custom_string = input("Enter a string: ")
# new_custom_string = custom_string.split()
# count = 0
# for word in new_custom_string:
#     if 'a' in word:
#         count += 1
# print(count)

# 2. Користувач вводить рядок. Додати після кожного пробіла ще один
# custom_string = input("Enter a string: ")
# new_custom_string = custom_string.split()
# count = 0
# for word in new_custom_string:
#     print(word, end='  ')


# 3. Користувач вводить рядок, змінити усі літери "а" на "о"
custom_string = input("Enter a string: ")
new_custom_string = custom_string.replace('a', '0')
print(new_custom_string)


# import random

# #pinCode
# pin = random.randint(1000, 9999)
# print("Pin = ", pin)

# #PinCode
# base = '1234567890-=!@#$%^&*()_+qwertyuiop[]asdfghjkl;zxcvbnm,./'
# pin =''
# for i in range(4):
#     pin += base[random.randint(0, 10)]
# print("Pin = ", pin)

# #password 6-10 symbol
# import random
# password = ''
# for i in range(random.randint(6, 10)):
#     number = random.randint(32, 127)
#     password += chr(number)
# print(f"Password = {password}")

# #базовий рядок
# base = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+[]{}:"<>?/'
# easypass = ''#майбутній пароль
# #кількість символів пароля - від 6 до 10
# for i in range(random.randint(6, 10)):
#     #додаємо в пароль випадкові символи з базового рядка
#     #з індексів від 0 до 63
#     easypass += base[random.randint(0, 63)]
# print(f"Easy password = {easypass}")

# hardpass = ''
# for i in range(random.randint(10,18)):
#     hardpass += base[random.randint(0, len(base)-1)]
# print(f"Hard password = {hardpass}")

# # пароль в якому 100% будуть всі варіанти символів
# hardpass2 = ''
# while True:
#     char = 0#кількість літер
#     num = 0#кількість цифр
#     sym = 0#кількість спецсимволів
#     cap = 0#кількість великих літер
#     for i in range(random.randint(10, 18)):
#         hardpass2 += base[random.randint(0, len(base) - 1)]
#     print(f"Hard password = {hardpass}")
#     #перебираємо усі символи в паролі
#     for i in hardpass2:
#         if i.isdigit(): num += 1#рахуємо цифри
#         elif i.isalpha():#літери
#             if i.islower():char += 1#маленьки
#             else: cap += 1#великі
#         else: sym += 1#спецсимволи
#     #якщо немає жодного лічільника, який дорівню 0
#     if num !=0 and cap !=0 and sym !=0 and char !=0:
#         break#зупиняємо цикл
# print(f"Hardpass = {hardpass2}")

# ###############################################################
# str = 'This is string about string'
# ls = str.split()#розділяєио рядок по словах та записуємо у список
# print(ls)
# index = 0#індекс найменьшого слова
# counter = len(ls[0])#кількість літер в слові
# for i in range(0, len(ls)):#перебираєсо усі елементи списку
#     if len(ls[i]) < counter:#якщо довжина поточного слова
#         #меньше ніж та, що записана в counter
#         index = i#зберыгаємо індекс цього слова
#         counter = len(ls[i])#counter запишемо нове значення

# print("Smallest word is ", ls[index])

# ###############################################################
# s = {1,2,3,4,5,6}
# print(s)

# s.add(3)#додає значення
# print(s)

# s.remove(2)#видаляє значення
# print(s)

# s.discard(3)
# print(s)

# number = s.pop()#теж видаляє значення
# print(number)

# ###############################################################
