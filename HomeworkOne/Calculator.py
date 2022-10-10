num_one = int(input("Enter first number: "))
op_arr = ["+", "-", "*", "/", "mod", "pow", "div"]
operation = input(f"Enter operation ({op_arr}): ")
num_two = int(input("Enter second number: "))

def calculation(a, b, c):
    if b in op_arr:
        match b:
            case "+":
                print(a + c)
            case "-":
                print(a - c)
            case "*":
                print(a * c)
            case "/":
                if (c != 0):
                    print(a / c)
                else:
                    print("You can not divide by 0")
            case "mod":
                if (c != 0):
                    print(a % c)
                else:
                    print("You can not divide by 0")
            case "pow":
                print(a ** c)
            case "div":
                if (c != 0):
                    print(a // c)
                else:
                    print("You can not divide by 0")
    else:
        print("Choose the correct operation")


calculation(num_one, operation, num_two)