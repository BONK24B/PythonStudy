# задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Функции FIND и COUNT юзать нельзя.

def subsequence_check(words):

    words = words.split()

    for i in words:
        if i == "абв" or "абв" in i:
           words.remove(i)

    words = ' '.join(words)
    return words

text = input("Enter your text: ")

try:
    print(subsequence_check(text))

except:
    print("Something's wrong")