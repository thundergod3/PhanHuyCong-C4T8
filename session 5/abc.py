from random import randint
a =(randint(0, 100))

if randint(0, 100) < 30:
    print('Rainly')
elif randint(0, 100) < 61:
    print('Cloudy')
elif randint(0, 100) < 100:
    print('Sunnt')
else :
    print('Bye')    

