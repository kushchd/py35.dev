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

cities = ['San Francisco', 'New York', 'Washington DC']
print('New York' not in cities) 


print(list(filter(lambda x: x % 2 == 0, range(100))))

print(list(filter(lambda x: x > 50, range(100))))