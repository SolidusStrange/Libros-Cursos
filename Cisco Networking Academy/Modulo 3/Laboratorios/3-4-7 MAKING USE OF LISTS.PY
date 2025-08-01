#acá la lista accede al número de la lista, no al valor, por eso usamos len y my_list[i]

my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)


# print(sum(my_list))


my_list = [10, 1, 8, 3, 5]
total = 0
 
for i in my_list:
    total += i
 
print(total)
 