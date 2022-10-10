#1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

#*Примеры:*

#- 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

#num = int(input("Enter the number: "))
#num_neg = -1 * num

#if num > 0:
    #while(num_neg <= num):
        #print(num_neg)
        #num_neg += 1
#elif num < 0:
    #while (num <= num_neg):
        #print(num)
        #num += 1
#else:
    #print("Something went wrong")

try:
    number = int(input("Enter the number: "))

    if number > 0:
        for i in range(-number, number + 1):
            print(i)
    elif number < 0:
        for i in range(number, -number + 1):
            print(i)

except:
    print("Enter whole number")