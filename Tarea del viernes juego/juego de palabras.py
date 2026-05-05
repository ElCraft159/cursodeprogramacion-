
print("Bienvenido al juego de Norwin")
print("Espero Que el profesor me ponga 20 :)")
print("Empezemos con el juego")
genero = input("¿Cual es tu genero? (MASCULINO/FEMENINO):").lower().strip()
if genero == "masculino":
    print("Bienvenido, caballero. Tu aventura comienza ahora.")
elif genero == "femenino":
    print("Bienvenida, dama. Tu aventura comienza ahora.")
else:
    print("Has elegido un camino mistico. Tu indentidad es un misterio.")
print("Te despiertas en un bosque oscuro, sin recordar cómo llegaste allí. A tu lado, encuentras una espada antigua y un mapa desgastado." \
"¿Qué decides hacer?")
print("1. Tomar la espada y seguir el mapa.")
print("2. Explorar el bosque sin el mapa.")
print("3. Dejar la espada y seguir el mapa.")
decision1 = input("Ingresa el número de tu decisión: ")
if decision1 == "1":
    print("Agarras la espada y sigues el mapa, adentrándote en el bosque. Después de caminar por un rato, encuentras una cabaña abandonada.")
    print("¿Qué decides hacer?")
    print("1. Entrar a la cabaña.")
    print("2. Continuar caminando por el bosque.")
    decision2 = input("Ingresa el número de tu decisión: ").lower().strip()
    if decision2 == "1":
        print("Entras a la cabaña y consigues un hada magica que esta encadenada." "¿Qué haces?")
        print("1. Liberar al hada.")
        print("2. Dejar al hada y salir de la cabaña.")
        decision3 = input("Ingresa el número de tu decisión: ").lower().strip()
        if decision3 == "1":
            print("Liberas al hada")
            print("El hada te agradece y te concede un deseo. ¿Qué deseas?")
            print("1. Deseo de inmortalidad.'Viste from?'")
            print("2. Deseo de riqueza. 'Lo mas obvio'")
            print("3. Deseo de volver a casa. 'Es la mas facil no lo hagas' ")
            decision4 = input("Ingresa el número de tu decisión: ").lower().strip()
            if decision4 == "1":
                print("Deseas inmortalidad, pero el hada te advierte que la inmortalidad viene con una maldición.")
                print("Te conviertes en un ser inmortal, pero con hambre y sed de sangre humana una especie de vampiro, y te condena a vagar por la eternidad buscando víctimas para saciar tu sed.")
                print("has vivido muchos años vistes naciones construirse y destruirse, buscas una forma de liberarte de esta maldición.")
                print("Después de siglos de búsqueda, finalmente encuentras un antiguo libro que contiene un hechizo para romper la maldición, sin embargo, el proceso es peligroso y no garantiza el éxito.")
                decision5 = input("¿Deseas intentar romper la maldición? (SI/NO): ").lower().strip()
                if decision5 == "si":
                    print("Decides intentar romper la maldición. lees el hechizo hay un ingrediente dificil de conseguir, sangre de una virgen, pero te das cuenta que las unicas virgenes son bebes y te resistes a matar a un bebe, pero eso significa que no romperas la maldición y sigues vagando por la eternidad como un ser inmortal.")
                    print("tienes que tomar una decision dificil, matar a un bebe o vivir con la maldicion, que decides?")
                    decision6 = input("¿Deseas matar a un bebe para romper la maldición? (SI/NO): ").lower().strip()
                    if decision6 == "si":
                        print("Decides matar a un bebe para romper la maldición. Realizas el hechizo con la sangre del bebe y logras romper la maldición, pero te sientes culpable por lo que has hecho y te das cuenta de que la inmortalidad no era tan deseable después de todo.")
                        print("Fin del juego.")
                    elif decision6 == "no":
                        print("Decides no matar a un bebe para romper la maldición. Aceptas tu destino como un ser inmortal y continúas vagando por la eternidad, enfrentando los desafíos y peligros que conlleva tu nueva existencia.")
                        print("Fin del juego.") 
                        #aqui qeude 
                elif decision5 == "no":
                    print("Decides no intentar romper la maldición y continúas vagando por la eternidad como un ser inmortal, enfrentando los desafíos y peligros que conlleva tu nueva existencia.")
                    print("Fin del juego.")
                else:
                    print("Opción no válida. Fin del juego.")
            elif decision4 == "2":
                print("Deseas riqueza, y el hada te concede una bolsa llena de oro. Sin embargo, pronto descubres que la riqueza no trae felicidad y te sientes vacío por dentro. Fin del juego.")
            elif decision4 == "3":
                print("Deseas volver a casa, y el hada te concede tu deseo. Regresas a tu hogar sano y salvo, pero siempre recordarás tu aventura en el bosque. Fin del juego.")
            else:
                print("Opción no válida. Fin del juego.")
        elif decision3 == "2":
            print("Dejas al hada y sales de la cabaña.")
        else:
            print("Solo tienes dos opciones, no seas tonto.")
    elif decision2 == "2":
        print("Decides continuar caminando por el bosque, pero te pierdes y no encuentras el camino de regreso. Fin del juego.")
    else:
        print("Opción no válida. Fin del juego.")