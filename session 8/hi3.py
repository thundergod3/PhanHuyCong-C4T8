items = ['beo', 'mo', 'bong', 'xinh', 'dep']

while True:
    print(items)
    a = input('C or R or U or D ? ').upper()
    if 'C' in a:
        items.append(input('What do you like ?'))
        print(items)
    elif 'R' in a:
        b = int(input('Number u like ?'))
        if b > len(items)-1:
            print('Repeat')
        print(items[b])
    elif 'U' in a:
        c = int(input('Number ?'))
        if c > len(items)-1:
            print('Bye')
        replacing_iteam = input('Update')
        items[c] = replacing_iteam
        print(items)
    elif 'D' in a:
        d = int(input('Num ?'))
        if d > len(items)-1:
            print('Repeat')
        items.pop(d)
        print(items)

