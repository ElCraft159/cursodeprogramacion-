
print("Bienvenido al juego de Norwin")
print("Espero Que el profesor me ponga 20 :) ")
print("Empezemos con el juego")
genero = input("¿Cual es tu genero? (MASCULINO/FEMENINO):").strip().upper()
if genero == "MASCULINO":
    print("Bienvenido, caballero. Tu aventura comienza ahora.")
elif genero == "FEMENINO":
    print("Bienvenida, dama. Tu aventura comienza ahora.")
else:
    print("Has elegido un camino mistico. Tu indentidad es un misterio.")
print("Te despiertas en un bosque oscuro, sin recordar cómo llegaste allí. A tu lado, encuentras una espada antigua y un mapa desgastado." \
"¿Qué decides hacer?")
print("TOMAR LA ESPADA Y SEGUIR EL MAPA.")
print("DEJAR LA ESPADA Y SEGUIR EL MAPA.")
print("EXPLORAR EL BOSQUE SIN EL MAPA.")
decision1 = input("Ingresa tu decisión: ").strip().upper()
if decision1 == "TOMAR LA ESPADA Y SEGUIR EL MAPA":
    print("Agarras la espada y sigues el mapa, adentrándote en el bosque. Después de caminar por un rato, encuentras una cabaña abandonada.")
    print("¿Qué decides hacer?")
    print("ENTRAR A LA CABAÑA.")
    print("CONTINUAR CAMINANDO POR EL BOSQUE.")
    decision2 = input("Ingresa tu decisión: ").strip().upper()
    if decision2 == "ENTRAR A LA CABAÑA":
        print("Entras a la cabaña y consigues un hada magica que esta encadenada." "¿Qué haces?")
        print("LIBERAR AL HADA.")
        print("DEJAR AL HADA Y SALIR DE LA CABAÑA.")
        decision3 = input("Ingresa tu decisión: ").strip().upper()
        if decision3 == "LIBERAR AL HADA":
            print("Liberas al hada")
            print("El hada te agradece y te concede un deseo. ¿Qué deseas?")
            print("DESEO DE INMORTALIDAD.'VISTE FROM?'")
            print("DESEO DE RIQUEZA. 'LO MAS OBVIO'")
            print("DESEO DE VOLVER A CASA. 'ES LA MAS FACIL NO LO HAGAS' ")
            decision4 = input("Ingresa tu decisión: ").strip().upper()
            if decision4 == "DESEO DE INMORTALIDAD":
                print("Deseas inmortalidad, pero el hada te advierte que la inmortalidad viene con una maldición.")
                print("Te conviertes en un ser inmortal, pero con hambre y sed de sangre humana una especie de vampiro, y te condena a vagar por la eternidad buscando víctimas para saciar tu sed.")
                print("has vivido muchos años vistes naciones construirse y destruirse, buscas una forma de liberarte de esta maldición.")
                print("Después de siglos de búsqueda, finalmente encuentras un antiguo libro que contiene un hechizo para romper la maldición, sin embargo, el proceso es peligroso y no garantiza el éxito.")
                decision5 = input("¿Deseas intentar romper la maldición? (SI/NO): ").strip().upper()
                if decision5 == "SI":
                    print("Decides intentar romper la maldición. lees el hechizo hay un ingrediente dificil de conseguir, sangre de una virgen, pero te das cuenta que las unicas virgenes son bebes y te resistes a matar a un bebe, pero eso significa que no romperas la maldición y sigues vagando por la eternidad como un ser inmortal.")
                    print("tienes que tomar una decision dificil, matar a un bebe o vivir con la maldicion, que decides?")
                    decision6 = input("¿Deseas matar a un bebe para romper la maldición? (SI/NO): ").strip().upper()
                    if decision6 == "SI":
                        print("Decides matar a un bebe para romper la maldición. Realizas el hechizo con la sangre del bebe y logras romper la maldición, pero te sientes culpable por lo que has hecho y te das cuenta de que la inmortalidad no era tan deseable después de todo.")
                        print("Fin del juego.")
                    elif decision6 == "NO":
                        print("Decides no matar a un bebe para romper la maldición. Aceptas tu destino como un ser inmortal y continúas vagando por la eternidad, enfrentando los desafíos y peligros que conlleva tu nueva existencia.")
                        print("Fin del juego.")  
                elif decision5 == "NO":
                    print("Decides no intentar romper la maldición y continúas vagando por la eternidad como un ser inmortal, enfrentando los desafíos y peligros que conlleva tu nueva existencia.")
                    print("Fin del juego.")
                else:
                    print("Opción no válida.")
            elif decision4 == "DESEO DE RIQUEZA":
                print("Deseas riqueza, y el hada te concede una bolsa llena de oro. Sin embargo una bolsa de oro no es tan util en el bosque, y te das cuenta de que el oro no te ayudará a sobrevivir ni a encontrar una salida del bosque.")
                print("Te añade peso a tu mochila y te hace mas lento, lo que dificulta tu aventura en el bosque.")
                print("Tienes varias opciones, puedes dejar tu bolsa de oro o dejar tu espada para aligerar la carga")
                print("¿Qué decides hacer?")
                print("Dejar el oro.")
                print("Dejar la espada.")
                decision5 = input("Ingresa tu decisión: ").strip().upper()
                if decision5 == "DEJAR EL ORO": 
                    print("Decides dejar el oro, lo dejas en un claro del bosque y sigues tu aventura sin el peso extra. poco tiempo despues encuentras un oso hambriento que te ataca, pero gracias a tu espada logras defenderte y salir victorioso del encuentro. Sin la espada, habrías sido una presa fácil para el oso.")
                    print("Gracias a él alboroto del combate llega un grupo de cazadores que te encuentran y te ayudan a salir del bosque, llevándote de regreso a la civilización. Sin el oro, pero con nuevos amigos y una historia increíble para contar.")
                    print("Le ganaste a un oso eso es un win.")
                elif decision5 == "DEJAR LA ESPADA":
                    print("Decides dejar la espada, lo dejas en un claro del bosque y sigues tu aventura sin la espada. Sin embargo, te das cuenta de que la espada podría haber sido útil para defenderte de los peligros del bosque.")
                    print("Mientras caminas por el bosque, te encuentras con un oso hambriento que te ataca. Sin la espada para defenderte, eres una presa fácil para el oso y terminas siendo devorado.")
                    print("GAME OVER !LA AVARICIA!.")
            elif decision4 == "DESEO DE VOLVER A CASA":
                print("Deseas volver a casa, y el hada te concede tu deseo. Regresas a tu hogar sano y salvo, pero sin historias para contar y te toca trabajar de mesero en un bar.")

            else:
                print("Opción no válida..")
        elif decision3 == "DEJAR AL HADA Y SALIR DE LA CABAÑA":
            print("Dejas al hada y sales de la cabaña.")
            print("Mientras caminas por el bosque, te encuentras con un grupo de bandidos que te atacan y te roban la espada, solo te dejan con el mapa miras detenidamente el mapa ves lo que parece ser un manantial de agua cerca de tu ubicación actual, decides ir hacia el manantial para buscar ayuda.")
            print("Al llegar al manantial, encuentras a un anciano sabio que te ofrece ayuda. Te dice que el manantial tiene propiedades curativas y puede ayudarte a recuperar tu fuerza. Sin embargo, te pide a cambio que le ayudes a resolver un acertijo para poder acceder al agua.")
            print("El acertijo es el siguiente: 'Tengo ciudades, pero no casas. Tengo montañas, pero no árboles. Tengo agua, pero no peces. ¿Qué soy?'")
            respuesta = input("Ingresa tu respuesta: ").strip().upper()
            if respuesta == "MAPA":
                print("Respondes correctamente al acertijo y el anciano te permite beber del manantial. Recuperas tu fuerza y te sientes renovado. El anciano te agradece por resolver el acertijo y te ofrece un consejo para continuar tu aventura: 'Sigue el camino del sol poniente, allí encontrarás lo que buscas.'")
                print("Sigues el consejo del anciano y te diriges hacia el oeste, siguiendo el camino del sol poniente. Después de caminar por un tiempo, encuentras una puerta antigua tallada en la roca. La puerta tiene un símbolo misterioso grabado en ella.")
                print("¿Qué decides hacer?")
                print("INTENTAR ABRIR LA PUERTA.")
                print("CONTINUAR CAMINANDO POR EL BOSQUE.")
                print("VOLVER AL MANANTIAL PARA QUEDARTE CON EL ANCIANO Y APREDER DE ÉL.")
                decision7 = input("Ingresa tu decisión: ").strip().upper()
                if decision7 == "INTENTAR ABRIR LA PUERTA":
                    print("Intentas abrir la puerta, pero está cerrada con llave. Sin embargo, encuentras una pequeña ranura en la puerta que parece ser para una llave. Buscas alrededor y encuentras una llave escondida debajo de una piedra cercana. Usas la llave para abrir la puerta y descubres un tesoro escondido dentro.")
                    print("El tesoro contiene una posion que brilla como el oro, dudas el beberla, pero decides probarla y poco a poco te vas convirtiendo en oro y receurdas esa frases que dicen los viejos no todo lo que brilla es oro, y te das cuenta de que has caído en una trampa y te has convertido en una estatua de oro.")
                    print("Gran forma de morir.")
                elif decision7 == "CONTINUAR CAMINANDO POR EL BOSQUE":
                    print("Decides continuar caminando por el bosque, ves a lo lejos un rio y al lado contrario una montaña")
                    print("¿A donde vas?")
                    print("Ir al rio")
                    print("Ir a la montaña")
                    decision8 = input("Ingresa tu decisión: ").strip().upper()
                    if decision8 == "IR AL RIO":
                        print("Decides ir al rio, al llegar al rio ves un barco viejo, decides subirte al barco y navegar rio abajo, despues de un rato nevegando ves una isla a lo lejos")
                        print("¿Decides ir a la isla o seguir navegando por el rio?")
                        decision9 = input("Ingresa tu decisión: ").strip().upper()
                        if decision9 == "IR A LA ISLA":
                            print("Decides ir a la isla, al llegar consigues un pueblo pides ayudas para llegar de nuevo a casa.")
                            print("Por fin logras regresar a casa con las manos vacias pero vivo.")
                        elif decision9 == "SEGUIR NAVEGANDO POR EL RIO":
                            print("Decides seguir navegando por el rio, despues de un rato navegando por el rio te encuentras con un monstruo marino que te ataca y te arrastra al fondo del rio.")
                            print("Para tu mala suerte le gusta la carne de humanos.")
                            print("Eres comida de peces.")
                    elif decision8 == "IR A LA MONTAÑA":
                        print("Decides ir a la montaña, al llegar a la montaña ves una cueva, decides entrar a la cueva y encuentras un dragón dormido, decides acercarte al dragón para ver si tiene algo de valor, pero el dragón se despierta y te hace una oferta.")
                        print("Te dice que el es el guardián de un tesoro escondido en la montaña, y te ofrece una prueba para ganar el tesoro. La prueba consiste en responder a una pregunta.")
                        print("En el corazon de la montaña, custodio lo que los hombres matan por poseer. Si me hablas, te ignoro, si me robas, te encuentro. Brillo mas que el sol, pero vivo en la oscuridad total. ¿Qué soy?")
                        respuesta2 = input("Ingresa tu respuesta: ").strip().upper()
                        if respuesta2 == "LA CODICIA":
                            print("Respondes correctamente a la pregunta del dragón y el te concede acceso al tesoro escondido en la montaña. El tesoro contiene una espada mágica que te otorga habilidades extraordinarias y te permite regresar a casa con seguridad.")
                            print("Gracias por jugar.")
                        else:
                            print("Respuesta incorrecta. El dragón se enoja y te devorá, terminando tu aventura de manera trágica.")
                            print("GAME OVER.")
                    else:
                        print("Opción no válida.")
                elif decision7 == "VOLVER AL MANANTIAL":
                    print("Decides volver al manantial para quedarte con el anciano y aprender de él")
                    print("El anciano te recibe con los brazos abiertos y te enseña sus conocimientos sobre el bosque y sus secretos. Pasas un tiempo aprendiendo de él y desarrollando tus habilidades, convirtiéndote en un aventurero más sabio y preparado para enfrentar los desafíos del bosque.")
                    print("AHORA TU ERES EL GUARDIAL DEL MANANTIAL.")
                    print("Hubiera preferido el final de ser inmortal.")
    elif decision2 == "CONTINUAR CAMINANDO POR EL BOSQUE":
        print("Decides continuar caminando por el bosque, pero te pierdes y no encuentras el camino de regreso.")
        print("intentas buscar un camino para encotrar tesoro.")
        print("Despues de caminar po un tiempo, encuentras lo que parace una masmorra oculta entre los arboles.")
        print("¿Que haces?")
        print("Entrar a la masmorra.")
        print("Seguir caminando por el bosque.")
        decision3 = input("Ingresa tu decisión: ").strip().upper()
        if decision3 == "ENTRAR A LA MASMORRA":
            print("Decides entrar a la masmorra, al entrar encuentras un monstruo gigante que te ataca, te defiendes con todo lo que tienes o no todo recuerdas esa abilidad que tienes.")
            print("Es ahora o nunca para usarla")
            print("Usa el combo correcto para derrotar al monstruo")
            print("1. ↓ ↘ → ↓ ↘ → + Botón de Beast (Media luna hacia adelante dos veces)")
            print("2. → ↓ ↘ + x Botón de Beast (Media luna hacia atras)")
            print("3. ↓ ↘ → + y Botón de Beast (Media luna hacia izquierda)")
            print("4. → ↘ ↓ + x oBotón de Beast (Media luna hacia derecha)")
            decision4 = input("Ingresa tu decisión: ").strip().upper()
            if decision4 == "1":
                print("Usas el combo correcto y logras derrotar al monstruo, encontrando un tesoro escondido en la masmorra. El tesoro contiene una llave mágica que te permite abrir una puerta secreta en el bosque, llevándote de regreso a la civilización con riquezas y aventuras para contar.")
            else: 
                print("Usas el combo incorrecto y el monstruo te derrota, terminando tu aventura de manera trágica.")
        elif decision3 == "SEGUIR CAMINANDO POR EL BOSQUE":
            print("Decides seguir caminando por el bosque, después de un tiempo, encuentras un grupo de cazadores que te encuentran y te quieres matar peleas con ellos vences a dos de ellos pero el tercero te derrota y te marta para tu mala suerte es un nigromante asi que te revivi como un esqueleto y le sirves por la eternidad,")
            print("el peor de los finales")
        else:
            print("Opción no válida.")
elif decision1 == "DEJAR LA ESPADA Y SEGUIR EL MAPA":
    print("Caminando por el bosques te encuentras a un aventurero mal herido")
    print("¿Que quires hacer?")
    print("Ayudar al aventurero")
    print("Ignorar al aventurero")
    print("Rematar al aventurero")
    decision2 = input("Ingresa tu decision: ").strip().upper()
    if decision2 == "AYUDAR AL AVENTURERO":
        print("El aventurero saca una navaja y te apunta con ella")
        print("Le explicas que vas ayudarlo y baja la navaja")
        print("lo ayudas y descubres que es un caballero real bajo la orden de la mano de plata")
        print("te agradece y te pide que si lo puedes ayudar a llegar a la cuidad")
        print("Ayudarlo")
        print("Dejarlo a su suerte")
        decision3 = input("Que haras?: ").strip().upper()
        if decision3 == "AYUDARLO":
            print("Lo ayudas a levata")
            print("sigues las ruta que te dice el caballero")
            print("a la lejania ves lo que parece ser una pequeña aldea, aun esta muy lejos pero ya ves una salida")
            print("la noche ya empiesa a caer")
            print("puedes quedarte y hacer una fogata para pasar la noche o seguir caminando")
            print("Quedarte y descansar")
            print("seguir caminando")
            decision4 = input("Que decides?: ").strip().upper()
            if decision4 == "QUEDARTE Y DESCANSAR":
                print("acuestas al caballero sobre un monto de hojas")
                print("Preparas unas ramas para hacer una hoguera")
                print("al intentar hacer el fuego, el caballero te llama te dice que el te ayudara")
                print("Quedas impresionado al ver que usa un hechiso de fuego para enceder la hoguera")
                print("Te recuestas a descasar")
                print("Te despierta un sonido muy fuerte algo a como un rugido te despierta miras aterrado ¡Un gran leo dientes de sable!")
                print("Te levanstas coges tu espada y te pones en guardia")
                print("Dudas en defenderte o atacar al leon dientes de sable")
                decisio5 = input("¿Defenderte o atacar?: ").strip().upper()
                if decisio5 == "DEFENDERTE":
                    print("Decides defenderte, el leon dientes de sable ataca con sus garras y colmillos afilados, pero logras bloquear sus ataques. Después de un intenso combate, logras vencer al leon dientes de sable, salvando tu vida y la del caballero.")
                    print("El caballero te agradece por tu valentía y te ofrece su amistad. Juntos continúan su viaje hacia la aldea.")
                    print("al llegar a la aldea, el caballero te presenta a sus superiores de la orden de la mano de plata, quienes te ofrecen unirte a su causa y entrenarte como un caballero.")
                    decision6 = input("¿Quieres unirte a la orden de la mano de plata? (SI/NO):").strip().upper()
                    if decision6 == "SI":
                        print("Decides unirte a la orden de la mano de plata, y comienzas tu entrenamiento como un caballero. A lo largo de tu entrenamiento, aprendes habilidades de combate, magia y estrategia, convirtiéndote en un guerrero formidable.")
                        print("Después de completar tu entrenamiento, te embarcas en misiones para proteger a los inocentes y luchar contra las fuerzas del mal, ganando fama y respeto en el reino.")
                        print("Gracias por jugar.'Profe ya no aguanbto massss'")
                    elif decision6 == "NO":
                        print("Decides no unirte a la orden de la mano de plata, y decides seguir tu propio camino como aventurero. Continúas explorando el mundo, enfrentando desafíos y viviendo aventuras por tu cuenta, sin la guía ni el apoyo de la orden.")
                        print("Aunque enfrentas dificultades y peligros, también encuentras momentos de libertad y emoción en tu viaje como aventurero solitario.")
                        print("Gracias por jugar.'Es mejor la livertad' ")
                    else:
                        print("Es una buena propuesta piensalo bien.")
                elif decisio5 == "ATACAR":
                    print("Decides atacar, el leon dientes de sable ataca con sus garras y colmillos afilados, no fue una buena idea atacar, el leon te destroza con sus garras y colmillos.")
                    print("GAME OVER.")        
                else:
                    print("Solo puedes defenderte o atacar.")
            elif decision3 == "DEJARLO A SU SUERTE":
                print("Decides dejarlo a su suerte, y continúas tu camino por el bosque. Sin embargo, te sientes culpable por no haber ayudado al aventurero, y te preguntas qué le habrá pasado.")
                print("Después de un tiempo, encuentras un grupo de cazadores que te encuentran y te cuentan que encontraron el cuerpo sin vida de un aventurero en el bosque, con heridas de batalla. Te das cuenta de que era el aventurero al que decidiste no ayudar.")
                print("Te sientes aún más culpable por tu decisión, y te preguntas si podrías haber hecho algo para salvarlo.")
                print("Los aventureiros te dicen que tiene la chapa de reconocimiento del caballero que encontró muerto en el bosque que al llegar a la aldea la llebara con la orden de la mano de plata.")
                print("Acopañas a llevar la chapa de reconocimiento a la orden de la mano de plata, y al llegar a la aldea, entregan la chapa a los superiores de la orden.")
                print("Te enteras de que tenia familia y hiejos que lo esperaban en casa, y te sientes aún más culpable por no haber ayudado al aventurero, sabiendo que su familia ahora está sufriendo por su pérdida.")
                print("la culpa te consume, te planteas de contar lo que paso a la familia del aventurero, pero temes que eso solo les cause mas dolor")
                print("Duermes y sueñas con el aventurero atormentadote decides que no aguastas mas que haras?")
                print("CONTAR LA VERDAD A LA FAMILIA DEL AVENTURERO")
                print("ACABAR CON EL TOMERTO DE LA CULPA Y ACABAR CON TU VIDA")
                decision7 = input("Ingresa tu decisión: ").strip().upper()
                if decision7 == "CONTAR LA VERDAD A LA FAMILIA DEL AVENTURERO":
                    print("Decides contar la verdad a la familia del aventurero, y te acercas a ellos para compartir lo que sucedió en el bosque. Les cuentas que encontraste al aventurero mal herido, pero decidiste no ayudarlo y continuar tu camino.")
                    print("La familia del aventurero se siente devastada por la noticia, te maldicen y te espulsa de la aldea.")
                    print("Te deja a tu suerte de nuevo en el bosque ahora sin espada ni mapa.")
                    print("Sin nada para defenderte ni para guiarte, es solo cuestión de tiempo antes de que te encuentres con un peligro mortal en el bosque, y termines siendo devorado por una bestia salvaje o muriendo de hambre y sed.")
                    print("Igual al caballero que decidio no ayudarlo.")
                    print("GAME OVER 'Moriste por el poder del guion' ")
                elif decision7 == "ACABAR CON EL TOMERTO DE LA CULPA Y ACABAR CON TU VIDA":
                    print("Decides acabar con el tormento de la culpa y acabar con tu vida.")
                    print("GAME OVER 'Moriste de una forma triste' ")
                else:
                    print("Se que son decisiones difíciles pero tienes que tomar una.")
    elif decision2 == "IGNORAR AL AVENTURERO":
        print("Decides ignorar al aventurero, y continúas tu camino por el bosque.")
        print("Después de un tiempo, encuentras un grupo de cazadores que te encuentran y quee llevan con ellos al caballero que dejaste atrás.")
        print("Te ofrecen ayuda y aceptas.")
        print("ves al caballero, por suerte para ti esta inconsciente y no se da cuenta de que lo dejaste atrás.")
        print("Ellos Regresaran a la aldea para darle atencion medica al caballero, te preguntan que haras tu?")
        print("ACOMPAÑARLOS A LA ALDEA")
        print("SEGUIR TU CAMINO POR EL BOSQUE")
        decision3 = input("Ingresa tu decisión: ").strip().upper()
        if decision3 == "ACOMPAÑARLOS A LA ALDEA":
            print("Decides acompañarlos a la aldea, y te unes a ellos en su viaje hacia la aldea. Durante el viaje, te sientes cada vez más culpable por haber ignorado al aventurero.")
            print("Al llegar a la aldea, los cazadores llevan al caballero al hospital para recibir atención médica. Sin embargo, el caballero sucumbe a sus heridas y muere poco después de llegar a la aldea.")
            print("Te sientes devastado por la noticia de su muerte, y te das cuenta de que tu decisión de ignorarlo no solo lo dejó sin ayuda, sino que también contribuyó a su muerte.")
            print("Buscas redecion por tus acciones, tiene que decidir contar la verdad a la familia del caballero o unirte a la orden de la mano de plata.")
            print("CONTAR LA VERDAD")
            print("UNIRTE A LA ORDEN")
            decision4 = input("Ingresa tu decisión: ").strip().upper()
            if decision4 == "CONTAR LA VERDAD":
                print("Decides contar la verdad a la familia del caballero, y te acercas a ellos para compartir lo que sucedió en el bosque. Les cuentas que encontraste al caballero mal herido, pero decidiste ignorarlo y continuar tu camino.")
                print("La familia del caballero se levanta para confrontarte.")
                print("Por que lo hiciste, preguntan.")
                print("Que respondes? 'Hasta yo me hago esa pregunta' ")
                print("Por idiota, respondes.")
                print("Por miedo, respondes.")
                print("Para ver cual seria la siguiente interacción, respondes.")
                decision5 = input("Ingresa tu respuesta: ").strip().upper()
                if decision5 == "POR IDIOTA":
                    print("Si que lo eres responde la familia.")
                    print("Te golpean hasta que pierdes el conocimiento.")
                    print("Los detiene un sacerdote, El te cura con su magia.")
                    print("Para que te sigan golpeando.")
                    print("Fin del juego 'al parecer no fue una buena idea' ")
                elif decision5 == "POR MIEDO":
                    print("Miedoo a queee.")
                    print("A que pensara que habia sido yo.")
                    print("llegar a la aldea con un caballero muerto, es algo que no se le perdona a nadie.")
                    print("me ahorcan sin siquiera preguntar dices.")
                    print("la familia te da la razon por tu miedo, y te ahorcan sin siquiera preguntar.")
                elif decision5 == "PARA VER CUAL SERIA LA SIGUIENTE INTERACCIÓN":
                    print("profe quiero decirle que esto a estado tedioso a eso sumele los bajones de luz el trabajo no haz sido facil pero me gusta <3 ")
                    print("llamele a esto el nivel secreto o algo asi.")
                    print("son como las 11:30 de la noche y ya no se que mas poner y todavia falta")
                    print("fin del juego 'aqui termina el nivel secreto' ")
                else:
                    print("La tercera pregunta rompe la cuarta pare? 'Escoje bien'.")            
            elif decision4 == "UNIRTE A LA ORDEN":
                print("Decides unirte a la orden de la mano de plata, y te unes a ellos en su misión para proteger a los inocentes y luchar contra las fuerzas del mal. A lo largo de tu tiempo con la orden, aprendes habilidades de combate, magia y estrategia, convirtiéndote en un guerrero formidable.")
                print("Aunque te sientes culpable por tu decisión de ignorar al caballero, también encuentras redención al unirte a la orden y dedicar tu vida a proteger a los demás.")
                print("Bien hecho.'Redencion' ")
            else:
                print("Estas buscando redencion pero no sabes como encontrarla, piensalo bien.")        
        elif decision3 == "SEGUIR TU CAMINO POR EL BOSQUE":
            print("Decides seguir tu camino por el bosque, pero la soleda se vuelva mas pesada.")
            print("la noche cae y ves como los pocos rayos de luz se desvanecen, se empieza a escuchar ruidos extraños a tu alrededor, y te das cuenta de que no estás solo en elbosque.")
            print("se escuchas aullidos y de la nada te rodean una manada de lobos.")
            print("Te atacan y te definedes, pero son demasiados te supera en numero.")
            print("Te estan devorando vivo, ves tu vida pasar frente a tus ojos.")
            print("una luz brillante aparece en el cielo, los lobos se detiene y huyen, una figura misteriosa aparece y te pregunta que haces en su bosque, le cuentas lo que paso y te dice que no deberias haber estado alli, que es peligroso para los humanos.")
            print("estas agonizando y la figura misteriosa te dice que te ayudara a salir del bosque, pero a cambio, debes prometerle que nunca volverás a entrar en su territorio.")
            print("que decides? (ACEPTAR/RECHAZAR)")
            decision4 = input("Ingresa tu decisión: ").strip().upper()
            if decision4 == "ACEPTAR":
                print("Decides aceptar la oferta de la figura misteriosa, y te ayuda a salir del bosque. Sin embargo, te advierte que si alguna vez vuelves a entrar en su territorio, enfrentarás consecuencias graves.")
                print("Agradecido por su ayuda, prometes no volver a entrar en el bosque y continúas tu vida, siempre recordando la lección que aprendiste sobre los peligros de adentrarse en territorios desconocidos.")
                print("Bien hecho.'Aprendiste la leccion?' ")
            elif decision4 == "RECHAZAR":
                print("Decides rechazar la oferta de la figura misteriosa, y te niegas a aceptar su ayuda. la figura misteriosa se enoja por tu rechazo y te dice que has cometido un grave error al rechazar su ayuda, y que ahora enfrentarás las consecuencias de tu decisión.")
                print("La figura misteriosa alza su mano y tu espiritu es arrancado de tu cuerpo, dejándote atrapado en elbosque para siempre como un espíritu errante, condenado a vagar por el bosque sin descanso, sin poder encontrar la paz")
                print("GAME OVER ")
            else:
                print("ACEPTAR o RECHAZAR 'INTENTA DE NUEVO'.")        
        else: 
            print("Tomas malas decisiones, para eestar aqui.")    
    elif decision2 == "REMATAR AL AVENTURERO":
        print("Decides rematar al aventurero, y con un golpe certero, acabas con su sufrimiento de una vez por todas.")
        print("Después de un tiempo, encuentras un grupo de cazadores que te encuentran y te cuentan que encontraron el cuerpo sin vida de un aventurero en elbosque, con heridas de batalla. Te das cuenta de que era el aventurero al que decidiste rematar.")
        print("Al ver tu espada llena de sangre, los cazadores se ponen en guardia.")
        print("¿Qué hiciste? Preguntan.")
        print("Que respondes?")
        print("Le remate para acabar con su sufrimiento, respondes.")
        print("No es lo que piensan, respondes.")
        print("atacas sin decir nada")
        decision3 = input("Ingresa tu decisión: ").strip().upper()
        if decision3 == "LE REMATE PARA ACABAR CON SU SUFRIMIENTO":
            print("Mataste a un cabellero de la orden de la mano de plata? ¡JA!, tu cabeza vale muchas monedas de oro,rodean para atacarte")
            print("No puedes detener todo los ataque a la vez.")
            print("asi que decides rendirte y te entrgas a los cazadores, ellos te llevan a la aldea y te entregan a las autoridades para que enfrentes las consecuencias de tus acciones.")
            print("En la aldea, eres juzgado por tus acciones y condenado a la horca.")
            print("GAME OVER 'Morir ahorcado debe ser sofocante' ")
        elif decision3 == "NO ES LO QUE PIENSAN":
            print("Los cazadores se sienten confundidos por tu respuesta, y te miran con desconfianza. Sin embargo, deciden no confrontarte directamente, y te advierten que el bosque es un lugar peligroso, y que debes tener cuidado con las decisiones que tomas en el futuro.")
            print("Aun asi te prreguntas si vas a compañarlos a la aldea.")
            print("¿Qué decides? (ACOMPAÑARLOS A LA ALDEA/SEGUIR TU CAMINO)")
            decision4 = input("Ingresa tu decisión: ").strip().upper()
            if decision4 == "ACOMPAÑARLOS A LA ALDEA":
                print("Decides acompañarlos a la aldea, de camino te pregunta por la sagre en tu espada.")
                print("Le cuentas que fuen con un lobo que te ataco, y que lo mataste para defenderte.")
                print("Te miran con desconfianza, te pregutan serguro que fue un lobo?")
                print("Si, respondes.")
                print("Los lobos son de andar en manada, responden.")
                print("Te empiezan a atacar, aunque logras defenderte de algunos ataques te superan en numero,")
                print("Tienes que hacer algo rapido")
                print("Tienes dos opciones, rendirte y entregarte a los cazadores, o seguir luchando contra ellos.")
                print("RENDIRTE Y ENTREGARTE A LOS CAZADORES")
                decision5 = input("Ingresa tu decisión: ").strip().upper()
                if decision5 == "RENDIRTE Y ENTREGARTE A LOS CAZADORES":
                    print("Decides rendirte y entregarte a los cazadores, y te entregas a ellos sin resistencia. Los cazadores te llevan a la aldea y te entregan a las autoridades para que enfrentes las consecuencias de tus acciones.")
                    print("En la aldea, eres juzgado por tus acciones y condenado a la horca.")
                    print("GAME OVER 'ya no tengo ideas para poner un final diferente'")
                elif decision5 == "SEGUIR LUCHANDO CONTRA ELLOS":
                    print("Decides seguir luchando contra los cazadores, y te defiendes con todas tus fuerzas. Aunque logras defenderte de algunos ataques, los cazadores te superan en número y te derrotan, dejándote gravemente herido y vulnerable en el bosque.")
                    print("Mientras estás tendido en el suelo, escuchas aullidos a lo lejos, y te das cuenta de que una manada de lobos se acerca hacia ti.")
                    print("Sin fuerzas para defenderte, eres devorado por los lobos, terminando tu aventura de manera trágica.")
                    print("GAME OVER 'ya no tengo ideas para poner un final diferente' ")
                else:
                    print("Solo puedes rendirte o seguir luchando, elige bien.")        
            elif decision4 == "SEGUIR TU CAMINO":
                print("Decides seguir tu camino por el bosque, pero la soledad se vuelve más pesada. La noche cae y ves como los pocos rayos de luz se desvanecen, se empiezan a escuchar ruidos extraños a tu alrededor, y te das cuenta de que no estás solo en el bosque.")    
            print("Bien hecho.'Compasion' ")
        elif decision3 == "ATACAS SIN DECIR NADA":
            print("Atacas previo aviso eliminas a un cazador, pero aun quedan tres.")
            print("los restantes se ponen en guardia, te rodean rapidamente.")
            print("Recuerdas que al eliminar al cabellero su habilidad de fuego la aprendiste.")
            print("Decides usarla para defenderte, lanzas un hechizo de fuego hacia los cazadores, logrando quemar a uno de ellos y asustar a los otros dos.")
            print("salen huyendo de ti, al parecer tener esa habilidad es algo especial")
            print("Ahora estas solo en el bosque, pero al menos has sobrevivido a los cazadores.")
            print("Eres libre por ahora")
            print("fin del juego 'sobreviviste a los cazadores'")
        else:
            print("Talves atacar sea la mejor opción.")                         
    else:
        print("Tienes buenas opciones")
elif decision1 == "EXPLORAR EL BOSQUE SIN EL MAPA":
    print("Caminas sin ruta alguna .")
    print("De pronto todo se vuelve oscuro, y te das cuenta de que has caído en una trampa oculta en el suelo. Quedas atrapado en un pozo profundo, sin forma de salir por tus propios medios.")
    print("Mientras estás atrapado en el pozo, escuchas ruidos extraños a tu alrededor, y te das cuenta de que no estás solo. Un grupo de criaturas salvajes se acerca hacia ti, atraídas por tu presencia.")
    print("Las criaturas te atacan, y aunque intentas defenderte, son demasiadas y te superan en número. Terminas siendo devorado por las criaturas, poniendo fin a tu aventura de manera trágica.")
    print("GAME OVER 'Moriste por no tener un mapa' ")          
else:
    print("Vamos empezando el juego y ya estas haciendo cosas raras,")