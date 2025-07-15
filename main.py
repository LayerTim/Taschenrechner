import functions
#Wir benutzen hier decimal, um das Runden der Floats zu vermeiden.
from decimal import Decimal
# Dictionary, um Eingaben auf Funktionen zu mappen.
ops = {
    "add": functions.add,
    "sub": functions.sub,
    "mul": functions.mul,
    "div": functions.div,
}

v = True
print("Was berechnen wir heute?\n"
      "Falls du das Programm während der Schleife beenden willst "
      "drück Strg + C.")
while v:
    x = input("Du hast folgende Optionen: add, sub, mul, div.\n")
    if x not in ops:
        print("Falsche Eingabe.")
        continue

    while True:
        y_str = input("Was soll die erste Zahl sein?\n")
        try:
            y = Decimal(y_str)
        except ValueError:
            print("Bitte nur Zahlen eingeben")
        else:
            break

    while True:
        z_str = input("Was soll die zweite Zahl sein?\n")
        try:
            z = Decimal(z_str)
        except ValueError:
            print("Bitte nur Zahlen eingeben")
        else:
            break

    # Sucht nach Schlüssel im dict,
    # existiert er bekommen wir die Fkt.
    # Alternativ liefert die Funktion None/False.
    func = ops.get(x)
    if func:
        result = func(y,z)
        print(result)
    else:
        print("Falscher input.")

    print("Willst du weiter rechnen? (y/n)")
    x = input()
    if x == "n":
        print("Have a nice day!")
        break
    else:
        continue
