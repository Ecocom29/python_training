# numero = 1

# while numero < 100:
#     print(numero)
#     numero *= 2

comando = ""

while comando.lower() != "Salir":
    comando = input("$ ")
    print(comando)
    if comando.lower() == "Salir":
        break