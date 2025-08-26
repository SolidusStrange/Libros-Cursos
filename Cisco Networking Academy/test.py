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
    try:
        usuario = int(usuario)
    except ValueError:
        print("Debe ingresar un número válido.")
        return False

    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == usuario:
                matriz[fila][columna] = "O"
                return True

    print("El movimiento ingresado no es válido. Intente nuevamente.")
    return False

def maquina_movimiento(matriz):
    disponibles = []
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if isinstance(matriz[fila][columna], int):
                disponibles.append((fila, columna))

    if disponibles:
        fila, columna = random.choice(disponibles)
        matriz[fila][columna] = "X"
        return True
    return False

def revisar_ganador(matriz, simbolo):
    for fila in range(3): #Recorre cada fila.
        temporal = []
        for valor in matriz[fila]:
            temporal.append(valor == simbolo) #temporal se llena con True/False dependiendo si cada valor coincide.
        if all(temporal): #all(temporal) confirma si toda la fila está ocupada por el mismo símbolo.
            print(f"Fila {fila+1} completa con {simbolo}")
            return True

    for columna in range(len(matriz[0])): #Recorre cada columna y verifica igual que con las filas.
        temporal = []
        for valor in range(len(matriz)):
            temporal.append(matriz[valor][columna] == simbolo)
        if all(temporal):
            print(f"Columna {columna+1} completa con {simbolo}")
            return 
        
    # Diagonal izquierda (0,0) (1,1) (2,2)
    temporal = []
    for fila in range(len(matriz)):
        temporal.append(matriz[fila][fila] == simbolo)

    if all(temporal):
        print(f"Diagonal izquierda completa con {simbolo}")
        return True

    # Diagonal derecha (0,2) (1,1) (2,0)
    temporal = []
    for fila in range(len(matriz)): #(0.2) (1,1) (2.0)
        temporal.append(matriz[fila][len(matriz) - fila - 1] == simbolo)

    if all(temporal):
        print(f"Diagonal derecha completa con {simbolo}")
        return True

    return False

# --- Bucle principal ---
while True:
    imprimir_tablero(tablero)

    # Movimiento jugador
    usuario = input("Ingrese su movimiento (número de casilla): ")
    if not movimiento(usuario, tablero):
        continue  # si no fue válido, vuelve a pedir
    
    # Revisar si ganó el jugador
    if revisar_ganador(tablero, "O"):
        imprimir_tablero(tablero)
        print("¡El jugador ganó!")
        break

    # Movimiento máquina
    if not maquina_movimiento(tablero):
        imprimir_tablero(tablero)
        print("¡Empate!")
        break

    # Revisar si ganó la máquina
    if revisar_ganador(tablero, "X"):
        imprimir_tablero(tablero)
        print("¡La máquina ganó!")
        break
    
    # Revisar empate después del turno del jugador
    if tablero_lleno(tablero):
        imprimir_tablero(tablero)
        print("¡Empate!")
        break




