"""""
2. Калькулятор податку на дохід
Створіть програму, яка приймає річний дохід користувача та обчислює податок на дохід за наступними умовами:
До 10 000 грн - 10%
Від 10 001 до 50 000 грн - 15%
Від 50 001 до 100 000 грн - 20%
Понад 100 000 грн - 25%
"""

taxdict={
1: "10%",
2: "15%",
3: "20%",
4: "25%"
}
income = float(input("Enter your income\n"))
if (income <= 10000):
    print("Your tax is =", taxdict[1])
elif (income >=10001 and income <= 50000):
    print("Your tax is =", taxdict[2])
elif (income >=50001 and income <= 100000):
    print("Your tax is =", taxdict[3])
else:
    print("Your tax is =", taxdict[4])
    ######hh