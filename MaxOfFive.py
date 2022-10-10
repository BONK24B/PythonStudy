#2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

#Примеры:

#- 1, 4, 8, 7, 5 -> 8
#- 78, 55, 36, 90, 2 -> 90

list_of_nums = []

for i in range(0, 5):
    number = int(input())

    list_of_nums.append(number)

print(list_of_nums)
print(max(list_of_nums))