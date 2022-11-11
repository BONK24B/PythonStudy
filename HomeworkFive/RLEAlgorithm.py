# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.


def rle_encoding(value):
    if value == "":
        return ""
    
    encoded = []
    length = 1

    for i in range(1, len(value)):
        if value[i] == value[i - 1]:
            length += 1
    
        else:
            encoded.extend([str(length), str(value[i - 1])])
            length = 1

    encoded.extend([str(length), str(value[-1])])
    
        
    return "".join(encoded)

value = input("Enter anything: ")

try:
    with open("code.txt", "w") as file:
        file.writelines(value)
        file.write("\n")
        file.writelines(rle_encoding(value))

except:
    print("Something's wrong")