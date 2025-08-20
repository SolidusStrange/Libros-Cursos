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




