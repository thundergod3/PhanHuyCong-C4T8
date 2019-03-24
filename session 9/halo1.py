#Part 2
number = [1,3,4,6,7,15,7,20]
print(number)
answer = input('enter your number')
if answer in number:
    number[int(answer)]
else:
    print('not found in our list')

print(sum(number))
a = 0
for i in number:
    a = a + i 
print(a)

number1 = input('number')
list_new_number1 = []
list_number1 = list(number1)
for i in list_number1:
    list_new_number1.append(int(i))
print(sum(list_new_number1))

number2 = input('number?')
list_number2 = list(number2)
list_new_number2 = []
for i in list_number2:
    if int(i) % 2 == 0:
        list_new_number2.append(int(i))
print(*list_new_number2, sep= ',')




