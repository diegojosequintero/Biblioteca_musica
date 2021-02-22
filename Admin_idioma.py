import mysql.connector
from mysql.connector import cursor

class Admin_idioma:
    def __init__(self):
        self.cnx = mysql.connector.connect(user='root', password='root', host='localhost', database="´musica´")

    def comprobar(self,idioma):
        cursor=self.cnx.cursor()
        select = "select nombre from idioma id where id.nombre like '%"+str(idioma)+"%'"
        cursor.execute(select)
        result = cursor.fetchone()
        if result is None:
            comprobacion = True
            select_id= "Select ididioma from idioma id where id.nombre like '%"+str(idioma)+"%'"
            cursor.execute(select_id)
            id_result = cursor.fetchone()
            cursor.close()
            return comprobacion, " "
        else:
            comprobacion = False
            select_id= "Select ididioma from idioma id where id.nombre like '%"+str(idioma)+"%'"
            cursor.execute(select_id)
            id_result = cursor.fetchone()
            cursor.close()
            return comprobacion, str(id_result[0])
    def create(self,idioma):
        comprobacion,id_idioma = self.comprobar(idioma)
        self.cnx._open_connection()
        cursor=self.cnx.cursor()
        if comprobacion == True:
            insert= "insert into idioma (nombre) values ('"+str(idioma)+"')"
            cursor.execute(insert)
            self.cnx.commit()
            mensaje = "Se ha insertado el idioma "+idioma+" a la base de datos"
            cursor.close()
        else:
            mensaje = "El idioma "+idioma+" ya existe en la base de datos"
            cursor.close()
        return mensaje

    def update(self,idioma):
        comprobacion,id_idioma = self.comprobar(idioma)
        cursor=self.cnx.cursor()
        if comprobacion == False:
            idioma= input("Qué idioma deseas introducir?")
            idioma = idioma.lower().capitalize()
            actualiza= "update idioma id set nombre='"+idioma+"' where ididioma = "+id_idioma[0]
            cursor.execute(actualiza)
            self.cnx.commit()
            mensaje = "Se ha actualizado el idioma "+idioma_previo+" a "+idioma
            cursor.close()
        else:
            mensaje = "El idioma "+idioma+" No existe en la base de datos, por lo que no se puede actualizar\n"
            cursor.close()
        return mensaje
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
        return idioma_list ## Return hacer en MAIN
    def delete(self,idioma):
        comprobacion,id_idioma = self.comprobar(idioma)
        cursor = self.cnx.cursor()
        if comprobacion == False:
            confirm = True
            while confirm:
                confirmacion = input("¿Está seguro que desea borrar el idioma "+str(idioma)+" permanentemente de la base de datos?: ")
                print("Presione 's' para confirmar y 'n' para volver")
                confirmacion = confirmacion.lower()
                if confirmacion == "s":
                    confirm = False
                    delete_query= "delete from idioma where ididioma ="+id_idioma
                    cursor.execute(delete_query)
                    self.cnx.commit()
                    mensaje = "Se ha borrado el idioma "+str(idioma)+" de la base de datos---\n"
                elif confirmacion == 'n':
                    confirm = False
                    mensaje = "No se ha borrado ningún registro"
                else:
                    print("ERROR, valor incorrecto. Introduzca 's' o 'n' por favor\n")
        else:
            mensaje="El idioma "+str(idioma)+," que ha indicado, no existe en la base de datos"
            cursor.close()
        return mensaje

    def cerrar_conexión(self):
        if self.cnx._open_connection:
            self.cnx.close()
   
