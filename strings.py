# Single line String
message = "Hi, welcome in python course!"

# Multi line string
message1 = ''' Welcome 

------
o o ooo o oo
'''

# String concatenation
firstName = 'Muhammad '
lastName = 'Waqas'
fullName = firstName + lastName;

print(f'-----Single Line String using------')
print(message)
print(f'-----Multi Line String using------')
print(message1)
print(f'----- String Concatenation using------')
print(fullName)

print('--------------------')
print('Access characters of string')
print('--------------------')

string1 = 'GeeksForGeeks'
print(f'initial string : ')
print(string1)

string1 = 'GeeksForGeeks'
print(f'\n first character of  string is : ')
print(string1[0])

string1 = 'GeeksForGeeks'
print(f'\n last character of string is : ')
print(string1[-1])

print('--------------------')
print('String Functions')
print('--------------------')

quote = 'to be or not to be'

print(f'String length : {len(quote)}')
print(quote.upper())
print(quote.capitalize())
print(quote.lower())
print(quote.find('be'))
print(quote.replace('be', 'me'))

print('--------------------')
print('String Slicing and indexing')
print('--------------------')
# [start:stop:step]

quote2 = 'GEEKSFORGEEKS'

print(f'Simple slicing :  {quote2[0:4]}')
print(f'Emit start index :  {quote2[:11]}')
print(f'Emit end index :  {quote2[0:]}')
print(f'Reverse iteration :  {quote2[::-1]}')
print(f'step by 2 :  {quote2[0:11:2]}')
print(f'Reverse step by 2 :  {quote2[::-2]}')
print('Reverse string : ' + quote2[1:12:-1])
