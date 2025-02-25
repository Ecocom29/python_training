def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2,6,7)
suma(2,6)
suma(2,8,9,6,9)