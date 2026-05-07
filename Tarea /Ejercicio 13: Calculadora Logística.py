# Ejercicio 13: Calculadora Logística
print("Ejercicio 13: Calculadora Logística")
zona = input("Zona (A/B/C): ").upper()
peso = float(input("Peso (kg): "))
volumen = float(input("Volumen (m3): "))
premium = input("Premium (si/no): ").lower() == "si"

costo_base = 100 if zona == "A" else 150 if zona == "B" else 200

costo = costo_base
if peso > 10:
    costo += costo * 0.5  # recargo 50%

if volumen > 1:
    costo += 50  # tarifa fija

if premium:
    costo -= costo * 0.1  # descuento 10%

print(f"Costo total: {costo}")

print()