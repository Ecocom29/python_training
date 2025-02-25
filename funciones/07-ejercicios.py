def no_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto

def revers(texto):
    texto_alreves = ""
    for char in texto:
        texto_alreves = char + texto_alreves
    return texto_alreves


def es_palindromo(texto):
    texto = no_space(texto)
    texto_al_reves = revers(texto)
    print(texto_al_reves)
    return texto.lower() == texto_al_reves.lower()

print(es_palindromo("Amo al perro"))
print(es_palindromo("Hola mundo"))
print(es_palindromo("Abba"))