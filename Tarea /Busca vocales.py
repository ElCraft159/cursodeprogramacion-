
frase = input("Ingrese una frase: ")
vocales = "aeiouAEIOU"
consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
contador_vocales = 0
contador_consonantes = 0
for letra in frase:
    if letra in vocales:
        contador_vocales += 1
    elif letra in consonantes:
        contador_consonantes += 1
print(f"Número de vocales: {contador_vocales}")
print(f"Número de consonantes: {contador_consonantes}")