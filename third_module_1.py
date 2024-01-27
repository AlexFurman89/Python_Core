# Сума чисел:
# Створіть програму, яка зчитує цілі числа від користувача, а потім виводить їхню суму.

numberOfDigits = int(input("Enter number of digits you want to fill in: "))
array = []
sum = 0
for i in range(numberOfDigits):
    # print(i+1, end=" ")
    array.append(int(input(f"{i+1} Number is: ")))
    sum += array[i]
print(sum)
