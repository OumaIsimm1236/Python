#exemple1
filin = open("zoo.txt", "r")
lignes = filin .readlines()
lignes
for ligne in lignes :
  print(ligne)
#
with open("zoo.txt", "r") as filin :
   lignes = filin . readlines()
   for ligne in lignes:
     print(ligne)

#Méthode .read()
with open("zoo.txt", "r") as filin:
   filin.read()
#Méthode .readline()
with open("zoo.txt", "r")as filin:
    ligne = filin . readline()
    while ligne != "":
      print(ligne)
      ligne = filin . readline()
#Itérations directe sur le fichier
with open("zoo.txt", "r")  as filin:
   for ligne in filin:
    print(ligne)
#Écriture dans un fichier
animaux2 = [" poisson ", " abeille ", " chat "]
with open("zoo2.txt", "w") as filout:
    for animal in animaux2:
     filout.write(animal)

#Ouvrir deux fichiers avec l’instruction with
with open("zoo.txt", "r") as fichier1, open("zoo2.txt", "w") as fichier2:
    for ligne in fichier1:
        fichier2.write("* " + ligne)
#EXERCICE Lecture du fichier et extraction des notes
# Lecture du fichier et extraction des notes
notes = []
with open("notes.txt", "r") as fichier:
    for ligne in fichier:
        note = float(ligne.strip())
        notes.append(note)

# Vérification si la liste notes est vide
if len(notes) > 0:
    # Calcul de la moyenne
    total = sum(notes)
    moyenne = total / len(notes)

    # Affichage de la moyenne avec deux décimales
    print(f"Moyenne des notes : {moyenne:.2f}")
else:
    print("Aucune note n'a été trouvée dans le fichier.")

with open("notes.txt", "r") as fichier:
    notes = [float(ligne.strip()) for ligne in fichier]
#exercice2
with open("notes2.txt", "w") as fichier2:
    for i, note in enumerate(notes, start=1):
        if note >= 10:
            fichier2.write(f"{i} {note:.1f} admis\n")
        else:
            fichier2.write(f"{i} {note:.1f} recalé\n")


