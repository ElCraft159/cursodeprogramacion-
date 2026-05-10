print("_" * 20 + "\n")

print ("Conteo básico secuencial" "\n")
for x in range(1, 16):
    print(x)

print("_" * 20 + "\n")

print("Conteo regresivo" "\n")
n = 10
while n >= 0:
    print(n)
    n -= 1

print("_" * 20 + "\n")

print ("Sumatoria de rango" "\n")
total = 0
for suma in range(1, 51):
    total += suma
print(f"La sumatoria del rango 1 al 50 es: {total}")

print("_" * 20 + "\n")

("Generador de tablas de multiplicar" "\n")
num = int(input("Ingrese un número del 1 al 10 para generar su tabla de multiplicar: "))
for M in range(1, 11):
    print(f"{num} x {M} = {num * M}")

print("_" * 20 + "\n")

print("Interacion de Cadenas" "\n")
p = "Programacion"
for x in p:
    print(f"{x}")

print("_" * 20 + "\n")

print("Identificacion de Numeros Pares" "\n")

num = 2
print("Numero de 2 en 2 hasta 3")
while num <= 30:
    print(num)
    num += 2

print("_" * 20 + "\n")

print("Interrucion de bucle" "\n")

for x in range(1, 101):
    if x % 13 == 0:
        print(f"Encotrado el primer numero es: {x}")
        break

print("_" * 20 + "\n")

print("Calculo de factorial" "\n")

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

print("Filtro de vocales" "\n")

frase = input("Ingresa tu frase: ")
vocales = "aeiouAEIOU"
contavoca = 0
for vocal in frase:
    if vocal in vocales:
        contavoca += 1
print(f"Tienes {contavoca} Vocales")

print("_" * 20 + "\n")

print("Salto de interacion" "\n")
for x in range(1, 21):
    if x % 3 == 0:
        continue
    print(x)

print("_" * 20 + "\n")

print("inversion de cadenas")
palabra = input("ingresa una palabra: ")
invertida = ""
for x in palabra:
    invertida = x + invertida
print(invertida)

print("_" * 20 + "\n")

print("Secuencia de fibonaccio")
fibo = int(input("ingresa un numero: "))
a = 0
b = 1
for x in range(fibo):
    print(a)
    c = a + b
    a = b
    b = c

print("_" * 20 + "\n")

print("Bucle centinela" "\n")
print("Adivina el numero")
num = 4
while True:
    intento = int(input("Ingresa un del 1 al 10: "))
    if intento == num:
        print("Adivinaste el numero")
        break
    else:
        print("No adivinaste el numero intenta de nuevo")

print("_" * 20 + "\n")

print("Validacion constante")
num = -1
while num <= 0:
    num = int(input("Ingresa un numero positivo: "))
    if num <= 0:
        print("Papi te dije un numero positivo dale de nuevo")
print(f"Perfecto, el numero es: {num} es valido")        

print("_" * 20 + "\n")