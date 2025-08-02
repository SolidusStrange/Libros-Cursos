EMPTY = ". "
WHITE_PAWN = "WP"
WHITE_ROOK = "WR"
WHITE_KNIGHT = "WN"
WHITE_BISHOP = "WB"
WHITE_QUEEN = "WQ"
WHITE_KING = "WK"

BLACK_PAWN = "BP"
BLACK_ROOK = "BR"
BLACK_KNIGHT = "BN"
BLACK_BISHOP = "BB"
BLACK_QUEEN = "BQ"
BLACK_KING = "BK"

# Crear filas
row8 = [BLACK_ROOK, BLACK_KNIGHT, BLACK_BISHOP, BLACK_QUEEN,
        BLACK_KING, BLACK_BISHOP, BLACK_KNIGHT, BLACK_ROOK]
row7 = [BLACK_PAWN] * 8
row6 = [EMPTY] * 8
row5 = [EMPTY] * 8
row4 = [EMPTY] * 8
row3 = [EMPTY] * 8
row2 = [WHITE_PAWN] * 8
row1 = [WHITE_ROOK, WHITE_KNIGHT, WHITE_BISHOP, WHITE_QUEEN,
        WHITE_KING, WHITE_BISHOP, WHITE_KNIGHT, WHITE_ROOK]

# Crear el tablero
chessboard = [row8, row7, row6, row5, row4, row3, row2, row1]

# Imprimir con dos for anidados
for row in chessboard:
    for square in row:
        print(square, end=" ")
    print()  # Salto de línea al final de cada fila

