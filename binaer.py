import random

#iZahl1 = random.randint(0,255)

#elem = 64 
iZahl1 = random.randint(0,255)
iZahl2 = random.randint(0,255)

def fnBin(elem): 
    #print(f"{elem}\n")
    bin = []
    while elem > 0:   
        if elem % 2 == 0:
            elem = int(elem / 2) 
            bin += "0"    
        else:
            elem = int(elem / 2)
            bin += "1"

    sZahl = bin [::-1]   
    return sZahl

bin1 = fnBin(iZahl1)
bin2 = fnBin(iZahl2)

a = "1010"
b = "10"

num1 = a[::-1]
num2 = b[::-1]
