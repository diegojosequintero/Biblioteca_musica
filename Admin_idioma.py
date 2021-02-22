import mysql.connector
from mysql.connector import cursor

class Admin_idioma:
    def __init__(self):
        self.cnx = mysql.connector.connect(user='root', password='root', host='localhost', database="´musica´")

    def comprobar(self,idioma):
        cursor=self.cnx.cursor()
        idioma = idioma.getNombre().lower().capitalize()
        select = "select nombre from idioma id where id.nombre like '%"+idioma+"%'"
        cursor.execute(select)
        result = cursor.fetchone()
        if result is None:
            comprobacion = True
            select_id= "Select ididioma from idioma id where id.nombre like '%"+idioma+"%'"
            cursor.execute(select_id)
            id_result = cursor.fetchone()
            cursor.close()
            self.cnx.close()
            return comprobacion,id_result
        else:
            comprobacion = False
            cursor.close()
            self.cnx.close()
            return comprobacion
    def create(self,idioma):
        comprobacion,id_idioma = self.comprobar(idioma)
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

    def update(self,idioma):
        comprobacion,id_idioma = self.comprobar(idioma)
        idioma = idioma.getNombre().lower().capitalize()
        self.cnx._open_connection()
        cursor=self.cnx.cursor
        if comprobacion == True:
            actualiza= "update idioma id set nombre='"+idioma+"' where ididioma = "+id_idioma
            cursor.execute(actualiza)
    def select_All(self):
        self.cnx._open_connection()
        cursor=self.cnx.cursor()
        list_all= 'SELECT * FROM idioma'
        cursor.execute(list_all)
        idioma_list = cursor.fetchall()
        print("LISTA DE IDIOMAS:")
        print("_________________")
        for idi in idioma_list:
            print( idi[1])
        print("+++++++++++++++++++")
        cursor.close()
        self.cnx.close()
   

         
