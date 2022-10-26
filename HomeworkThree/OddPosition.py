# Задача 1 Задайте список из нескольких чисел. Напишите программу,
#  которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def find_position(array):
    counter = 0
    for i in range(0, len(array)):
        if i % 2 != 0:
            counter += array[i]

    return counter

arr = [2, 3, 5, 9, 3, 2]

try:
    print(find_position(arr))
except:
    print("Something went wrong")
