# Задача 3. Напишите программу, в которой пользователь будет 
# задавать две строки, а программа - определять количество вхождений 
# одной строки в другой. COUNT или FIND нельзя юзать! говорил же на семинаре.

def lines(first_line, second_line):
    counter = 0
    first_line = first_line.split(" ")

    for i in first_line:
        if second_line in i:
            counter += 1
    
    return counter

line_1 = input("Введите строку, в которой хотите искать: ")
line_2 = input("Введите искомую строку: ")

try:
    print(lines(line_1, line_2))

except:
    print("Something went wrong")