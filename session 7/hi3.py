# Part3
a = input('Usename')
print(a)
b = input('Pass')
if len(b) < 7 and not b.isalpha() and b.isdigit():
    print("Pass has't strong enough")
else:
    c = input('Pass again')
    if b == c:
        print('Right')
        d = input('Email')
        if "@" and "..." in d:
            print('Right')
        else :
            print('Try again')

    else :
        print('Welcome')
