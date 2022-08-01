#chess

board = [[' ' for j in range(8)] for i in range(8)]

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
    
#begin
reset_board()
while 1:
    draw_board()
    print ("Input move (e.g. a2a4 )")
    move = input();
    
    x = letter2num(move[0],'a')
    y = letter2num(move[1],'1')
    
    x1 = letter2num(move[2],'a')
    y1 = letter2num(move[3],'1')
    
    board[x1][y1] = board[x][y]
    board[x][y] = 
