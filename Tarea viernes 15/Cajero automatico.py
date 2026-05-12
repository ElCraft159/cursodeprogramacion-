print("_" * 50 + "")
print("\n" "Bienvenido al cajero automatico")
print("_" * 50 + "")
saldo = 1000
pin = ""
print("Create una cuenta")
usuario = input("Ingresar tu nombre: ").upper()
intentos = 3
print("_" * 50 + "")
print(f"Crea una contraseña de 4 digitos numericos tienes {intentos} intentos")
while intentos > 0:
    pin = int(input("Ingrese un pin: "))
    if pin >= 1000 and pin <= 9999:
         print("_" * 50 + "")
         print("Contrasena creada exitosamente")
         break
    else:
        print("_" * 50 + "")
        print("Pin incorrecto")
        intentos -= 1
    if intentos == 0:
        print("_" * 50 + "")
        print("Has agotado tus intentos")
        exit()            
print("_" * 50 + "")

print("Iniciar sesion")
print("Bienvenido", usuario)
intento = 3
while intento > 0:
    contra = int(input("Ingrese tu pin: "))
    if contra == pin:
        print("_" * 50 + "")
        print("\n""Sesion iniciada")
        break
    else:
        print("_" * 50 + "")
        print("Contrasena incorrecta")
        intento -= 1
    if intento == 0:
        print("_" * 50 + "")
        print("Usuario bloqueado")
        print("_" * 50 + "")
        exit()
print("_" * 50 + "")
print("Usuario", usuario)
print("Tu saldo es: ", saldo ,"$")
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
        print("_" * 50 + "")
        retirar = int(input("Ingrese la cantidad a retirar: "))
        if retirar > saldo:
            print("_" * 50 + "")
            print("Saldo insuficiente")
            print("Saldo restante: ", saldo,"$")
        elif retirar % 10 != 0:
            print("_" * 50 + "")
            print("Solo puedes retirar multiplos de 10") 
        else:
            saldo -= retirar
            print("_" * 50 + "")
            print(f"Retiro exitoso {retirar}$")
            b100 = retirar // 100
            resto = retirar % 100
            b50 = resto // 50
            resto = resto % 50
            b20 = resto // 20
            resto = resto % 20
            b10 = resto // 10
            print(f"entregado: {b10} Billetes de 10, {b20} Billetes de 20, {b50} Billetes de 50, {b100} Billetes de 100: {retirar}$")
            print(f"Saldo restante: ", saldo,"$")
        print("_" * 50 + "")
    elif opcion == 2:
        print("_" * 50 + "")
        depositar = int(input("Ingrese la cantidad a depositar: "))
        saldo += depositar
        print("_" * 50 + "")
        print("Deposito exitoso")
        print(f"Saldo actual: ", saldo,"$")
        print("_" * 50 + "")
    elif opcion == 3:
        print("_" * 50 + "")
        print("Tu saldo es: ", saldo,"$")
        print("_" * 50 + "")    
    elif opcion == 4:
        print("_" * 50 + "")
        print("Gracias por usar el cajero automatico")
        print("_" * 50 + "")
        break
    else:
        print("Opcion no valida del menu")