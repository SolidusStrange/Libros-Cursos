import random

tablero = [
    [1, 2, 3],
    [4, "X", 6],
    [7, 8, 9]
]

def imprimir_tablero(matriz):
    print("+-------+-------+-------+")
    for fila in matriz:
        print("|       |       |       |")
        print("|" + "|".join(f" {str(valor).center(5)} " for valor in fila) + "|")
        print("|       |       |       |")
        print("+-------+-------+-------+")

# imprimir_tablero(tablero)

def movimiento(usuario, matriz):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == usuario:
                matriz[fila][columna] = "O" # Si es así, reemplazar por "X" y salir de la función
                return True # movimiento válido

    print("El movimiento ingresado no es válido. Intente nuevamente") #Si no fue válido, salta el return y pasa a imprimir este msj
    return False #Retorna false para el IF que evalua

def maquina_movimiento(matriz):
    # maquina = random.choice(tablero)
    disponibles = [] #Buscar todos los valores que sean números (casillas libres)
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if isinstance(matriz[fila][columna], int): # solo números libres
                disponibles.append((fila, columna))
            
    #Elegir una posición al azar
    if disponibles: #disponibles guarda tuplas (fila, columna) de todas las casillas libres.
        fila, columna = random.choice(disponibles) #elige una de esas posiciones
        matriz[fila][columna] = "X"
        return True
    return False

def revisar_ganador(matriz):
    for fila in range(3):
        if all(valor == "X" for valor in matriz[fila]):
            print(F"Fila {fila+1} completa con X")

    for columna in range(3):
        if all(matriz[fila][columna] == "X" for fila in range(3)):
            print(f"Columna {columna+1} completa en X")
        
    if all(matriz[i][i] == "X" for i in range(3)): #[0][0], [1][1], [2][2]
        print("Diagonal principal completa con X")

    #posiciones [0][2], [1][1], [2][0]
    if all(matriz[i][2-i] == "X" for i in range(3)):
        print("Diagonal secundaria completa con X")
        
        
revisar_ganador(tablero)

# while True:
#     usuario = int(input("Ingrese un movimiento válido: "))
#     if movimiento(usuario, tablero):
#         imprimir_tablero(tablero)
#         break



