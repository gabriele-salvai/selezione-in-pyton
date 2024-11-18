
reddito=float(input("inserisci il tuo redditto:\t"))
if reddito<15000:
    aliquota= (reddito*0.12)
else:
    aliquota= (reddito*0.22)
print("l'mposta dovuta è pari a:", aliquota, "€")


