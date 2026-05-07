# Ejercicio 8: Impuesto Marginal de Múltiples Tramos
print("Ejercicio 8: Impuesto Marginal de Múltiples Tramos")
ingreso = float(input("Ingreso: "))

impuesto = 0
if ingreso > 60000:
    impuesto += (ingreso - 60000) * 0.35
    ingreso = 60000
if ingreso > 30000:
    impuesto += (ingreso - 30000) * 0.25
    ingreso = 30000
if ingreso > 10000:
    impuesto += (ingreso - 10000) * 0.15

print(f"Impuesto a pagar: {impuesto}")

print()