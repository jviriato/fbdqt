#!/usr/bin/python
import sys

from database import Database
from mainCurso import *
from mainProfessor import *
from mainDisciplina import *
from mainAluno import *
from mainTurma import *
from mainCurso_has_Disciplina import *

from view.main import Ui_MainWindow

db = Database("127.0.0.1", "viriato", "dinossauro", "mydb")

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.btnCursos.clicked.connect(lambda: self.clicou_em_Cursos())
        self.btnProfessores.clicked.connect(lambda: self.clicou_em_Professores())
        self.btnDisciplinas.clicked.connect(lambda: self.clicou_em_Disciplinas())
        self.btnAlunos.clicked.connect(lambda: self.clicou_em_Alunos())
        self.btnCurso_has_Disciplinas.clicked.connect(lambda: self.clicou_em_Curso_has_Disciplinas())
        self.btnTurmas.clicked.connect(lambda: self.clicou_em_Turmas())



    def clicou_em_Cursos(self):
         window_curso = Curso()
         window_curso.show()
         window_curso.popularTabela(db, "Curso")

    def clicou_em_Professores(self):
         window_professor = Professor()
         window_professor.show()
         window_professor.popularTabela(db, "Professor")
            
    def clicou_em_Disciplinas(self):
         window_disciplina = Disciplina()
         window_disciplina.show()
         window_disciplina.popularTabela(db, "Disciplina")

    def clicou_em_Curso_has_Disciplinas(self):
         window_disciplina = Curso_has_Disciplina()
         window_disciplina.show()
         window_disciplina.popularTabela(db, "curso_e_disc")

    def clicou_em_Alunos(self):
         window_aluno = Aluno()
         window_aluno.show()
         window_aluno.popularTabela(db, "Aluno")

    def clicou_em_Turmas(self):
         window_aluno = Turma()
         window_aluno.show()
         window_aluno.popularTabela(db, "vw_Turma")

def main():

    app = QApplication(sys.argv)
    window_main = MainWindow()
    window_main.show()

    sys.exit(app.exec_())



if __name__ == "__main__":
    main()
