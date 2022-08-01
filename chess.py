#chess

board = [[' ' for j in range(8)] for i in range(8)]

startpieces = ['R','N','B','K','Q','B','N','R']
pawnrow = ['P','P','P','P','P','P','P','P']

#copy because python normally just refs
board[0] = startpieces.copy()
board[1] = pawnrow.copy()
board[6] = pawnrow.copy()
board[7] = startpieces.copy()

def letter2num (n):
    return (ord(n) - ord('a'))

def xaxis (n):
    return(ord ('8') - ord(n))

while 1:
    for row in board:
        print(row)
    print ("Input move:")
    move = input();
    
    y = letter2num(move[0])
    x = xaxis(move[1])
    
    y1 = letter2num(move[2])
    x1 = xaxis(move[3])
     
    board[x1][y1] = board[x][y]
    board[x][y] = ' '
    



