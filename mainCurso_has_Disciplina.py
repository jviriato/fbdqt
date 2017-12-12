from PyQt5.QtWidgets import *
from view.curso_has_disciplina import Ui_curso_has_disciplina

from main import *
class Curso_has_Disciplina(QMainWindow, Ui_curso_has_disciplina):
    def __init__(self):
        super(Curso_has_Disciplina, self).__init__()
        self.setupUi(self)
        header = self.tableCurso_has_Disciplina.setColumnWidth(1, 200)
        header = self.tableCurso_has_Disciplina.setColumnWidth(3, 300)
        header = self.tableCurso_has_Disciplina.setColumnWidth(0, 50)
        header = self.tableCurso_has_Disciplina.setColumnWidth(2, 50)
        self.btnInserir.clicked.connect(lambda: self.adicionar_item_Tabela_Curso_has_Disciplinas(db, "Curso_has_Disciplina"))
        self.btnExcluir.clicked.connect(lambda: self.remover_item_Tabela_Curso_has_Disciplinas(db, "Curso_has_Disciplina"))
        self.btnEditar.clicked.connect(lambda: self.editar_item_Tabela_Curso_has_Disciplinas(db, "Curso_has_Disciplina"))
        self.lineBusca.textChanged.connect(lambda: self.buscar_item_Tabela_Curso_has_Disciplinas(db, "Curso_has_Disciplina"))

    def popularTabela(self, db, table_name):
        num_rows = db.returnNumRows(table_name)
        self.tableCurso_has_Disciplina.setRowCount(num_rows)
        query = "SELECT * FROM " + table_name
        db.cur.execute(query)
        result = db.cur.fetchall()
        print(result)

        for i, row in enumerate(result):
            idCurso = row["idCurso"]
            idDisciplina = row["idDisciplina"]
            nomeDisciplina = row["nomeDisciplina"]
            nomeCurso = row["nomeCurso"]
            self.tableCurso_has_Disciplina.setItem(i, 0, QTableWidgetItem(str(idCurso)))
            self.tableCurso_has_Disciplina.setItem(i, 1, QTableWidgetItem(str(nomeCurso)))
            self.tableCurso_has_Disciplina.setItem(i, 2, QTableWidgetItem(str(idDisciplina)))
            self.tableCurso_has_Disciplina.setItem(i, 3, QTableWidgetItem(str(nomeDisciplina)))

    def check_if_exists_in_db(self, result, nomeDisciplina, nomeCurso):
        for i, entry in enumerate(result):
            if nomeDisciplina == entry['nomeDisciplina'] and nomeCurso == entry['nomeCurso']:
                erro = QMessageBox()
                erro.setText("Essa Disciplina já está no Curso!")
                erro.exec()
                return 1
        return 0

    def adicionar_item_Tabela_Curso_has_Disciplinas(self, db, table_name):
        query = "SELECT * FROM " + "curso_e_disc"
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
                    query = "INSERT INTO Curso_has_Disciplina VALUES('{0}', '{1}')".format(idCurso, idDisciplina)
                    db.cur.execute(query)
                    db.db.commit()
                else:
                    #add idDisciplina, idCurso no Curso_has_Disciplina
                    for i, data in enumerate(result):
                        idDisciplina = data["idDisciplina"]
                    query = "INSERT INTO Curso_has_Disciplina VALUES('{0}', '{1}')".format(idCurso, idDisciplina)
                    db.cur.execute(query)
                    db.db.commit()

                # query = "INSERT INTO %s VALUES (NULL, '%s', '%s')" % (Curso_has_Disciplina, idCurso, idDisciplina)
                # print(query)
                # db.cur.execute(query)
                # db.db.commit()
                self.popularTabela(db, "curso_e_disc")

    def remover_item_Tabela_Curso_has_Disciplinas(self, db, table_name):
        index = self.tableCurso_has_Disciplina.currentIndex()
        row = index.row()
        column = index.column()
        # print(row, column)

        #column 0 = id
        item = self.tableCurso_has_Disciplina.item(row,2)
        idDisciplina = int(item.text())

        item = self.tableCurso_has_Disciplina.item(row, 0)
        idCurso = int(item.text())
#       remover disciplina do Curso
        query = "DELETE FROM Curso_has_Disciplina WHERE Disciplina_idDisciplina = {0} AND Curso_idCurso = {1}".format(idDisciplina, idCurso)
        print(query)
        db.cur.execute(query)
        db.db.commit()
        self.popularTabela(db, "curso_e_disc")

        # if self.check_if_exists_in_another_table(id) == 0:
        #     query = "DELETE FROM %s WHERE Curso_idCurso = %d" % (table_name, id)
        #     db.cur.execute(query)
        #     db.db.commit()
        #     self.popularTabela(db, "curso_e_disc")
        # else:
        #     erro = QMessageBox()
        #     erro.setText("Curso_has_Disciplina presente na tabela Curso_has_Disciplina!")
        #     erro.exec()


    def editar_item_Tabela_Curso_has_Disciplinas(self, db, table_name):
        index = self.tableCurso_has_Disciplina.currentIndex()
        row = index.row()
        column = index.column()

        idCurso = int(self.tableCurso_has_Disciplina.item(row,0).text())
        nomeCurso = str(self.tableCurso_has_Disciplina.item(row,1).text())
        idDisciplina = int(self.tableCurso_has_Disciplina.item(row,2).text())
        nomeDisciplina = str(self.tableCurso_has_Disciplina.item(row,3).text())

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


        self.popularTabela(db, "curso_e_disc")

    def buscar_item_Tabela_Curso_has_Disciplinas(self, db, table_name):
        text = self.lineBusca.text()
        query = "SELECT * FROM {0} WHERE {1} LIKE '{2}%' OR {3} LIKE '{2}%'".format("curso_e_disc", "nomeCurso", text, "nomeDisciplina")
        num_rows = db.cur.execute(query)
        result = db.cur.fetchall()

        self.tableCurso_has_Disciplina.setRowCount(num_rows)
        for i, row in enumerate(result):
            Curso_idCurso = row["nomeCurso"]
            Disciplina_idDisciplina = row["nomeDisciplina"]
            self.tableCurso_has_Disciplina.setItem(i, 0, QTableWidgetItem(str(Curso_idCurso)))
            self.tableCurso_has_Disciplina.setItem(i, 1, QTableWidgetItem(str(Disciplina_idDisciplina)))
