def is_prime(num):
    #primero si es impar
    if num>0:
        divisiones = 1
        for i in range(1, num):
            if ((num/i) - (num//i)) == 0:
                divisiones += 1
    
    if divisiones == 2:
        return True
    else:
        return False
             
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
  
