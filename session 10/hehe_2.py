a = {
    'name' : 'Phan Huy Cong',
    'age' : 16,
    'place' : 'Hanoi'
}
print(a)
output = input('what do you want to check')
if output in a:
    print(output , 'is exists in my dictionary')
else:
    print(output , 'is not exists in my dictiona

while True:
    b = {
        'explain' : 'giải thích',
        'refuse' : 'từ chối',
        'define' : 'định nghĩa',
    }
    print('explain', 'refuse', 'define')
    output = input('what do you want to know').lower()
    if output in b:
        print(output, 'là', b[output])
    else:
        print('Not exits this word')


