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
        self.btnInserir.clicked.connect(lambda: self.adicionar_item_Tabela_Turma_has_Alunos(db, "Frequencia"))
        self.btnExcluir.clicked.connect(lambda: self.remover_item_Tabela_Turma_has_Alunos(db, "Frequencia"))
        self.btnEditar.clicked.connect(lambda: self.editar_item_Tabela_Turma_has_Alunos(db, "Frequencia"))
        self.lineBusca.textChanged.connect(lambda: self.buscar_item_Tabela_Turma_has_Alunos(db, "vw_Turm_has_Alunos"))

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
            self.tableTurma_has_Alunos.setItem(i, 2, QTableWidgetItem(str(idTurma)))
            self.tableTurma_has_Alunos.setItem(i, 3, QTableWidgetItem(str(nomeTurma)))

    def check_if_exists_in_db(self, result, nomeAluno, nomeTurma):
        for i, entry in enumerate(result):
            if nomeAluno == entry['nomeAluno'] and nomeTurma == entry['nomeTurma']:
                erro = QMessageBox()
                erro.setText("Esse Aluno já está na Turma!")
                erro.exec()
                return 1
        return 0

    def adicionar_item_Tabela_Turma_has_Alunos(self, db, table_name):
        query = "SELECT * FROM " + "vw_Turma_has_Alunos"
        db.cur.execute(query)
        result = db.cur.fetchall()
        nomeAluno  = self.linenomeAluno.text()
        nomeTurma  = self.lineNomeTurma.text()
        matricula  = self.lineMatricula.text()  
        if(nomeAluno != '' and nomeTurma != ''):
            num_rows = db.returnNumRows(table_name)

            if self.check_if_exists_in_db(result, nomeAluno, nomeTurma) == 0:
                query = "SELECT idTurma FROM Turma WHERE nomeTurma = '{0}'".format(nomeTurma)
                db.cur.execute(query)
                result = db.cur.fetchall()
                if result == ():
                    erro = QMessageBox()
                    erro.setText("Essa Turma não existe")
                    erro.exec()
                    return
                else:
                    for i, data in enumerate(result):
                        idTurma = data["idTurma"]
                query = "SELECT idAluno FROM Aluno WHERE nomeAluno = '{0}'".format(nomeAluno)
                db.cur.execute(query)
                result = db.cur.fetchall()
                #se a turma nao existe
                if result == ():
                    #create ALUNO
                    query = "INSERT INTO Aluno VALUES(NULL, '{0}', '{1}')".format(nomeAluno, matricula)

                    db.cur.execute(query)
                    print("query", query)
                    print("cur:",db.cur.fetchall())

                    db.db.commit()
                    query = "SELECT idAluno FROM Aluno WHERE nomeAluno = '{0}'".format(nomeAluno)
                    db.cur.execute(query)
                    result = db.cur.fetchall()
                    for i, data in enumerate(result):
                        idAluno = data["idAluno"]
                    #insert into C_h_D
                    query = "INSERT INTO Frequencia VALUES(NULL, '{0}', '{1}', NULL, NULL)".format(idTurma, idAluno)
                    db.cur.execute(query)
                    db.db.commit()
                else:
                    #add idAluno, idTurma no Turma_has_Alunos
                    for i, data in enumerate(result):
                        idAluno = data["idAluno"]
                    query = "INSERT INTO Frequencia VALUES(NULL, '{0}', '{1}', NULL, NULL)".format(idTurma, idAluno)
                    db.cur.execute(query)
                    db.db.commit()

                # query = "INSERT INTO %s VALUES (NULL, '%s', '%s')" % (Turma_has_Alunos, idTurma, idAluno)
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
        idAluno = int(item.text())

        item = self.tableTurma_has_Alunos.item(row, 0)
        idTurma = int(item.text())
#       remover aluno do Turma
        query = "DELETE FROM Frequencia WHERE Aluno_idAluno = {0} AND Turma_idTurma = {1}".format(idAluno, idTurma)
        print(query)
        db.cur.execute(query)
        db.db.commit()
        self.popularTabela(db, "vw_Turma_has_Alunos")

        # if self.check_if_exists_in_another_table(id) == 0:
        #     query = "DELETE FROM %s WHERE Turma_idTurma = %d" % (table_name, id)
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

        idTurma = int(self.tableTurma_has_Alunos.item(row,0).text())
        nomeTurma = str(self.tableTurma_has_Alunos.item(row,1).text())
        idAluno = int(self.tableTurma_has_Alunos.item(row,2).text())
        nomeAluno = str(self.tableTurma_has_Alunos.item(row,3).text())

        query = "SELECT nomeTurma, idTurma FROM Turma WHERE nomeTurma = '{0}'".format(nomeTurma)
        result = db.cur.execute(query);
        if result == 0:
            #turma não existe, só dar update
            query = "UPDATE Turma SET nomeTurma = '{0}' WHERE idTurma = '{1}'".format(nomeTurma, idTurma)
            db.cur.execute(query)
            db.db.commit()
        else:
            #turma existe, mudar ids
            valor = db.cur.fetchall()
            for i, row in enumerate(valor):
                idTurmaNEW = row["idTurma"]

            query = "UPDATE Turma SET idTurma = '{0}' WHERE idTurma = '{1}'".format(idTurmaNEW, idTurma)
            db.cur.execute(query)
            db.db.commit()


        # query = "SELECT nomeAluno FROM Aluno WHERE nomeAluno = '{0}'".format(nomeAluno)
        # result = db.cur.execute(query)
        # if result == 0:
        #     #aluno não existe
        #     #cria aluno
        # else:
        #     #aluno existe


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
            self.tableTurma_has_Alunos.setItem(i, 2, QTableWidgetItem(str(idTurma)))
            self.tableTurma_has_Alunos.setItem(i, 3, QTableWidgetItem(str(nomeTurma)))
