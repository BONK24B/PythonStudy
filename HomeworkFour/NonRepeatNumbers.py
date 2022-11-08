#  Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

def non_repeated(arr):
    non_rep_arr = []

    for i in range(len(arr)):
        j = 0

        while j < len(arr):
            if i != j and arr[i] == arr[j]:
                break
            j += 1

            if j == len(arr):
                non_rep_arr.append(arr[i])
            
    return non_rep_arr

array = [2, 2, 2, 4, 1, 5, 1, 14]

print(non_repeated(array))