# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


def even_array(arr):
    arr_2 = []

    for i in range(len(arr) // 2):
        arr_2.append(arr[i] * arr[-i - 1])
    
    return arr_2

def odd_array(arr):
    arr_2 = []

    for i in range(len(arr) // 2):
        arr_2.append(arr[i] * arr[-i - 1])

    for i in range(len(array)):
        if i == len(array) // 2:
            arr_2.append(array[i] ** 2)
    
    return arr_2
    
array = [2, 4, 3]

try:
    if len(array) % 2 == 0:
        print(even_array(array))
    else:
        print(odd_array(array))

except:
    print("Something went wrong")
