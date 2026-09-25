print("Python mini viktorīna")

punkti = 0

atbilde = input("1. Kāds atslēgvārds sāk nosacījumu? ").lower()
if atbilde == "if" :
    punkti +=1

atbilde = input("2. Kāda funkcija izvada tekstu? ").lower()
if atbilde == "print":
    punkti += 1

atbilde = input("3. Kāds cikls iet cauri elementiem? ").lower()
if atbilde == "for":
    punkti += 1

print(f"Tu ieguvi {punkti} no 3 punktiem.")

