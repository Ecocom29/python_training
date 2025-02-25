usuarios = [[4, "Buck"], [3, "Wilson"], [8, "Chili"], [2, "Nanis"]]


nombres = []

# for usuario in usuarios:
#     nombres.append(usuario[1])

# print(nombres)

# nombres = [usuario[1] for usuario in usuarios] #Transformación de una lista

# filtrar elementos
# nombres = [usuario[0] for usuario in usuarios if usuario[0] > 2] #filtrar y transformar

nombres = list(map(lambda usuario: usuario[0], usuarios))


menosUsuarios = list(filter(lambda usuario: usuario[0] > 2, usuarios))
print(menosUsuarios)
