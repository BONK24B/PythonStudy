# Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр. Через строку нельзя решать.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11



    
number = input("Enter any number: ")
array = []
counter = 0

if("." in number):
    number = number.split(".")
    line = ""

    for i in number:
        line += i
    
    for i in line:
        array.append(int(i))
    
else:
    for i in number:
        array.append(int(i))

for i in array:
    counter += i

print(counter)