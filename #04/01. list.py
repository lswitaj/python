newList = [[1, 2, 3], ['great', 'sun']]

print(newList[0])
print(newList[0][2])
print(newList[1][1])

print(newList[0][-3])

#3 is not viewed
print(newList[0][1:3])

print(newList[0][:2])
print(newList[0][1:])
print(newList[0][:])

print('Next try')

mergedList = newList[0] + newList[1] * 2
del mergedList[:2]
print(mergedList)