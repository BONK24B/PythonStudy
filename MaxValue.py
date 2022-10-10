#1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

#*Примеры:*

#- 5, 25 -> да
#- 4, 16 -> да
#- 25, 5 -> да
#- 8,9 -> нет

first_num = int(input())
secound_num = int(input())

if (first_num * first_num == secound_num):
    print("yes")
elif (secound_num * secound_num == first_num):
    print("yes")
else:
    print("no")