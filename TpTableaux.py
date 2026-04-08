# Déclaration 

eleve1 = [12, 14, 8, 7]
eleve2 = [13, 18, 18, 6]
eleve3 = [17, 12, 18, 2]

eleves = [eleve1,
          eleve2, 
          eleve3]

# Traitement 

for i, eleve in enumerate(eleves):
    notes = ""
    moyenne = 0
    
    for j, note in enumerate(eleve):
        moyenne += note
        notes += str(note) + " "

    moyenne = moyenne / (j + 1)
    print(f"Eleve {i+1} : {notes} ({moyenne:.2f}/20)")


