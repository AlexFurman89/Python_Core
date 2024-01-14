# Таблиця множення:
# Напишіть програму, яка виводить таблицю множення для введеного користувачем числа.

number = int(input("Enter the Number to built the multiplication table: "))
array = []
for i in range(11):
    print(f"{number} * {i} = {i*number}")
