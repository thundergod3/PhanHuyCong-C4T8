while True:
    string = []
    string = input('Pass')
    print( not string.isalpha() or string.isupper())
    if len(string)<8 or not string.isalpha() or string.isupper():
        break
