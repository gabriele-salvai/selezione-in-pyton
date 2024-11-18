eta=int(input("inserisci l'età:\t"))
rob=0
if eta<14:
    rob=10.0
elif eta>65:
    rob=15.0
elif (eta<=15 and eta<=65):
    rob=34.0
print("devi pagare:",rob,"euro")