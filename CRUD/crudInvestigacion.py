import mysql.connector
#python -m pip install mysql-connector-python
from entidades.investigacion import investigacion


class crudInvestigacion:

    investigaciones = []
    mydb = 0
    def __init__(self, host, user, passw, db):
        self.mydb = mysql.connector.connect(
            host= host,
            user=user,
            password=passw,
            database=db
        )

    def createInvestigacion(self, id, nombre, enfoque, temaId):
        self.myCursor = self.mydb.cursor()
        sql = "SELECT id FROM investigacion WHERE id = %s"
        val = (id,)
        self.myCursor.execute(sql, val)
        if self.myCursor.fetchall() != []:
            return 1

        sql = "SELECT id FROM tema WHERE id = %s"
        val = (temaId,)
        self.myCursor.execute(sql, val)
        if self.myCursor.fetchall() == []:
            return 2

        sql = "INSERT INTO investigacion(id, nombre, enfoque, tema_id) VALUES (%s, %s, %s, %s)"
        val = (id, nombre, enfoque, temaId,)
        self.myCursor.execute(sql, val)
        self.mydb.commit()
        return 0


    def getInvestigaciones(self):
        self.investigaciones = []
        self.myCursor = self.mydb.cursor()
        self.myCursor.execute("SELECT * FROM investigacion")
        for x in self.myCursor.fetchall():
            temp = investigacion(x[0],x[1],x[2],x[3])
            self.investigaciones.append(temp)
        return self.investigaciones


