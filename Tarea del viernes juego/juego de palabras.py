
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
                elif decision5 == "no":
                    print("Decides no intentar romper la maldición y continúas vagando por la eternidad como un ser inmortal, enfrentando los desafíos y peligros que conlleva tu nueva existencia.")
                    print("Fin del juego.")
                else:
                    print("Opción no válida.")
            elif decision4 == "2":
                print("Deseas riqueza, y el hada te concede una bolsa llena de oro. Sin embargo una bolsa de oro no es tan util en el bosque, y te das cuenta de que el oro no te ayudará a sobrevivir ni a encontrar una salida del bosque.")
                print("Te añade peso a tu mochila y te hace mas lento, lo que dificulta tu aventura en el bosque.")
                print("Tienes varias opciones, puedes dejar tu bolsa de oro o dejar tu espada para aligerar la carga")
                print("¿Qué decides hacer?")
                print("Dejar el oro.")
                print("Dejar la espada.")
                decision5 = input("Ingresa tu decisión: ").lower().strip()
                if decision5 == "dejar el oro": 
                    print("Decides dejar el oro, lo dejas en un claro del bosque y sigues tu aventura sin el peso extra. poco tiempo despues encuentras un oso hambriento que te ataca, pero gracias a tu espada logras defenderte y salir victorioso del encuentro. Sin la espada, habrías sido una presa fácil para el oso.")
                    print("Gracias a él alboroto del combate llega un grupo de cazadores que te encuentran y te ayudan a salir del bosque, llevándote de regreso a la civilización. Sin el oro, pero con nuevos amigos y una historia increíble para contar.")
                    print("Le ganaste a un oso eso es un win.")
                elif decision5 == "dejar la espada":
                    print("Decides dejar la espada, lo dejas en un claro del bosque y sigues tu aventura sin la espada. Sin embargo, te das cuenta de que la espada podría haber sido útil para defenderte de los peligros del bosque.")
                    print("Mientras caminas por el bosque, te encuentras con un oso hambriento que te ataca. Sin la espada para defenderte, eres una presa fácil para el oso y terminas siendo devorado.")
                    print("GAME OVER !LA AVARICIA!.")
            elif decision4 == "3":
                print("Deseas volver a casa, y el hada te concede tu deseo. Regresas a tu hogar sano y salvo, pero sin historias para contar y te toca trabajar de mesero en un bar.")
            else:
                print("Opción no válida..")
        elif decision3 == "2":
            print("Dejas al hada y sales de la cabaña.")
            print("Mientras caminas por el bosque, te encuentras con un grupo de bandidos que te atacan y te roban la espada, solo te dejan con el mapa miras detenidamente el mapa ves lo que parece ser un manantial de agua cerca de tu ubicación actual, decides ir hacia el manantial para buscar ayuda.")
            print("Al llegar al manantial, encuentras a un anciano sabio que te ofrece ayuda. Te dice que el manantial tiene propiedades curativas y puede ayudarte a recuperar tu fuerza. Sin embargo, te pide a cambio que le ayudes a resolver un acertijo para poder acceder al agua.")
            print("El acertijo es el siguiente: 'Tengo ciudades, pero no casas. Tengo montañas, pero no árboles. Tengo agua, pero no peces. ¿Qué soy?'")
            respuesta = input("Ingresa tu respuesta: ").lower().strip()
            if respuesta == "mapa":
                print("Respondes correctamente al acertijo y el anciano te permite beber del manantial. Recuperas tu fuerza y te sientes renovado. El anciano te agradece por resolver el acertijo y te ofrece un consejo para continuar tu aventura: 'Sigue el camino del sol poniente, allí encontrarás lo que buscas.'")
                print("Sigues el consejo del anciano y te diriges hacia el oeste, siguiendo el camino del sol poniente. Después de caminar por un tiempo, encuentras una puerta antigua tallada en la roca. La puerta tiene un símbolo misterioso grabado en ella.")
                print("¿Qué decides hacer?")
                print("1. Intentar abrir la puerta.")
                print("2. Continuar caminando por el bosque.")
                print("3. Volver al manantial para quedarte con el anciano y apreder de él.")
                decision7 = input("Ingresa el número de tu decisión: ").lower().strip()
                if decision7 == "1":
                    print("Intentas abrir la puerta, pero está cerrada con llave. Sin embargo, encuentras una pequeña ranura en la puerta que parece ser para una llave. Buscas alrededor y encuentras una llave escondida debajo de una piedra cercana. Usas la llave para abrir la puerta y descubres un tesoro escondido dentro.")
                    print("El tesoro contiene una posion que brilla como el oro, dudas el beberla, pero decides probarla y poco a poco te vas convirtiendo en oro y receurdas esa frases que dicen los viejos no todo lo que brilla es oro, y te das cuenta de que has caído en una trampa y te has convertido en una estatua de oro.")
                    print("Gran forma de morir.")
                elif decision7 == "2":
                    print("Decides continuar caminando por el bosque, ves a lo lejos un rio y al lado contrario una montaña")
                    print("¿A donde vas?")
                    print("Ir al rio")
                    print("Ir a la montaña")
                    decision8 = input("Ingresa tu decisión: ").lower().strip()
                    if decision8 == "ir al rio":
                        print("Decides ir al rio, al llegar al rio ves un barco viejo, decides subirte al barco y navegar rio abajo, despues de un rato nevegando ves una isla a lo lejos")
                        print("¿Decides ir a la isla o seguir navegando por el rio?")
                        decision9 = input("Ingresa tu decisión: ").lower().strip()
                        if decision9 == "ir a la isla":
                            print("Decides ir a la isla, al llegar consigues un pueblo pides ayudas para llegar de nuevo a casa.")
                            print("Por fin logras regresar a casa con las manos vacias pero vivo.")
                        elif decision9 == "seguir navegando por el rio":
                            print("Decides seguir navegando por el rio, despues de un rato navegando por el rio te encuentras con un monstruo marino que te ataca y te arrastra al fondo del rio.")
                            print("Para tu mala suerte le gusta la carne de humanos.")
                            print("Eres comida de peces.")
                    elif decision8 == "ir a la montaña":
                        print("Decides ir a la montaña, al llegar a la montaña ves una cueva, decides entrar a la cueva y encuentras un dragón dormido, decides acercarte al dragón para ver si tiene algo de valor, pero el dragón se despierta y te hace una oferta.")
                        print("Te dice que el es el guardián de un tesoro escondido en la montaña, y te ofrece una prueba para ganar el tesoro. La prueba consiste en responder a una pregunta.")
                        print("En el corazon de la montaña, custodio lo que los hombres matan por poseer. Si me hablas, te ignoro, si me robas, te encuentro. Brillo mas que el sol, pero vivo en la oscuridad total. ¿Qué soy?")
                        respuesta2 = input("Ingresa tu respuesta: ").lower().strip()
                        if respuesta2 == "la codicia":
                            print("Respondes correctamente a la pregunta del dragón y el te concede acceso al tesoro escondido en la montaña. El tesoro contiene una espada mágica que te otorga habilidades extraordinarias y te permite regresar a casa con seguridad.")
                            print("Gracias por jugar.")
                        else:
                            print("Respuesta incorrecta. El dragón se enoja y te devorá, terminando tu aventura de manera trágica.")
                            print("GAME OVER.")
                    else:
                        print("Opción no válida.")
                elif decision7 == "3":
                    print("Decides volver al manantial para quedarte con el anciano y aprender de él")
                    print("El anciano te recibe con los brazos abiertos y te enseña sus conocimientos sobre el bosque y sus secretos. Pasas un tiempo aprendiendo de él y desarrollando tus habilidades, convirtiéndote en un aventurero más sabio y preparado para enfrentar los desafíos del bosque.")
                    print("AHORA TU ERES EL GUARDIAL DEL MANANTIAL.")
                    print("Hubiera preferido el final de ser inmortal.")
    elif decision2 == "2":
        print("Decides continuar caminando por el bosque, pero te pierdes y no encuentras el camino de regreso.")
        print("intentas buscar un camino para encotrar tesoro.")
        print("Despues de caminar po un tiempo, encuentras lo que parace una masmorra oculta entre los arboles.")
        print("¿Que haces?")
        print("Entrar a la masmorra.")
        print("Seguir caminando por el bosque.")
        decision3 = input("Ingresa tu decisión: ").lower().strip()
        if decision3 == "entrar a la masmorra":
            print("Decides entrar a la masmorra, al entrar encuentras un monstruo gigante que te ataca, te defiendes con todo lo que tienes o no todo recuerdas esa abilidad que tienes.")
            print("Es ahora o nunca para usarla")
            print("Usa el copmbo correcto para derrotar al monstruo")
            print("1. ↓ ↘ → ↓ ↘ → + Botón de Beast (Media luna hacia adelante dos veces)")
            print("2. → ↓ ↘ + x Botón de Beast (Media luna hacia atras)")
            print("3. ↓ ↘ → + y Botón de Beast (Media luna hacia izquierda)")
            print("4. → ↘ ↓ + x oBotón de Beast (Media luna hacia derecha)")
            decision4 = input("Ingresa tu decisión: ").lower().strip()
            if decision4 == "1":
                print("Usas el combo correcto y logras derrotar al monstruo, encontrando un tesoro escondido en la masmorra. El tesoro contiene una llave mágica que te permite abrir una puerta secreta en el bosque, llevándote de regreso a la civilización con riquezas y aventuras para contar.")
            else: 
                print("Usas el combo incorrecto y el monstruo te derrota, terminando tu aventura de manera trágica.")
        elif decision3 == "seguir caminando por el bosque":
            print("Decides seguir caminando por el bosque, después de un tiempo, encuentras un grupo de cazadores que te encuentran y te quieres matar peleas con ellos vences a dos de ellos pero el tercero te derrota y te marta para tu mala suerte es un nigromante asi que te revivi como un esqueleto y le sirves por la eternidad,")
            print("el peor de los finales")
        else:
            print("Opción no válida.")
elif decision1 == "2":
    print("Decides explorar el bosque sin el mapa, pero te pierdes y no encuentras el camino de regreso. Después de caminar por un tiempo, encuentras una cabaña abandonada.")
    print("¿Qué decides hacer?")