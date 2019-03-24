#Part1
a = {}
b = {
    'name' : 'Phan Huy Cong',
    'age' : 16,
    'place' : 'Hanoi'
}

print(a)
print(b)

film = {
    'Name' : 'Harry Potter',
    'Series' : 7,
    'Novel' : 7,
}
c = input('information you like')
film[c] = input('Do you like this film')

d = input('information you know about the novel of this film')
film['Novel'] = d
print(film)

e = input('what do you want to remove')
del film[e]
print(film)
