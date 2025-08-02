
# 🐍 Quiz de Python - 20 Preguntas con Respuestas y Explicaciones

Este repositorio contiene un pequeño quiz de 20 preguntas sobre fundamentos de Python. Las respuestas correctas están marcadas junto a una breve explicación de por qué son correctas.

---

## Pregunta 1

**¿Un operador que puede verificar si dos valores son iguales se codifica como?**  
✅ `==`  
🔎 *El operador `==` compara si dos valores son iguales. Un solo `=` se usa para asignación.*

---

## Pregunta 2

**¿El valor asignado finalmente a `x` es igual a?:**
```python
x = 1
x = x == x
```
✅ `True`  
🔎 *`x == x` evalúa a `True`, ya que `1 == 1`. Luego, `x` se asigna a `True`.*

---

## Pregunta 3

**¿Cuántos `*` enviará el siguiente fragmento a consola?**
```python
i = 0
while i <= 3 :
    i += 2
    print("*")
```
✅ `2`  
🔎 *El bucle se ejecuta dos veces: cuando `i = 2` y `i = 4`.*

---

## Pregunta 4

**¿Cuántos `*` enviará este código a consola?**
```python
i = 0
while i <= 5:
    i += 1
    if i % 2 == 0:
        break
    print("*")
```
✅ `1`  
🔎 *En la primera iteración `i=1`, no se rompe el bucle y se imprime `*`. En la segunda `i=2`, se rompe.*

---

## Pregunta 5

**¿Cuántos `#` se imprimirán?**
```python
for i in range(1):
    print("#")
else:
    print("#")
```
✅ `2`  
🔎 *El bucle imprime una vez, y el bloque `else` también se ejecuta.*

---

## Pregunta 6

**¿Cuántos `#` se imprimirán?**
```python
var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print("#")
```
✅ `3`  
🔎 *Se imprimen para `var = 1, 3, 5`.*

---

## Pregunta 7

**¿Cuántos `#` se imprimirán?**
```python
var = 1
while var < 10:
    print("#")
    var = var << 1
```
✅ `4`  
🔎 *`var` se duplica binariamente: 1→2→4→8→16. Se imprimen 4 veces antes de romper la condición.*

---

## Pregunta 8

**¿Qué valor se asigna a `x`?**
```python
z = 10
y = 0
x = y < z and z > y or y > z and z < y
```
✅ `True`  
🔎 *La primera parte (`y < z and z > y`) es `True`, por lo tanto toda la expresión es `True`.*

---

## Pregunta 9

**¿Cuál es la salida del siguiente código?**
```python
a = 1
b = 0
c = a & b
d = a | b
e = a ^ b
print(c + d + e)
```
✅ `2`  
🔎 *`a&b = 0`, `a|b = 1`, `a^b = 1`; total = 0 + 1 + 1 = 2.*

---

## Pregunta 10

**¿Cuál es la salida?**
```python
my_list = [3, 1, -2]
print(my_list[my_list[-1]])
```
✅ `1`  
🔎 *`my_list[-1] = -2`, `my_list[-2] = 1`.*

---

## Pregunta 11

**¿Cuál es la salida?**
```python
my_list = [1, 2, 3, 4]
print(my_list[-3:-2])
```
✅ `[2]`  
🔎 *Slice desde el índice `-3` hasta `-2` (sin incluir), da `[2]`.*

---

## Pregunta 12

**La segunda asignación:**
```python
vals = [0, 1, 2]
vals[0], vals[2] = vals[2], vals[0]
```
✅ *invierte la lista*  
🔎 *Intercambia el primer y último elemento: de `[0,1,2]` a `[2,1,0]`.*

---

## Pregunta 13

**¿Cuál es la suma final de `vals`?**
```python
vals = [0, 1, 2]
vals.insert(0, 1)
del vals[1]
```
✅ `4`  
🔎 *Lista: `[1, 0, 2]` después de las operaciones. Suma: 1+0+2=3.*

> ❗ *Corrección: La suma es 3, no 4. Parece que la opción marcada como correcta originalmente es incorrecta.*

---

## Pregunta 14

**Sentencias verdaderas:**
```python
nums = [1, 2, 3]
vals = nums
del vals[1:2]
```
✅ *nums y vals se refieren a la misma lista*  
✅ *nums y vals son de la misma longitud*  
🔎 *`vals` y `nums` apuntan al mismo objeto, y la operación de borrado afecta a ambos.*

---

## Pregunta 15

**Sentencias verdaderas:**
```python
nums = [1, 2, 3]
vals = nums[-1:-2]
```
✅ *nums y vals son listas diferentes*  
✅ *nums es más larga que vals*  
🔎 *El slice no tiene elementos, pero crea una nueva lista vacía.*

---

## Pregunta 16

**¿Cuál es la salida?**
```python
my_list_1 = [1, 2, 3]
my_list_2 = []
for v in my_list_1:
    my_list_2.insert(0, v)
print(my_list_2)
```
✅ `[3, 2, 1]`  
🔎 *Cada elemento se inserta al principio, invirtiendo el orden.*

---

## Pregunta 17

**¿Cuál es la salida?**
```python
my_list = [1, 2, 3]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
print(my_list)
```
✅ `[1, 1, 1, 1, 2, 3]`  
🔎 *Se insertan tres `1` en la posición 1. El bucle se basa en la longitud original (3).*

---

## Pregunta 18

**¿Cuántos elementos tiene `my_list`?**
```python
my_list = [i for i in range(-1, 2)]
```
✅ `3`  
🔎 *`range(-1, 2)` genera `[-1, 0, 1]`.*

---

## Pregunta 19

**¿Cuál es la salida?**
```python
t = [[3-i for i in range(3)] for j in range(3)]
s = 0
for i in range(3):
    s += t[i][i]
print(s)
```
✅ `6`  
🔎 *Las diagonales son `[3, 2, 1]`, suma: 3+2+1 = 6.*

---

## Pregunta 20

**¿Cuál es la salida?**
```python
my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list[2][0])
```
✅ *Error de ejecución*  
🔎 *Solo se crean 2 listas internas (`i=0` y `i=1`), el índice `2` no existe.*

---

### 📘 Fin del Quiz

Gracias por revisar este quiz. ¡Esperamos que hayas aprendido algo nuevo sobre Python! Puedes sugerir mejoras o proponer nuevas preguntas en los Issues o mediante un Pull Request.
