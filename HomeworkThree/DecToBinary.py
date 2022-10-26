# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Нельзя использовать готовые функции.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def binary_cast(num):
    rest = []

    if num == 0:
        return 0

    while num != 1:
        rest.append(num % 2)
        num = num // 2

    rest.append(num % 2)
    rest = rest[::-1]

    return arr_to_str(rest)

def arr_to_str(arr):
    tmp = ''
    for i in arr:
        tmp += str(i)

    return int(tmp)

try:
    number = int(input("Enter your number: "))
    print(binary_cast(number))

except:
    print("Something went wrong")