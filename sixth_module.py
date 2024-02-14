# 1. Користувач вводить рядок. Вивести на екран кількість слів, в яких більше 4 символів
# string = input("Enter your string\n")
# temp = string.split()
# for word in temp:
#     if len(word) >= 4:
#         print(word)
# # 2. Користувач вводить рядок. Вивести на екран всі слова, в яких більше 1 символа "і"
# string = input("Enter your string\n")
# temp = string.split()
# for word in temp:
#     if "i" in word:
#         print(word)
# 3. Користувач вводить рядок. Програма повинна перетворити його на "бісячий" текст типа ThIs Is AnGrY TeXt
# string = input("Enter your string\n")
# result = ""
# capitalize = True
# for letter in string:
#     if letter.isalpha():
#         if capitalize:
#             result += letter.upper()
#         else:
#             result += letter.lower()
#         capitalize = not capitalize
#     else:
#         result += letter
# print(result)

# 4. Користувач вводить рядок. Додати після кожного пробіла ще один
# string = input("Enter your string\n")
# temp = ""
# for letter in string:
#     if letter == " ":
#         temp = temp + " "
#     else:
#         temp = temp+letter
# print(temp)


# 5. Користувач вводить рядок, перевернути його задом наперед
temp = ""
string = input("Enter your string\n")
length = len(string)
for letter in range(length-1, -1, -1):
    temp += string[letter]
print(temp)
