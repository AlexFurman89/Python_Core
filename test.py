# array=[1,2,3,4]
# # print(array.pop(2))
# # print(array)
# # array.append(5)
# # print(array[1])
# array_2=[5,6]
# # print(array+array_2)
# array_3=array_2
# array_3=array_2[:]
# array_3.append(10)
# print(array_2)

# var ={
# 'a':'abc',
# 'price':123
# }
# var_2 ={
# 'price':123,
# 'a':'abc'
# }
# print(var==var_2)
# print(id(var))
# print(id(var_2))
# print(id(var)==id(var_2))
# print(type(var))

# var=[4,3,7,2,1]
# # var.sort(reverse=True)
# var.sort(reverse=True)
# var.append(102)
# var.pop(-2)
# print(var)


# var= {
#     'brand':'Nike',
#     'price':1000,
#     'currency':'uah',
#     'contact_info':{
#         'Name':'Alex',
#         'Surname':'Furman'
#     }
#     }
# var['phone']='None'
# del var['phone']
# print(var)
# var.pop['brand']
# print(var)
# print(var['cell'])
# print(var.get('cell'))
# print(var.get('cell','not exist'))


# import random
# ls = []#Пустий список
# size = int(input("Enter size of array\n"))#отримали розмір списка
# for i in range(size):#перебираємо усі елементи
#     while True:#нескінчений цикл
#         #створюємо випадкове значення від 0 до 100
#         number = random.randint(0, 100)
#         #якщо його немає у списку
#         if number not in ls:
#             break#виходимо з нескінченого цикла
#     ls.append(number)#додаємо елемент у список
#     #якщо такий елемент у списку буде ми знов повернемось
#     #до нескінченого цикла и створимо но4ву змінну
# print(ls)


# for i in range(5, 0, -1):
#     print(i, end=" ")

ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ls.sort(reverse=True)
ls.reverse()
print(ls, end=" ")
