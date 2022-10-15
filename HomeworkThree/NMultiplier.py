# Задача 2. Напишите 
# программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def make_array(array, number):
    counter = 1
    for i in range(0, len(array)):
        array[i] = array[i] * counter * array[i - 1]
        counter += 1

    return array



number = int(input("Введите целое число: "))
arr = [1] * number

try:
    print(make_array(arr, number))

except:
    print("Something went wrong")