set1 = {1, 2, 3, 4, 5}

print(type(set1))
print(len(set1))
print(set1)

set1.add(6)
print(set1)

fruits_sets = {'banana', 'appel', 'orange', 'cherry'}

set1.update(fruits_sets)
print(set1)

set1.remove(4)
print(set1)

set1.remove('banana')
print(set1)

# set1.remove('kiwi')
# print(f'remove {set1}')

# set1.remove(-1)

set1.discard('kiwi')
print(f'remove {set1}')

set1.pop()
print(set1)

# set1.clear()
# print(set1)

# del set1
# print(set1)