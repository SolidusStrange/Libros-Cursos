## 2.4.11 RESUMEN DE LA SECCIÓN: VARIABLES EN PYTHON

Una **variable** es un espacio con nombre reservado en la memoria para almacenar valores. Una variable se **crea o inicializa automáticamente** cuando se le asigna un valor por primera vez.  
📌 *Referencia: 2.1.4.1*

### 🏷️ Identificadores y nombres válidos

Cada variable debe tener un **nombre único**, llamado *identificador*.  
Un identificador válido en Python debe cumplir con las siguientes reglas:

- Debe ser una **secuencia no vacía** de caracteres.
- Debe comenzar con una **letra (a-z, A-Z)** o un **guion bajo (_)**.
- No puede ser una **palabra clave de Python** (por ejemplo: `if`, `while`, `def`, etc.).
- Puede contener letras, guiones bajos y números después del primer carácter.
- Python distingue entre mayúsculas y minúsculas, por lo tanto, `Variable` y `variable` son nombres distintos.

### 🔄 Tipado dinámico

Python es un lenguaje de **tipado dinámico**, lo que significa que **no necesitas declarar el tipo** de la variable antes de usarla.  
Ejemplo de asignación básica:

```python
var = 1
```

### ➕ Operadores de asignación compuesta

Además del signo igual (`=`) para asignación simple, Python permite el uso de **operadores de asignación compuesta**, que combinan operaciones aritméticas con asignación:

```python
var += 1   # equivalente a var = var + 1
var /= 5 * 2  # primero evalúa 5*2, luego divide var entre el resultado
```

### 🔁 Reasignación de variables

Puedes asignar nuevos valores a una variable ya existente utilizando `=` u operadores compuestos:

```python
var = 2
print(var)

var = 3
print(var)

var += 1
print(var)
```

### 🖨️ Combinar texto y variables

Puedes **combinar cadenas de texto y variables** usando el operador `+`, y mostrar el resultado usando la función `print()`:

```python
var = "007"
print("Agente " + var)
```

### 💡 Complemento: asignación múltiple

En Python también puedes asignar valores a múltiples variables en una sola línea:

```python
x, y, z = 1, 2, 3
print(x, y, z)
```

Y puedes asignar el **mismo valor** a varias variables:

```python
a = b = c = 0
print(a, b, c)
```

### ✅ Buenas prácticas

- Usa nombres descriptivos para las variables (`edad`, `total_ventas`, etc.).
- Evita nombres como `x`, `temp` o `var` fuera de ejemplos simples o contextos matemáticos.
- No uses caracteres especiales ni espacios.
