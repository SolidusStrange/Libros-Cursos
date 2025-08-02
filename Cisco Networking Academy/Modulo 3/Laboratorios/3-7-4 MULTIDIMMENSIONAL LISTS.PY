# Imagina que desarrollas una pieza de software para una estación meteorológica automática.
# El dispositivo registra la temperatura del aire cada hora y lo hace durante todo el mes. 
# Esto te da un total de 24 × 31 = 744 valores. Intentemos diseñar una lista capaz de 
# almacenar todos estos resultados.

temps = [[0.0 for columnas in range(24)] for filas in range(31)]
# temps = [[[columnas, filas] for columnas in range(24)] for filas in range(31)]

for temp in temps: print(temp)

# Ahora es el momento de determinar la temperatura promedio mensual del mediodía. 
# Suma las 31 lecturas registradas al mediodía y divida la suma por 31. 
# Puedes suponer que la temperatura de medianoche se almacena primero.
# Aquí está el código:

temps = [[0.0 for i in range(24)] for j in range(31)]
#
# La matriz se actualiza aquí.
#

total = 0.0

for day in temps:
    total += day[11]

average = total / 31

print("Temperatura promedio al mediodía:", average)    

#Ahora encuentra la temperatura más alta durante todo el mes - analiza el código:

temp = [[0.0 for i in range(24)] for j in range(31)]
#
# La matriz se actualiza aquí.
#
 
highest = -100.0
 
for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp
 
print("La temperatura más alta fue:", highest)

# la variable day itera en todas las filas de la matriz temps;
# la variable temp itera a través de todas las mediciones tomadas en un día.

# Ahora cuenta los días en que la temperatura al mediodía fue de al menos 20 ℃:

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# La matriz se actualiza aquí.
#
 
hot_days = 0
 
for day in temps:
    if day[11] > 20.0:
        hot_days += 1
 
print(hot_days, "fueron los días calurosos.")

