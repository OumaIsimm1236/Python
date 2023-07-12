import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(200, 200, 400, 300)

        # Création des champs d'identifiant et de mot de passe
        identifiant_label = QLabel("Identifiant")
        self.identifiant_entry = QLineEdit()
        mot_de_passe_label = QLabel("Mot de passe")
        self.mot_de_passe_entry = QLineEdit()
        self.mot_de_passe_entry.setEchoMode(QLineEdit.Password)

        # Ajout d'un bouton de connexion
        bouton_login = QPushButton("Connexion")
        bouton_login.clicked.connect(self.login)

        # Ajout d'un layout vertical pour les champs et le bouton de connexion
        layout_vertical = QVBoxLayout()
        layout_vertical.addWidget(identifiant_label)
        layout_vertical.addWidget(self.identifiant_entry)
        layout_vertical.addWidget(mot_de_passe_label)
        layout_vertical.addWidget(self.mot_de_passe_entry)
        layout_vertical.addWidget(bouton_login)

        # Création d'un widget pour contenir le layout vertical
        widget = QWidget()
        widget.setLayout(layout_vertical)

        self.setCentralWidget(widget)

    def login(self):
        # Vérification de l'identifiant et du mot de passe
        if self.identifiant_entry.text() == "admin" and self.mot_de_passe_entry.text() == "1234":
            # Suppression de la fenêtre de connexion
            self.close()

            # Création de la fenêtre de résultat
            resultat_window = ResultatWindow()
            resultat_window.show()
        else:
            # Affichage d'un message d'erreur si l'identifiant ou le mot de passe est incorrect
            erreur_label = QLabel("Identifiant ou mot de passe incorrect")
            layout_vertical.addWidget(erreur_label)


class ResultatWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Résultat")
        self.setGeometry(200, 200, 400, 300)
        # Configuration de la fenêtre principale
        self.setWindowTitle("zone SUSO")
        self.setStyleSheet("background-color: grey")

        # Ajouter les champs de saisie et les étiquettes pour les résultats
        self.entry1 = QLineEdit()
        self.number1_label = QLabel("Le nombre de 12 pol : ")

        self.entry10 = QLineEdit()
        self.z1_label = QLabel("z1 : ")

        self.result_label = QLabel("La somme de nombre du plaque est égale à ")
        self.idriss_label = QLabel("Le nombre humaine : ")
        self.rania_label = QLabel("Le nombre de tambaure : ")
        self.p1_label = QLabel("Le nombre de tambaure pour 12 pol : ")

        # Créer une mise en page verticale pour les widgets
        layout = QVBoxLayout()
        layout.addWidget(self.entry1)
        layout.addWidget(self.number1_label)

        layout.addWidget(self.entry10)
        layout.addWidget(self.z1_label)

        layout.addWidget(self.result_label)
        layout.addWidget(self.idriss_label)
        layout.addWidget(self.rania_label)
        layout.addWidget(self.p1_label)

        self.setLayout(layout)

        # Lier les champs de saisie à la fonction de calcul
        self.entry1.textChanged.connect(self.calculate)
        self.entry10.textChanged.connect(self.calculate)

    def calculate(self):
        # Récupérer les valeurs saisies par l'utilisateur
        number1 = int(self.entry1.text())
        z1 = int(self.entry10.text())

        # Calculer les résultats
        result = number1
        idriss = int(result / (3000 * z1)) + 1
        rania = int(result / (1000 * z1)) + 1
        p1 = int(number1 / (1000 * z1)) + 1

        # Afficher les résultats
        self.result_label.setText("La somme de nombre du plaque est égale à " + str(result))
        self.number1_label.setText("Le nombre de 12 pol : " + str(number1))
        self.z1_label.setText("Le nombre de poste: " + str(z1))
        self.idriss_label.setText("Le nombre humaine : " + str(idriss))
        self.rania_label.setText("Le nombre de tambaure : " + str(rania))
        self.p1_label.setText("Le nombre de tambaure pour 12 pol : " + str(p1))

    if __name__ == '__main__':
        # Créer l'application et la fenêtre principale
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()

        # Lancer la boucle principale
        sys.exit(app.exec_())