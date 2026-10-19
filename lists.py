myLists = [0, 1, 2, 3, 4]
print(type(myLists))
print(myLists[-1])
print(len(myLists))

myLists.append(10)
print(myLists)

# myLists.append("Hassan")
# print(myLists)

myFruits = ['banana', 'appel', 'orange', 'cherry']
myFruits.append('Kiwi')
print(myFruits)

# myLists.remove('Hassan')
# print(myLists)

myLists.remove(4)
print(myLists)

# myLists.pop()
# print(myLists)

# myLists.pop(-1)
# print(myLists)

# myLists.pop(2)
# print(myLists)

# del myLists[0]
# print(myLists)

# myLists.clear()
# print(myLists)

myLists.extend(myFruits)
print(myLists)

newList = []

# for x in myFruits:
#     if 'a' in x:
#         newList.append(x)
# print(newList)

newList = [x for x in myFruits if 'a' in x]
print(newList)

ranging_list = [x for x in range(11)]
print(ranging_list)


print(ranging_list[0:5])
print(ranging_list[5:])