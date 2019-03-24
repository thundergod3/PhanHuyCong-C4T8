import math
yob = int(input('Give me a number'))
age = 2018 - yob
print(age)
if age < 14:
    print("Bạn chưa đủ tuổi xem video này")
else:
    print("Mời bạn xem video")

print('Chương trình giải phương trình bậc 2')
a = float(input('give me numbera:'))
b = float(input('give me numberb:'))
c = float(input('give me numberc:'))


if a == 0:
    if b == 0 and c == 0:
        print('Pt vô số nghiệm')
    elif b == 0 and c != 0:
        print('Pt vô nghiệm')
    else:
        x = -c/b
        print(x)

else:
    delta = b**2 - 4*a*c
    if delta > 0:
        print('Pt có 2 nghiệm phân biệt')

        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print(x1, x2)
    elif delta ==0:
        print('Pt có nghiệm kép')
        x1 = x2 = -b/2*a
        print(x1, x2)
    else:
        print('Pt vô nghiệm')
                 




  
    
    

x1 = (-b + math.sqrt(delta))/(2*a)
x2 = (-b - math.sqrt(delta))/(2*a)
