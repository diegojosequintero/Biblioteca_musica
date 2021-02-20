import mysql.connector

class Admin_idioma:
    def __init__(self):
        self.cnx = mysql.connector.connect(user='root', password='root', host='localhost', database="´musica´")

    def comprobar(self,idioma):
        cursor=self.cnx.cursor()
        idioma = idioma.getNombre().lower().capitalize()
        select = "select count(nombre) from idioma id where id.nombre like '%"+idioma+"%' group by id.nombre"
        cursor.execute(select)
        result = cursor.fetchone()
        if result is None:
            comprobacion = True
            cursor.close()
            self.cnx.close()
        else:
            comprobacion = False
            cursor.close()
            self.cnx.close()
        return comprobacion
    def create(self,idioma):
        comprobacion = self.comprobar(idioma)
        idioma = idioma.getNombre().lower().capitalize()
        self.cnx._open_connection()
        cursor=self.cnx.cursor()
        if comprobacion == True:
            insert= "insert into idioma (nombre) values ('"+idioma+"')"
            cursor.execute(insert)
            self.cnx.commit()
            mensaje = "Se ha insertado el idioma "+idioma+" a la base de datos"
            cursor.close()
            self.cnx.close()
        else:
            mensaje = "El idioma "+idioma+" ya existe en la base de datos"
            cursor.close()
            self.cnx.close()
        return mensaje