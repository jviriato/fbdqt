from PyQt5.QtWidgets import *
from view.curso_has_disciplina import Ui_curso_has_disciplina

from main import *
class Curso_has_Disciplina(QMainWindow, Ui_curso_has_disciplina):
    def __init__(self):
        super(Curso_has_Disciplina, self).__init__()
        self.setupUi(self)
        header = self.tableCurso_has_Disciplina.setColumnWidth(1, 300)
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
            Curso_idCurso = row["nomeCurso"]
            Disciplina_idDisciplina = row["nomeDisciplina"]
            self.tableCurso_has_Disciplina.setItem(i, 0, QTableWidgetItem(str(Curso_idCurso)))
            self.tableCurso_has_Disciplina.setItem(i, 1, QTableWidgetItem(str(Disciplina_idDisciplina)))

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
                    print(idCurso, "Oiiwjd")
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
        item = self.tableCurso_has_Disciplina.item(row,0)

        id = int(item.text())
        if self.check_if_exists_in_another_table(id) == 0:
            query = "DELETE FROM %s WHERE Curso_idCurso = %d" % (table_name, id)
            db.cur.execute(query)
            db.db.commit()
            self.popularTabela(db, "curso_e_disc")
        else:
            erro = QMessageBox()
            erro.setText("Curso_has_Disciplina presente na tabela Curso_has_Disciplina!")
            erro.exec()



    def editar_item_Tabela_Curso_has_Disciplinas(self, db, table_name):
        index = self.tableCurso_has_Disciplina.currentIndex()
        row = index.row()
        column = index.column()

        Curso_idCurso = int(self.tableCurso_has_Disciplina.item(row,0).text())
        Disciplina_idDisciplina = str(self.tableCurso_has_Disciplina.item(row,1).text())

        query = "UPDATE %s SET Disciplina_idDisciplina = '%s' WHERE Curso_idCurso = %d" % (table_name, Disciplina_idDisciplina, Curso_idCurso)
        db.cur.execute(query)
        db.db.commit()
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
