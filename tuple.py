#Déclaration
mon_tuple = (10, 20, 30)

#Traitement
maListe = list(mon_tuple) 

maListe[1] = 15


mon_tuple = tuple(maListe)

print(f"Ancien tuple : {mon_tuple}")
