# Ejercicio 10: Decodificador de Permisos Linux (chmod)
print("Ejercicio 10: Decodificador de Permisos Linux (chmod)")
numero = int(input("Número (0-7): "))

permisos = ""
if numero & 4:
    permisos += "Lectura "
if numero & 2:
    permisos += "Escritura "
if numero & 1:
    permisos += "Ejecución "

if permisos:
    print(f"Permisos: {permisos.strip()}")
else:
    print("Sin permisos")

print()