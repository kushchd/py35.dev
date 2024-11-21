#
a=7
b=8
print((a > 2) and (b >= 6)) 

print(True and True)
print(True and False)
print(True or False)
print(not True)  

a="Kira"
print(a)

a = 1
b = 1
print (a is b)

x3 = [1,2,3]
y3 = [1,2,3]
print(x3 is not y3)

var = 1
print(type (var))
print(id (var))
print(2 ** 200)

print("""
Hello
Word
""")
print("Hello      Word")
print("_" * 80)

name = "Jon"
last_name = "Don"
print(f"My name {name} {last_name}")

def hell(p):
    print(f"Hello {p}")

hell("Word")

hello = "Hello Word"
for c in hello:
    print(c)

#from random import randint
#r=randint(1,100)
#x=int(input("Угадай число от 1 до 100: "))
#while x!=r:
 #   x=int(input("Попробуй еще раз: "))
  #  if x<r:
   #     print("Больше! ")
    #elif x>r:
     #   print("Меньше! ")
#print("Угадал! ")

import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)

    print("Відгадайте число від 1 до 100")

    while True:
        guess = int(input("Ваш здогад: "))
        if guess < number_to_guess:
            print("Загадане число більше.")
        elif guess > number_to_guess:
            print("Загадане число менше.") 
        else: 
            print(f"Вітаємо! Ви відгадали число {number_to_guess}.")
            break

guess_the_number()




