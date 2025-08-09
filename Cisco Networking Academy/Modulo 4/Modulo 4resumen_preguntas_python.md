# Resumen de Preguntas y Respuestas – Python Essentials

---

## Pregunta 2  
**Función con parámetro por defecto**  
```python
def function(x=0):
    return x
```

### Respuesta correcta:  
- Puede ser invocada sin ningún argumento.  
- Puede ser invocada con exactamente un argumento.  

### Explicación:  
El parámetro `x` tiene un valor por defecto `0`, por lo que si no se pasa argumento, se usa `0`. Si se pasa un argumento, se usa ese valor.  
Las otras opciones que dicen que debe ser invocada con exactamente un argumento o sin argumentos son falsas porque no es obligatorio pasar argumento.  

---

## Pregunta 3  
**Función integrada (built-in function)**  

### Respuesta correcta:  
- Viene con Python, y es una parte integral de Python.  

### Explicación:  
Las funciones integradas como `print()`, `len()`, `type()` están incluidas en Python y no requieren importación. No están ocultas ni agregadas por otros programadores.  

---

## Pregunta 4  
**Tuplas y tipos de secuencia**  

### Respuesta correcta:  
- Se pueden indexar y rebanar como las listas.  

### Explicación:  
Tuplas son inmutables, por eso no se pueden modificar ni extender ni eliminar elementos. Tampoco son listas, solo un tipo de secuencia similar.  

---

## Pregunta 5  
**Salida función recursiva**  
```python
def f(x):
    if x == 0:
        return 0
    return x + f(x - 1)

print(f(3))
```

### Respuesta correcta:  
- `6`  

### Explicación:  
La función suma `3 + 2 + 1 + 0 = 6` usando recursión.  

---

## Pregunta 6  
**Salida función con incremento**  
```python
def fun(x):
    x += 1
    return x

x = 2
x = fun(x + 1)
print(x)
```

### Respuesta correcta:  
- `4`  

### Explicación:  
Se llama a `fun(3)` (porque `x + 1 = 3`), dentro de la función `3 + 1 = 4`, que se retorna e imprime.  

---

## Pregunta 7  
**Impresión del contenido en diccionario con tuplas**  

### Respuesta correcta:  
- `print(k[0])`  

### Explicación:  
Los valores en el diccionario son tuplas con un solo elemento `(my_list[i], )`. Imprimir `k` muestra la tupla, con paréntesis y coma. Para imprimir solo el valor `'a'`, `'b'`, `'c'` se usa `k[0]`.  

---

## Pregunta 8  
**Función con parámetros faltantes**  
```python
def func(a, b):
    return a ** a

print(func(2))
```

### Respuesta correcta:  
- Es erróneo.  

### Explicación:  
La función espera 2 argumentos, pero solo se pasa 1, causando error de tipo `TypeError`.  

---

## Pregunta 9  
**Salida composición de funciones**  
```python
def func_1(a):
    return a ** a

def func_2(a):
    return func_1(a) * func_1(a)

print(func_2(2))
```

### Respuesta correcta:  
- `16`  

### Explicación:  
`func_1(2) = 4`, luego `func_2(2) = 4 * 4 = 16`.  

---

## Pregunta 10  
**Definición correcta de función con dos parámetros con valores por defecto**  

### Respuesta correcta:  
- `def fun(a=0, b=0):`  

### Explicación:  
La sintaxis correcta define parámetros separados con coma, cada uno con su valor por defecto. Las otras opciones no son válidas en Python.  

---

## Pregunta 11  
**Uso de None en Python**  

### Respuestas correctas:  
- El valor None puede ser asignado a variables.  
- El valor None puede ser comparado con otras variables.  

### Explicación:  
`None` representa la ausencia de valor, puede asignarse y compararse. No puede usarse en operaciones aritméticas y sí puede usarse fuera de funciones (no está restringido).  

---

## Pregunta 12  
**Salida función con retorno implícito None**  
```python
def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return

print(fun(fun(2)) + 1)
```

### Respuesta correcta:  
- El código provocará un error de tiempo de ejecución.  

### Explicación:  
`fun(2)` retorna 1, luego `fun(1)` retorna `None` porque no tiene retorno explícito. Sumar `None + 1` genera error.  

---

## Pregunta 13  
**Uso de variable global**  
```python
def fun(x):
    global y
    y = x * x
    return y

fun(2)
print(y)
```

### Respuesta correcta:  
- `4`  

### Explicación:  
La variable global `y` se asigna dentro de la función y puede usarse fuera.  

---

## Pregunta 14  
**Salida función con impresión y variable global**  
```python
def any():
    print(var + 1, end='')

var = 1
any()
print(var)
```

### Respuesta correcta:  
- `21`  

### Explicación:  
`any()` imprime `2` sin salto de línea, luego se imprime `1`.  

---

## Pregunta 15  
**Modificación ilegal en tupla**  
```python
my_tuple[1] = my_tuple[1] + my_tuple[0]
```

### Respuesta correcta:  
- Es ilegal.  

### Explicación:  
Las tuplas son inmutables, no permiten asignar valores a elementos.  

---

## Pregunta 16  
**Salida función que modifica lista pero no retorna**  
```python
my_list = ['Mary', 'had', 'a', 'little', 'lamb']

def my_list(my_list):
    del my_list[3]
    my_list[3] = 'ram'

print(my_list(my_list))
```

### Respuesta correcta:  
- No hay salida, el fragmento es erróneo (porque imprime `None`).  

### Explicación:  
La función no retorna valor, por lo que imprimir el resultado muestra `None`.  

---

## Pregunta 17  
**Salida función con parámetros posicionales y nombrados**  
```python
def fun(x, y, z):
    return x + 2 * y + 3 * z

print(fun(0, z=1, y=3))
```

### Respuesta correcta:  
- `9`  

### Explicación:  
El cálculo es `0 + 2*3 + 3*1 = 9`.  

---

## Pregunta 18  
**Salida función con parámetros por defecto y argumento nombrado**  
```python
def fun(inp=2, out=3):
    return inp * out

print(fun(out=2))
```

### Respuesta correcta:  
- `4`  

### Explicación:  
`inp` usa valor por defecto `2`, `out=2` se pasa, resultado `2*2=4`.  

---

## Pregunta 19  
**Cadena de referencias en diccionario**  
```python
dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dictionary['one']

for k in range(len(dictionary)):
    v = dictionary[v]

print(v)
```

### Respuesta correcta:  
- `two`  

### Explicación:  
Se sigue la cadena: `'one' -> 'two' -> 'three' -> 'one' -> 'two'`. Después de 3 iteraciones queda `'two'`.  

---

## Pregunta 20  
**Slices y acceso a tuplas**  
```python
tup = (1, 2, 4, 8)
tup = tup[1:-1]
tup = tup[0]
print(tup)
```

### Respuesta correcta:  
- `2`  

### Explicación:  
`[1:-1]` da `(2, 4)`, luego `[0]` da `2`.  

---

## Pregunta 21  
**Sentencias verdaderas sobre try-except**  

### Respuestas correctas (selecciona dos):  
- El código que sigue a la sentencia except será ejecutado si el código en el bloque try se encuentra con un error.  
- Si sospechas que un fragmento de código puede generar una excepción, se debe colocar dentro del bloque try.  

### Explicación:  
`except` maneja excepciones en `try`. Errores de sintaxis no se manejan con `except`. El código dentro de `except` que genera error no es manejado automáticamente.  
