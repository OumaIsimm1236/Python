from PyQt5 import QtWidgets, QtCore, QtGui
from design import Ui_MainWindow as GUI


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.window = GUI()
        self.window.setupUi(self)
        self.window.retranslateUi(self)
        self.window.stackedWidget.setCurrentIndex(0)

        self.window.connectBtn.clicked.connect(self.authenticate_user)

        # Ajout d'une action au bouton de calcul
        self.window.calculateBtn.clicked.connect(self.calculate_sum)

    def authenticate_user(self):
        username = self.window.username.text()
        password = self.window.password.text()
        if username == "admin" and password == "1234":
            self.window.stackedWidget.setCurrentIndex(1)
        else:
            QtWidgets.QMessageBox.warning(self, "Title", "Authentication failed")

    def calculate_sum(self):
        x1 = int(self.window.input1.text())
        x2 = int(self.window.input2.text())
        z1 = int(self.window.divisor.text())

        # Calcul de la somme
        result = x1 + x2

        # Calcul de la division
        if z1 != 0:
            result = result / z1

        # Affichage du résultat
        self.window.resultLabel.setText(str(result))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    sys.exit(app.exec_())
