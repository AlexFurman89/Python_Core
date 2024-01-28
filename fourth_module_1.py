
# 1. Заповнити масив випадковими числами.
# - знайти найбільший елемент масива
# - знайти найменший елемент масива
# - Вивести на екран індекси найменшого і найбільшого елемента масива
# - змінити місцями перший та останній елемент масива
# - знайти суму елементів між найбільшим та найменшим елементами 
# - порахувати і вивести на екран суму в першій частині масива та в другій частині масива


import random
list=[]
count=int(input("Enter the numbe of elements in the list: \n"))
list = [random.randint(0, 100) for i in range(count)]
print(list)
print(max(list))
print(min(list))
max_index=list.index(max(list))
min_index=list.index(min(list))
print(max_index, " ", min_index)
temp=list[0]
list[0]=list[count-1]
list[count-1]=temp
print(list)
temp_list=list[:]
temp_list.sort()
print(temp_list)
print(sum(temp_list))
half_counter=count/2
first_half_list=temp_list[0:(count//2)]
second_half_list=temp_list[(count//2):count]
sum_1=sum(first_half_list)
sum_2=sum(second_half_list)
print(first_half_list)
print(second_half_list)
print(sum_1)
print(sum_2)

