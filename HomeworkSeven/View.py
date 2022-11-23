def get_value():
    return int(input("value = "))

def get_operation():
    a = input("operation: ")

    if a == "+" or a == "-" or a == "*" or a == "/":
        return a
    else:
        return "Error"


def print_data(data):
    print(data)