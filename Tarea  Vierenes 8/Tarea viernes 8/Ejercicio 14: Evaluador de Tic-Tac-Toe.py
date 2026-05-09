# Ejercicio 14: Evaluador de Tic-Tac-Toe
print("Ejercicio 14: Evaluador de Tic-Tac-Toe")
# Asumiendo variables a1 a9 para el tablero
a1 = input("a1: ")
a2 = input("a2: ")
a3 = input("a3: ")
b1 = input("b1: ")
b2 = input("b2: ")
b3 = input("b3: ")
c1 = input("c1: ")
c2 = input("c2: ")
c3 = input("c3: ")

gana_x = (a1 == "X" and a2 == "X" and a3 == "X") or \
         (b1 == "X" and b2 == "X" and b3 == "X") or \
         (c1 == "X" and c2 == "X" and c3 == "X") or \
         (a1 == "X" and b1 == "X" and c1 == "X") or \
         (a2 == "X" and b2 == "X" and c2 == "X") or \
         (a3 == "X" and b3 == "X" and c3 == "X") or \
         (a1 == "X" and b2 == "X" and c3 == "X") or \
         (a3 == "X" and b2 == "X" and c1 == "X")

if gana_x:
    print("X gana")
else:
    print("X no gana")

print()