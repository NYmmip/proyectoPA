import mysql.connector
#python -m pip install mysql-connector-python
from entidades.publicacion import  publicacion


class crudPublicaciones:

    publicaciones = []
    mydb = 0
    def __init__(self, host, user, passw, db):
        self.mydb = mysql.connector.connect(
            host= host,
            user=user,
            password=passw,
            database=db
        )

    def createPublicacion(self, id, nombre, fecha, cantidadP, investigacionId):
        self.myCursor = self.mydb.cursor()
        sql = "SELECT id FROM publicacion WHERE id = %s"
        val = (id,)
        self.myCursor.execute(sql, val)
        if self.myCursor.fetchall() != []:
            return 1

        sql = "SELECT id FROM investigacion WHERE id = %s"
        val = (investigacionId,)
        self.myCursor.execute(sql, val)
        if self.myCursor.fetchall() == []:
            return 2

        sql = "INSERT INTO publicacion(id, nombre, fecha, cantidad_palabras, investigacion_id) VALUES (%s, %s, %s, %s, %s)"
        val = (id, nombre, fecha, cantidadP, investigacionId,)
        self.myCursor.execute(sql, val)
        self.mydb.commit()
        return 0


    def getPublicaciones(self):
        self.publicaciones = []
        self.myCursor = self.mydb.cursor()
        self.myCursor.execute("SELECT * FROM publicacion")
        for x in self.myCursor.fetchall():
            temp = publicacion(x[0],x[1],x[2],x[3], x[4])
            self.publicaciones.append(temp)
        return self.publicaciones


