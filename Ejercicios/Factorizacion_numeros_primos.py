# Veamos como factorizar un número en sus primos.
# Es decir, cualquier número que se te ocurra puede
# ser expresado como la multiplicación de varios
# números primos.

# El 8 es 2*2*2.
# El 765 es 3*3*5*17.
# ---------------------------------------------
def factorizar(n):
    factores = []

    for divisor in range(2, int(n**0.5) + 1):
        while n % divisor == 0:
            factores.append(divisor)
            n //= divisor

    if n > 1:
        factores.append(n)
    return factores


numero = 8
factores = factorizar(numero)
print(f"{numero} = {'*'.join(map(str, factores))}")
# 8 = 3*3*5*17
