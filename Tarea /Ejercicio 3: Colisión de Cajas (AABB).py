# Ejercicio 3: Colisión de Cajas (AABB)
print("Ejercicio 3: Colisión de Cajas (AABB)")
x1_min = float(input("Rectángulo 1 x min: "))
y1_min = float(input("Rectángulo 1 y min: "))
x1_max = float(input("Rectángulo 1 x max: "))
y1_max = float(input("Rectángulo 1 y max: "))

x2_min = float(input("Rectángulo 2 x min: "))
y2_min = float(input("Rectángulo 2 y min: "))
x2_max = float(input("Rectángulo 2 x max: "))
y2_max = float(input("Rectángulo 2 y max: "))

if x1_max > x2_min and x1_min < x2_max and y1_max > y2_min and y1_min < y2_max:
    print("Colisión detectada")
else:
    print("No hay colisión")

print()
