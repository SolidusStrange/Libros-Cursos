user_word = input("Ingrese un nombre: ").upper()
for i in user_word:
    if i in ("A", "E", "I", "O", "U"):
        continue
    else:
        print(i)