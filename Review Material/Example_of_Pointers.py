# integers are immutable
a = 10
b = a
print(f'a: {a}, b: {b}')
a = 20
print(f'a: {a}, b: {b}')

# lists are mutable
a = [1, 2, 3]
b = a
print(f'a: {a}, b: {b}')
a.append(4)
print(f'a: {a}, b: {b}')

# so are dictionaries
a = {'a': 1, 'b': 2}
b = a
print(f'a: {a}, b: {b}')
a['c'] = 3
print(f'a: {a}, b: {b}')