import pymysql


class Database(object):

    def __init__(self, db_host, db_user, db_pass, db_name):
        self.db = pymysql.connect(host=db_host,
                                  user=db_user,
                                  password=db_pass,
                                  db=db_name,
                                  cursorclass=pymysql.cursors.DictCursor)


    def __enter__(self):
        return self

    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     if self.db:
    #         self.db.close()


    def selectAllfromTable(self, tabelaNome):
        query = "SELECT * FROM " + tabelaNome
        self.cur = self.db.cursor()

        self.cur.execute(query)
        for row in self.cur.fetchall():
            print (row)

    def populaTabela(self, tabelaNome):
        query = "SELECT DISTINCT (id%s) FROM " % tabelaNome
        query += tabelaNome
        print(query)
        self.cur = self.db.cursor()
        row_count = self.cur.execute(query)
        print (row_count)
