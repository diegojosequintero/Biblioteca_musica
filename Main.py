import mysql.connector
from Idioma import Idioma
from Admin_idioma import Admin_idioma

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
        dato=input("Ingresar idioma: ")
        update_idioma = Idioma(dato)
        upd_idioma= update_idioma.update(insert_idioma)
        print()
    elif opcion == "4":
        pass
    elif opcion == "0":
        print("Hasta Luego!!")
        menu = False
        
    else: 
        print("Ha introducido un valor de opción incorrecto, ha introducido '{}' y las opciones disponibles son (0,1,2,3,4)\n ")
