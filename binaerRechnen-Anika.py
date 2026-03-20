# Wir addieren Zahlen nach Umrechnung Dezimal auf Binär #
# Autor Nicky K 20260320 #

##########
# Import #
##########

import random

#############
# Variablen #
#############

iZahlEins = random.randint(0,255)
iZahlZwei = random.randint(0,255)

##############
# Funktionen #
##############

 # Funktion Random-Dezimalzahlen in Binärzahlen wandeln #

def fnBin(iZahl):
    sZahl = ""                
    for iExponent in range(9, -1, -1):   
        iBasis = 2 ** iExponent          
        if iBasis <= iZahl:
            iZahl = iZahl - iBasis
            sZahl += "1"
        else:
            sZahl += "0"
    return sZahl
        
 # Funktion die Binärzahlen wie ein Mensch zu addieren #


def fnAddition(sZahlEins, sZahlZwei):
    iLaenge = 10
    sErgebnis = ""    
    sUebertrag = 0      
      
    for bit in range(iLaenge - 1, -1, -1):         # Von rechts nach links durchgehen
        sBitEins = int(sZahlEins[bit])
        sBitZwei = int(sZahlZwei[bit])
        sTotal = sBitEins + sBitZwei + sUebertrag
        
        sErgebnis = str(sTotal % 2) + sErgebnis    
        sUebertrag = sTotal // 2               
      
    if sUebertrag:                                # Letzten sUebertrag anhängen, falls vorhanden
        sErgebnis = str(sUebertrag) + sErgebnis
    
    return sErgebnis

###########
# Aufrufe #
###########

sZahlEins = fnBin(iZahlEins)
print(sZahlEins)
sZahlZwei = fnBin(iZahlZwei)
print(f"{sZahlZwei} +")

print("----------")
print(fnAddition(sZahlEins, sZahlZwei))

