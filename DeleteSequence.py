from os import remove


seq = input("Enter anything: ").split()

for i in seq:

    if "абв" in i or i == "абв":
        seq.remove(i) 

seq = ' '.join(seq)

print(seq)