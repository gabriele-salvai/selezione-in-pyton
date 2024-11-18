
reddito=float(input("inserisci il tuo redditto"))
if reddito<15000:
    aliquota= (15000*0.12)
else:
    aliquota= (15000*0.22)
print("l'mposta dovuta è pari a:", aliquota, "€")


