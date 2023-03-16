# More Operators

# Member operator
print('\nMember operator')
people = [1, 2, 3, 'Ana', 'Carla']
print(2 in people)
print(5 not in people)
print('Carla' not in people)

# Identity operator
print('\nIdentity operator')
x = 3
y = x
z = 3
print(x is y)
print(y is z)
print(y is not z)

# More examples
print('\nMore examples')
list_a = [1, 2, 3]
list_b = list_a
list_c = [1, 2, 3]
print(list_a is list_b)
print(list_b is list_c)
print(list_a is not list_c)
