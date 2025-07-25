# 2.1.15 SECTION QUIZ – Función `print()` en Python

## Preguntas y código en bloque

```python
# Pregunta 1: ¿Cuál es la salida del siguiente programa?
print("My\nname\nis\nBond.", end=" ")
print("James Bond.")
# Salida:
# My
# name
# is
# Bond. James Bond.

# Pregunta 2: ¿Cuál es la salida del siguiente programa?
# print(sep="&", "fish", "chips")
# Salida:
# SyntaxError: positional argument follows keyword argument

# Pregunta 3: ¿Cuál de las siguientes invocaciones de print() generará un SyntaxError?
print('Greg\'s book.')           # ✅ Válido
print("'Greg's book.'")          # ✅ Válido
print('"Greg\'s book."')         # ✅ Válido
print("Greg\'s book.")           # ✅ Válido
# print('"Greg's book."')        # ❌ SyntaxError: comillas sin escapar
