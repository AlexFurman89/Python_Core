"""
3. Максимум з трьох чисел
Напишіть програму, яка приймає три числа від користувача і виводить найбільше з них.
"""
first_number = float(input("Enter the first number\n"))
second_number = float(input("Enter the second number\n"))
third_number = float(input("Enter the third number\n"))
max_value = first_number
if (second_number > max_value):
    max_value = second_number
if (third_number > max_value):
    max_value = third_number
    print("The biggest number =", max_value)
else:
    print("The biggest number =", max_value)


