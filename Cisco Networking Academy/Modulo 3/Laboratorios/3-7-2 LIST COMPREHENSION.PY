#COMPRENSIÓN DE LISTA

print("EJEMPLO 1: ")
white_pawn = "*"
row = [white_pawn for i in range(8)]
print(row)

print("EJEMPLO 2: ")
squares = [x ** 2 for x in range(10)]
print(squares)

print("EJEMPLO 3: ")
twos = [2 ** i for i in range(8)]
print(twos)

print("EJEMPLO 4: ")
odds = [x for x in squares if x % 2 != 0]
print(odds)

