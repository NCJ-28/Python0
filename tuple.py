#Déclaration
mon_tuple = (10, 20, 30)

#Traitement
try: 
    mon_tuple[2] = 40

except TypeError:
    print ("\U000026A0 Erreur : impossible de modifier un élément d'un tuple car il est immuable")

print(mon_tuple)

