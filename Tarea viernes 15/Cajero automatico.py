print("_" * 50 + "")
print("\n" "Bienvenido al cajero automatico")
print("_" * 50 + "")
saldo = 22,35
print("Create tu cuenta")
usuario = input("Ingresar tu nombre: ").upper()
intentos = 3
print(f"Crea una contrasena de 4 digitos numericos tienes {intentos} intentos")
while intentos > 0:
    pin = int(input("Ingrese un pin: "))
    if pin >= 1000 and pin <= 9999:
         print("Contrasena creada exitosamente")
         break
    else:
        print("Pin incorrecto")
        intentos -= 1
    if intentos == 0:
        print("Has agotado tus intentos")
        exit()            
print("_" * 50 + "")

print("Iniciar sesion")
print("Bienvenido", usuario)
intentos = 3
while intentos > 0:
    pin = int(input("Ingrese tu pin: "))
    if pin == pin:
        print("Sesion iniciada")
        break
    else:
        print("Contrasena incorrecta")
        intentos -= 1
    if intentos == 0:
        print("Usuario bloqueado")
        exit()
print("_" * 50 + "")
print("Usuario", usuario)
print("Tu saldo es: ", saldo)
print("_" * 50 + "")
print("MENU")

while True:
    print("1. Retirar dinero")
    print("2. Depositar dinero")
    print("3. Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        retirar = float(input("Ingrese la cantidad a retirar: "))
        if retirar > saldo:
            print("Saldo insuficiente")
        else:
            saldo -= retirar
            print("Retiro exitoso")
    elif opcion == 2:
        depositar = float(input("Ingrese la cantidad a depositar: "))
        saldo += depositar
        print("Deposito exitoso")
    elif opcion == 3:
        print("Gracias por usar el cajero automatico")
        break