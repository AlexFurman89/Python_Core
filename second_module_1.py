'''
Парна чи непарна?
1.  Напишіть програму, яка приймає число від користувача і визначає, чи є воно парним чи непарним.
'''

var = int(input("Please Enter the number\n"))
if var%2 ==0:
    print("The number is even")
else:
    print("The number is NOT even")