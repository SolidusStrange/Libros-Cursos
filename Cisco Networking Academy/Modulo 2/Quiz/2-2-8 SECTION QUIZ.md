# 2.2.8 SECTION QUIZ - Resumen y Explicación

## Tipos de literales en Python

En Python, los **literales** son representaciones fijas de valores en el código. Los tipos principales son:

- **Literales de cadena (string literals):** texto entre comillas, por ejemplo `"Hello "` o `"007"`.
- **Literales numéricos:** incluyen enteros (`int`) y números de punto flotante (`float`).
- **Literales booleanos:** valores `True` o `False`.

---

## Pregunta 1

### ¿Qué tipos de literales son los siguientes?

"Hello ", "007"

Respuesta: Ambos son literales de cadena (strings).

## Pregunta 2
### ¿Qué tipos de literales son los siguientes?

"1.5", 2.0, 528, False

"1.5" es un literal de cadena (string).

2.0 es un literal numérico de tipo float (punto flotante).

528 es un literal numérico de tipo int (entero).

False es un literal booleano.

## Pregunta 3
### ¿Cuál es el valor decimal del siguiente número binario?
1011

Respuesta: Es 11, porque se calcula sumando las potencias de 2 correspondientes a los bits que están en 1.

Cómo convertir un número binario a decimal
Cada bit en un número binario representa una potencia de 2, comenzando desde la derecha con la potencia 0.

Por ejemplo, para el número binario 1011:

Posición (de derecha a izquierda)	3	2	1	0
Dígito binario	1	0	1	1

Los bits que están en 1 suman:

decimal = (1 * 2**3) + (0 * 2**2) + (1 * 2**1) + (1 * 2**0)
print(decimal)  # Esto imprime 11

Así, 1011 en binario equivale a 11 en decimal.

### Resumen adicional
El sistema binario usa base 2, sólo los dígitos 0 y 1.

Para convertir binario a decimal, multiplica cada bit por 2 elevado a la posición del bit y suma los resultados.

Los literales en Python incluyen cadenas, números enteros, números flotantes y booleanos.

