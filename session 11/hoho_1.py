#Part 3
movie = {
    'name' : 'Harry Potter',
    'year' : 1997,
    'actors' : ['Watson', 'Grint'],
}

movie['the firm'] = 'picture 1992'
print(movie)

movie['actors'] = ['a', 'b']
movie['actors'].append('c')
movie['actors'].pop(0)

for k,v in movie.items():
    print(k, '-', v)
 
print(movie['actors'][1])

for i in movie['actors']:
    print(*i)

