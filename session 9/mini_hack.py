#Part 1
list_color = ['red', 'blue', 'green', 'black']
print("our color" , ':', *list_color)

more_color = input('color you like')
list_color.append(more_color)
print('new color', ':', *list_color)

position = int(input('enter position'))
if position > len(list_color)-1:
    print('number not exist')
else:
    print(list_color[position])

a = input('number or position')
if a.isdigit():
    if int(a) > len(list_color)-1:
        print('number not exist')
    else:
        list_color.pop(int(a)-1)
        print(*list_color)
elif not a.isalpha():
    print('Try again')
elif a not in list_color:
    print('Try again')
else:
    list_color.remove(a)
    print(list_color)

from turtle import*

list_color = ['red', 'blue', 'green', 'black']
for i in list_color:
    for j in range(1):
        width(30)
        color(i)
        forward(50)

mainloop()



