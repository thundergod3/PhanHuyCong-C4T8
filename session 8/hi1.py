item3 = ['gsx-150'.upper(), 'zx10r'.upper(), 'bmw 1000r'.upper(), 'ducati'.upper()]
item3.append('cbr-250'.upper())
print(*item3, sep="| ")

i = 0
replacing_item = 'Harry Potter'
item3[i] = replacing_item
print(item3)

k = len(item3)-1
replacing_item3 = 'One Piece'
item3[k] = replacing_item3
print(item3)

j = int(input('0 or 1 or 2 or 3 or ...'))
if j > len(item3)-1:
    print('a')
replacing_item2 = input('What do you like')
item3[j] = replacing_item2
print(item3)

item3.pop(1)
print(item3)

a = input('?')
if a not in item3:
    print('item not exist')

b = input('what do you want to remove')
item3.remove(b)
print(item3)

c = int(input('0 or 1 or 2 ?'))
item3.pop(c)
print(item3)