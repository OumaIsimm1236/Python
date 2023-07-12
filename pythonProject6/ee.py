from tkinter import *


def login():
    # Vérification de l'identifiant et du mot de passe
    if identifiant_entry.get() == "admin" and mot_de_passe_entry.get() == "1234":
        # Suppression de la fenêtre de connexion
        fenetre_connexion.destroy()

        # Création de la fenêtre de résultat
        fenetre_resultat = Tk()
        fenetre_resultat.title("Résultat")
        fenetre_resultat.geometry("400x300")



    else:
        # Affichage d'un message d'erreur si l'identifiant ou le mot de passe est incorrect
        erreur_label = Label(fenetre_connexion, text="Identifiant ou mot de passe incorrect")
        erreur_label.pack()


# Création de la fenêtre de connexion
fenetre_connexion = Tk()
fenetre_connexion.title("Login")
fenetre_connexion.geometry("400x300")

# Ajout des champs d'identifiant et de mot de passe
identifiant_label = Label(fenetre_connexion, text="Identifiant")
identifiant_entry = Entry(fenetre_connexion)
mot_de_passe_label = Label(fenetre_connexion, text="Mot de passe")
mot_de_passe_entry = Entry(fenetre_connexion, show="*")
identifiant_label.pack()
identifiant_entry.pack()
mot_de_passe_label.pack()
mot_de_passe_entry.pack()

# Ajout d'un bouton de connexion
bouton_login = Button(fenetre_connexion, text="Connexion", command=login)
bouton_login.pack()

# Lancement de la boucle principale de la fenêtre de connexion
fenetre_connexion.mainloop()



def calculate(*args):
    # Récupérer les valeurs saisies par l'utilisateur
    number1 = int(entry1.get())
    number2 = int(entry2.get())
    number3 = int(entry3.get())
    number4 = int(entry4.get())
    number5 = int(entry5.get())
    number6 = int(entry6.get())
    number7 = int(entry7.get())
    number8 = int(entry8.get())
    number9 = int(entry9.get())
    z1 = int(entry10.get())

    # Calculer les résultats
    result = number1 + number2 + number3 + number4 + number5 + number6 + number7 + number8 + number8 + number9
    idriss = int(result / (3000 * z1)) + 1
    rania = int(result / (1000 * z1)) + 1
    p1 = int(number1 / (1000 * z1)) + 1
    p2 = int(number2 / (1000 * z1)) + 1
    p3 = int(number3 / (1000 * z1)) + 1
    p4 = int(number4 / (1000 * z1)) + 1
    p5 = int(number5 / (1000 * z1)) + 1
    p6 = int(number6 / (1000 * z1)) + 1
    p7 = int(number7 / (1000 * z1)) + 1
    p8 = int(number8 / (1000 * z1)) + 1
    p9 = int(number9 / (1000 * z1)) + 1

    # Afficher les résultats
    result_label.config(text="La somme de nombre du plaque est égale à " + str(result), fg="red")
    number1_label.config(text="Le nombre de 12 pol : " + str(number1), bg="green", fg="black")
    number2_label.config(text="Le nombre de 24 pol : " + str(number2), bg="green", fg="black")
    number3_label.config(text="Le nombre de 52 pol : " + str(number3), bg="green", fg="black")
    number4_label.config(text="Le nombre de 54 pol : " + str(number4), bg="green", fg="black")
    number5_label.config(text="Le nombre de 64 pol : " + str(number5), bg="green", fg="black")
    number6_label.config(text="Le nombre de 9 pol : " + str(number6), bg="green", fg="black")
    number7_label.config(text="Le nombre de v1 : " + str(number7), bg="green", fg="black")
    number8_label.config(text="Le nombre de v2 : " + str(number8), bg="green", fg="black")
    number9_label.config(text="Le nombre de v3 : " + str(number9), bg="green", fg="black")
    z1_label.config(text="Le nombre de poste: " + str(z1), bg="purple")

    idriss_label.config(text="Le nombre humaine : " + str(idriss), bg="red", fg="black")
    rania_label.config(text="Le nombre de tambaure : " + str(rania), bg="red", fg="black")
    p1_label.config(text="Le nombre de tambaure pour 12 pol : " + str(p1), bg="blue", fg="black")
    p2_label.config(text="Le nombre de tambaure pour 24 pol : " + str(p2), bg="blue", fg="black")
    p3_label.config(text="Le nombre de tambaure pour 52 pol : " + str(p3), bg="blue", fg="black")
    p4_label.config(text="Le nombre de tambaure pour 54 pol : " + str(p4), bg="blue", fg="black")
    p5_label.config(text="Le nombre de tambaure pour 64 pol : " + str(p5), bg="blue", fg="black")
    p6_label.config(text="Le nombre de tambaure pour 9 pol : " + str(p6), bg="blue", fg="black")
    p7_label.config(text="Le nombre de tambaure pour v1 : " + str(p7), bg="blue", fg="black")
    p8_label.config(text="Le nombre de tambaure pour v2 : " + str(p8), bg="blue", fg="black")
    p9_label.config(text="Le nombre de tambaure pour v3 : " + str(p9), bg="blue", fg="black")


# Créer la fenêtre principale
root = Tk()

# Changement du titre de la fenêtre
root.title("zone SUSO")

# Configuration de la couleur de fond de la fenêtre
root.configure(bg="grey")

# Ajouter les champs de saisie et les étiquettes pour les résultats
entry1 = Entry(root, width=10)
entry1.grid(column=0, row=0)
number1_label = Label(root, text="Le nombre de 12 pol : ")
number1_label.grid(column=1, row=0)

entry2 = Entry(root, width=10)
entry2.grid(column=0, row=1)
number2_label = Label(root, text="Le nombre de 24 pol : ")
number2_label.grid(column=1, row=1)

entry3 = Entry(root, width=10)
entry3.grid(column=0, row=2)
number3_label = Label(root, text="Le nombre de 52 pol : ")
number3_label.grid(column=1, row=2)

entry4 = Entry(root, width=10)
entry4.grid(column=0, row=3)
number4_label = Label(root, text="Le nombre de 54 pol : ")
number4_label.grid(column=1, row=3)

entry5 = Entry(root, width=10)
entry5.grid(column=0, row=4)
number5_label = Label(root, text="Le nombre de 64 pol : ")
number5_label.grid(column=1, row=4)

entry6 = Entry(root, width=10)
entry6.grid(column=0, row=5)
number6_label = Label(root, text="Le nombre de 9 pol : ")
number6_label.grid(column=1, row=5)

entry7 = Entry(root, width=10)
entry7.grid(column=0, row=6)
number7_label = Label(root, text="Le nombre de v1: ")
number7_label.grid(column=1, row=6)

entry8 = Entry(root, width=10)
entry8.grid(column=0, row=7)
number8_label = Label(root, text="Le nombre de v2 : ")
number8_label.grid(column=1, row=7)

entry9 = Entry(root, width=10)
entry9.grid(column=0, row=8)
number9_label = Label(root, text="Le nombre de v3: ")
number9_label.grid(column=1, row=8)

entry10 = Entry(root, width=10)
entry10.grid(column=0, row=9)
z1_label = Label(root, text="z1 : ")
z1_label.grid(column=1, row=10)

result_label = Label(root, text="La somme de nombre du plaque est égale à ")
result_label.grid(column=0, row=14)

idriss_label = Label(root, text="Le nombre humaine : ")
idriss_label.grid(column=0, row=16)

rania_label = Label(root, text="Le nombre de tambaure : ")
rania_label.grid(column=0, row=18)

p1_label = Label(root, text="Le nombre de tambaure pour 12 pol : ")
p1_label.grid(column=5, row=20)

p2_label = Label(root, text="Le nombre de tambaure pour 24 pol : ")
p2_label.grid(column=5, row=21)

p3_label = Label(root, text="Le nombre de tambaure pour 52 pol : ")
p3_label.grid(column=5, row=22)

p4_label = Label(root, text="Le nombre de tambaure pour 54 pol : ")
p4_label.grid(column=5, row=23)

p5_label = Label(root, text="Le nombre de tambaure pour 64 pol : ")
p5_label.grid(column=5, row=24)

p6_label = Label(root, text="Le nombre de tambaure pour 9 pol : ")
p6_label.grid(column=5, row=25)

p7_label = Label(root, text="Le nombre de tambaure pour v1 : ")
p7_label.grid(column=5, row=26)

p8_label = Label(root, text="Le nombre de tambaure pour v2  : ")
p8_label.grid(column=5, row=27)

p9_label = Label(root, text="Le nombre de tambaure pour v3 : ")
p9_label.grid(column=5, row=28)

# Lier les champs de saisie à la fonction de calcul
entry1.bind('<KeyRelease>', calculate)
entry2.bind('<KeyRelease>', calculate)
entry3.bind('<KeyRelease>', calculate)
entry4.bind('<KeyRelease>', calculate)
entry5.bind('<KeyRelease>', calculate)
entry6.bind('<KeyRelease>', calculate)
entry7.bind('<KeyRelease>', calculate)
entry8.bind('<KeyRelease>', calculate)
entry9.bind('<KeyRelease>', calculate)

entry10.bind('<KeyRelease>', calculate)
i = 4
if i == 4:
    # Lancer la boucle principale
    root.mainloop()




