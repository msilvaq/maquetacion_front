"""print("Hola Mundo!!!!")
print("Ingresa tu nombre:\n")
nombre=input()
print("Bienvenido, " + nombre)

print("Today's date")
day=input()
print("Breakfast calories")
breakfast=int(input())
print("Lunch calories")
lunch=int(input())
print("Dinner calories")
dinner=int(input())
print("Snack calories")
snack=int(input())

calories = breakfast + lunch + dinner + snack

print("Calorie content for "+ day + ": " + str(calories))

print(type('Hello world'))
print(type(7))

print(type(True))
print(type(False))

print(type('True'))
print(type('False'))

print(bool('True'))
print(bool('False'))
print(bool(''))
print(bool(' '))
print(bool('Hello world'))

print("Would you like to continue? ")
rsp = input()

if rsp == 'yes' or rsp == 'y':
    print("Continuing...")
    print("complete!!")
elif rsp =='no' or rsp=='n':
    print("Exiting")
else :
    print("Please try again and respond with yes or no")
"""
import random as alias
roll = alias.randint(1,10)
print(f'You rolled {roll}.')