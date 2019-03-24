yob = int(input("your year of birth?"))
age = 2018 - yob
print(age)

# Chú ý ưu tiên dòng 7 rồi đến 10 rồi đến 13
# Nếu age nhỏ hơn 10 in Baby
if age < 10:
    print("Baby")
# Nếu age nằm trong khoảng 10<age<18
elif age < 18:
    print("Teenager")
# Nếu age từ 18 trở đi thì in Adult
else:
    print("Adult")
    print("...")

# Những dòng thụt vào đầu dòng sẽ ko bị ảnh hưởng bởi elif  
print("Bye ")

