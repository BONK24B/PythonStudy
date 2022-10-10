#2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

#*Примеры:*

#- 6,78 -> 7
#- 5 -> нет
#- 0,34 -> 3

number = float(input("Enter float number: "))

try:
    n = int(number * 10) % 10
    
    if n != 0:
        print(n)
    else:
        print("No")
    

except:
    print("Enter float number")