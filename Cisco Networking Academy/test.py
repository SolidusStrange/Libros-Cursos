lista_inicial = [
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

# imprimir_tablero(lista_inicial)

def movimiento(usuario, matriz):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == usuario:
                matriz[fila][columna] = "O" # Si es así, reemplazar por "X" y salir de la función
                return True # movimiento válido

    print("El movimiento ingresado no es válido") #Si no fue válido, salta el return y pasa a imprimir este msj
    return False #Retorna false para el IF que evalua


usuario = int(input("Ingrese un movimiento válido"))
if movimiento(usuario, lista_inicial):
    imprimir_tablero(lista_inicial)



