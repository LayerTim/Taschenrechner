import functions
v = True
print("Was berechnen wir heute?")
print("Falls du das Programm während der Schleife beenden willst drück Strg + C")
while v:
    x = input("Du hast folgende Optionen: add, sub, mul, div.\n")
    if x not in ("add", "sub", "mul", "div"):
        print("Falsche Eingabe.")
        continue

    while True:
        try:
            y = float(input("Was soll die erste Zahl sein?\n"))
        except ValueError:
            print("Bitte nur Zahlen eingeben")
            continue
        else:
            break

    while True:
        try:
            z = float(input("Was soll die zweite Zahl sein?\n"))
        except ValueError:
            print("Bitte nur Zahlen eingeben")
            continue
        else:
            break

    if x == "add":
        print(functions.add(y, z))
    elif x == "sub":
        print(functions.sub(y, z))
    elif x == "mul":
        print(functions.mul(y, z))
    elif x == "div":
        print(functions.div(y, z))
    else:
        print("Wrong input")

    print("Willst du weiter rechnen? (y/n)")
    x = input()
    if x == "n":
        print("Have a nice day!")
        break
    else:
        continue
