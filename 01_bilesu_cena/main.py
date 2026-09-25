print("Biļešu cenas kalkulators")

vecums = int(input("Ievadi savu vecumu: "))
if vecums < 0:
    print("Vecums nevar būt negatīvs.")
elif vecums <= 17:
    cena = 0
elif vecums <= 64:
    cena = 7
else:
    cena = 4
if vecums >= 0:
    print(f"Biļetes cena ir {cena} EUR.")

# TODO: ar if, elif un else nosaki pareizo cenu
cena = 0


    
