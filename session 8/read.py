items = ['Com' , 'Pho' , 'Chao' , 'Com rang']
print(items)
print(*items , sep=', ') # separator - dấu cách phân cách giữa các phần tử

# index - chỉ số

print('Index 1')
print(items[1])

print('Index 0')
print(items[0])

i = int(input('Enter index: '))
print(items[i])