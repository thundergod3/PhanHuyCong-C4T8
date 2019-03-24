from random import *
board = [["_","_","_","_"],["_","_","_","_"],["_","_","_","_"],["_","_","_","_"]]
number = ["1","2","3","4","5","6","7","8","9","10"]
#Random_Position
_loop_position = True
while (_loop_position):
    a_bom1 = randint(0,3)
    b_bom1 = randint(0,3)
    a_bom2 = randint(0,3)
    b_bom2 = randint(0,3)
    a_bom3 = randint(0,3)
    b_bom3 = randint(0,3)
    if (a_bom1 != a_bom2 and a_bom1 != a_bom3 and b_bom1 != b_bom2 and b_bom1 != b_bom3 and a_bom2 != a_bom3 and b_bom2 != b_bom3):
        x_bom1 = a_bom1
        y_bom1 = b_bom1
        x_bom2 = a_bom2
        y_bom2 = b_bom2
        x_bom3 = a_bom3
        y_bom3 = b_bom3
        # board[a_bom1][b_bom1] = "B"
        # board[a_bom2][b_bom2] = "B"
        # board[a_bom3][b_bom3] = "B"
        _loop_position = False


#-----------------------------------------------------
print("Welcome To The Game! Press Q to Quit game....")
_win = 0
_loopchose = True
_lose = False
_loop = True
_flag = True
while ( _loop ):
    _countflag = 0
    for x in range(0,4):
        for y in range(0,4):
            print(board[x][y],end=" ")
            if (board[x][y] == "_"):
                _countflag += 1
        print(" ")
    _countflag = _countflag - 3

    #Condition Win
    if (_countflag == 0):
        print("You Win!!!")
        break

    #Position Boom
    print(y_bom1+1," ",x_bom1+1)
    print(y_bom2+1," ",x_bom2+1)
    print(y_bom3+1," ",x_bom3+1)

    #Input
    print ("Nhập tọa độ X/Y: ")
    choice_yy = input("X: ")
    while(True):
        if choice_yy in number:
            choice_y = int(choice_yy)
            while (choice_y < 0 or choice_y > 4):
                choice_y = int(input("X: "))
            choice_y = choice_y - 1
            break
        else:
            choice_yy = input("X: ")

    choice_xx = input("Y: ")
    while(True):
        if choice_xx in number:
            choice_x = int(choice_xx)
            while (choice_x < 0 or choice_x > 4):
                choice_x = int(input("Y: "))
            choice_x = choice_x - 1
            break
        else:
            choice_xx = input("Y: ")

    #Condition Lose
    if ( (choice_x == x_bom1 and choice_y == y_bom1) or (choice_x == x_bom2 and choice_y == y_bom2) or (choice_x == x_bom3 and choice_y == y_bom3) ):
        print("BOOM! You Lose!")
        break
    else:
        count = 0
        for i in range(choice_x - 1,choice_x + 2):
            for j in range(choice_y - 1, choice_y + 2):
                if (( i == x_bom1 and j == y_bom1) or (i == x_bom2 and j == y_bom2) or (i == x_bom3 and j == y_bom3)):
                    count += 1
        board[choice_x][choice_y] = count