# Ejercicio 15: Identificador de Cuadrantes
print("Ejercicio 15: Identificador de Cuadrantes")
x = float(input("x: "))
y = float(input("y: "))

if x == 0 and y == 0:
    print("Origen")
elif x == 0:
    print("Eje Y")
elif y == 0:
    print("Eje X")
elif x > 0 and y > 0:
    print("Cuadrante I")
elif x < 0 and y > 0:
    print("Cuadrante II")
elif x < 0 and y < 0:
    print("Cuadrante III")
elif x > 0 and y < 0:
    print("Cuadrante IV")