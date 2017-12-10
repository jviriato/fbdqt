#!/usr/bin/python
import sys

from PyQt5.QtWidgets import *
from view.mainWindow import Ui_MainWindow

from database import Database

db = Database("127.0.0.1", "viriato", "dinossauro", "mydb")


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.btnInserir.clicked.connect(lambda: self.adicionar_item_Tabela_Cursos(db, "Curso"));

    def popularTabela(self, db, table_name):
        num_rows = db.returnNumRows(table_name)
        self.tableCurso.setRowCount(num_rows)
        query = "SELECT * FROM " + table_name
        db.cur.execute(query)
        result = db.cur.fetchall()

        for num, valores in enumerate(result):
            # print(num,valores["siglaCurso"])
            col = 0
            for col_number, data in valores.items():
                print(data, "col:", col)
                self.tableCurso.setItem(num, col, QTableWidgetItem(str(data)))
                col = col + 1
                if col == num_rows:
                    col = 0


    def check_if_exists_in_db(self, result, siglaCurso, nomeCurso):
        for i, entry in enumerate(result):
            if siglaCurso == entry['siglaCurso']:
                print("Essa sigla já existe!")
                return 1
            elif nomeCurso == entry['nomeCurso']:
                print("Esse curso já existe!")
                return 1
        return 0

    def adicionar_item_Tabela_Cursos(self, db, table_name):
        query = "SELECT * FROM " + table_name
        db.cur.execute(query)
        result = db.cur.fetchall()
        nomeCurso  = self.linenomeCurso.text()
        siglaCurso = self.lineSiglaCurso.text()

        if(nomeCurso != '' and siglaCurso != ''):
            num_rows = db.returnNumRows(table_name)
            self.tableCurso.setRowCount(num_rows + 1)

            if self.check_if_exists_in_db(result, siglaCurso, nomeCurso) == 0:
                query = "INSERT INTO %s VALUES ('%s', '%s', '%s')" % (
                table_name, db.returncountId("Curso") + 1, nomeCurso, siglaCurso)
                print(query)
                db.cur.execute(query)
                db.db.commit()
                # db.commit_isso(query);





                # query = "SELECT EXISTS(SELECT * FROM %s WHERE siglaCurso = '%s' AND nomeCurso = '%s')" % (table_name, siglaCurso, nomeCurso)
            # db.cur.execute(query)
            # check_if_exists = db.cur.fetchall()
            # print(check_if_exists)



def main():

    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()


    main_window.popularTabela(db, "Curso")
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()