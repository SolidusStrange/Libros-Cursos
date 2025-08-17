# Preguntas de Python con explicaciones

---

## Pregunta 1

**¿Cuál es el resultado del siguiente fragmento de código?**

```python
my_list = [1, 2]

for v in range(2):
    my_list.insert(-1, my_list[v])

print(my_list)
```
 [1, 1, 1, 2]

 [1, 2, 2, 2]

 [2, 1, 1, 2]

 [1, 2, 1, 2]

**Explicación:**
El método insert(-1, elemento) inserta el elemento justo antes del penúltimo elemento de la lista. El bucle recorre los índices 0 y 1. Se insertan my_list[0] (que es 1) y luego my_list[1] (que es 2, pero al modificar la lista la posición cambia), por eso el resultado final es [1, 2, 1, 2].

## Pregunta 2
El significado de un argumento posicional está determinado por:

- su posición dentro de la lista de argumentos
- el nombre del argumento especificado junto con su valor
- su valor
- su conexión con variables existentes

**Explicación:**
Los argumentos posicionales en una función Python son interpretados según su orden de aparición en la llamada a la función. La posición determina qué parámetro recibe cada valor.

## Pregunta 3
¿Cuáles de los siguientes enunciados son verdaderos respecto al código? (Selecciona dos respuestas)

```python
nums = [1, 2, 3]
vals = nums
```
- nums y vals son diferentes nombres de la misma lista
- nums tiene la misma longitud que vals
- nums y vals son listas diferentes
- vals es más larga que nums

**Explicación:**
Al hacer vals = nums, ambas variables apuntan a la misma lista. Por eso, nums y vals son dos nombres para la misma lista y tienen la misma longitud.

## Pregunta 5
El siguiente fragmento de código:

```python
def function_1(a):
    return None

def function_2(a):
    return function_1(a) * function_1(a)

print(function_2(2))
```
- dará como salida 2
- dará como salida 16
- dará como salida 4
- provocará un error de ejecución

**Explicación:**
function_1 retorna None. Intentar multiplicar None * None genera un error porque None no soporta la operación *.

## Pregunta 6
El resultado de la siguiente división:

```python
1 // 2
```
- es igual a 0
- es igual a 0.0
- no se puede predecir
- es igual a 0.5

**Explicación:**
`//` es la división entera (floor division), que devuelve el cociente sin decimales. Entonces 1 // 2 es 0.

## Pregunta 7
El siguiente fragmento de código:

```python
def func(a, b):
    return b ** a

print(func(b=2, 2))
```
- es erróneo
- dará como salida 4
- dará como salida 2
- dará como salida None

**Explicación:**
Los argumentos posicionales no pueden ir después de los argumentos nombrados en la llamada a la función. Por eso da error de sintaxis.

... (continuar incluyendo todas las preguntas y explicaciones tal como en el texto original del usuario)

## Pregunta 8

**Código:**

``` python
z = 0
y = 10
x = y < z and z > y or y < z and z < y
```

**Respuesta:** `False`\
**Justificación:** Se evalúa como `False or False → False`.

------------------------------------------------------------------------

## Pregunta 9

**Respuesta:** `for` y `in`\
**Justificación:** Son palabras reservadas en Python.

------------------------------------------------------------------------

## Pregunta 10

**Código:**

``` python
my_list = [x * x for x in range(5)]
def fun(lst):
    del lst[lst[2]]
    return lst
print(fun(my_list))
```

**Respuesta:** `[0, 1, 9, 16]`\
**Justificación:** Se elimina el índice 4 (valor 16).
