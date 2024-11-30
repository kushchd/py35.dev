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

#####

import sys

def print_square(number):
    print(number ** 2)

def print_help():
    print("usage: square.py number [-h]")
    print()
    print("positional arguments:")
    print("  number         display a square of a given number")
    print()
    print("options:")
    print("  -h | --help  show this help message and exit")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_help()
        sys.exit(1)
        
    arg = sys.argv[1]
    if arg in ("-h", "--help"):
        print_help()
    else:
        try:
            number = float(arg)
            print_square(number)
        except ValueError:
            print("Error: 'number' must be a valid number.")
            print_help()

