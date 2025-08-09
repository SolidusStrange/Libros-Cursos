#INTRODUCCION DICCIONARIO CON IN PARA VER SI ESTA

dictionary = {"cat": "gato", "perro": "chien", "caballo": "cheval"}
words = ['cat', 'león', 'caballo']
 
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "no está en el diccionario")

print()

print("KEYS()")#KEYS ()
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
for key in dictionary.keys():
    print(key, "->", dictionary[key])
 
print()        

print("ITEMS()")#CON ITEMS()
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
for spanish, french in dictionary.items():
    print(spanish, "->", french)
    
print()

print("MODIFICAR DICCIONARIOS")
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
print(dictionary, end=" -> ")
dictionary['gato'] = 'minou'
print(dictionary)
print()

print("ORDENAR DICCIONARIO CON SORTED()")

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
# for key in sorted(dictionary.keys()):
for french in dictionary.values():
    print(french)

print()

print("AGREGAR NUEVAS CLAVES AL DICCIONARIO: ")
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
dictionary['cisne'] = 'cygne'
print(dictionary)
print()

#también es posible con:
# dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
# dictionary.update({"pato": "canard"})
# print(dictionary)
 
print("PARA ELIMINAR UNA CLAVE Y UN VALOR: ")
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
del dictionary['perro']
print(dictionary)

print()    

