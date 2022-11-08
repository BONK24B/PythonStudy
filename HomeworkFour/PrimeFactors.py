# 1. Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

def prime_factors(num):
    prime_array = []

    for i in range(1, num + 1):
        if num % i == 0:
            counter = 0
            
            for j in range(1, i + 1):
                if i % j == 0:
                    counter += 1
            if counter == 2:
                prime_array.append(i)
                    
                
    return prime_array


number = int(input("Enter the number to see it's prime factors: "))

try:
    print(prime_factors(number))

except:
    print("Something went wrong")


