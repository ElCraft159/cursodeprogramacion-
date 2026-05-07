# Ejercicio 7: Piedra, Papel, Tijera, Lagarto, Spock
print("Ejercicio 7: Piedra, Papel, Tijera, Lagarto, Spock")
jugador1 = input("Jugador 1 (piedra, papel, tijera, lagarto, spock): ").lower()
jugador2 = input("Jugador 2 (piedra, papel, tijera, lagarto, spock): ").lower()

if jugador1 == jugador2:
    print("Empate")
elif (jugador1 == "piedra" and (jugador2 == "tijera" or jugador2 == "lagarto")) or \
     (jugador1 == "papel" and (jugador2 == "piedra" or jugador2 == "spock")) or \
     (jugador1 == "tijera" and (jugador2 == "papel" or jugador2 == "lagarto")) or \
     (jugador1 == "lagarto" and (jugador2 == "papel" or jugador2 == "spock")) or \
     (jugador1 == "spock" and (jugador2 == "piedra" or jugador2 == "tijera")):
    print("Jugador 1 gana")
else:
    print("Jugador 2 gana")

print()