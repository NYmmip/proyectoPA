import mysql.connector
#python -m pip install mysql-connector-python
from entidades.tema import tema


class crudTemas:

    temas = []
    mydb = 0
    def __init__(self, host, user, passw, db):
        self.mydb = mysql.connector.connect(
            host= host,
            user=user,
            password=passw,
            database=db
        )

    def createTema(self, id, nombre):
        self.myCursor = self.mydb.cursor()
        sql = "SELECT id FROM tema WHERE id = %s"
        val = (id,)
        self.myCursor.execute(sql, val)
        if self.myCursor.fetchall() != []:
            return 1

        sql = "INSERT INTO tema(id, nombre) VALUES (%s, %s)"
        val = (id, nombre,)
        self.myCursor.execute(sql, val)
        self.mydb.commit()
        return 0


    def getTemas(self):
        self.temas = []
        self.myCursor = self.mydb.cursor()
        self.myCursor.execute("SELECT * FROM tema")
        for x in self.myCursor.fetchall():
            temp = tema(x[0], x[1])
            self.temas.append(temp)
        return self.temas


