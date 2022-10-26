# Задача 3. Задайте список из вещественных чисел. Напишите программу,
#  которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def fractions(arr):
    arr_2 = []

    for i in arr:
        arr_2.append(round(i % 1, 2))
    
    return min_fraction(arr_2) + max_fraction(arr_2)

def min_fraction(arr):
    minimum = arr[0]

    for i in range(len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]
    
    return minimum

def max_fraction(arr):
    maximum = arr[0]

    for i in range(len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]
    
    return maximum


try:
    array = [1.1, 1.2, 3.1, 5.9, 10.01]
    print(fractions(array))

except:
    print("Something went wrong")

