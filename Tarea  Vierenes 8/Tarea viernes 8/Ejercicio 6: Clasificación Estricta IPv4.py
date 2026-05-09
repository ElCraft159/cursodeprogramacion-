# Ejercicio 6: Clasificación Estricta IPv4
print("Ejercicio 6: Clasificación Estricta IPv4")
oct1 = int(input("Octeto 1: "))
oct2 = int(input("Octeto 2: "))
oct3 = int(input("Octeto 3: "))
oct4 = int(input("Octeto 4: "))

if not (0 <= oct1 <= 255 and 0 <= oct2 <= 255 and 0 <= oct3 <= 255 and 0 <= oct4 <= 255):
    print("Dirección inválida")
elif oct1 >= 1 and oct1 <= 126:
    print("Clase A")
elif oct1 >= 128 and oct1 <= 191:
    print("Clase B")
elif oct1 >= 192 and oct1 <= 223:
    print("Clase C")
elif oct1 >= 224 and oct1 <= 239:
    print("Clase D")
elif oct1 >= 240 and oct1 <= 255:
    print("Clase E")
else:
    print("Dirección inválida")

print()