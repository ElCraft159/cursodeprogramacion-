print("_" * 50 + "")
print("\n" "Bienvenido al cajero automatico")
print("_" * 50 + "")
print("Create tu cuenta")
usuario = input("Ingresar tu nombre: ").lower()
intentos = 3
print(f"Crea una contrasena de 4 digitos numericos intentantos restantes: {intentos}")
while intentos > 0:
    entrada = int(input("Ingrese un pin: "))
    if "entrada".isnumeric():
        pin = entrada
        if pin <= 9999 and pin >= 1000:
            print("Contrasena creada exitosamente")
            break
        else:
            print("Pin incorrecto")
            intentos -= 1
if intentos == 0:
    print("Has agotado tus intentos")            
dinero = float(input("Ingrese Tu dinero: "))