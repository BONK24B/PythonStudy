x = bool(input())
y = bool(input())
z = bool(input())

try:
    if (not(x or y or z) == (not x) and (not y) and (not z)):
        print("True")
    else:
        print("False")

except:
    print("Enter boolean value")