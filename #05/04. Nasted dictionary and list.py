allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guest, item):
    numBorught = 0
    for k, v in guest.items():
        numBorught += v.get(item, 0)
    return numBorught

print('Number of things being brought:')
print('Apples ' + str(totalBrought(allGuests, 'apples')))
print(totalBrought(allGuests, 'cups'))
print(totalBrought(allGuests, 'cakes'))
print(totalBrought(allGuests, 'ham sandwiches'))
print(totalBrought(allGuests, 'apple pies'))