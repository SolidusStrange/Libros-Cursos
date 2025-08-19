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

def revisar_ganador(matriz, simbolo):
    # Revisar filas
    for fila in range(3):
        if all(valor == simbolo for valor in matriz[fila]):
            print(f"Fila {fila+1} completa con {simbolo}")
            return True

    # Revisar columnas
    for columna in range(3):
        if all(matriz[fila][columna] == simbolo for fila in range(3)):
            print(f"Columna {columna+1} completa con {simbolo}")
            return True

    # Revisar diagonal principal
    if all(matriz[i][i] == simbolo for i in range(3)):
        print(f"Diagonal principal completa con {simbolo}")
        return True

    # Revisar diagonal secundaria
    if all(matriz[i][2-i] == simbolo for i in range(3)):
        print(f"Diagonal secundaria completa con {simbolo}")
        return True

    return False
        
if revisar_ganador(tablero, "X"):
    print("¡La máquina ganó!")
elif revisar_ganador(tablero, "O"):
    print("¡El jugador ganó!")

# while True:
#     usuario = int(input("Ingrese un movimiento válido: "))
#     if movimiento(usuario, tablero):
#         imprimir_tablero(tablero)
#         break



