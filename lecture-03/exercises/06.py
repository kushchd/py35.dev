#
from random import randint
r=randint(1,100)
x=0
print("Угадай число от 1 до 100")

while x != r:
    x=int(input("Напиши число: "))

    if x<r:
        print("Число больше! ")
    elif x > r:
        print("Число меньше! ")
print("Угадал! ")
