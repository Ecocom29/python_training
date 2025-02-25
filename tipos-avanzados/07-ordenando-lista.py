numeros = [2, 7, 5, 23, 5, 98, 6, 4, 45, 1, 8]

# numeros.sort(reverse =True)
numeros2 = sorted(numeros, reverse=True)

print(numeros)
print(numeros2)

usuarios = [[4, "Buck"], [3, "Wilson"], [8, "Chili"], [2, "Nanis"]] #aplica solamente cuando sea ordenable

# def ordenar(elemento):
#     return elemento[1]

usuarios.sort(key=lambda el: el[1], reverse=False) #funciones anonimas, solo cuando sea unica vez nada mas

print(usuarios)