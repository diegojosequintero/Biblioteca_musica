import mysql.connector
from Admin_idioma import Admin_idioma
from Idioma import Idioma

menu = True
while menu:
    print("Menú de Tabla idioma:")
    print("1) Ver datos")
    print("2) Insertar datos")
    print("3) Actualizar datos")
    print("4) Borrar datos")
    print("\n\n0) Salir")

    opcion = input("Seleccionar Opción: ")
    if opcion == "1":
        adm_idioma = Admin_idioma()
        adm_idioma.select_All()

    elif opcion == "2":
        dato=input("Ingresar idioma: ")
        insert_idioma = Idioma(dato)
        adm_idioma = Admin_idioma()
        mensaje=adm_idioma.create(insert_idioma)
        print(mensaje)
    elif opcion == "3":
        dato=input("Ingresar idioma que desea actualizar: ")
        update_idioma = Idioma(dato)
        adm_idioma = Admin_idioma()
        mensaje= adm_idioma.update(update_idioma)
        print(mensaje)
    elif opcion == "4":
        dato= input("Ingresar idioma que desea borrar: ")
        delete_idioma= Idioma(dato)
        adm_idioma = Admin_idioma()
        mensaje= adm_idioma.delete(delete_idioma)
        print(mensaje)
    elif opcion == "0":
        Admin_idioma().cerrar_conexión()
        print("Hasta Luego!!")
        menu = False
        
        
    else: 
        print("Ha introducido un valor de opción incorrecto, ha introducido '{}' y las opciones disponibles son (0,1,2,3,4)\n ")
