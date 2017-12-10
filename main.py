#!/usr/bin/python
import sys

from PyQt5.QtWidgets import *
from view.mainWindow import Ui_MainWindow
from PyQt5 import QtSql

from database import Database

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


    def popularTabela(self, db, table_name):
        num_rows = db.returnNumRows(table_name)
        self.tableCurso.setRowCount(num_rows)
        query = "SELECT * FROM " + table_name
        db.cur.execute(query)
        result = db.cur.fetchall()
        # self.tableCurso.setItem(0,0,QTableWidgetItem(resultado[0]))
        col = 0
        for num in range(0, num_rows):
            for col_number,data in result[num].items():
                self.tableCurso.setItem(num, col, QTableWidgetItem(str(data)))
                col = col+1
                if col == num_rows:
                    col = 0


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()

    db = Database("127.0.0.1", "viriato", "dinossauro", "mydb")

    resultado = db.selectAllfromTable("Professor")

    main_window.popularTabela(db, "Curso")

    sys.exit(app.exec_())



if __name__ == "__main__":
    main()