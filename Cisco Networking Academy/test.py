# board= [[i for i in range(1,10)] for j in range(1,10)]
# print(board)

board = []
counter = 1

board = [["X" for i in range(3)] for j in range(3)]

counter = 0
for i in range(3):
    for j in range(3):
        counter += 1
        board[i][j] = counter
print(board)

for r in board:
    print(r)

print("+-------+\n|\n|\n|\n+-------+")  