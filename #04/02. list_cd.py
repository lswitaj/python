catNames = ['']
while catNames[len(catNames)-1] != 'stop':
    print('Enter the name of cat:')
    catNames += [input()]

print('cat names are:')

sortedCatNames = catNames[1:-1]
sortedCatNames.sort(key = str.lower)
print(sortedCatNames)
sortedCatNames.sort(reverse = True)
print(sortedCatNames)

if 'burek' in catNames:
    print('burek is here!')