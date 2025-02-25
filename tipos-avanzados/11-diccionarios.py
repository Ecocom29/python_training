punto = {"x": 25, "y": 90}

print(punto)
print(punto["x"])
print(punto["y"])
print(punto)

punto["z"] = 30
print(punto["z"])


if "z" in punto:
    print("Encontrado", punto["z"])

print(punto.get("x"))
print(punto.get("r", 100))

print(punto)

for item in punto:
    print(item)

for llave, valor in punto.items():
    print(llave, "-", valor)

usuarios = [
    {"id":1, "nombre":"wilson"  },
    {"id":2, "nombre":"buck"  },
    {"id":3, "nombre":"chili"  },
    {"id":4, "nombre":"nelson"  }
]

for usuarios in usuarios:
    print(usuarios["nombre"])
