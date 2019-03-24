while True:
    string = input('Pass')
    print(not string.isalpha()) 
    if not string.isalpha():
        break


k = 0
while k < 5:
    print(k)
    k +=1

loop_count = 0
while True:
    loop_count +=1
    print(loop_count)
    if loop_count > 6:
        break
    
