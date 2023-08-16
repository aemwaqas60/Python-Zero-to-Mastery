# Creating an empty tuple
tuple1 = ()
print(f'Initial empty tuple : {tuple1}')

# Creating an tuple with the use of strings
tuple1 = ('me', 'or', 'me', 'not')
print(f'\nTuple with the use of strings : {tuple1}')

# Creating an tuple with the use of list
list1 = ['me', 'or', 'me', 'not', 'or', 'you']
print(f'\nTuple with the use of list :  {tuple(list1)}')

# Creating an tuple with the use of built-in function
tuple1 = tuple('me')
print(f'\nTuple with the use of built in function : {tuple1}')

# Creating an tuple with nested tuples
tuple1 = ('me', 'or')
tuple2 = ('me', 'not')
tuple3 = (tuple1, tuple2)
print(f'\nTuple with the use of nested tuples : {tuple3}')

# Accessing the tuple elements
tuple1 = tuple([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(f'\n------ Accessing the Tuple elements -----')

print(f'Tuple Elements : {tuple1}')
print(f'\nFirst element of tuple : {tuple1[0]}')
print(f'\nLast element of tuple : {tuple1[-1]}')
print(f'\n3rd last element of tuple : {tuple1[-3]}')
