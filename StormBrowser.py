import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton

class NavigateurWeb(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.barre_de_recherche = QLineEdit()
        self.layout.addWidget(self.barre_de_recherche)

        self.bouton_rechercher = QPushButton("Rechercher")
        self.bouton_rechercher.clicked.connect(self.rechercher)
        self.layout.addWidget(self.bouton_rechercher)

        self.naviguateur_web = QWebEngineView()
        self.layout.addWidget(self.naviguateur_web)

    def rechercher(self):
        recherche = self.barre_de_recherche.text()
        if recherche:
            recherche = recherche.replace(" ", "+")  # Remplace les espaces par des +
            url = f"https://www.mojeek.com/search?q={recherche}"
            self.naviguateur_web.setUrl(QUrl(url))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    navigateur = NavigateurWeb()
    navigateur.show()
    sys.exit(app.exec_())