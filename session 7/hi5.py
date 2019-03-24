import random

a = random.randrange(0, 20, 1)
b = random.randrange(0, 20, 1)
c = a + b
result_false = c + random.randrange(-3, 3, 1)

print(a, '+' ,b, '=' ,result_false)

# flag check false
flag = result_false == c 
while True:
    d = input('Answer: ').lower()
    if d == "t":
        # ng dùng nhập true
        checking = True
        # kiểm tra câu trả lời của ng dùng với flag
        if (checking == flag):
            print("Dung")
            break
        else:
            print("Sai")
            break
    elif d == "f":  
        # ng dùng nhập false hoặc true 
        checking = False
        if (checking == flag):
            print("Dung")
            break
        else:
            print("Sai")
            break
    

