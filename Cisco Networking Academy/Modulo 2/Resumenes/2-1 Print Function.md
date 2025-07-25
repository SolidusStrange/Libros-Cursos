
# Notas sobre la función `print()` en Python

## 1. Función `print()`

La función `print` es una función incorporada que imprime o envía un mensaje específico a la pantalla o ventana de la consola.

### Ejemplo:
```python
print("Hola mundo")
```

## 2. Funciones incorporadas

Las funciones incorporadas, a diferencia de las funciones definidas por el usuario, siempre están habilitadas y no necesitan ser importadas.  
Python 3.8 incluye **69 funciones incorporadas**. Puedes ver la lista completa en orden alfabético en la biblioteca estándar de Python:

🔗 [Funciones incorporadas en Python 3](https://docs.python.org/3/library/functions.html)

## 3. Llamadas a funciones

Para **llamar una función** (también conocido como *invocación de función*), debes usar el **nombre de la función** seguido de paréntesis.

- Puedes pasar **argumentos** dentro de los paréntesis, separados por comas.
- Una función `print()` vacía imprimirá una línea en blanco en la pantalla.

### Ejemplo:
```python
print("Hola", "Mundo")
print()  # Línea vacía
```

## 4. Strings en Python

Los **strings** en Python se delimitan con comillas:

- Comillas dobles: `"I am a string"`
- Comillas simples: `'I am a string, too'`

### Ejemplo:
```python
print("Esto es un string")
print('Esto también es un string')
```

## 5. Instrucciones en un programa

Un **programa de computadora** es una colección de instrucciones.  
Una **instrucción** es un comando que realiza una tarea específica cuando se ejecuta, como imprimir un mensaje en la pantalla.

### Ejemplo:
```python
print("Instrucción 1")
print("Instrucción 2")
```

## 6. Caracteres especiales

En los strings, el **backslash** (`\`) es un **carácter especial** que modifica el significado del siguiente carácter.  
Por ejemplo:

- `\n` representa un **salto de línea**.

### Ejemplo:
```python
print("Hola\nMundo")  # imprime: Hola
Mundo (con doble backslash)
print("Hola
Mundo")   # imprime:
# Hola
# Mundo
```

## 7. Argumentos posicionales

Los **argumentos posicionales** son aquellos cuyo **significado depende de su posición**.

### Ejemplo:
```python
print("Primero", "Segundo", "Tercero")
```

## 8. Argumentos con palabras clave (Keyword Arguments)

Los **Keyword Arguments** no dependen de su posición, sino de una **clave especial** que los identifica.

### Ejemplo:
```python
print("Hola", "Mundo", sep="-", end="!!!\n")
```

## 9. Parámetros `sep` y `end` en `print()`

- `sep`: Especifica el **separador** entre los argumentos.
- `end`: Especifica lo que se imprimirá **al final** de la instrucción `print`.

### Ejemplos:
```python
print("H", "E", "L", "L", "O", sep="-")  # H-E-L-L-O
print("Hola", end="!!!\n")             # Hola!!!
```
