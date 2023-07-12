#Chapitre 6 Tests
x = 2
if x == 2:
  print(" Le test est vrai !")
#Tests à plusieurs cas
x = 2
if x == 2:
   print(" Le test est vrai !")
else:
      print(" Le test est faux !")
#
import random

base = random.choice(["a", "t", "c", "g"])

if base == "a":
    print("Choix d'une adénine")
elif base == "t":
    print("Choix d'une thymine")
elif base == "c":
    print("Choix d'une cytosine")
elif base == "g":
    print("Choix d'une guanine")
#
nombres = [4, 5, 6]

for nb in nombres:
    if nb == 5:
        print("Le test est vrai")
        print("car la variable nb vaut {}".format(nb))

nombres = [4, 5, 6]

for nb in nombres:
    if nb == 5:
        print("Le test est vrai")
    print("car la variable nb vaut {}".format(nb))
#
for i in range(5):
  if i > 2:
   break
print(i)
#
for i in range(5):
   if i == 2:
    continue
print(i)
#Tests de valeur sur des floats
delta = 0.001
var = 0.299

if 0.3 - delta < var < 0.3 + delta:
    print("La valeur est proche de 0.3")
else:
    print("La valeur est différente de 0.3")
# exercice 1 Jours de la semaine
semaine = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']

for jour in semaine:
    if jour in ['lundi', 'mardi', 'mercredi', 'jeudi']:
        print(jour + " - Au travail")
    elif jour == 'vendredi':
        print(jour + " - Chouette c'est vendredi")
    else:
        print(jour + " - Repos ce week-end")
#EXERCIE2 Minimum d’une liste
liste = [8, 4, 6, 1, 5]
plus_petit = liste[0]  # On initialise l'élément de référence avec le premier élément de la liste

for element in liste:
    if element < plus_petit:
        plus_petit = element

print("Le plus petit élément de la liste est :", plus_petit)
# EXERCICE 3 Notes et mention d’un étudiant
notes = [14, 9, 13, 15, 12]

note_max = max(notes)
note_min = min(notes)
moyenne = sum(notes) / len(notes)

print("Note maximale :", note_max)
print("Note minimale :", note_min)
print("Moyenne :", "{:.2f}".format(moyenne))

if 10 <= moyenne < 12:
    mention = "Passable"
elif 12 <= moyenne < 14:
    mention = "Assez bien"
else:
    mention = "Bien"

print("Mention :", mention)
#Nombres pairs
for nombre in range(21):
    if nombre <= 10 and nombre % 2 == 0:
        print(nombre, "est un nombre pair inférieur ou égal à 10")
    elif nombre > 10 and nombre % 2 != 0:
        print(nombre, "est un nombre impair strictement supérieur à 10")
#Attribution de la structure secondaire des acides aminés d’une protéine (exercice +++)
angles_amino_acides = [
    [48.6, 53.4],
    [-124.9, 156.7],
    [-66.2, -30.8],
    [-58.8, -43.1],
    [-73.9, -40.6],
    [-53.7, -37.5],
    [-80.6, -26.0],
    [-68.5, 135.0],
    [-64.9, -23.5],
    [-66.9, -45.5],
    [-69.6, -41.0],
    [-62.7, -37.5],
    [-68.2, -38.3],
    [-61.2, -49.1],
    [-59.7, -41.1]
]

for i, angles in enumerate(angles_amino_acides):
    phi, psi = angles
    if -87 <= phi <= -27 and -77 <= psi <= -17:
        print(f"{i+1} {angles} est en hélice")
    else:
        print(f"{i+1} {angles} n'est pas en hélice")
#Détermination des nombres premiers inférieurs à 100 (exercice +++)
nombres_premiers = []

for num in range(2, 100):
    est_premier = True

    for i in range(2, num):
        if num % i == 0:
            est_premier = False
            break

    if est_premier:
        nombres_premiers.append(num)

print("Nombres premiers inférieurs à 100:")
print(nombres_premiers)
print("Nombre de nombres premiers entre 0 et 100:", len(nombres_premiers))




