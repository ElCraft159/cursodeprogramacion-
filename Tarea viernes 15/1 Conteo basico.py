# Conteo básico secuencial
for x in range(1, 16):
    print(x)

# Conteo regresivo
while n := int(input("Ingrese un número para contar hacia atrás: ")) > 0:
    for x in range(n, 0, -1):
        print(x)