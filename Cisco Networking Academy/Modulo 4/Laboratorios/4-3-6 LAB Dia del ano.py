def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if month < 1 or month > 12:
        return None
    
    days = [31, 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31]
    if is_year_leap(year) and month == 2:
            return 29
    return days[month - 1]
    
    # else:
    #     months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    #     days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # for i in range(len(months)):
        #     if months[i] == month:
        #         day = days[i]
        #         return day
            
def day_of_year(year, month, day):
     # Validar mes y día
    max_day = days_in_month(year, month)
    if max_day is None or day < 1 or day > max_day:
        return None
     
    # Sumar días de los meses anteriores
    total_days = sum(days_in_month(year, m) for m in range(1, month))
    #list comprehension
    
    # total_days = 0
    # for m in range(1, month):
    #     dias_del_mes = days_in_month(year, m)
    #     total_days += dias_del_mes
        
    return total_days + day
                                
    
#CASOS DE PRUEBA

print(day_of_year(2000, 12, 31))  # → 366 (año bisiesto)
print(day_of_year(2023, 2, 28))   # → 59
print(day_of_year(2023, 2, 29))   # → None (2023 no es bisiesto)
print(day_of_year(2024, 2, 29))   # → 60 (2024 sí es bisiesto)
print(day_of_year(2024, 13, 1))   # → None (mes inválido)
print(day_of_year(2024, 0, 10))   # → None (mes inválido)
print(day_of_year(2024, 4, 31))   # → None (abril tiene 30 días)
print(day_of_year(2024, 4, 30))   # → 121

