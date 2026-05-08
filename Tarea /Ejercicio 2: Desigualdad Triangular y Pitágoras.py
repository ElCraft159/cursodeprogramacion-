# Ejercicio 2: Desigualdad Triangular y Pitágoras
print("Ejercicio 2: Desigualdad Triangular y Pitágoras")
a = float(input("Ingrese lado a: "))
b = float(input("Ingrese lado b: "))
c = float(input("Ingrese lado c: "))

if a + b > c and a + c > b and b + c > a:
    # Es triángulo
    # Encontrar el mayor
    if a > b and a > c:
        mayor = a
        lado1 = b
        lado2 = c
    elif b > c:
        mayor = b
        lado1 = a
        lado2 = c
    else:
        mayor = c
        lado1 = a
        lado2 = b

    if mayor**2 == lado1**2 + lado2**2:
        print("Triángulo rectángulo")
    elif mayor**2 < lado1**2 + lado2**2:
        print("Triángulo acutángulo")
    else:
        print("Triángulo obtusángulo")
else:
    print("No forma un triángulo")

print()
