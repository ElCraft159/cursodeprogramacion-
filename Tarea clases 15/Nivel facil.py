# Operaciones con listas
lista = [1, 2, 3, 4, 5]
print(lista)
lista.append(6)
lista.pop(0)
print(lista)

# Extraccion de tuplas
tupla = ("Daniel", "Espitia", "25")
nombre = tupla[0]
apellido = tupla[1]
edad = tupla[2]
print(f"Nombre: {nombre}\nApellido: {apellido} \nEdad: {edad}")

# Area de un circulo
import math
radio = float(input("Ingrese el radio del circulo: "))
area = math.pi * radio ** 2
circunfere = math.pow(radio, 2)
print(f"El area del circulo es: {area} y la circunferencia es: {circunfere}")

# Evaluacion de temperatura y indicador del estado del agua
temperatura = float(input("Ingrese la temperatura: "))
if temperatura < 0:
    print("El agua es congelada")
elif temperatura > 100:
    print("El agua es vapor")
else:
    print("El agua es liquida")

# Registro de inventario
inventario = {"Haria pan": 1.50, 
            "leche": 3.50, 
            "yogurt": 2.50
            }
inventario["huevos"] = 4.00
inventario["Harina pan"] = 2.50
print(inventario)

#Teoria de conjutos
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
print(set1 | set2)

#Valores aleatorios
import random
aleatorio = random.randint(1, 20)
print(aleatorio)

#Simulacion Matematico
import random 
import math
vueltas = 3
while vueltas > 0:
    angulo = random.randint(0, 90)
    velocidad = random.randint(1, 10)
    distancia = velocidad * math.sin(math.radians(angulo))
    print(f"La distancia recorrida es: {distancia}")
    vueltas -= 1