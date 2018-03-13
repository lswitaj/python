import sys

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 11', 'Mike': 'Jan 22'}

while True:
    print('Enter name (or q to quit):')
    name = input()
    if name == 'q':
        #sys.exit()
        break

    if name in birthdays:
        print(name + ' your bday is ' + birthdays[name])
    else:
        print('We dont have yours bday')
        print('Enter it to our DB please')
        birthdays[name] = input()
        print('Bday DB updated')

print('')

for i in birthdays.keys():
    print(i)
print(list(birthdays.values()))
for i in birthdays.items():
    print(i)