#3. Напишите программу, в которой пользователь 
#будет задавать две строки, а программа - определять количество вхождений одной строки в другой.



str1 = input()
str2 = input()
arr1 = []
arr2 = []
count = 0

for i in str1:
    arr1.append(i)

for i in str2:
    arr2.append(i)

for i in range(0, len(str1) + len(str2)):
    if arr2 in arr1:
        count += 1

print(count)
