
# Puntos clave: Expresiones y Operadores en Python

1. Una **expresión** es una combinación de valores (o variables, operadores, llamadas a funciones — lo aprenderás pronto) que se **evalúa a un valor**, por ejemplo:

```python
1 + 2  # Resultado: 3
```

2. Los **operadores** son símbolos o palabras clave especiales que permiten operar con valores y realizar operaciones (matemáticas), por ejemplo:

```python
x * y  # El operador * multiplica dos valores
```

3. **Operadores aritméticos en Python**:

| Operador | Descripción                      | Ejemplo             | Resultado |
|----------|----------------------------------|---------------------|-----------|
| `+`      | Suma                             | `2 + 3`             | `5`       |
| `-`      | Resta                            | `5 - 2`             | `3`       |
| `*`      | Multiplicación                   | `4 * 3`             | `12`      |
| `/`      | División clásica (siempre float) | `5 / 2`             | `2.5`     |
| `%`      | Módulo (resto de la división)    | `5 % 2`             | `1`       |
| `**`     | Exponenciación                   | `2 ** 3`            | `8`       |
| `//`     | División entera (piso)           | `3 // 2.0`          | `1.0`     |

4. Un **operador unario** es un operador con **un solo operando**, por ejemplo:

```python
-1
+3
```

5. Un **operador binario** es un operador con **dos operandos**, por ejemplo:

```python
4 + 5
12 % 5
```

6. Algunos operadores se ejecutan **antes que otros** — esta es la jerarquía de prioridades en Python:

- El operador `**` (exponenciación) tiene la **mayor prioridad**.
- Luego los operadores unarios `+` y `-` (nota: un operador unario a la derecha de un `**` se aplica primero. Ejemplo: `4 ** -1` da `0.25`)
- Después: `*`, `/`, y `%`
- Por último, los de **menor prioridad**: `+` y `-` binarios.

7. Las **subexpresiones entre paréntesis** siempre se evalúan primero. Por ejemplo:

```python
15 - 1 * (5 * (1 + 2))  # Resultado: 0
```

8. El operador de **exponenciación** se asocia **de derecha a izquierda** (right-sided binding). Por ejemplo:

```python
2 ** 2 ** 3  # Resultado: 256
# Se evalúa como: 2 ** (2 ** 3) = 2 ** 8 = 256
```
