#Say hello and ask 4 name

print('Hello, type name')
name = input()
print('Nice to meet you ' + name)
print('Your name contains: ' + str(len(name)))
print('Now type age: ')
age = input()
print('You\'ll be ' + str(int(age) + 1) + ' in a year')
