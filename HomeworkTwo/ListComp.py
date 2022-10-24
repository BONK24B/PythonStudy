given_numbers = [1, 2, 3, 5, 8, 15, 23, 38]

a = lambda x: x ** 2

b = [(i, a(i)) for i in given_numbers if i % 2 == 0]

print(b)