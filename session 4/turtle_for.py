from turtle import*

colormode(255)
#thay đổi nét vẽ
width(20)
#thay đổi màu: rgb
speed(0)
for i in range(5):
    color(255, i*40, 0)
    for j in range(4):
        forward(100)
        left(90)
    
    left(30)




mainloop()