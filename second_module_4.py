"""
4. Пошук коренів квадратного рівняння
Створіть програму, яка приймає коефіцієнти квадратного рівняння (ax^2 + bx + c = 0) і знаходить його корені (розв'язки).
"""
import math
a = int(input("Enter a\n"))
b = int(input("Enter b\n"))
c = int(input("Enter c\n"))
descriminant = int(math.pow(b, 2) - 4*a*c)
if descriminant < 0:
    print("There is no answers\n")
elif (descriminant == 0):
    x1 = float(-b/2*a)
    print("There is ONLY one answer, x= ", x1)
else:
    x1 = float((-b+math.sqrt(descriminant))/2*a)
    x2 = float((-b-math.sqrt(descriminant))/2*a)
    print(f"There are two answers, x1 = {x1}, x2 = {x2}\n")
