#!/usr/bin/python
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from view.mainWindow import Ui_MainWindow

from database import Database

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()

    db = Database("127.0.0.1", "viriato", "dinossauro", "mydb")
    db.populaTabela("Curso")
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()