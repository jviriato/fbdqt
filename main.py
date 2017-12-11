#!/usr/bin/python
import sys

from database import Database
from mainCurso import *
from view.main import Ui_MainWindow

db = Database("127.0.0.1", "viriato", "dinossauro", "mydb")

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.btnCursos.clicked.connect(lambda: self.clicou_em_Cursos())

    def clicou_em_Cursos(self):
         window_curso = Curso()
         window_curso.show()
         window_curso.popularTabela(db, "Curso")


def main():

    app = QApplication(sys.argv)
    window_main = MainWindow()
    window_main.show()

    # window_curso = Curso()
    # window_curso.show()
    # window_curso.popularTabela(db, "Curso")
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()