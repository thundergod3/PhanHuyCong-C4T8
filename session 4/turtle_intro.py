#lấy toàn bộ thông tin trong turtle
from turtle import *

#thay đổi hình dạng mũi tên
shape("turtle")
#thay đổi màu sắc
color("orange")
speed(0)

#hãy lặp lại 6 lần những câu lệnh đc thụt vào trg
#có thể lặp lại những câu trong for đấy bằng cách tạo câu lệnh như thế nữa xg lùi phần câu lệnh vào 1 bậc nữa
#ở dưới gọi là nested loop(vòng lặp trống)
for i in range(400):
    for i in range(4):
        forward(100)
        left(90)

    left(2)



mainloop()