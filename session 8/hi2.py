item3 = ['gsx-150'.upper(), 'zx10r'.upper(), 'bmw 1000r'.upper(), 'ducati'.upper()]
for item in item3:
    print(item)

for i,item in enumerate(item3):
    print(i + 1, '.', item)

name_string = input('What are your favorite')
name = name_string.split(',')
print(name)

import random

a = input('Give me smt')
b = list(a)
random.shuffle(b)
print(b)    

quizz = ['home', 'table', 'rice', 'halo']

c = random.choice(quizz)
list_quizz = list(c)
random.shuffle(list_quizz)
print(*list_quizz)
answer = input('what this word ?')
if answer == c:
    print("wowwww")
else:
    print('Try again =)')
for i in quizz:
    if 'o' in i:
        print(i)



    


