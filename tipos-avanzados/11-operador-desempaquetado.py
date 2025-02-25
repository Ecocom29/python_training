lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(*lista)

lista_dos = [10, 11]

combinada = [*lista, *lista_dos]

print(combinada)

punto_uno = {"x": 35}
punto_dos = {"y": 70}

punto = {**punto_uno, **punto_dos}

print(punto)


# Obtener los tipos de datos, comprobar el tipo
print(type("Soy un string"))
print(type(10))
print(type((4, 7, 9, 6, 4)))
print(type({7, 8, 54}))
print(type([7, 8, 54]))
