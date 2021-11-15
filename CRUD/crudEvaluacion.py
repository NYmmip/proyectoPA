import mysql.connector
#python -m pip install mysql-connector-python
from entidades.evaluacion import evaluacion


class crudEvaluacion:

    evaluaciones = []
    mydb = 0
    def __init__(self, host, user, passw, db):
        self.mydb = mysql.connector.connect(
            host= host,
            user=user,
            password=passw,
            database=db
        )

    def createEvaluacion(self, id, nombre, fecha, cPreguntas, documentoP):
        self.myCursor = self.mydb.cursor()
        sql = "SELECT id FROM evaluacion WHERE id = %s"
        val = (id,)
        self.myCursor.execute(sql, val)
        if self.myCursor.fetchall() != []:
            return 1

        print("2")
        sql = "SELECT documento FROM profesor WHERE documento = %s"

        val = (documentoP,)
        self.myCursor.execute(sql, val)
        print("Aqui")
        if self.myCursor.fetchall() == []:
            return 2

        print("3")
        sql = "INSERT INTO evaluacion(id, nombre, fecha, cantidad_preguntas, profesor_documento) VALUES (%s, %s, %s, %s, %s)"
        val = (id, nombre, fecha, cPreguntas, documentoP,)
        self.myCursor.execute(sql, val)
        self.mydb.commit()
        return 0


    def getEvaluaciones(self):
        self.evaluaciones = []
        self.myCursor = self.mydb.cursor()
        self.myCursor.execute("SELECT * FROM evaluacion")
        for x in self.myCursor.fetchall():
            temp = evaluacion(x[0],x[1],x[2],x[3], x[4])
            self.evaluaciones.append(temp)
        return self.evaluaciones


