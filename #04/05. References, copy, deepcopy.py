import copy

lala = [1, 2, 3]
nana = lala
nana[1] = 'pfff'

print(lala)

lala = copy.copy(nana)
lala[1] = 'im changed'
print(lala != nana)

print(nana)
print(lala)

#we also can use deepcopy