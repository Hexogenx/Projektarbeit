# Programm zum Umrechnen von Zahlen aus einem Zahlensystem in ein Anderes.
# Module liegen im Unterordner /modules
import modules.calculations as calc
import modules.menues as menu

# Kontinuierliche Menüerstellung
while True:
    # Aufruf des Hauptmenüs
    menu.mainmenu()
    inp = input("Ihre Wahl: ")
    # Fallunterscheidung Hauptmenüauswahl
    if inp == "1":
        menu.hexmenu()
        inph = input("Ihre Wahl: ")
        while True:
            # Kontinuierlicher Aufruf des Untermenüs und Fallunterscheidung der Menüauswahl
            if inph == "1":
                # Hexadezimal nach Dezimal
                zahlh = input("Bitte Zahl für Umrechnung eingeben: ")
                if calc.testHex(zahlh):
                    # Direkte Berechnung
                    result = calc.toDec("h", zahlh)
                    print(result)
                    input("Weiter mit der Eingabe-Taste")
                    break
                else:
                    print("Diese Zahl ist keine hexadezimale Zahl. Bitte Eingabe überprüfen.")
            elif inph == "2":
                # Hexadezimal nach Oktal
                zahlh = input("Bitte Zahl für Umrechnung eingeben: ")
                if calc.testHex(zahlh):
                    # Von Hexadezimal nach Dezimal, von Dezimal nach Oktal
                    result = calc.decTo("o", calc.toDec("h", zahlh))
                    print(result)
                    input("Weiter mit der Eingabe-Taste")
                    break
                else:
                    print("Diese Zahl ist keine hexadezimale Zahl. Bitte Eingabe überprüfen.")
            elif inph == "3":
                # Hexadezimal nach Binär
                zahlh = input("Bitte Zahl für Umrechnung eingeben: ")
                if calc.testHex(zahlh):
                    # Von Hexadezimal nach Dezimal, von Dezimal nach Binär
                    result = calc.decTo("b", calc.toDec("h", zahlh))
                    print(result)
                    input("Weiter mit der Eingabe-Taste")
                    break
                else:
                    print("Diese Zahl ist keine hexadezimale Zahl. Bitte Eingabe überprüfen.")
            elif inph == "q":
                break
            else:
                print("Fehlerhafte Eingabe. Bitte wählen sie einen Menüpunkt.")
                break
    elif inp == "2":
        menu.decmenu()
        inph = input("Ihre Wahl: ")
        while True:
            # Kontinuierlicher Aufruf des Untermenüs und Fallunterscheidung der Menüauswahl
            if inph == "1":
                # Dezimal nach Hexadezimal
                zahld = input("Bitte Zahl für Umrechnung eingeben: ")
                if calc.testDec(zahld):
                    # Direkte Berechnung
                    result = calc.decTo("h", int(zahld))
                    print(result)
                    input("Weiter mit der Eingabe-Taste")
                    break
                else:
                    print("Diese Zahl ist keine dezimale Zahl. Bitte Eingabe überprüfen.")
            elif inph == "2":
                # Dezimal nach Oktal
                zahld = input("Bitte Zahl für Umrechnung eingeben: ")
                if calc.testDec(zahld):
                    # Direkte Berechnung
                    result = calc.decTo("o", int(zahld))
                    print(result)
                    input("Weiter mit der Eingabe-Taste")
                    break
                else:
                    print("Diese Zahl ist keine dezimale Zahl. Bitte Eingabe überprüfen.")
            elif inph == "3":
                # Dezimal nach Binär
                zahld = input("Bitte Zahl für Umrechnung eingeben: ")
                if calc.testDec(zahld):
                    # Direkte Berechnung
                    result = calc.decTo("b", int(zahld))
                    print(result)
                    input("Weiter mit der Eingabe-Taste")
                    break
                else:
                    print("Diese Zahl ist keine dezimale Zahl. Bitte Eingabe überprüfen.")
            elif inph == "q":
                break
            else:
                print("Fehlerhafte Eingabe. Bitte wählen sie einen Menüpunkt.")
                break
    elif inp == "3":
        menu.octmenu()
        # Kontinuierlicher Aufruf des Untermenüs und Fallunterscheidung der Menüauswahl
        inph = input("Ihre Wahl: ")
        while True:
            if inph == "1":
                # Oktal nach Hexadezimal
                zahlo = input("Bitte Zahl für Umrechnung eingeben: ")
                if calc.testOct(zahlo):
                    # Von Oktal nach Dezimal, von Dezimal nach Hexadezimal
                    result = calc.decTo("h", calc.toDec("o", zahlo))
                    print(result)
                    input("Weiter mit der Eingabe-Taste")
                    break
                else:
                    print("Diese Zahl ist keine oktale Zahl. Bitte Eingabe überprüfen.")
            elif inph == "2":
                # Oktal nach Dezimal
                zahlo = input("Bitte Zahl für Umrechnung eingeben: ")
                if calc.testOct(zahlo):
                    # Direkte Berechnung
                    result = calc.toDec("o", zahlo)
                    print(result)
                    input("Weiter mit der Eingabe-Taste")
                    break
                else:
                    print("Diese Zahl ist keine oktale Zahl. Bitte Eingabe überprüfen.")
            elif inph == "3":
                # Oktal nach Binär
                zahlo = input("Bitte Zahl für Umrechnung eingeben: ")
                if calc.testOct(zahlo):
                    # Von Oktal nach Dezimal, von Dezimal nach Binär
                    result = calc.decTo("b", calc.toDec("o", zahlo))
                    print(result)
                    input("Weiter mit der Eingabe-Taste")
                    break
                else:
                    print("Diese Zahl ist keine oktale Zahl. Bitte Eingabe überprüfen.")
            elif inph == "q":
                break
            else:
                print("Fehlerhafte Eingabe. Bitte wählen sie einen Menüpunkt.")
                break
    elif inp == "4":
        menu.binmenu()
        # Kontinuierlicher Aufruf des Untermenüs und Fallunterscheidung der Menüauswahl
        inph = input("Ihre Wahl: ")
        while True:
            if inph == "1":
                # Binär nach Hexadezimal
                zahlb = input("Bitte Zahl für Umrechnung eingeben: ")
                if calc.testBin(zahlb):
                    # Von Binär nach Dezimal, von Dezimal nach Hexadezimal
                    result = calc.decTo("h", calc.toDec("b", zahlb))
                    print(result)
                    input("Weiter mit der Eingabe-Taste")
                    break
                else:
                    print("Diese Zahl ist keine binäre Zahl. Bitte Eingabe überprüfen.")
            elif inph == "2":
                # Binär nach Dezimal
                zahlb = input("Bitte Zahl für Umrechnung eingeben: ")
                if calc.testBin(zahlb):
                    # Direkte Berechnung
                    result = calc.toDec("b", zahlb)
                    print(result)
                    input("Weiter mit der Eingabe-Taste")
                    break
                else:
                    print("Diese Zahl ist keine binäre Zahl. Bitte Eingabe überprüfen.")
            elif inph == "3":
                # Binär nach Oktal
                zahlb = input("Bitte Zahl für Umrechnung eingeben: ")
                if calc.testBin(zahlb):
                    # Von Binär nach Dezimal, von Dezimal nach Oktal
                    result = calc.decTo("o", calc.toDec("b", zahlb))
                    print(result)
                    input("Weiter mit der Eingabe-Taste")
                    break
                else:
                    print("Diese Zahl ist keine binäre Zahl. Bitte Eingabe überprüfen.")
            elif inph == "q":
                break
            else:
                print("Fehlerhafte Eingabe. Bitte wählen sie einen Menüpunkt.")
                break
    elif inp == "q":
        break
    else:
        # Bei fehlerhafen Eingaben wird das Hauptmenü neu erstellt
        print("Fehlerhafte Eingabe. Bitte wählen sie einen Menüpunkt.")