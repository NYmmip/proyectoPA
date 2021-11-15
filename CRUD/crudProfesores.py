import mysql.connector
#python -m pip install mysql-connector-python
from entidades.profesor import profesor


class crudProfesores:

    profesores = []
    mydb = 0
    def __init__(self, host, user, passw, db):
        self.mydb = mysql.connector.connect(
            host= host,
            user=user,
            password=passw,
            database=db
        )

    def createProfesor(self, nm, nombre, apellido, inid):
        self.myCursor = self.mydb.cursor()
        sql = "SELECT documento FROM profesor WHERE documento = %s"
        val = (nm,)
        self.myCursor.execute(sql, val)
        if self.myCursor.fetchall() != []:
            return 1

        sql = "SELECT numero_extension FROM profesor WHERE numero_extension = %s"
        val = (inid,)
        self.myCursor.execute(sql, val)
        if self.myCursor.fetchall() != []:
            return 2
        sql = "INSERT INTO profesor(documento, nombre_compelto, modalidad, numero_extension) VALUES (%s, %s, %s, %s)"
        val = (nm, nombre, apellido, inid,)
        self.myCursor.execute(sql, val)
        self.mydb.commit()
        return 0

    def getProfesores(self):
        self.profesores = []
        self.myCursor = self.mydb.cursor()
        self.myCursor.execute("SELECT * FROM profesor")
        for x in self.myCursor.fetchall():
            temp = profesor(x[0],x[1],x[2],x[3])
            self.profesores.append(temp)
        return self.profesores