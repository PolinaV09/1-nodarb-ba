atzimes = [7, 5, 9, 4, 8]
videja=sum(atzimes) / len(atzimes)
augstaka = max(atzimes)
zemaka = min(atzimes)

sekmigo_skaits=0
for atzime in atzimes:
    if atzime >=4:
       sekmigo_skaits += 1

print(f"Vidējais vērtējums: {videja}")
print(f"Augstākais vērtējums: {augstaka}")
print(f"Zemākais vērtējums: {zemaka}")
print(f"Sekmīgo vērtējumu skaits: {sekmigo_skaits}")

