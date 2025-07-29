# 2.6.13 CUESTIONARIO COMPLETO – FUNCIONES `print()` e `input()`

---

### ❓ Pregunta 1: El digrafo `\n` obliga a la función `print()` a:

- [ ] Detener su ejecución  
- [ ] Imprimir exactamente dos caracteres: `\` y `n`  
- [ ] Duplicar el carácter junto al digrafo  
- ✅ Romper la línea de salida  

**Explicación:**  
El carácter especial `\n` se llama **nueva línea** y hace que el texto continúe en la línea siguiente.

---

### ❓ Pregunta 2: El significado de un parámetro con nombre se determina por:

- [ ] Su posición en la lista de argumentos  
- [ ] Su valor  
- ✅ El nombre del argumento especificado junto con su valor  
- [ ] Su conexión con variables existentes  

**Explicación:**  
Los argumentos con nombre se indican como `nombre=valor`, permitiendo especificarlos en cualquier orden.

---

### ❓ Pregunta 3: El número 20.12 × 10⁸ se debe escribir como:

- [ ] `20.12E8.0`  
- ✅ `20.12E8`  
- [ ] `20E12.8`  
- [ ] `20.12*10^8`  

**Explicación:**  
Python usa la notación científica con la letra `E` para representar potencias de diez.

---

### ❓ Pregunta 4: El prefijo `0o` indica que el número está expresado en:

- [ ] Decimal  
- ✅ Octal  
- [ ] Binario  
- [ ] Hexadecimal  

**Explicación:**  
`0o` o `0O` indican que el número está en base 8.

---

### ❓ Pregunta 5: El operador `**`:

- ✅ Realiza exponenciación  
- [ ] No existe  
- [ ] Realiza multiplicación flotante  
- [ ] Realiza multiplicación duplicada  

**Explicación:**  
`**` es el operador de potencia en Python, como en `2 ** 3 = 8`.

---

### ❓ Pregunta 6: El resultado de la división `1 / 1` es:

- ✅ `1.0`  
- [ ] No puede predecirse  
- [ ] No se puede evaluar  
- [ ] `1`  

**Explicación:**  
El operador `/` siempre devuelve un número decimal (`float`).

---

### ❓ Pregunta 7: ¿Cuáles afirmaciones son verdaderas? (Selecciona dos)

- [ ] La suma tiene prioridad sobre la multiplicación  
- [ ] El resultado de `/` siempre es un entero  
- ✅ El argumento derecho de `%` no puede ser cero  
- ✅ El operador `**` usa vinculación por la derecha  

**Explicación:**  
Dividir por cero con `%` lanza un error. La expresión `2**2**3` se evalúa como `2**(2**3)`.

---

### ❓ Pregunta 8: ¿Cuál es el resultado de `1 // 2 * 3`?

- [ ] `0.1666666...`  
- [ ] `0.0`  
- [ ] `4.5`  
- ✅ `0`  

**Explicación:**  
La evaluación es de izquierda a derecha: `1 // 2 = 0`, luego `0 * 3 = 0`.

---

### ❓ Pregunta 9: ¿Qué nombres de variables son ilegales? (Selecciona dos)

- ✅ `True`  
- ✅ `and`  
- [ ] `TRUE`  
- [ ] `true`  

**Explicación:**  
`True` y `and` son palabras reservadas en Python. Las demás son válidas pero no recomendadas.

---

### ❓ Pregunta 10: La función `print()` puede mostrar:

- ✅ Cualquier cantidad de argumentos (incluido cero)  
- [ ] No más de cinco argumentos  
- [ ] Cualquier cantidad de argumentos (excluyendo cero)  
- [ ] Solo un argumento  

**Explicación:**  
`print()` permite múltiples argumentos separados por comas, incluso ninguno.

### ❓ Pregunta 11: ¿Cuál es la salida del siguiente código?

```python
x = 1
y = 2
z = x
x = y
y = z
print(x, y)
```

- [ ] 1 2  
- [ ] 1 1  
- [ ] 2 2  
- ✅ 2 1  

**Explicación:** Se intercambian los valores usando una variable auxiliar. `x` toma el valor de `y`, y `y` el valor original de `x`.

---

### ❓ Pregunta 12: ¿Qué se imprime si el usuario ingresa `2` y luego `4`?

```python
x = input()
y = input()
print(x + y)
```

- [ ] 6  
- [ ] 4  
- [ ] 2  
- ✅ 24  

**Explicación:** Ambas entradas son cadenas. Se concatenan como texto: `"2" + "4"` produce `"24"`.

---

### ❓ Pregunta 13: ¿Qué ocurre si se ingresan `2` y `4`?

```python
x = int(input())
y = int(input())
x = x // y
y = y // x
print(y)
```

- [ ] 8.0  
- ✅ Error en tiempo de ejecución  
- [ ] 4.0  
- [ ] 2.0  

**Explicación:** `x // y = 0`, luego `y // x` lanza `ZeroDivisionError` por división por cero.

---

### ❓ Pregunta 14: ¿Qué se imprime si el usuario ingresa `2` y `4`?

```python
x = int(input())
y = int(input())
x = x / y
y = y / x
print(y)
```

- [ ] Error en tiempo de ejecución  
- [ ] 2.0  
- ✅ 8.0  
- [ ] 4.0  

**Explicación:** `x = 2 / 4 = 0.5`, `y = 4 / 0.5 = 8.0`.

---

### ❓ Pregunta 15: ¿Qué se imprime si se ingresan `11` y `4`?

```python
x = int(input())
y = int(input())
x = x % y
x = x % y
y = y % x
print(y)
```

- [ ] 2  
- [ ] 4  
- ✅ 1  
- [ ] 3  

**Explicación:** `x = 11 % 4 = 3`, luego `x = 3 % 4 = 3`, y finalmente `y = 4 % 3 = 1`.

---

### ❓ Pregunta 16: ¿Qué se imprime si se ingresa `3` y `6`?

```python
x = input()
y = int(input())
print(x * y)
```

- [ ] 18  
- [ ] 36  
- [ ] 666  
- ✅ 333333  

**Explicación:** `"3" * 6` repite la cadena `"3"` seis veces, resultando en `"333333"`.

---

### ❓ Pregunta 17: ¿Qué se imprime?

```python
z = y = x = 1
print(x, y, z, sep='*')
```

- [ ] 1 1 1  
- ✅ 1*1*1  
- [ ] x y z  
- [ ] x*y*z  

**Explicación:** Las variables `x`, `y` y `z` tienen el valor `1`. El separador `'sep="*"'` imprime: `1*1*1`.

---

### ❓ Pregunta 18: ¿Cuál es el resultado?

```python
y = 2 + 3 * 5.
print(Y)
```

- [ ] 17.0  
- [ ] 25.0  
- ✅ Error de ejecución  
- [ ] 17  

**Explicación:** La variable `Y` no está definida (es `y` en minúscula). Python es sensible a mayúsculas y minúsculas, lo que genera `NameError`.

---

### ❓ Pregunta 19: ¿Cuál es el resultado?

```python
x = 1 / 2 + 3 // 3 + 4 ** 2
print(x)
```

- ✅ 17.5  
- [ ] 17  
- [ ] 8.5  
- [ ] 8  

**Explicación:** Se evalúa:  
- `4 ** 2 = 16`  
- `1 / 2 = 0.5`  
- `3 // 3 = 1`  
Suma total: `0.5 + 1 + 16 = 17.5`.

---

### ❓ Pregunta 20: ¿Qué se imprime si el usuario ingresa `2` y `4`?

```python
x = int(input())
y = int(input())
print(x + y)
```

- [ ] 2  
- [ ] 4  
- ✅ 6  
- [ ] 24  

**Explicación:** Se ingresan enteros y se suman: `2 + 4 = 6`.

---