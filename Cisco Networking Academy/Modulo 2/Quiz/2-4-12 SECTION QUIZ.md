## 2.4.12 CUESTIONARIO DE LA SECCIÓN: VARIABLES EN PYTHON

### ❓ Pregunta 1: ¿Cuál es la salida del siguiente código?

```python
var = 2
var = 3
print(var)
```

**Respuesta correcta:** `3`

Explicación: la variable `var` se actualiza a 3 antes del `print()`.

---

### ❓ Pregunta 2: ¿Cuáles de los siguientes nombres de variables son ilegales en Python? (Selecciona tres respuestas)

- `my_var` ✅
- `m` ✅
- `101` ❌ (Empieza con un número, no permitido)
- `averylongVariablename` ✅
- `m101` ✅
- `m 101` ❌ (Contiene un espacio, no permitido)
- `Del` ✅ (aunque es legal, no es recomendable usar nombres que se parezcan a palabras clave)
- `del` ❌ (Es una palabra clave de Python, ilegal como nombre de variable)

**Respuestas ilegales:** `101`, `m 101`, `del`

---

### ❓ Pregunta 3: ¿Cuál es la salida del siguiente fragmento?

```python
a = '1'
b = "1"
print(a + b)
```

**Respuesta correcta:** `'11'`

Explicación: ambas variables son cadenas de texto, se concatenan como `'1' + '1'`.

---

### ❓ Pregunta 4: ¿Cuál es la salida del siguiente fragmento?

```python
a = 6
b = 3
a /= 2 * b
print(a)
```

**Respuesta correcta:** `1.0`

Explicación: `2 * b` es `6`, y `6 / 6` es `1.0`. El operador `/=` siempre devuelve un `float`.

---
