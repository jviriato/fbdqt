from PyQt5.QtWidgets import *
from view.turma_has_alunos import Ui_Alunos_em_Turmas

from main import *
class Turma_has_alunos(QMainWindow, Ui_Alunos_em_Turmas):
    def __init__(self):
        super(Turma_has_alunos, self).__init__()
        self.setupUi(self)
        header = self.tableTurma_has_Alunos.setColumnWidth(0, 90)
        header = self.tableTurma_has_Alunos.setColumnWidth(1, 300)
        header = self.tableTurma_has_Alunos.setColumnWidth(2, 90)
        header = self.tableTurma_has_Alunos.setColumnWidth(3, 300)
        self.btnInserir.clicked.connect(lambda: self.adicionar_item_Tabela_Turma_has_Alunos(db, "Turma_has_Alunos"))
        self.btnExcluir.clicked.connect(lambda: self.remover_item_Tabela_Turma_has_Alunos(db, "Turma_has_Alunos"))
        self.btnEditar.clicked.connect(lambda: self.editar_item_Tabela_Turma_has_Alunos(db, "Turma_has_Alunos"))
        self.lineBusca.textChanged.connect(lambda: self.buscar_item_Tabela_Turma_has_Alunos(db, "Turma_has_Alunos"))

    def popularTabela(self, db, table_name):
        num_rows = db.returnNumRows(table_name)
        self.tableTurma_has_Alunos.setRowCount(num_rows)
        query = "SELECT * FROM " + table_name
        db.cur.execute(query)
        result = db.cur.fetchall()
        print(result)

        for i, row in enumerate(result):
            idAluno = row["idAluno"]
            nomeAluno = row["nomeAluno"]
            idTurma = row["idTurma"]
            nomeTurma = row["nomeTurma"]
            self.tableTurma_has_Alunos.setItem(i, 0, QTableWidgetItem(str(idAluno)))
            self.tableTurma_has_Alunos.setItem(i, 1, QTableWidgetItem(str(nomeAluno)))
            self.tableTurma_has_Alunos.setItem(i, 2, QTableWidgetItem(str(idAluno)))
            self.tableTurma_has_Alunos.setItem(i, 3, QTableWidgetItem(str(nomeTurma)))

    def check_if_exists_in_db(self, result, nomeDisciplina, nomeCurso):
        for i, entry in enumerate(result):
            if nomeDisciplina == entry['nomeDisciplina'] and nomeCurso == entry['nomeCurso']:
                erro = QMessageBox()
                erro.setText("Essa Disciplina já está no Curso!")
                erro.exec()
                return 1
        return 0

    def adicionar_item_Tabela_Turma_has_Alunos(self, db, table_name):
        query = "SELECT * FROM " + "vw_Turma_has_Alunos"
        db.cur.execute(query)
        result = db.cur.fetchall()
        nomeDisciplina  = self.linenomeDisciplina.text()
        nomeCurso  = self.lineNomeCurso.text()
        if(nomeDisciplina != '' and nomeCurso != ''):
            num_rows = db.returnNumRows(table_name)

            if self.check_if_exists_in_db(result, nomeDisciplina, nomeCurso) == 0:
                query = "SELECT idCurso FROM Curso WHERE nomeCurso = '{0}'".format(nomeCurso)
                db.cur.execute(query)
                result = db.cur.fetchall()
                if result == ():
                    erro = QMessageBox()
                    erro.setText("Esse Curso não existe")
                    erro.exec()
                    return
                else:
                    for i, data in enumerate(result):
                        idCurso = data["idCurso"]
                query = "SELECT idDisciplina FROM Disciplina WHERE nomeDisciplina = '{0}'".format(nomeDisciplina)
                db.cur.execute(query)
                result = db.cur.fetchall()
                #se a disciplina nao existe
                if result == ():
                    #create DISCIPLINA
                    query = "INSERT INTO Disciplina VALUES(NULL, '{0}')".format(nomeDisciplina)
                    db.cur.execute(query)
                    db.db.commit()
                    query = "SELECT idDisciplina FROM Disciplina WHERE nomeDisciplina = '{0}'".format(nomeDisciplina)
                    db.cur.execute(query)
                    result = db.cur.fetchall()
                    for i, data in enumerate(result):
                        idDisciplina = data["idDisciplina"]
                    #insert into C_h_D
                    query = "INSERT INTO Turma_has_Alunos VALUES('{0}', '{1}')".format(idCurso, idDisciplina)
                    db.cur.execute(query)
                    db.db.commit()
                else:
                    #add idDisciplina, idCurso no Turma_has_Alunos
                    for i, data in enumerate(result):
                        idDisciplina = data["idDisciplina"]
                    query = "INSERT INTO Turma_has_Alunos VALUES('{0}', '{1}')".format(idCurso, idDisciplina)
                    db.cur.execute(query)
                    db.db.commit()

                # query = "INSERT INTO %s VALUES (NULL, '%s', '%s')" % (Turma_has_Alunos, idCurso, idDisciplina)
                # print(query)
                # db.cur.execute(query)
                # db.db.commit()
                self.popularTabela(db, "vw_Turma_has_Alunos")

    def remover_item_Tabela_Turma_has_Alunos(self, db, table_name):
        index = self.tableTurma_has_Alunos.currentIndex()
        row = index.row()
        column = index.column()
        # print(row, column)

        #column 0 = id
        item = self.tableTurma_has_Alunos.item(row,2)
        idDisciplina = int(item.text())

        item = self.tableTurma_has_Alunos.item(row, 0)
        idCurso = int(item.text())
#       remover disciplina do Curso
        query = "DELETE FROM Turma_has_Alunos WHERE Disciplina_idDisciplina = {0} AND Curso_idCurso = {1}".format(idDisciplina, idCurso)
        print(query)
        db.cur.execute(query)
        db.db.commit()
        self.popularTabela(db, "vw_Turma_has_Alunos")

        # if self.check_if_exists_in_another_table(id) == 0:
        #     query = "DELETE FROM %s WHERE Curso_idCurso = %d" % (table_name, id)
        #     db.cur.execute(query)
        #     db.db.commit()
        #     self.popularTabela(db, "vw_Turma_has_Alunos")
        # else:
        #     erro = QMessageBox()
        #     erro.setText("Turma_has_Alunos presente na tabela Turma_has_Alunos!")
        #     erro.exec()


    def editar_item_Tabela_Turma_has_Alunos(self, db, table_name):
        index = self.tableTurma_has_Alunos.currentIndex()
        row = index.row()
        column = index.column()

        idCurso = int(self.tableTurma_has_Alunos.item(row,0).text())
        nomeCurso = str(self.tableTurma_has_Alunos.item(row,1).text())
        idDisciplina = int(self.tableTurma_has_Alunos.item(row,2).text())
        nomeDisciplina = str(self.tableTurma_has_Alunos.item(row,3).text())

        query = "SELECT nomeCurso, idCurso FROM Curso WHERE nomeCurso = '{0}'".format(nomeCurso)
        result = db.cur.execute(query);
        if result == 0:
            #curso não existe, só dar update
            query = "UPDATE Curso SET nomeCurso = '{0}' WHERE idCurso = '{1}'".format(nomeCurso, idCurso)
            db.cur.execute(query)
            db.db.commit()
        else:
            #curso existe, mudar ids
            valor = db.cur.fetchall()
            for i, row in enumerate(valor):
                idCursoNEW = row["idCurso"]

            query = "UPDATE Curso SET idCurso = '{0}' WHERE idCurso = '{1}'".format(idCursoNEW, idCurso)
            db.cur.execute(query)
            db.db.commit()


        # query = "SELECT nomeDisciplina FROM Disciplina WHERE nomeDisciplina = '{0}'".format(nomeDisciplina)
        # result = db.cur.execute(query)
        # if result == 0:
        #     #disciplina não existe
        #     #cria disciplina
        # else:
        #     #disciplina existe


        self.popularTabela(db, "vw_Turma_has_Alunos")

    def buscar_item_Tabela_Turma_has_Alunos(self, db, table_name):
        text = self.lineBusca.text()
        query = "SELECT * FROM {0} WHERE {1} LIKE '{2}%' OR {3} LIKE '{2}%'".format("vw_Turma_has_Alunos", "nomeAluno", text, "nomeTurma")
        num_rows = db.cur.execute(query)
        result = db.cur.fetchall()

        self.tableTurma_has_Alunos.setRowCount(num_rows)
        for i, row in enumerate(result):
            idAluno = row["idAluno"]
            nomeAluno = row["nomeAluno"]
            idTurma = row["idTurma"]
            nomeTurma = row["nomeTurma"]
            self.tableTurma_has_Alunos.setItem(i, 0, QTableWidgetItem(str(idAluno)))
            self.tableTurma_has_Alunos.setItem(i, 1, QTableWidgetItem(str(nomeAluno)))
            self.tableTurma_has_Alunos.setItem(i, 2, QTableWidgetItem(str(idAluno)))
            self.tableTurma_has_Alunos.setItem(i, 3, QTableWidgetItem(str(nomeTurma)))
