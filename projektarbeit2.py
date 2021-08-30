# Programm zum Umrechnen von Zahlen aus einem Zahlensystem in ein Anderes.
# Module liegen im Unterordner /modules
import modules.calculations as calc
import modules.menues as menu

# Kontinuierliche Menüerstellung
while True:
    menu.mainmenu()
    inp = input("Ihre Wahl: ")
    if inp == "1":
        while True:
            zahl = input("Bitte Zahl für Umrechnung eingeben: ")
            if calc.testHex(zahl):
                break
            else:
                print("Die eingegebene Zahl ist keine hexadezimale Zahl. Bitte erneut versuchen.")
        menu.hexmenu()
        inph = input("Ihre Wahl: ")
        while True:
                if inph == "1":
                # Hexadezimal nach Dezimal
                    # Direkte Berechnung
                    result = calc.toDec("h", zahl)
                    print(f"Ergebnis: {result}")
                    input("Weiter mit der Eingabe-Taste")
                    break
                elif inph == "2":
                # Hexadezimal nach Oktal
                    # Von Hexadezimal nach Dezimal, von Dezimal nach Oktal
                    result = calc.decTo("o", calc.toDec("h", zahl))
                    print(f"Ergebnis: {result}")
                    input("Weiter mit der Eingabe-Taste")
                    break
                elif inph == "3":
                # Hexadezimal nach Binär
                    # Von Hexadezimal nach Dezimal, von Dezimal nach Binär
                    result = calc.decTo("b", calc.toDec("h", zahl))
                    print(f"Ergebnis: {result}")
                    input("Weiter mit der Eingabe-Taste")
                    break
                elif inph == "q":
                    break
                else:
                    print("Fehlerhafte Eingabe. Bitte wählen sie einen Menüpunkt.")
                    break
    elif inp == "2":
        while True:
            zahl = input("Bitte Zahl für Umrechnung eingeben: ")
            if calc.testDec(zahl):
                break
            else:
                print("Die eingegebene Zahl ist keine dezimale Zahl. Bitte erneut versuchen.")
        menu.decmenu()
        inpd = input("Ihre Wahl: ")
        while True:
            if inpd == "1":
                # Dezimal nach Hexadezimal
                    # Direkte Berechnung
                    result = calc.decTo("h", int(zahl))
                    print(f"Ergebnis: {result}")
                    input("Weiter mit der Eingabe-Taste")
                    break
            elif inpd == "2":
                # Dezimal nach Oktal
                    # Direkte Berechnung
                    result = calc.decTo("o", int(zahl))
                    print(f"Ergebnis: {result}")
                    input("Weiter mit der Eingabe-Taste")
                    break
            elif inpd == "3":
                # Dezimal nach Binär
                    # Direkte Berechnung
                    result = calc.decTo("b", int(zahl))
                    print(f"Ergebnis: {result}")
                    input("Weiter mit der Eingabe-Taste")
                    break
            elif inpd == "q":
                break
            else:
                print("Fehlerhafte Eingabe. Bitte wählen sie einen Menüpunkt.")
                break
    elif inp == "3":
        while True:
            zahl = input("Bitte Zahl für Umrechnung eingeben: ")
            if calc.testOct(zahl):
                break
            else:
                print("Die eingegebene Zahl ist keine oktale Zahl. Bitte erneut versuchen.")
        menu.octmenu()
        inpo = input("Ihre Wahl: ")
        while True:
            if inpo == "1":
                # Oktal nach Hexadezimal
                    # Von Oktal nach Dezimal, von Dezimal nach Hexadezimal
                    result = calc.decTo("h", calc.toDec("o", zahl))
                    print(f"Ergebnis: {result}")
                    input("Weiter mit der Eingabe-Taste")
                    break
            elif inpo == "2":
                # Oktal nach Dezimal
                    # Direkte Berechnung
                    result = calc.toDec("o", zahl)
                    print(f"Ergebnis: {result}")
                    input("Weiter mit der Eingabe-Taste")
                    break
            elif inpo == "3":
                # Oktal nach Binär
                    # Von Oktal nach Dezimal, von Dezimal nach Binär
                    result = calc.decTo("b", calc.toDec("o", zahl))
                    print(f"Ergebnis: {result}")
                    input("Weiter mit der Eingabe-Taste")
                    break
            elif inpo == "q":
                break
            else:
                print("Fehlerhafte Eingabe. Bitte wählen sie einen Menüpunkt.")
                break
    elif inp == "4":
        while True:
            zahl = input("Bitte Zahl für Umrechnung eingeben: ")
            if calc.testBin(zahl):
                break
            else:
                print("Die eingegebene Zahl ist keine binäre Zahl. Bitte erneut versuchen.")
        menu.binmenu()
        inpb = input("Ihre Wahl: ")
        while True:
            if inpb == "1":
                # Binär nach Hexadezimal
                    # Von Binär nach Dezimal, von Dezimal nach Hexadezimal
                    result = calc.decTo("h", calc.toDec("b", zahl))
                    print(f"Ergebnis: {result}")
                    input("Weiter mit der Eingabe-Taste")
                    break
            elif inpb == "2":
                # Binär nach Dezimal
                    # Direkte Berechnung
                    result = calc.toDec("b", zahl)
                    print(f"Ergebnis: {result}")
                    input("Weiter mit der Eingabe-Taste")
                    break
            elif inpb == "3":
                # Binär nach Oktal
                    # Von Binär nach Dezimal, von Dezimal nach Oktal
                    result = calc.decTo("o", calc.toDec("b", zahl))
                    print(f"Ergebnis: {result}")
                    input("Weiter mit der Eingabe-Taste")
                    break
            elif inpb == "q":
                break
            else:
                print("Fehlerhafte Eingabe. Bitte wählen sie einen Menüpunkt.")
                break
    elif inp == "q":
        break
    else:
        # Bei fehlerhafen Eingaben wird das Hauptmenü neu erstellt
        print("Fehlerhafte Eingabe. Bitte wählen sie einen Menüpunkt.")