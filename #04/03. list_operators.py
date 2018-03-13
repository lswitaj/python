cat = ['black', 3]

print('Type name of cat: ')
cat += [input()]

colour, age, name = cat

print('Your cats name is ' + name + ' and this cat is ' + colour)

try:
    print('Gutek is under index number: ' + str(cat.index('Gutek')))
    cat.remove('Gutek')
    cat.insert(2, 'Stasiek')
    print('Your cat has new  name: ' + cat[2])
except ValueError:
    print('Gutek isnt hier')


# we can use cat.insert(X, 'sth') - insert on X position
# and cat.append - simple add at the end