
animaux = [' girafe ', 'tigre ', 'singe ', 'souris ']
tailles = [5 , 2.5 , 1.75 , 0.15]
mixte = [' girafe ', 5, 'souris ', 0.15]
print(animaux)
print(mixte)
print(animaux[0])
print(animaux[2])
print(animaux[2], tailles[2])

ani1 = ['girafe', 'tigre']
ani2 = ['singe', 'souris']
print(ani1 + ani2)
a = []
print([])
print(a)
a = a + [-5]
print(a)
a = a + [15]
print(a)
#FONCTION .appred()
a. append(13)
print(a)
a. append(13)
print(a)
#LISTE
liste = ['girafe', 'tigre', 'singe', 'souris']
print(liste)
animaux = [' girafe ','tigre ','singe ',' souris ']
#indice négatif
print(animaux[-1])
print(animaux[-4])
#TRANCHE:
print(animaux[0:2])
print(animaux[0:])
print(animaux[:])
#Fonction len(): pour connaitre la longeur d'un liste
animaux = [' girafe ', 'tigre ', 'singe ', 'souris ']
taille = len(animaux)
print(taille)
#Les fonctions range() et list(): pour donner une liste des entiers données
resultat = list(range(0, 5))
print(resultat)
resultat = list(range(0, 1000, 200))
print(resultat)
resultat = list(range(2, -2, -1))
print(resultat)
#liste de liste:
enclos1 = [' girafe ', 4]
enclos2 = ['tigre ', 2]
enclos3 = ['singe ', 5]
zoo= [enclos1, enclos2, enclos3]
print(zoo)
#Minimum, maximum et somme d’une liste
liste = list(range(10))
print(liste)
print(sum(liste ))
print(min(liste))
print(max(liste))
#EXERCICE 1: Jours de la semaine
semaine = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']

# Récupération des 5 premiers jours de la semaine
premiers_jours = semaine[:-2]
print(premiers_jours)

# Récupération des jours du week-end
weekend = semaine[-2:]
print(weekend)
#
dernier_jour = semaine[-1]
print(dernier_jour)
#
dernier_jour = semaine[len(semaine)-1]
print(dernier_jour)
#EXERCICE 2 Jours de la semaine
semaine = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
semaine_inverse = semaine[::-1]
print(semaine_inverse)
#EXERCICE 3 Saisons
hiver = ['décembre', 'janvier', 'février']
printemps = ['mars', 'avril', 'mai']
ete = ['juin', 'juillet', 'août']
automne = ['septembre', 'octobre', 'novembre']

saisons = [hiver, printemps, ete, automne]
resultat = [saison[1] for saison in saisons]
print(resultat)
#Table de multiplication par 9:
table_multiplication = [9 * i for i in range(1, 11)]
print(table_multiplication)
#EXERCICE 4 Nombres pairs:
nombres_pairs = [x for x in range(2, 10001) if x % 2 == 0]
nombre_pairs_total = len(nombres_pairs)
print(nombre_pairs_total)

