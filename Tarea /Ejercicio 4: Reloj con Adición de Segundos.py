# Ejercicio 4: Reloj con Adición de Segundos
print("Ejercicio 4: Reloj con Adición de Segundos")
hh = int(input("Horas: "))
mm = int(input("Minutos: "))
ss = int(input("Segundos: "))
segundos_a_sumar = int(input("Segundos a sumar: "))

total_segundos = hh * 3600 + mm * 60 + ss + segundos_a_sumar

hh_nueva = (total_segundos // 3600) % 24
mm_nueva = (total_segundos % 3600) // 60
ss_nueva = total_segundos % 60

print(f"Nueva hora: {hh_nueva:02d}:{mm_nueva:02d}:{ss_nueva:02d}")

print()