print("_" * 20 + "\n")

# Conteo básico secuencial
for x in range(1, 16):
    print(x)

print("_" * 20 + "\n")

# Conteo regresivo
n = 10
while n >= 0:
    print(n)
    n -= 1

print("_" * 20 + "\n")

# Sumatoria de rango
total = 0
for suma in range(1, 51):
    total += suma
print(f"La sumatoria del rango 1 al 50 es: {total}")

print("_" * 20 + "\n")

# Generador de tablas de multiplicar
num = int(input("Ingrese un número del 1 al 10 para generar su tabla de multiplicar: "))
for M in range(1, 11):
    print(f"{num} x {M} = {num * M}")

print("_" * 20 + "\n")

# Interacion de Cadenas
p = "Programacion"
for x in p:
    print(f"{x}")

print("_" * 20 + "\n")

# Identificacion de Numeros Pares

num = 2
print("Numero de 2 en 2 hasta 3")
while num <= 30:
    print(num)
    num += 2

print("_" * 20 + "\n")

#Interrucion de bucle

for x in range(1, 101):
    if x % 13 == 0:
        print(f"Encotrado el primer numero es: {x}")
        break

print("_" * 20 + "\n")

#Calculo de factorial

num = int(input("Ingresa un numero para buscar su factorial: "))
factorial = 1
if num < 0:
    print("Tiene que ser un numero entero: ")
elif num == 0:
    print("El factorial de 0 es 1")
else:
    for f in range(1, num + 1):
        factorial = factorial * f
    print(f"El factorial de {num} es: {factorial}")

print("_" * 20 + "\n")