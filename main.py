#!/usr/bin/python
import sys

from database import Database
from mainCurso import *
from mainProfessor import *

from view.main import Ui_MainWindow

db = Database("127.0.0.1", "viriato", "dinossauro", "mydb")
#teste
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.btnCursos.clicked.connect(lambda: self.clicou_em_Cursos())
        self.btnProfessores.clicked.connect(lambda: self.clicou_em_Professores())

    def clicou_em_Cursos(self):
         window_curso = Curso()
         window_curso.show()
         window_curso.popularTabela(db, "Curso")

    def clicou_em_Professores(self):
         window_professor = Professor()
         window_professor.show()
         window_professor.popularTabela(db, "Professor")


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