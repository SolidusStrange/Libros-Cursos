
# 📚 4.1.6 Resumen de Sección

## 1️⃣ ¿Qué es una función?
Una **función** es un bloque de código que realiza una tarea específica cuando es **llamada** (invocada).  
Las funciones son útiles porque permiten que el código sea:
- **Reutilizable**
- **Organizado**
- **Más legible**

Una función puede:
- Tener **parámetros** (entradas)
- **Regresar valores** (salidas)

---

## 2️⃣ Tipos básicos de funciones en Python

1. **Funciones integradas**  
   Son parte del núcleo de Python.  
   Ejemplo: `print()`.  
   📄 Lista completa: [Funciones integradas de Python](https://docs.python.org/3/library/functions.html)

2. **Funciones en módulos pre-instalados**  
   Vienen con Python, pero requieren importarse.  
   *(Se verán más adelante en el curso Fundamentos de Python 2)*

3. **Funciones definidas por el usuario**  
   Escritas por los programadores para sus propios programas.

4. **Funciones lambda**  
   Funciones anónimas y rápidas. *(Se verán más adelante en Fundamentos de Python 2)*

---

## 3️⃣ Sintaxis de una función propia

```python
def nombre_funcion(parametros_opcionales):
    # Cuerpo de la función
```

### Ejemplo sin argumentos:
```python
def message():  # definiendo una función
    print("Hello")  # cuerpo de la función

message()  # invocación de la función
```

### Ejemplo con un argumento:
```python
def hello(name):  # definiendo una función
    print("Hello,", name)  # cuerpo de la función

name = input("Ingresa tu nombre: ")

hello(name)  # invocación de la función
```

> ℹ️ Más sobre funciones parametrizadas se verá en la siguiente sección.

---
