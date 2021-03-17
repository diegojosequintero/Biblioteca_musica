import csv
import re

lista = []
with open('C:\\Users\\Matí\\Desktop\\Nueva carpeta\\ejemplo_naive.csv', newline='') as File:  
    reader = csv.reader(File)
    i = 0
    for row in reader:
        if i==0:
            i+=1
            continue
        lista.append(row[0])

print(lista)
print(type(lista[0]))


def palabra_general(registros):
    lista_tratada = []
    i = 0
    suma_total=0
    lista_de_palabras = []
    for registro in registros:
        print(registro)
        lista_tratada.append(registro.split(";"))
        for cada_palabra in lista_tratada[i][1].split(" "):
            cada_palabra = cada_palabra.capitalize().strip(".")
            if cada_palabra not in lista_de_palabras:
                lista_de_palabras.append(cada_palabra)
        i+=1
    return lista_de_palabras,len(lista_de_palabras)
    print(lista_de_palabras)
def contar_palabras(palabra,registros):
    lista_tratada = []
    i = 0
    suma_total=0
    apariciones_positivas = 0
    apariciones_negativas = 0
    lista_de_palabras = []
    for registro in registros:
        print(registro)
        lista_tratada.append(registro.split(";"))
        apariciones_palabra = lista_tratada[i][1].count(palabra)
        print(apariciones_palabra)
        if lista_tratada[i][2]=="+":
            apariciones_positivas += lista_tratada[i][1].count(palabra)
        else:
            apariciones_negativas += lista_tratada[i][1].count(palabra)
        suma_total += apariciones_palabra
        i+=1
    print("{}  {}  {}".format(suma_total,apariciones_positivas,apariciones_negativas))

lista_total, num_list_total =palabra_general(lista)
print("{}----{}".format(lista_total,num_list_total))
   