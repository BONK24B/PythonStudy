x = 0
y = 0

def init(a, b):
    global x, y

    x = a
    y = b

def sum():
    return x + y

def sub():
    return x - y

def mult():
    return x * y

def div():
    if y == 0:
        return "Error"
    else:
        return x / y