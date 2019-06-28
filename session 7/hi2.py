# # Part 2
# a = int(input('Give me a number that smaller than 13'))
# if a < 13:
#     print('Right')
# else :
#     print('Try again')

# b = int(input('Give me a number'))
# if b % 2 ==0:
#     print('This is even number')
# else:
#     print('This is not even number')

# c = int(input('Give a month'))
# if c == 1 :
#     print('31')
# elif c == 2:
#     print('28,29')
# elif c == 3:
#     print('31')
# elif c == 4:
#     print('30')
# elif c == 5:
#     print('31')
# elif c == 6:
#     print('30')
# elif c == 7:
#     print('31')
# elif c == 8:
#     print('31')
# elif c == 9:
#     print('30')
# elif c == 10:
#     print("31")
# elif c == 11:
#     print('30')
# elif c == 12:
#     print('31')
# else :
#     print('not exist')

c = int(input('nhap'))
for i in range(c + 1):
    print(c, 'a')

    d = c % 2
    if d == 1:
        print(c)
    c += - 1
        
