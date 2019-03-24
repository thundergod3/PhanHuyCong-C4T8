# #Part 1 + 2 + 3 + 4
computer = { 
    'HP' : 20,
    'DELL' : 50,
    'MACBOOK' : 12,
    'ASUS' : 30,
}

computer['TOSHIBA'] = 10
# computer['DELL'] +=10
# computer['MACBOOK'] = int(input('number ?'))
computer['FUJISU'] = 15
computer['ALIENWARE'] = 5
computer['ACER'] = 20 # phục vụ cho part 4

# for i,j in computer.items():
#     print(i, ':', j)

# print(computer['MACBOOK'])

# computer1 = {}

# # a = input('your computer you like ?')
# # computer1[a] = input('number?')
# # b = input('your computer you like ?')
# # computer1[b] = input('number?')
# # c = input('your computer you like ?')
# # computer1[c] = input('number?')
# # d = input('your computer you like ?')
# # computer1[d] = input('number?')
# # e = input('your computer you like ?')
# # computer1[e] = input('number?')

# x = 0
# for v in computer.values():
#     x = v + x
# print(x)

computer_prices = {
    'HP' : 600,
    'DELL' : 650,
    'MACBOOK' : 12000,
    'ASUS' : 400,
    'ACER' : 350,
    'TOSHIBA' : 600,
    'FUJISU' : 900,
    'ALIENWARE' : 1000,
}

# print('price of ASUS', computer_prices['ASUS'])

# for k,l in computer_prices.items():
#     print(k, ':', l)

# ouput = input('computer you like').upper()
# print(computer_prices[ouput])

# prices = computer_prices['ASUS']*5
# print(prices)

# ouput1 = input('computer you like').upper()

# if ouput1 in computer_prices:
#     prices1 = input('how much do you want to buy')
#     prices2 = int(prices) * computer_prices[ouput1]
#     print(prices2)
# else :
#     print('Not exist this computer')

prices_list1 = [20, 50, 12, 30, 10, 15, 5, 20]
prices_list2 = [600, 650, 12000,400,350, 600, 900, 1000]
prices4 = 0

for m in range(len(prices_list1)):
    prices3 = prices_list1[m] * prices_list2[m]
    print(prices3)
    prices4 = prices3 + prices4
print(prices4)



