board = []
EMPTY = ""
  
for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)



board = [[[j,i]for i in range(8)] for j in range(8)] #ANIDADA

board[0][0] = "ROOK"
board[0][7] = "ROOK"
board[7][0] = "ROOK"
board[7][7] = "ROOK"

for number in board: print(number)