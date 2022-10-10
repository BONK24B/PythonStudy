number = int(input("Enter the number from 1 to 7 to see if it's weekend: "))

try:
    if(number in range(1, 6)):
        print("No")
    elif (number in range(6, 8)):
        print("Yes")
    else:
        print("Your number is not in range 1 - 7")

except:
    print("Something's went wrong")