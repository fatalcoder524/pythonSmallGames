board=[[' ' for i in range(0,3)]for j in range(0,3)]

def move(player,i,j):
    if(player==1):
        if(i<3 and j<3 and board[i][j]==' '):
            board[i][j]='X'
            if(checkWinner(player)):
                print("Player 1 Wins!")
                exit(0);
        else:
            print('Invalid Move. Try again!!!')
            play(1)
    else:
        if(i<3 and j<3 and board[i][j]==' '):
            board[i][j]='O'
            if(checkWinner(player)):
                print("Player 2 Wins!")
                exit(0);
        else:
            print('Invalid Move. Try again!!!')
            play(2)

def checkWinner(player):
    cnt=0
    for i in range(0,3):
        for j in range(0,3):
            if(board[i][j]==' '):
                cnt+=1
    if(cnt==0):
        print("Game Tie!!!")
        exit(0)
    if(player==1):
        i,j=0,0
        if(board[i+1][j+1]==board[i+2][j+2]==board[i][j]=='X'):
            return 1
        i,j=2,0
        if(board[i-1][j+1]==board[i-2][j+2]==board[i][j]=='X'):
            return 1
        for i in range(0,3):
            j=0
            if(board[i][j+1]==board[i][j+2]==board[i][j]=='X'):
                return 1
            else:
                return 0
        for j in range(0,3):
            i=0
            if(board[i+1][j]==board[i+2][j]==board[i][j]=='X'):
                return 1
            else:
                return 0
    else:
        i,j=0,0
        if(board[i+1][j+1]==board[i+2][j+2]==board[i][j]=='O'):
            return 1
        i,j=2,0
        if(board[i-1][j+1]==board[i-2][j+2]==board[i][j]=='O'):
            return 1
        for i in range(0,3):
            j=0
            if(board[i][j+1]==board[i][j+2]==board[i][j]=='O'):
                return 1
            else:
                return 0
        for j in range(0,3):
            i=0
            if(board[i+1][j]==board[i+2][j]==board[i][j]=='O'):
                return 1
            else:
                return 0

def printBoard():
    print("+- - -+")
    print("|"+ board[0][0] + '|' + board[0][1] + '|' + board[0][2]+"|")
    print("+- - -+")
    print("|"+ board[1][0] + '|' + board[1][1] + '|' + board[1][2]+"|")
    print("+- - -+")
    print("|"+ board[2][0] + '|' + board[2][1] + '|' + board[2][2]+"|")
    print("+- - -+")

def play(player):
    print("Player {}: Enter i,j value:-".format(player))
    i,j=map(int,input().split())
    move(player,i,j)

while True:
    play(1)
    printBoard()
    play(2)
    printBoard()
