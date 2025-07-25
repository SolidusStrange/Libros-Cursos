
# 2.2.7 RESUMEN DE LA SECCIÓN

## 1. Literales

Los **literales** son notaciones que representan valores fijos en el código. Python tiene varios tipos de literales.  
Por ejemplo, un literal puede ser:

- un número (**literal numérico**), como `123`
- una cadena (**literal de cadena**), como `"Soy un literal."`

### Ejemplo:
```python
numero = 123
cadena = "Soy un literal."
```

## 2. Sistemas de numeración

El **sistema binario** es un sistema de números que utiliza el **2 como base**.  
Por lo tanto, un número binario está compuesto solo por **0s y 1s**.  
Ejemplo: `1010` en binario equivale a `10` en decimal.

Los sistemas de numeración **octal** y **hexadecimal**, de forma similar, usan como base el **8** y el **16**, respectivamente.

- El sistema **octal** emplea los dígitos del 0 al 7.
- El sistema **hexadecimal** utiliza los números del 0 al 9 y seis letras adicionales (`A` a `F`).

### Ejemplo:
```python
binario = 0b1010       # 10 en decimal
octal = 0o12           # 10 en decimal
hexadecimal = 0xA      # 10 en decimal
```

## 3. Números enteros (int)

Los **enteros** (o simplemente `int`) son uno de los tipos numéricos que Python admite.  
Son números escritos **sin componente decimal**, como por ejemplo:

### Ejemplo:
```python
positivo = 256
negativo = -1
```

## 4. Números de punto flotante (float)

Los **números de punto flotante** (o simplemente `float`) son otro tipo numérico en Python.  
Representan números que **contienen o pueden contener una parte fraccionaria**.

### Ejemplo:
```python
numero_decimal = 1.27
```

## 5. Comillas y caracteres de escape en strings

Para codificar una **coma simple** (apostrofe `'`) o una **comilla doble** (`"`) dentro de un string:

- Puedes usar el **carácter de escape** `\`:

```python
print('I\'m happy.')
```

- O puedes usar el tipo opuesto de comillas para abrir y cerrar el string:

```python
print("I'm happy.")
print('He said "Python", not "typhoon"')
```

## 6. Valores booleanos

Los **valores booleanos** son los objetos constantes `True` y `False`, que representan **valores de verdad**.

- En contextos numéricos:
  - `True` equivale a `1`
  - `False` equivale a `0`

### Ejemplo:
```python
print(True > False)   # True
print(True < False)   # False
```

## Extra: el literal `None`

Existe un literal especial llamado `None`. Es un objeto del tipo `NoneType`, y se utiliza para representar **la ausencia de un valor**.

### Ejemplo:
```python
valor = None
print(valor)  # None
```

> Aprenderás más sobre `None` más adelante.
