while True:
    string = []
    string = input('Pass')
    print(not string.isalpha())
    if len(string) <8 or not string.isalpha():
        break
