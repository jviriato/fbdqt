import pymysql

from PyQt5 import QtCore, QtGui


class Database(object):

    def __init__(self, db_host, db_user, db_pass, db_name):
        self.db = pymysql.connect(host=db_host,
                                  user=db_user,
                                  password=db_pass,
                                  db=db_name,
                                  cursorclass=pymysql.cursors.DictCursor,
                                  autocommit=True)
        self.cur = self.db.cursor()


    def __enter__(self):
        return self

    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     if self.db:
    #         self.db.close()



    def selectAllfromTable(self, tabelaNome):
        query = "SELECT * FROM " + tabelaNome

        self.cur.execute(query)

        # for row in self.cur:
        #     print (row)

        return list(self.cur)

    def returnNumRows(self, tabelaNome):
        query = "SELECT * FROM " + tabelaNome

        self.cur.execute(query)
        num_rows = self.cur.fetchall()
        return len(num_rows)

    def returncountId(self, tabelaNome):
        query = "SELECT COUNT(*) FROM " + tabelaNome
        self.cur.execute(query)
        total_id = self.cur.fetchall()
        for i, entry in enumerate(total_id):
            return (entry['COUNT(*)'])

        db.commit()

    # def returnNumColumns(self, tabelaNome):
    #     # query = "SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS WHERE table_schema = 'mydb' AND table_name = '%s';" % tabelaNome
    #     query = "SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS WHERE table_schema = 'mydb' AND table_name = 'Curso';"
    #     print(query)
    #     res = self.cur.execute(query)
    #     print(res)