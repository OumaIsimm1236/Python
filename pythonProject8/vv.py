from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter as tk

fenetre_resultat = None
fenetre_connexion = None

result = {}
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

def login(identifiant_entry, mot_de_passe_entry):
    global fenetre_resultat, fenetre_connexion

    # Vérification de l'identifiant et du mot de passe
    if identifiant_entry.get() == "admin" and mot_de_passe_entry.get() == "1234":
        # Suppression de la fenêtre de connexion
        fenetre_connexion.destroy()
    else:
        # Affichage d'un message d'erreur si l'identifiant ou le mot de passe est incorrect
        messagebox.showerror("Erreur", "Identifiant ou mot de passe incorrect")


# Création de la fenêtre de connexion
fenetre_connexion = tk.Tk()
fenetre_connexion.title("Login")
fenetre_connexion.geometry("400x300")
# Create a photoimage object of the image in the path
image1 = Image.open("C:/Users/lenovo/Downloads/ranya.png")
test = ImageTk.PhotoImage(image1)

label1 = tk.Label(image=test)
label1.image = test

# Position image
label1.place(x=0, y=0, relwidth=1, relheight=1)

# Ajout des champs d'identifiant et de mot de passe

identifiant_label = Label(fenetre_connexion, text="Identifiant")
identifiant_entry = tk.Entry(fenetre_connexion)
mot_de_passe_label = Label(fenetre_connexion, text="Mot de passe")
mot_de_passe_entry = tk.Entry(fenetre_connexion, show="*")
identifiant_label.pack()
identifiant_entry.pack()
mot_de_passe_label.pack()
mot_de_passe_entry.pack()

# Ajout d'un bouton de connexion
bouton_login = Button(fenetre_connexion, text="Connexion", command=lambda: login(identifiant_entry, mot_de_passe_entry))
bouton_login.pack()

# Lancement de la boucle principale de la fenêtre de connexion
fenetre_connexion.mainloop()

# Créer la fenêtre principale
fenetre_resultat = tk.Tk()

# Changement du titre de la fenêtre
fenetre_resultat.title("zone SUSO")

# Create a photoimage object of the image in the path
image1 = Image.open("C:/Users/lenovo/Downloads/ranya.png")
test = ImageTk.PhotoImage(image1)

label1 = tk.Label(image=test)
label1.image = test

# Position image
label1.place(x=0, y=0, relwidth=1, relheight=1)

label_frame = tk.LabelFrame(fenetre_resultat, text="Enter data")
label_frame.pack()

# Create a button to trigger the calculation
calculate_button = tk.Button(label_frame, text="Calculate", command=calculate)
calculate_button.pack()

fenetre_resultat.mainloop()
