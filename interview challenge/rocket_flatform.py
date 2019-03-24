from random import randint

x = 4
y = 4
horizontal_dash = '-'
miss_position = 'X'
hit_position = 'O'
output_count = 5
enermy_count = 0 
enermy_left = 2
list_save = []

mapping = [['-','-','-','-'],['-','-','-','-'],['-','-','-','-'],['-','-','-','-']]

def show_map():
    for i in mapping:
        print(*i)

show_map()

while True:
    x_enermy1 = randint(0, 3)
    y_enermy1 = randint(0, 3)
    x_enermy2 = randint(0, 3)
    y_enermy2 = randint(0, 3)   
    if not (x_enermy1 == x_enermy2) and (y_enermy1 == y_enermy2):
        break

while True:
    output_x = int(input("What's your x position ?")) - 1
    output_y = int(input("What's your y position ?")) - 1
    output_count -= 1

    if (output_x == x_enermy1) and (output_y == y_enermy1):
        mapping[output_y][output_x] = 'O'
        enermy_left -= 1

        if enermy_left == 0:
            print('You won !!!')
            print(output_count, 'rockects left')
            print(enermy_left, 'enermy left')
            show_map()
            break

        if output_count == 0:
            print('Out of rocket !!!')
            print(enermy_count, 'enermy(s) around')
            print(output_count, 'rockects left')
            print(enermy_left, 'enermy left')
            mapping[output_y][output_x] = 'X'
            show_map()
            break

        print('You hit')
        print(enermy_count, 'enermy(s) around')
        print(output_count, 'rockects left')
        print(enermy_left, 'enermy left')

    elif (output_x == x_enermy2) and (output_y == y_enermy2):
        mapping[y_enermy2][x_enermy2] = 'O'  

        if enermy_left == 0:
            print('You won !!!')
            print(output_count, 'rockects left')
            print(enermy_left, 'enermy left')
            show_map()
            break

        if output_count == 0:
            print('Out of rocket !!!')
            print(enermy_count, 'enermy(s) around')
            print(output_count, 'rockects left')
            print(enermy_left, 'enermy left')
            mapping[output_y][output_x] = 'X'
            show_map()
            break    

        print('You hit')
        print(enermy_count, 'enermy(s) around')
        print(output_count, 'rockects left')      
        print(enermy_left, 'enermy left')  

    else:   
        if output_x > 0 and output_y > 0 and output_x < 3 and output_y < 3:    
            for m in range(output_x - 1, output_x + 2
            ):
                for n in range(output_y - 1, output_y + 2):
                    if (((mapping[n][m] != 'O') and ((m == x_enermy1) and (n == y_enermy1))) or ((mapping[n][m] != 'O') and ((m == x_enermy2) and (n == y_enermy2)))):
                        enermy_count += 1
                        if enermy_count > 2: 
                            enermy_count -= 1
            
            if output_count == 0:
                print('Out of rocket !!!')
                print(enermy_count, 'enermy(s) around')
                print(output_count, 'rockects left')
                print(enermy_left, 'enermy left')
                mapping[output_y][output_x] = 'X'
                show_map()
                break

            print('You missed')
            print(enermy_count, 'enermy(s) around')
            print(output_count, 'rockects left')
            print(enermy_left, 'enermy left')
    
        elif output_x == 0 and output_y == 0 :
            for m in range(output_x, output_x + 2):
                for n in range(output_y, output_y + 2):
                    if (((mapping[n][m] != 'O') and ((m == x_enermy1) and (n == y_enermy1))) or ((mapping[n][m] != 'O') and ((m == x_enermy2) and (n == y_enermy2)))):
                        enermy_count += 1
                        if enermy_count > 2: 
                            enermy_count -= 1
            
            if output_count == 0:
                print('Out of rocket !!!')
                print(enermy_count, 'enermy(s) around')
                print(output_count, 'rockects left')
                print(enermy_left, 'enermy left')
                mapping[output_y][output_x] = 'X'
                show_map()
                break

            print('You missed')
            print(enermy_count, 'enermy(s) around')
            print(output_count, 'rockects left')
            print(enermy_left, 'enermy left')

        elif output_x == 0 and output_y > 0 and output_y < 3:
            for m in range(output_x, output_x + 2):
                for n in range(output_y - 1, output_y + 2):
                    if (((mapping[n][m] != 'O') and ((m == x_enermy1) and (n == y_enermy1))) or ((mapping[n][m] != 'O') and ((m == x_enermy2) and (n == y_enermy2)))):
                        enermy_count += 1
                        if enermy_count > 2: 
                            enermy_count -= 1
            
            if output_count == 0:
                print('Out of rocket !!!')
                print(enermy_count, 'enermy(s) around')
                print(output_count, 'rockects left')
                print(enermy_left, 'enermy left')
                mapping[output_y][output_x] = 'X'
                show_map()
                break

            print('You missed')
            print(enermy_count, 'enermy(s) around')
            print(output_count, 'rockects left')
            print(enermy_left, 'enermy left')

        elif output_x == 0 and output_y == 2:
            for m in range(output_x, output_x + 2):
                for n in range(output_y - 1, output_y + 1):
                    if (((mapping[n][m] != 'O') and ((m == x_enermy1) and (n == y_enermy1))) or ((mapping[n][m] != 'O') and ((m == x_enermy2) and (n == y_enermy2)))):
                        enermy_count += 1
                        if enermy_count > 2: 
                            enermy_count -= 1

            if output_count == 0:
                print('Out of rocket !!!')
                print(enermy_count, 'enermy(s) around')
                print(output_count, 'rockects left')
                print(enermy_left, 'enermy left')
                mapping[output_y][output_x] = 'X'
                show_map()
                break

            print('You missed')
            print(enermy_count, 'enermy(s) around')
            print(output_count, 'rockects left')
            print(enermy_left, 'enermy left')

        elif output_x == 0 and output_y == 3:
            for m in range(output_x, output_x + 2):
                for n in range(output_y - 1, output_y):
                    if (((mapping[n][m] != 'O') and ((m == x_enermy1) and (n == y_enermy1))) or ((mapping[n][m] != 'O') and ((m == x_enermy2) and (n == y_enermy2)))):
                        enermy_count += 1
                        if enermy_count > 2: 
                            enermy_count -= 1
            
            if output_count == 0:
                print('Out of rocket !!!')
                print(enermy_count, 'enermy(s) around')
                print(output_count, 'rockects left')
                print(enermy_left, 'enermy left')
                mapping[output_y][output_x] = 'X'
                show_map()
                break
            
            print('You missed')
            print(enermy_count, 'enermy(s) around')
            print(output_count, 'rockects left')
            print(enermy_left, 'enermy left')


        elif output_x > 0 and output_x < 3 and output_y == 3:
            for m in range(output_x - 1, output_x + 2):
                for n in range(output_y - 1, output_y):
                    if (((mapping[n][m] != 'O') and ((m == x_enermy1) and (n == y_enermy1))) or ((mapping[n][m] != 'O') and ((m == x_enermy2) and (n == y_enermy2)))):
                        enermy_count += 1
                        if enermy_count > 2: 
                            enermy_count -= 1
            
            if output_count == 0:
                print('Out of rocket !!!')
                print(enermy_count, 'enermy(s) around')
                print(output_count, 'rockects left')
                print(enermy_left, 'enermy left')
                mapping[output_y][output_x] = 'X'
                show_map()
                break

            print('You missed')
            print(enermy_count, 'enermy(s) around')
            print(output_count, 'rockects left')
            print(enermy_left, 'enermy left')

        elif output_x == 2 and output_y == 3:
            for m in range(output_x - 1, output_x +1):
                for n in range(output_y - 1, output_y):
                    if (((mapping[n][m] != 'O') and ((m == x_enermy1) and (n == y_enermy1))) or ((mapping[n][m] != 'O') and ((m == x_enermy2) and (n == y_enermy2)))):
                        enermy_count += 1
                        if enermy_count > 2: 
                            enermy_count -= 1
            
            if output_count == 0:
                print('Out of rocket !!!')
                print(enermy_count, 'enermy(s) around')
                print(output_count, 'rockects left')
                print(enermy_left, 'enermy left')
                mapping[output_y][output_x] = 'X'
                show_map()
                break

            print('You missed')
            print(enermy_count, 'enermy(s) around')
            print(output_count, 'rockects left')
            print(enermy_left, 'enermy left')

        elif output_x == 3 and output_y == 3:
            for m in range(output_x - 1, output_x):
                for n in range(output_y - 1, output_y):
                    if (((mapping[n][m] != 'O') and ((m == x_enermy1) and (n == y_enermy1))) or ((mapping[n][m] != 'O') and ((m == x_enermy2) and (n == y_enermy2)))):
                        enermy_count += 1
                        if enermy_count > 2: 
                            enermy_count -= 1
                            
            if output_count == 0:
                print('Out of rocket !!!')
                print(enermy_count, 'enermy(s) around')
                print(output_count, 'rockects left')
                print(enermy_left, 'enermy left')
                mapping[output_y][output_x] = 'X'
                show_map()
                break

            print('You missed')
            print(enermy_count, 'enermy(s) around')
            print(output_count, 'rockects left')
            print(enermy_left, 'enermy left')

        elif output_x == 3 and output_y > 0 and output_y < 3:
            for m in range(output_x - 1, output_x):
                for n in range(output_y - 1, output_y + 2):
                    if (((mapping[n][m] != 'O') and ((m == x_enermy1) and (n == y_enermy1))) or ((mapping[n][m] != 'O') and ((m == x_enermy2) and (n == y_enermy2)))):
                        enermy_count += 1
                        if enermy_count > 2: 
                            enermy_count -= 1

            if output_count == 0:
                print('Out of rocket !!!')
                print(enermy_count, 'enermy(s) around')
                print(output_count, 'rockects left')
                print(enermy_left, 'enermy left')
                mapping[output_y][output_x] = 'X'
                show_map()
                break

            print('You missed')
            print(enermy_count, 'enermy(s) around')
            print(output_count, 'rockects left')
            print(enermy_left, 'enermy left')

        elif output_x == 3 and output_y == 2:
            for m in range(output_x - 1, output_x):
                for n in range(output_y - 1, output_y + 1):
                    if (((mapping[n][m] != 'O') and ((m == x_enermy1) and (n == y_enermy1))) or ((mapping[n][m] != 'O') and ((m == x_enermy2) and (n == y_enermy2)))):
                        enermy_count += 1
                        if enermy_count > 2: 
                            enermy_count -= 1
            
            if output_count == 0:
                print('Out of rocket !!!')
                print(enermy_count, 'enermy(s) around')
                print(output_count, 'rockects left')
                print(enermy_left, 'enermy left')
                mapping[output_y][output_x] = 'X'
                show_map()
                break

            print('You missed')
            print(enermy_count, 'enermy(s) around')
            print(output_count, 'rockects left')
            print(enermy_left, 'enermy left')

        elif output_x == 3 and output_y == 0:
            for m in range(output_x - 1, output_x):
                for n in range(output_y, output_y + 2):
                    if (((mapping[n][m] != 'O') and ((m == x_enermy1) and (n == y_enermy1))) or ((mapping[n][m] != 'O') and ((m == x_enermy2) and (n == y_enermy2)))):
                        enermy_count += 1
                        if enermy_count > 2: 
                            enermy_count -= 1
            
            if output_count == 0:
                print('Out of rocket !!!')
                print(enermy_count, 'enermy(s) around')
                print(output_count, 'rockects left')
                print(enermy_left, 'enermy left')
                mapping[output_y][output_x] = 'X'
                show_map()
                break

            print('You missed')
            print(enermy_count, 'enermy(s) around')
            print(output_count, 'rockects left')
            print(enermy_left, 'enermy left')

        elif output_x > 0 and output_x < 3 and output_y == 0:
            for m in range(output_x - 1, output_x + 2):
                for n in range(output_y, output_y + 2):
                    if (((mapping[n][m] != 'O') and ((m == x_enermy1) and (n == y_enermy1))) or ((mapping[n][m] != 'O') and ((m == x_enermy2) and (n == y_enermy2)))):
                        enermy_count += 1
                        if enermy_count > 2: 
                            enermy_count -= 1

            if output_count == 0:
                print('Out of rocket !!!')
                print(enermy_count, 'enermy(s) around')
                print(output_count, 'rockects left')
                print(enermy_left, 'enermy left')
                mapping[output_y][output_x] = 'X'
                show_map()
                break

            print('You missed')
            print(enermy_count, 'enermy(s) around')
            print(output_count, 'rockects left')
            print(enermy_left, 'enermy left')

        elif output_x == 2 and output_y == 0:
            for m in range(output_x - 1, output_x + 1):
                for n in range(output_y, output_y + 2):
                    if (((mapping[n][m] != 'O') and ((m == x_enermy1) and (n == y_enermy1))) or ((mapping[n][m] != 'O') and ((m == x_enermy2) and (n == y_enermy2)))):
                        enermy_count += 1
                        if enermy_count > 2: 
                            enermy_count -= 1

            if output_count == 0:
                print('Out of rocket !!!')
                print(enermy_count, 'enermy(s) around')
                print(output_count, 'rockects left')
                print(enermy_left, 'enermy left')
                mapping[output_y][output_x] = 'X'
                show_map()
                break

            print('You missed')
            print(enermy_count, 'enermy(s) around')
            print(output_count, 'rockects left')
            print(enermy_left, 'enermy left')

        mapping[output_y][output_x] = 'X'

    show_map()
    
    