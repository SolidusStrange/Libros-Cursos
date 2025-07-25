# 2.2.9 SECTION QUIZ - Resumen y Explicación

## Pregunta 1

### ¿Cuál es la salida esperada del siguiente fragmento?

```python
print((2 ** 4), (2 * 4.), (2 * 4))
```

#### Salida:
```
16 8.0 8
```

#### Explicación:
- `2 ** 4` es 2 elevado a la 4: `2 * 2 * 2 * 2 = 16`
- `2 * 4.` multiplica un entero por un flotante → el resultado es flotante: `8.0`
- `2 * 4` multiplica dos enteros → resultado entero: `8`

---

## Pregunta 2

### ¿Cuál es la salida esperada del siguiente fragmento?

```python
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
```

#### Salida:
```
-0.5 0.5 0 -1
```

#### Explicación:
- `-2 / 4` → división flotante: `-0.5`
- `2 / 4` → división flotante: `0.5`
- `2 // 4` → división entera: `0` (porque 4 cabe 0 veces en 2)
- `-2 // 4` → división entera: `-1` (se redondea hacia abajo)

---

## Pregunta 3

### ¿Cuál es la salida esperada del siguiente fragmento?

```python
print((2 % -4), (2 % 4), (2 ** 3 ** 2))
```

#### Salida:
```
-2 2 512
```

#### Explicación:
- `2 % -4` → el resultado tiene el mismo signo que el divisor (-4), por eso da `-2`.
- `2 % 4` → 4 cabe 0 veces en 2, sobra 2 → `2 % 4 = 2`
- `2 ** 3 ** 2` → asociatividad derecha: `2 ** (3 ** 2) = 2 ** 9 = 512`

---

## 🧠 Nota adicional sobre el operador módulo (`%`)

En Python, el resultado del módulo siempre tiene el **mismo signo que el divisor**.

Por ejemplo:

```python
print(2 % 4)   # 2 (positivo, porque 4 es positivo)
print(2 % -4)  # -2 (negativo, porque -4 es negativo)
```

La fórmula que se cumple es:

\[
a = b × q + r
\]

Donde:
- `a` es el dividendo
- `b` es el divisor
- `q` es el cociente entero (`a // b`)
- `r` es el residuo (`a % b`)
