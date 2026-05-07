# Ejercicio 1: Validación Completa de Fecha
print("Ejercicio 1: Validación Completa de Fecha")
dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))

es_bisiesto = (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

if mes < 1 or mes > 12 or dia < 1 or año < 1:
    print("Fecha inválida")
elif mes == 2:
    if es_bisiesto and dia <= 29:
        print("Fecha válida")
    elif not es_bisiesto and dia <= 28:
        print("Fecha válida")
    else:
        print("Fecha inválida")
elif mes in [4, 6, 9, 11] and dia <= 30:
    print("Fecha válida")
elif mes in [1, 3, 5, 7, 8, 10, 12] and dia <= 31:
    print("Fecha válida")
else:
    print("Fecha inválida")

print()
