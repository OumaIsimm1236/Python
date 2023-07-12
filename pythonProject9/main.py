from PyQt5 import QtWidgets, QtCore, QtGui
from design import Ui_MainWindow as GUI

import sys

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.window = GUI()
        self.window.setupUi(self)
        self.window.retranslateUi(self)
        self.window.stackedWidget.setCurrentIndex(0)

        self.window.connectBtn.clicked.connect(self.authenticate_user)

        # Connexion du bouton pour effectuer le calcul
        self.window.calculateBtn.clicked.connect(self.calculate)

    def authenticate_user(self):
        username = self.window.username.text()
        password = self.window.password.text()
        if username == "admin" and password == "1234":
            self.window.stackedWidget.setCurrentIndex(1)
        else:
            QtWidgets.QMessageBox.warning(self, "Title", "Authentication failed")

    def calculate(self):
        # Récupération des nombres saisis
        num1 = float(self.window.num1Edit.text())
        num2 = float(self.window.num2Edit.text())

        # Calcul de la somme et affichage dans la fenêtre de résultat
        result_sum = num1 + num2
        self.window.sumResultLabel.setText(str(result_sum))

        # Calcul de la multiplication et affichage dans la fenêtre de résultat
        z1 = result_sum * 10
        self.window.multResultLabel.setText(str(z1))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    sys.exit(app.exec_())

