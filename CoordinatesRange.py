#4. Напишите программу, которая по заданному 
#номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

num = int(input("Введите номер четверти: "))

match num:
    case 1:
        print(" x > 0; y > 0")
    case 2:
        print(" x < 0; y > 0")
    case 3:
        print(" x < 0; y < 0")
    case 4:
        print(" x > 0; y < 0")
    case _:
        print("Что то не так")