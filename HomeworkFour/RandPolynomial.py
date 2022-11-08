# Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# *Пример:* 

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random


def coefficients_list(num):
    arr = [] * num

    for i in range(num):
        i = random.randint(0, 10)
        arr.append(i)
    
    return arr

def create_polynomial(arr):
    poly = ""
    n = len(arr)
    str_arr = []

    for i in arr:
        str_arr.append(str(i))

    for i in range(len(str_arr)):

        if arr[i] == 0:
            continue

        if n == 1:
            poly += ' ' + str_arr[i] + "x^" + str(n)
            break

        poly += ' ' + str_arr[i] + "x^" + str(n) + " +"
        n -= 1

    return poly + " = 0"


n = int(input("Enter your number: "))
arr = coefficients_list(n)
res = create_polynomial(arr)

f = open("polynomial.txt", "a")
f.write(res)
f.close

