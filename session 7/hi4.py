for i in range(3, 13, 1):
    print(i)

a = int(input('Give me a number'))
for j in range(0, a, 1):
    print(j)

b = int(input('Number you like?'))
for k in range(b, -1, -1):
    print(k)

from turtle import*

c = int(input('How many sides would you like'))
for z in range(c):
    forward(60)
    left(360/c)



mainloop()