# Ejercicio 5: Simulador de Compuertas Lógicas
print("Ejercicio 5: Simulador de Compuertas Lógicas")
a = input("Booleano A (True/False): ").lower() == "true"
b = input("Booleano B (True/False): ").lower() == "true"
compuerta = input("Compuerta (XOR, NAND, NOR, XNOR): ").upper()

if compuerta == "XOR":
    resultado = (a or b) and not (a and b)
elif compuerta == "NAND":
    resultado = not (a and b)
elif compuerta == "NOR":
    resultado = not (a or b)
elif compuerta == "XNOR":
    resultado = not ((a or b) and not (a and b))
else:
    resultado = None

if resultado is not None:
    print(f"Resultado: {resultado}")
else:
    print("Compuerta no reconocida")

print()