print("_" * 50 + "")
print("\n" "Bienvenido al cajero automatico")
print("_" * 50 + "")
saldo = 1000
print("Create una cuenta")
usuario = input("Ingresar tu usuario: ").upper()
intentos = 3
print(f"Crea una contraseña de 4 digitos numericos tienes {intentos} intentos")
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
print("\t" "---MENU---")

while True:
    print("1. Retirar dinero")
    print("2. Depositar dinero")
    print("3. Consultar saldo")
    print("4. Salir")
    print("_" * 50 + "")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        retirar = int(input("Ingrese la cantidad a retirar: "))
        if retirar > saldo:
            print("Saldo insuficiente")
        elif retirar % 10 != 0:
            print("Solo puedes retirar multiplos de 10") 
        else:
            saldo -= retirar
            print(f"Retiro exitoso {retirar}$")
            b100 = retirar // 100
            resto = retirar % 100
            b50 = resto // 50
            resto = resto % 50
            b20 = resto // 20
            resto = resto % 20
            b10 = resto // 10
            print(f"entregado: {b10} Billetes de 10, {b20} Billetes de 20, {b50} Billetes de 50, {b100} Billetes de 100: {retirar}$")
            print(f"Saldo restante: ", saldo)
        print("_" * 50 + "")
    elif opcion == 2:
        depositar = int(input("Ingrese la cantidad a depositar: "))
        saldo += depositar
        print("Deposito exitoso")
        print(f"Saldo actual: ", saldo)
        print("_" * 50 + "")
    elif opcion == 3:
        print("Tu saldo es: ", saldo)
        print("_" * 50 + "")    
    elif opcion == 4:
        print("Gracias por usar el cajero automatico")
        break
    else:
        print("Opcion no valida del menu")