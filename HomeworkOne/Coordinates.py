x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))

try:
    if (x > 0 and y > 0):
        print(1)
    elif (x < 0 and y > 0):
        print(2)
    elif (x < 0 and y < 0):
        print(3)
    elif (x > 0 and y < 0):
        print(4)
    else:
        print("0 ; 0")
except:
    print("Non integer value entered")