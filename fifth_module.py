# 1. Написати програму заповнення списка Працывників. Склад:
# 	- ПІБ
# 	- ID
# 	- Вік
# 	- Ставка
# Написати меню з пунктами:
# 	- Додавання елемента
# 	- вивод на екран списка
# 	- Створення списка працівників, Ставка яких меньше вказаного значення
# 	- Вивод на екран працівника по ID
# 	- Редагування вказанного поля вказанного Працівника

def show_the_list():
    print("NAME\tID\tAGE\tSALARY")
    for employee in company:
        for data in employee:
            print(data, end="\t")
        print("")


def search_by_id(ID):
    print("NAME\tID\tAGE\tSALARY")
    for employee in company:
        if ID in employee:
            for data in employee:
                print(data, end="\t")
            print("\n")
            break
    else:
        print("There is no such ID\n")
# 1-Name\n2-ID


def edit_by_field(field, company):
    if field == 1:
        old_name = input("Select the name to edit: ")
        for employee in company:
            if old_name in employee:
                new_name = input("Enter a new name: ")
                employee[0] = new_name
            else:
                print("There is no such name to edit\n")
    if field == 2:
        old_id = int(input("Select the ID to edit: "))
        flag = 0
        for employee in company:
            if old_id in employee:
                flag = 1
        if flag == 1:
            new_id = int(input("Enter a new id: "))
            for employee in company:
                if new_id in employee:
                    print("This ID is being used, select another")
                    break
            for employee in company:
                if old_id in employee:
                    employee[1] = new_id
        elif flag == 0:
            print("There is no such ID")


def create_first_employee():
    employee = []
    employee.append(input("Enter employee's full name: "))
    employee.append(int(input("Enter his ID: ")))
    employee.append(int(input("Enther his age: ")))
    employee.append(int(input("Enter his salary: ")))
    company.append(employee)


def create_employee():
    employee = []
    employee.append(input("Enter employee's full name: "))
    employee.append(ID)
    employee.append(int(input("Enther his age: ")))
    employee.append(int(input("Enter his salary: ")))
    company.append(employee)


company = []
while True:
    if len(company) == 0:
        choice = int(
            input("Enter your action: \n 1-Add a new employee\n 2-Exit from the menu\n"))
        if choice == 1:
            create_first_employee()
        if choice == 2:
            break
    else:
        choice = int(input(
            "Enter your action: \n 1-Add a new employee\n 2-Show employees \n 3-Show by ID \n 4-Edit by selected field\n 5-Exit\n"))
        if choice == 1:
            ID = int(input("Enter ID of a new employee: "))
            flag = 0
            for employee in company:
                if ID in employee:
                    print("Wrong ID, you need to enter unique ID")
                    flag = 1
                    break
            if flag == 0:
                create_employee()
        elif choice == 2:
            show_the_list()
        elif choice == 3:
            id_employee = int(input("Enter ID of employee: "))
            search_by_id(id_employee)
        elif choice == 4:
            field = int(
                input("Which field to edit\n1-Name\n2-ID\n"))
            edit_by_field(field, company)
        elif choice == 5:
            break
