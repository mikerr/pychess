# simplechess

board = [[' ' for j in range(8)] for i in range(8)]
moves = []

def reset_board() :
    blackpcs = ['R','N','B','K','Q','B','N','R']
    whitepcs = ['r','n','b','k','q','b','n','r']
    
    for x in range(8) :
        board[x][0] = blackpcs[x]
        board[x][1] = 'P'
        board[x][6] = 'p'
        board[x][7] = whitepcs[x]
        
def draw_board() :
    for i in range(8):
        for j in range(8):
            print (board[j][7-i],end=' ')
        print ("")
        
def letter2num (n,m):
    return (ord(n) - ord(m))

def occupied (x,y) :
    if (board[x][y] != ' ') : return True
    else : return False

def addmove(x,y) :
    if occupied(x,y) == False :
        moves.append((x,y))

def whitepawn():
    # up one
    addmove(x,y+1)
    # up two on first move
    if y == 1 : addmove(x,y+2) 
    # diagonal only if destination is occupied i.e. taking)
    if occupied(x-1,y+1) == True : moves.append((x-1,y+1))
    if occupied(x-1,y+1) == True : moves.append((x+1,y+1))
    
def blackpawn():
    # up one
    addmove(x,y-1)
    # up two on first move
    if y == 6 : addmove(x,y-2) 
    # diagonal only if destination is occupied i.e. taking)
    if occupied(x-1,y-1) == True : moves.append((x-1,y-1))
    if occupied(x-1,y-1) == True : moves.append((x+1,y-1))

def rook(x,y):
    # horizontal 
    for x1 in range(x,8):
        addmove(x1,y)
    for x1 in range(0,x):
        addmove(x1,y)
    # vertical
    for y1 in range(0,y):
        addmove(x,y1)
    for y1 in range(y,8):
        addmove(x,y1)
    
def knight():
    addmove(x,y)
    
def bishop(x,y):
    #NE
    x1 = x
    y1 = y
    while (x1 < 7 and y1 < 7):
        x1 += 1
        y1 += 1
        addmove(x1,y1)
    #NW
    x1 = x
    y1 = y
    while (x1 > 0 and y1 < 7):
        x1 -= 1
        y1 += 1
        addmove(x1,y1)
    #SE
    x1 = x
    y1 = y
    while (x1 < 7 and y1 > 0):
        x1 += 1
        y1 -= 1
        addmove(x1,y1)    
    #SW
    x1 = x
    y1 = y
    while (x1 > 0 and y1 > 0):
        x1 -= 1
        y1 -= 1
        addmove(x1,y1)
    
def king():
    addmove(x,y)
def queen(x,y):
    #queen combines rook and bishop moves
    rook(x,y)
    bishop(x,y)

#begin
reset_board()
while 1:
    draw_board()
    print ("Input move (e.g. a2a4 )")
    imove = input();
    
    x = letter2num(imove[0],'a')
    y = letter2num(imove[1],'1')
    
    movex = letter2num(imove[2],'a')
    movey = letter2num(imove[3],'1')
    playermove = (movex,movey)
    
    moves = []
    
    piece = board[x][y]
    if piece == 'P' : whitepawn()
    if piece == 'p' : blackpawn()
    
    piece = piece.upper()
    if piece == 'R' : rook(x,y)
    if piece == 'N' : knight(x,y)
    if piece == 'B' : bishop(x,y)
    if piece == 'K' : king(x,y)
    if piece == 'Q' : queen(x,y)
        
    if playermove in moves: allowed = True
    else : allowed = False
    
    if allowed == False:
        print ("illegal move")
    else :
        board[movex][movey] = board[x][y]
        board[x][y] = ' '
