import mysql.connector
#python -m pip install mysql-connector-python
from entidades.estudiante import estudiante


class crudEstudiantes:

    estudiantes = []
    mydb = 0
    def __init__(self, host, user, passw, db):
        self.mydb = mysql.connector.connect(
            host= host,
            user=user,
            password=passw,
            database=db
        )

    def createEstudiante(self, nm, nombre, apellido, inid):
        self.myCursor = self.mydb.cursor()
        sql = "SELECT numero_matricula FROM alumno WHERE numero_matricula = %s"
        val = (nm,)
        self.myCursor.execute(sql, val)
        if self.myCursor.fetchall() != []:
            return 1

        sql = "SELECT id FROM investigacion WHERE id = %s"
        val = (inid,)
        self.myCursor.execute(sql, val)
        if self.myCursor.fetchall() == []:
            return 2

        sql = "INSERT INTO alumno(numero_matricula, nombre, apellido, investigacion_id) VALUES (%s, %s, %s, %s)"
        val = (nm, nombre, apellido, inid, )
        self.myCursor.execute(sql, val)
        self.mydb.commit()
        return 0


    def getEstudiantes(self):
        self.estudiantes = []
        self.myCursor = self.mydb.cursor()
        self.myCursor.execute("SELECT * FROM alumno")
        for x in self.myCursor.fetchall():
            temp = estudiante(x[0],x[1],x[2],x[3])
            self.estudiantes.append(temp)
        return self.estudiantes


