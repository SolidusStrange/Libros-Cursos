## 2.6.12 RESUMEN DE LA SECCIÓN: FUNCIONES print() E input()

### 1. Comunicación con el usuario

- La función `print()` envía datos a la consola.
- La función `input()` obtiene datos desde la consola.

### 2. El parámetro opcional de input()

La función `input()` acepta un **parámetro opcional**, que es una **cadena de texto para mostrar como mensaje** antes de que el usuario escriba algo.

```python
name = input("Ingresa tu nombre: ")
print("Hola, " + name + ". ¡Un gusto conocerte!")
```

### 3. Funcionamiento de input(): pausa del flujo

Cuando se llama a `input()`, el **flujo del programa se detiene** hasta que el usuario ingresa un dato y presiona la tecla **Enter**.

💡 **Nota:**  
En plataformas como Edube, el tiempo de ejecución está limitado por razones de optimización, por lo que si no ingresas nada en unos segundos, el programa se detendrá automáticamente. Sin embargo, en IDLE u otro entorno local, el programa **esperará indefinidamente**.

👉 Esta característica puede usarse para **esperar que el usuario cierre el programa manualmente**:

```python
name = input("Ingresa tu nombre: ")
print("Hola, " + name + ". ¡Un gusto conocerte!")

print("\nPresiona Enter para finalizar el programa.")
input()
print("FIN.")
```

### 4. input() siempre devuelve una cadena

La función `input()` **devuelve una cadena de texto (string)**. Si se usan operadores como `+`, se concatenan como texto:

```python
num_1 = input("Ingresa el primer número: ")  # Ejemplo: 12
num_2 = input("Ingresa el segundo número: ") # Ejemplo: 21

print(num_1 + num_2)  # Salida: 1221 (no suma, concatena)
```

### 5. Replicación de cadenas

También puedes **multiplicar cadenas** usando el operador `*`, lo que genera una **repetición** del texto:

```python
my_input = input("Escribe algo: ")  # Ejemplo: hola
print(my_input * 3)  # Salida: holaholahola
```

---
