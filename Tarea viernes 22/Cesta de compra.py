lista_productos = {
    1: {"articulo": "Harina pan", "precio": 1.50}, 
    2: {"articulo": "Leche", "precio": 3.75},
    3: {"articulo": "Yogurt", "precio": 2.50},
    4: {"articulo": "Cafe", "precio": 4.00},
    5: {"articulo": "Cafe con leche", "precio": 5.00},
    6: {"articulo": "Chocolate", "precio": 2.00},
} 

def mostrar_menu():    
    print("_" * 20 + "\n")
    print("----Menu----\n")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Mostrar cesta de compra")
    print("4. Calcular total")
    print("5. Salir")
    print("_" * 20 + "\n")

def agregar_producto(cesta):
    print("_" * 20 + "\n")
    print("----Agregar producto----\n")
    for producto, valor in lista_productos.items():
        print(f"[{producto}] {valor['articulo']} - {valor['precio']}$")
    print("_" * 20 + "\n")
    
    try: 
        seleccion = int(input("Seleccione el producto que desea agregar: "))
        if seleccion in lista_productos:
            sele = lista_productos[seleccion]
            
            encontrado = False
            for elemento in cesta:
                if elemento['articulo'] == sele['articulo']:
                    elemento['cantidad'] += 1
                    encontrado = True
                    break
            
            if not encontrado:
                nuevo_item = {
                    "articulo": sele["articulo"],
                    "precio": sele["precio"],
                    "cantidad": 1
                }
                cesta.append(nuevo_item)
                
            print(f"{sele['articulo']} agregado a la cesta")
        else:
            print("Producto no disponible")
    except ValueError:
        print("Por favor ingrese un numero")

def eliminar_producto(cesta):
    print("_" * 20 + "\n")
    print("----Eliminar producto----\n")
    hay_productos = mostrar_cesta(cesta)
    if not hay_productos:
        return
    
    try:
        print("_" * 20 + "\n") 
        seleccion = int(input("Seleccione el producto que desea eliminar: "))
        if 1 <= seleccion <= len(cesta):
            articulo_seleccionado = cesta[seleccion - 1]
            articulo_seleccionado["cantidad"] -= 1
            if articulo_seleccionado["cantidad"] == 0:
                cesta.pop(seleccion - 1)
                print(f"{articulo_seleccionado['articulo']} eliminado de la cesta")
            else:
                print(f"Se redujo la cantidad de {articulo_seleccionado['articulo']}\nQuedan {articulo_seleccionado['cantidad']}")
        else:
            print("Producto no disponible")
    except ValueError:
        print("Por favor ingrese un numero")

def mostrar_cesta(cesta):
    print("\n----Tu cesta de compra----")
    if not cesta:
        print("Tu cesta está vacía.")
        return False

    for indice, elemento in enumerate(cesta, start=1):
        cant = elemento['cantidad']
        subtotal = elemento['precio'] * cant
        print(f"{indice}. {elemento['articulo']} x{cant} - {subtotal:.2f}$")
        
    return True

def calcular_total(cesta):
    print("_" * 20 + "\n")
    print("----Total----\n")
    if not cesta:
        print("Tu cesta de compra esta vacia")
        return
    mostrar_cesta(cesta)
    total = sum(elemento["precio"] * elemento["cantidad"] for elemento in cesta)
    print("_" * 20 + "\n")
    print(f"Total: {total:.2f}$")
    print("_" * 20 + "\n") 

cesta = []
programa_activo = True

while programa_activo:
    mostrar_menu()
    try:
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            agregar_producto(cesta)
        elif opcion == 2:
            eliminar_producto(cesta)
        elif opcion == 3:
            mostrar_cesta(cesta)
        elif opcion == 4:
            calcular_total(cesta)
        elif opcion == 5:
            print("Saliendo de la cesta de compra")
            programa_activo = False
        else:
            print("Opcion no disponible")
    except ValueError:
        print("Por favor ingrese un numero")