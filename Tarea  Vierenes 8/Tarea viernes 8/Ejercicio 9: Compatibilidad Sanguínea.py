# Ejercicio 9: Compatibilidad Sanguínea
print("Ejercicio 9: Compatibilidad Sanguínea")
donante_grupo = input("Grupo sanguíneo del donante (A/B/AB/O): ").upper()
donante_factor = input("Factor del donante (+/-): ")
receptor_grupo = input("Grupo sanguíneo del receptor (A/B/AB/O): ").upper()
receptor_factor = input("Factor del receptor (+/-): ")

compatible = False
if donante_factor == "-" and receptor_factor == "+":
    compatible = False
elif donante_grupo == "O":
    compatible = True
elif donante_grupo == "A" and receptor_grupo in ["A", "AB"]:
    compatible = True
elif donante_grupo == "B" and receptor_grupo in ["B", "AB"]:
    compatible = True
elif donante_grupo == "AB" and receptor_grupo == "AB":
    compatible = True

if compatible:
    print("Transfusión segura")
else:
    print("Transfusión no segura")

print()