#
a = int(input("Enter the desired future value: "))
b = float(input("Enter the annual interest rate: "))
c = int(input("Enter the number of years the money will grow: "))

print("You will need to deposit this amount:" , (a / ((1 + b)) ** c))