import mysql.connector
#python -m pip install mysql-connector-python
from entidades.resultadoEvaluacion import resultadoEvaluacion


class crudResultadosEvaluacion:

    resultadosEvaluaciones = []
    mydb = 0
    def __init__(self, host, user, passw, db):
        self.mydb = mysql.connector.connect(
            host= host,
            user=user,
            password=passw,
            database=db
        )

    def createResultado(self, nME, evaluacionId, resultado):
        self.myCursor = self.mydb.cursor()
        sql = "SELECT numero_matricula FROM alumno WHERE numero_matricula = %s"
        val = (nME,)
        self.myCursor.execute(sql, val)
        if self.myCursor.fetchall() == []:
            return 1

        sql = "INSERT INTO resultadoevaluaciones(alumno_numero_matricula, evaluacion_id, resultado) VALUES (%s, %s, %s)"
        val = (nME, evaluacionId, resultado,)
        print(nME, evaluacionId, resultado)
        self.myCursor.execute(sql, val)
        self.mydb.commit()
        return 0


    def getResultados(self):
        self.resultadosEvaluaciones = []
        self.myCursor = self.mydb.cursor()
        self.myCursor.execute("SELECT * FROM resultadoEvaluaciones")
        for x in self.myCursor.fetchall():
            temp = resultadoEvaluacion(x[0],x[1],x[2])
            self.resultadosEvaluaciones.append(temp)
        return self.resultadosEvaluaciones


