def hola(nombre, apellido = "Feliz"): #parametros
    print("Hola mundo")
    print(f"Bienvenido {nombre} - {apellido}")


hola("Eliezer") #argumentos
hola("Wilson", "Cruz")

hola(apellido = "Wilson", nombre ="Cruz")