
# Ejemplo final – Hotel con habitaciones usando listas anidadas

Imaginemos un hotel enorme con las siguientes características:

- **3 edificios**
- **15 pisos por edificio**
- **20 habitaciones por piso**

Cada habitación puede estar **ocupada (`True`)** o **libre (`False`)**.

## Paso 1: Crear la estructura del hotel

Usamos una lista tridimensional para representar las habitaciones:

```python
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
```

### Significado de los índices:
- `rooms[t][f][r]`
  - `t`: índice del edificio (0 a 2)
  - `f`: índice del piso (0 a 14)
  - `r`: número de habitación (0 a 19)

Inicialmente, **todas las habitaciones están libres (`False`)**.

---

## Paso 2: Reservar una habitación

Reservamos una habitación para dos recién casados:
- Edificio 2 (índice 1)
- Piso 10 (índice 9)
- Habitación 14 (índice 13)

```python
rooms[1][9][13] = True
```

---

## Paso 3: Desocupar una habitación

Liberamos la segunda habitación del quinto piso en el primer edificio:

```python
rooms[0][4][1] = False
```

---

## Paso 4: Verificar disponibilidad en un piso

Queremos saber cuántas habitaciones hay disponibles en el piso 15 del tercer edificio:

```python
vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1
```

- Si `vacancy == 0`: todas las habitaciones están ocupadas.
- Si `vacancy > 0`: hay ese número de habitaciones disponibles.

---

¡Felicitaciones! Has llegado al final del módulo. 🏁 Sigue con el buen trabajo.
