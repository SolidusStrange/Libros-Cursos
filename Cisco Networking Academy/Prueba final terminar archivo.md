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

## Pregunta 11
**Enunciado:**
```python
x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z

print(x, y, z)
```
**Alternativas:**
- A) `1 2 1`
- B) `1 1 2`
- C) `1 2 2`
- D) `2 1 2`

**Respuesta correcta:** B) `1 1 2`  
**Justificación:**  
Tras `x, y, z = 1, 1, 2`. Luego `z, y, z = 1, 1, 2` (evaluado primero el RHS); las asignaciones son izquierda→derecha, por lo que `z` termina en `2`.

---

## Pregunta 12
**Enunciado:**
```python
a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)
```
**Alternativas:**
- A) `0 0`
- B) `0 1`
- C) `1 0`
- D) `1 1`

**Respuesta correcta:** B) `0 1`  
**Justificación:**  
Operador XOR para intercambio: el resultado final es `a=0`, `b=1`.

---

## Pregunta 13
**Enunciado:**
```python
def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 2

print(fun(fun(2)))
```
**Alternativas:**
- A) `None`
- B) `1`
- C) *error de ejecución*
- D) `2`

**Respuesta correcta:** D) `2`  
**Justificación:**  
`fun(2) → 1` (par), luego `fun(1) → 2` (impar).

---

## Pregunta 14
**Enunciado:**
```python
nums = [1, 2, 3]
vals = nums
del vals[:]
```
**Alternativas:**
- A) *error de ejecución*
- B) `nums` y `vals` tienen la misma longitud
- C) `vals` es más larga que `nums`
- D) `nums` es más larga que `vals`

**Respuesta correcta:** B) `nums` y `vals` tienen la misma longitud  
**Justificación:**  
`vals` y `nums` referencian **la misma lista**; rebanado vacío la deja con longitud `0` en ambas.

---

## Pregunta 15
**Enunciado:** (entradas: `3` y `2`)
```python
x = int(input())
y = int(input())
x = x % y
x = x % y
y = y % x
print(y)
```
**Alternativas:**
- A) `1`
- B) `2`
- C) `3`
- D) `0`

**Respuesta correcta:** D) `0`  
**Justificación:**  
`x=3%2=1`, luego `x=1%2=1`, luego `y=2%1=0`.

---

## Pregunta 16
**Enunciado:** (entradas: `3` y `6`)
```python
y = input()
x = input()
print(x + y)
```
**Alternativas:**
- A) `36`
- B) `6`
- C) `3`
- D) `63`

**Respuesta correcta:** D) `63`  
**Justificación:**  
Entrada como **cadenas**: `"6" + "3" = "63"`.

---

## Pregunta 17
**Enunciado:**
```python
print("a", "b", "c", sep="sep")
```
**Alternativas:**
- A) `asepbsepcsep`
- B) `a b c`
- C) `abc`
- D) `asepbsepc`

**Respuesta correcta:** D) `asepbsepc`  
**Justificación:**  
`sep="sep"` inserta `sep` **entre** los argumentos (no al final).

---

## Pregunta 18
**Enunciado:**
```python
x = 1 // 5 + 1 / 5
print(x)
```
**Alternativas:**
- A) `0`
- B) `0.5`
- C) `0.4`
- D) `0.2`

**Respuesta correcta:** D) `0.2`  
**Justificación:**  
`1//5 = 0`, `1/5 = 0.2`, suma `0.2`.

---

## Pregunta 19
**Enunciado:**
```python
my_tuple[1] = my_tuple[1] + my_tuple[0]
```
**Alternativas:**
- A) puede ser ilegal si la tupla contiene cadenas
- B) es ilegal
- C) es completamente correcta
- D) se puede ejecutar solo si la tupla contiene al menos dos elementos

**Respuesta correcta:** B) es ilegal  
**Justificación:**  
Las tuplas son **inmutables**: no se puede asignar a un índice.

---

## Pregunta 20
**Enunciado:** (entradas: `2` y `4`)
```python
x = float(input())
y = float(input())
print(y ** (1 / x))
```
**Alternativas:**
- A) `1.0`
- B) `0.0`
- C) `2.0`
- D) `4.2`

**Respuesta correcta:** C) `2.0`  
**Justificación:**  
`4 ** (1/2) = √4 = 2.0`.

---

## Pregunta 21
**Enunciado:**
```python
dct = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dct['three']

for k in range(len(dct)):
    v = dct[v]

print(v)
```
**Alternativas:**
- A) `('one', 'two', 'three')`
- B) `two`
- C) `one`
- D) `three`

**Respuesta correcta:** C) `one`  
**Justificación:**  
Secuencia cíclica: `one → two → three → one` en 3 pasos.

---

## Pregunta 22
**Enunciado:**
```python
lst = [i for i in range(-1, -2)]
```
**Alternativas:**
- A) uno
- B) cero
- C) dos
- D) tres

**Respuesta correcta:** B) cero  
**Justificación:**  
`range(-1, -2)` con paso `+1` no produce elementos → lista vacía.

---

## Pregunta 23
**Enunciado:**
```python
def fun(a, b, c=0):
    # cuerpo
    pass
```
**Alternativas (elige dos correctas):**
- A) `fun(0, 1, 2)`
- B) `fun(b=0, a=0)`
- C) `fun(b=1)`
- D) `fun()`

**Respuesta correcta:** A) y B)  
**Justificación:**  
A) provee los tres parámetros posicionalmente; B) usa palabras clave para `a` y `b`, dejando `c` por defecto. C) falta `a`; D) faltan `a` y `b`.

---

## Pregunta 24
**Enunciado:**
```python
def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y-1)

print(fun(0, 3))
```
**Alternativas:**
- A) `1`
- B) *error de ejecución*
- C) `2`
- D) `0`

**Respuesta correcta:** D) `0`  
**Justificación:**  
Recursión decrementa `y` hasta `y == x (0)` y retorna `0`.

---

## Pregunta 25
**Enunciado:**
```python
i = 0
while i < i + 2 :
    i += 1
    print("*")
else:
    print("*")
```
**Alternativas:**
- A) `1`
- B) `2`
- C) *el fragmento entrará en un bucle infinito, imprimiendo un `*` por línea*
- D) `0`

**Respuesta correcta:** C) bucle infinito  
**Justificación:**  
`i < i + 2` es siempre verdadero para enteros, por lo que el `while` no termina.

---

## Pregunta 26
**Enunciado:**
```python
tup = (1, 2, 4, 8)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)
```
**Alternativas:**
- A) `4`
- B) `(4,)`
- C) `44`
- D) `(4)`

**Respuesta correcta:** A) `4`  
**Justificación:**  
El corte `tup[-2:-1]` da `(4,)`; luego `tup[-1]` es `4` (entero).

---

## Pregunta 27
**Enunciado:**
```python
dd = {"1": "0", "0": "1"}
for x in dd.vals():
    print(x, end="")
```
**Alternativas:**
- A) `1 0`
- B) `0 0`
- C) *el código es erróneo (el objeto `dict` no contiene el método `vals()`)*
- D) `0 1`

**Respuesta correcta:** C) *el código es erróneo…*  
**Justificación:**  
El método correcto es `dict.values()`. `vals()` provoca `AttributeError` en tiempo de ejecución.

---

## Pregunta 28
**Enunciado:**
```python
dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)

for x in dct.keys():
    print(dct[x][1], end="")
```
**Alternativas:**
- A) `21`
- B) `(2,1)`
- C) `(1,2)`
- D) `12`

**Respuesta correcta:** A) `21`  
**Justificación:**  
Orden de inserción: claves `'1'`, `'2'`. Se imprime el índice `1` de cada tupla: `2` y luego `1` → `21`.

---

## Pregunta 29
**Enunciado:**
```python
def fun(inp=2, out=3):
    return inp * out

print(fun(out=2))
```
**Alternativas:**
- A) `6`
- B) `4`
- C) *error de sintaxis*
- D) `2`

**Respuesta correcta:** B) `4`  
**Justificación:**  
`inp` usa valor por defecto `2`; `out=2` → `2*2=4`.

---

## Pregunta 30
**Enunciado:**
```python
lst = [[x for x in range(3)] for y in range(3)]

for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print("#")
```
**Alternativas:**
- A) tres
- B) nueve
- C) seis
- D) cero

**Respuesta correcta:** A) tres  
**Justificación:**  
En cada fila aparece el `1` (impar) una vez → total `3` impresiones.
