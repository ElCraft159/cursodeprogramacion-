# Ejercicio 11: Evaluador de Crédito (Scoring)
print("Ejercicio 11: Evaluador de Crédito (Scoring)")
ingresos = float(input("Ingresos: "))
deudas = float(input("Deudas: "))
edad = int(input("Edad: "))
morosidad = input("Morosidad (si/no): ").lower() == "si"

puntuacion = 500  # base

if ingresos > 50000:
    puntuacion += 100
elif ingresos > 30000:
    puntuacion += 50

if deudas < 10000:
    puntuacion += 50
elif deudas > 50000:
    puntuacion -= 100

if edad > 25 and edad < 65:
    puntuacion += 50

if morosidad:
    puntuacion -= 200

if puntuacion >= 600:
    print("Crédito aprobado")
else:
    print("Crédito denegado")

print()