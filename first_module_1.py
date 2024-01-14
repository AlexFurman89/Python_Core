age = 10
weight = 67
print("Human age =", age)
print(f"Human age = {age} and weight = {weight}")
print("Human age =  {} and weight = {}".format(age, weight))

print(age, weight, sep="#", end="     ")
print("Hello")

###

name = input("Enter name\n")
age = int(input("Enter age\n"))
weight = float(input("Enter you weight\n"))
age = age + 1
print("Hello,",name, "You are",age,"yeare old and you weight is", weight)
