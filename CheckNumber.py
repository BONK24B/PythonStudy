# 20. Задайте список. Напишите программу, которая
#  определит, присутствует ли в заданном списке строк некое число.

list = [24, 43, 14, 57, 88, 526, 2, 24, 2222]
number = int(input("Input your number to check if it's in the list: "))

if (number in list):
    print("Your number in the list")
else:
    print("No")