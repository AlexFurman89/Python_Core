#отримали кількість зірочок
number = int(input("Enter star number\n"))
while True:#"нескінчений цикл"
    print("*", end = "")#виводимо *
    number-=1#кількість * -=1
    if number == 0:#якщо зірочок 0
        break#зупиняємо роботу цикла

#цикли for
#отримали кількість *
number = int(input("\nEnter number\n"))
#перебираємо всі цифри від 0 до number 
for star in range(number):
    print("*", end= "")

################################################################################
size = 9
for i in range(size):
    for j in range(size):
        if i == j or i + j ==size-1:
            print("*", end ="")
        else: print(" ", end="")
    print()
########################################
print()
for i in range(size):
    for j in range(size):
        if (i >= j): print("*", end = "")
        else: print(" ", end="")
    print()
#########################################
print()
for i in range(size):
    for j in range(size):
        if i==0 or j ==0 or i==size-1 or j==size-1:
            print("*", end = "")
        else: print(" ", end ="")
    print()
#######################################
print()
for i in range(size):
    for j in range (size):
        if i + j <= size-1 and j >= i:
            print("*", end= "")
        else: print(" ", end="")
    print()


########################################################
ls = [] #Створили пустий список
ls1 = list()#теж створили пустий список
ls1.append(34)#додаємо до списка елементи
ls1.append(56)
ls1.append(3)
print(ls1[0])#звертаємося до елементів по індексу
print(ls1[1])
print(ls1[2])
####
ls = []#Пустий список
temp = [1,2,3]#додатковий список
ls.append(34) #додає елемент до списка
print(ls)#вивели список на екран
ls.extend(temp)#розширили перший список елементами другого
print(ls)
#вставили елемент по індексу
ls.insert(1, "word")
print(ls)
#видаляє першу 2 яку зустріне
ls.remove(2)
print(ls)
#видаляємо елемент з індексом1 із списка та 
# записуємо у змінну var
var = ls.pop(1)
print(var)
print(ls)
ls.extend(temp)
print(ls)
#записує у змінну var індекс першої 3 яку зустрічає
var = ls.index(3)
print(var)
#записує у змінну var кількість 1
var = ls.count(1)
print("count 1 = ", var)
ls.sort()#сортує список
print(ls)
ls.sort(reverse=True)#сортує список задом-наперед
print(ls)
ls.reverse()#перевертає список
print(ls)
/////////////////////////////////////////////////////////////////////////
ls = [1,2,3,45,6,7,8,9]#список елементів
#отримали індекс елемента під видалення
index = int(input("Enter index variable for delete\n"))
#якщо індекс меньше 0 або більше індекса останнього елемента
if index < 0 or index > len(ls)-1:
    print("Wrong index")#виводимо помилку
else:#інакше - видаляємо елемент із списка
    ls.pop(index)
print(ls)

#видалення по значенню
number = int(input("Enter number\n"))#отримали значення
if number in ls:#якщо значення є у списку
    ls.remove(number)#видаляємо його
else:#інакше - помилка
    print("Wrong element")
print(ls)

##############################################
import random

ls = []
size = int(input("Enter size of array\n"))
for i in range(size):
    ls.append(random.randint(0, 100))
print(ls)
#порахувати і порівняти суму елементів на парних та непарних
#індексах та вивести результат на екран

sum_even = 0#змінна для суми елементів з парними індексами
sum_odd = 0#змінна для суми елементів з непарними індексами
#перебираємо індекси від 0 до довжини списка
for i in range(len(ls)):
    #якщо індекс - парний
    if i % 2 == 0:
        #додаємо елемент до суми парних
        sum_even += ls[i]
        #інакше - додаємо до суми неперних
    else:
        sum_odd += ls[i]
        
#порівнюємо елементи між собою
if sum_even == sum_odd:
    print("Sum even == sum odd")
elif sum_even > sum_odd:
    print("Sum even > sum odd")
else:
    print("Sum odd > sum_even")
##########################################################################
import random
##################variant 1######################
size = int(input("Enter size of array\n"))#отримали розмір списка
#заповнили список випадковими значеннями
ls = [random.randint(0,100) for i in range(size)]
print(ls)
sum = 0
for i in ls:#перебираємо усі елементи списка
    if i > 50:#якщо елемент більше 50
        sum+=i#додаємо його до суми
print("Sum = ", sum)
###############variant 2#######################
ls = []#пустий список
sum = 0#сума елементів
#отримали розмір списка
size = int(input("Enter size of array\n"))
#перебираємо індекси списка
for i in range(size):
    #створюємо випадкове число від 0 до 100
    number  = random.randint(0, 100)
    #додаємо його до списка
    ls.append(number)
    #якщо воно більше 50
    if number > 50:
        #додаємо його до суми
        sum += number
print(ls)
print("\nSum = ", sum)
##############################################
import random
#створили список на 12 елементів, заповнили випадковими числами
ls = [random.randint(0, 100) for i in range(12)]
print(ls)

temp = []#тимчасовий списко
for i in ls:#перебираємо усі елементи в списку
    if i % 2 != 0:#якшо він не парний
        temp.append(i)#додаємо його до тимчасового списка
ls = temp#змінюємо поточний список на тимчасовий
print(ls)
##########################################################################
group = []
while True:
    if len(group) == 0:
        choice = int(input("Enter choice\n1-Add\n0-Exit\n"))
        if choice == 1:
            student = []
            student.append(input("Enter name\n"))
            student.append(int(input("Enter ID\n")))
            group.append(student)
        elif choice == 0: break
        else: print("Wrong choice")
    else:
        choice = int(input("Enter choice\n1-Add\n2-Show\n0-Exit\n"))
        if choice == 1:
            student = []
            student.append(input("Enter name\n"))
            student.append(int(input("Enter ID\n")))
            group.append(student)
        elif choice == 2:
            for student in group:
                for data in student:
                    print(data, end = "\t")
                print()
        elif choice == 0: break
        else: print("Wrong choice\n")
##############################################################
import random
ls = []#Пустий список
size = int(input("Enter size of array\n"))#отримали розмір списка
for i in range(size):#перебираємо усі елементи
    while True:#нескінчений цикл
        #створюємо випадкове значення від 0 до 100
        number = random.randint(0, 100)
        #якщо його немає у списку
        if number not in ls:
            break#виходимо з нескінченого цикла
    ls.append(number)#додаємо елемент у список
    #якщо такий елемент у списку буде ми знов повернемось
    #до нескінченого цикла и створимо но4ву змінну
print(ls)
###############################################################
ls = ["Ivanor T.Y.", 34556, [4, 4, 5]]
for i in ls:#виводимо всі елементи списка на екран
    print(i, end= "\t")

sum = 0
#рахуємо середній бал
#перебираємо усі оцінки, які по суті є списком
for i in range(len(ls[2])):
    sum += ls[2][i]#додаємо до суми
print("Average = ", sum / len(ls[2]))

#виводимо елементи списка "красиво"
for i in ls:#перебираємо усі елементи списка
    if isinstance(i, list):#якщо перед нами - список
        for data in i:#заходимо до нього
            print(data, end = "\t")#виводимо кожен елмент окремо
    #усі інші елемент виводяться однаково
    else:print(i, end ="\t")
