# Definieren von Konstanten, eigentlich als Tupel, aber hier einfacher als Listen zu realisieren.
# Der Status als Konstante wird nur durch Großschreibung impliziert.
# Diese Konstanten dienen der Typbestimmung und Umwandlung von Hexadezimalwerten

BINARY = ["0","1"]
OCTAL = ["0","1","2","3","4","5","6","7"]
DECIMAL = ["0","1","2","3","4","5","6","7","8","9"]
HEXADECIMAL = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
HEXADECIMAL_CONVERT_TO = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
HEXADECIMAL_CONVERT_FROM = {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15}

def decTo(target: str, zahl: int) -> str:
    """Konvertiert eine Dezimalzahl [zahl] in ein gewähltes Zahlensystem [target].
    Parameter:

    target - Ein String, der das Zielsystem angibt.

        "b" für Binär

        "o" für Oktal

        "h" für Hexadezimal

    zahl - Der Integer, der umgerechnet werden soll.

    return - Die umgerechnete Zahl im Zielsystem als String."""
    if target == "b":
        # Durch 2 teilen bis 0. Reste aufschreiben und invertieren.
        if zahl == 0:
            return 0
        result = []
        while zahl > 0:
            result.append(zahl%2)
            zahl = zahl // 2
        result.reverse()
        result = [str(i) for i in result]
        return "".join(result)
    elif target == "o":
        # Durch 8 teilen bis 0. Reste aufschreiben und invertieren.
        result = []
        if zahl == 0:
            return 0
        while zahl > 0:
            result.append(zahl%8)
            zahl = zahl // 8
        result.reverse()
        result = [str(i) for i in result]
        return "".join(result)
    elif target == "h":
        # Durch 16 Teilen bis 0. Reste aufschreiben und invertieren.
        # Zahlen über 9 durch entsprechende Buchstaben tauschen.
        result = []
        if zahl == 0:
            return 0
        while zahl > 0:
            result.append(zahl%16)
            zahl = zahl // 16
        for i in range(0,len(result)):
            if result[i] > 9:
                result[i] = HEXADECIMAL_CONVERT_TO[result[i]]
        result.reverse()
        result = [str(i) for i in result]
        return "".join(result)
    else:
        print("Fehler in Modul calculations, Funktion decTo")

def toDec(source: str, zahl: str) -> int:
    """Konvertiert eine Zahl aus einem Quellsystem in eine Dezimalzahl.

    Parameter:
    source - Ein String, der das Quellsystem angibt.

        "b" für Binär

        "o" für Oktal

        "h" für Hexadezimal

    zahl - Der Integer, der umgerechnet werden soll.

    return - Die umgerechnete Zahl im Dezimalsystem als Integer."""
    if source == "b":
        # Ziffern der Zahl invertieren.
        # Aufaddieren der Zahl multipliziert mit der Basis (hier 2) des Zahlensystems hoch Stellenwert.
        result = 0
        if zahl == "0":
            return 0
        zahl = list(zahl)[::-1]
        for i in range(0,len(zahl)):
            result = result + (int(zahl[i])*2**i)
        return result
    elif source == "o":
        # Ziffern der Zahl invertieren.
        # Aufaddieren der Zahl multipliziert mit der Basis (hier 2) des Zahlensystems hoch Stellenwert.
        result = 0
        if zahl == "0":
            return 0
        zahl = list(zahl)[::-1]
        for i in range(0,len(zahl)):
            result = result + (int(zahl[i])*8**i)
        return result
    elif source == "h":
        # Ziffern der Zahl invertieren.
        # Hexadezimale Ziffern in Dezimalzahlen konvertieren. Eventuell capitalizen.
        # Aufaddieren der Zahl multipliziert mit der Basis (hier 2) des Zahlensystems hoch Stellenwert.
        result = 0
        if zahl == "0":
            return 0
        zahl = list(zahl)[::-1]
        for i in range(0,len(zahl)):
            if not zahl[i].isdigit():
                zahl[i] = zahl[i].capitalize()
                zahl[i] = HEXADECIMAL_CONVERT_FROM[zahl[i]]
        for i in range(0,len(zahl)):
            result = result + (int(zahl[i])*16**i)
        return result
    else:
        print("Fehler in Modul calculations, Funktion toDec")

def testBin(sample: str) -> bool:
    """Testet, ob ein eingegebener String [sample] eine valide Darstellung einer binären Zahl ist"""
    for i in range(0,len(sample)):
        if not BINARY.count(sample[i]):
            return False
    if sample == "":
        return False
    return True

def testOct(sample: str) -> bool:
    """Testet, ob ein eingegebener String [sample] eine valide Darstellung einer oktalen Zahl ist"""
    for i in range(0,len(sample)):
        if not OCTAL.count(sample[i]):
            return False
    if sample == "":
        return False
    return True

def testDec(sample: str) -> bool:
    """Testet, ob ein eingegebener String [sample] eine valide Darstellung einer dezimalen Zahl ist"""
    for i in range(0,len(sample)):
        if not DECIMAL.count(sample[i]):
            return False
    if sample == "":
        return False
    return True

def testHex(sample: str) -> bool:
    """Testet, ob ein eingegebener String [sample] eine valide Darstellung einer hexadezimalen Zahl ist"""
    for i in range(0,len(sample)):
        if not HEXADECIMAL.count(sample[i].capitalize()):
            return False
    if sample == "":
        return False
    return True