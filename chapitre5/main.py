animaux = [' girafe ', 'tigre ', 'singe ', 'souris ']
print(animaux[0])
print(animaux[1])
print(animaux[2])
print(animaux[3])

animaux = ['girafe', 'tigre', 'singe', 'souris']

for animal in animaux:
    print(animal)
for animal in animaux:
  print(animal)
  print(animal *2)
  print("C' est fini ")
animaux = [' girafe ', 'tigre ', 'singe ', 'souris ']
for animal in animaux [1:3]:
    print(animal)
for i in [1 , 2, 3]:
     print (i)
#Fonction range()
for i in range (4):
    print (i)
#Itération sur les indices:
animaux = [' girafe ', 'tigre ', 'singe ', 'souris ']
for i in range(4):
   print(animaux[i])
animaux = [' girafe ', 'tigre ', 'singe ', 'souris ']
for animal in animaux :
   print(animal)
for i in range ( len ( animaux )):
   print("L' animal {} est un ( e) {}". format(i, animaux[i]))
animaux = [' girafe ','tigre ','singe ',' souris ']
#2em methode
for i , animal in enumerate ( animaux ):
   print("L' animal {} est un ( e) {}". format (i , animal))
#Comparaisons:
animal = " tigre "
resultat = animal == " tig "
print(resultat)
#Boucles while:
i = 1
while i <= 4:
    print(i)
    i = i + 1
i = 0
while i < 10:
    reponse = input("Entrez un entier supérieur à 10 : ")
    i = int(reponse)
#exercice1 Boucles de base
liste = ['vache', 'souris', 'levure', 'bacterie']
i = 0
while i < len(liste):
    print(liste[i])
    i += 1
#exercice 2 Boucle et jours de la semaine:
semaine = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']

# Affichage des jours de la semaine avec une boucle for
print("Jours de la semaine (boucle for):")
for jour in semaine:
    print(jour)

# Affichage des jours du week-end avec une boucle while
print("Jours du week-end (boucle while):")
i = 5  # Indice correspondant au premier jour du week-end (Samedi)
while i < len(semaine):
    print(semaine[i])
    i += 1
#Nombres de 1 à 10 sur une ligne
for i in range(1, 11):
    print(i, end=' ')
#Nombres pairs et impairs
impairs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

pairs = [nombre + 1 for nombre in impairs]

print(pairs)
#Calcul de la moyenne
notes = [14, 9, 6, 8, 12]
moyenne = sum(notes) / len(notes)

print("La moyenne est : {:.2f}".format(moyenne))
#Produit de nombres consécutifs
entiers = list(range(2, 21, 2))

produits = []
for i in range(len(entiers) - 1):
    produit = entiers[i] * entiers[i + 1]
    produits.append(produit)

print(produits)
#Triangle
n = 10  # Nombre de lignes du triangle

for i in range(1, n+1):
    ligne = "*" * i
    print(f"{i} {ligne}")
#Triangle inversé
n = 10  # Nombre de lignes du triangle

for i in range(n, 0, -1):
    ligne = "*" * i
    print(f"{i} {ligne}")
#Triangle gauche
n = 10  # Nombre de lignes du triangle

for i in range(1, n+1):
    ligne = "*" * i
    print(ligne)
#Pyramide
n = 10  # Nombre de lignes de la pyramide

for i in range(1, n+1):
    espaces = " " * (n - i)  # Nombre d'espaces avant les étoiles
    etoiles = "*" * (2*i - 1)  # Nombre d'étoiles pour la ligne
    ligne = espaces + etoiles
    print(ligne)
#Parcours de matrice
n = 3  # Taille de la matrice carrée

print("Parcours avec boucles for:")
print("{:>4s} {:>4s} {:>4s}".format("Num", "Ligne", "Colonne"))
num = 1
for ligne in range(1, n+1):
    for colonne in range(1, n+1):
        print("{:>4d} {:>4d} {:>4d}".format(num, ligne, colonne))
        num += 1
#avex while
n = 3  # Taille de la matrice carrée

print("Parcours avec boucles while:")
print("{:>4s} {:>4s} {:>4s}".format("Num", "Ligne", "Colonne"))
num = 1
ligne = 1
while ligne <= n:
    colonne = 1
    while colonne <= n:
        print("{:>4d} {:>4d} {:>4d}".format(num, ligne, colonne))
        num += 1
        colonne += 1
    ligne += 1
