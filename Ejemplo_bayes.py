import csv
import re

def palabra_general(registros):
    lista_tratada = []
    i = 0
    suma_total=0
    clase_positiva = 0
    clase_negativa = 0
    total_de_palabras_positivas = 0
    total_de_palabras_negativas = 0
    lista_de_palabras = []
    for registro in registros:
        lista_tratada.append(registro.split(";"))
        for cada_palabra in lista_tratada[i][1].split(" "):
            cada_palabra = cada_palabra.capitalize().strip(".")
            if cada_palabra not in lista_de_palabras:
                lista_de_palabras.append(cada_palabra)
        if lista_tratada[i][2]=="+":
            clase_positiva += 1
            total_de_palabras_positivas += len(registro.split(";"))
        else:
            clase_negativa += 1
            total_de_palabras_negativas += len(registro.split(";"))
        suma_de_clases = clase_positiva + clase_negativa
        i+=1
    return lista_de_palabras,len(lista_de_palabras),total_de_palabras_positivas,total_de_palabras_negativas,suma_de_clases,clase_positiva,clase_negativa

def contar_palabras(palabra,registros):
    lista_tratada = []
    i = 0
    suma_total=0
    apariciones_positivas = 0
    apariciones_negativas = 0
    lista_de_palabras = []
    for registro in registros:
        lista_tratada.append(registro.split(";"))
        if lista_tratada[i][2]=="+":
            apariciones_positivas += lista_tratada[i][1].count(palabra)
        else:
            apariciones_negativas += lista_tratada[i][1].count(palabra)
        suma_total = apariciones_positivas + apariciones_negativas
        i+=1
    return suma_total, apariciones_positivas, apariciones_negativas

def cantidad_calses(registros):
    i = 0
    for registro in registros:
        lista_tratada.append(registro.split(";"))
        clase_positiva = 0
        clase_negativa = 0
        if lista_tratada[i][2]=="+":
            clase_positiva += 1
        else:
            clase_negativa += 1
        i+=1
    return 
def determinar_porcentajes_clase(frase,registros):
    diccionario_frase = {}
    diccionario_probabilidad = {}
    probabilidad_positiva_palabra = 1
    probabilidad_negativa_palabra = 1
    lista_palabras,vocabulario,total_de_palabras_positivas,total_de_palabras_negativas,cantidad_clases,clase_positiva,clase_negativa = palabra_general(registros)
    frase_lista = frase.split()
    for palabra in frase_lista:
        diccionario_frase[palabra]=list(contar_palabras(palabra,registros))
    probabilidad_general_positiva= clase_positiva/cantidad_clases
    probabilidad_general_negativa= clase_negativa/cantidad_clases
    for key,valor in diccionario_frase.items():
        diccionario_probabilidad[key+" +"] = (valor[1]+1)/(total_de_palabras_positivas+vocabulario)
        diccionario_probabilidad[key+" -"] = (valor[2]+1)/(total_de_palabras_negativas+vocabulario)
    for key,valor in diccionario_probabilidad.items():
        if key.endswith("+"):
            probabilidad_positiva_palabra *= valor
        else:
            probabilidad_negativa_palabra *= valor
    probabilidad_documento_positivo = probabilidad_general_positiva * probabilidad_positiva_palabra
    probabilidad_documento_negativo = probabilidad_general_negativa * probabilidad_negativa_palabra
    print(diccionario_probabilidad)
    print(diccionario_frase)
    return probabilidad_documento_positivo,probabilidad_documento_negativo


lista = []
with open('C:\\Users\\user\\Desktop\\Biblioteca CD\\Biblioteca_musica\\ejemplo_naive.csv', newline='') as File:  
    reader = csv.reader(File)
    i = 0
    for row in reader:
        if i==0:
            i+=1
            continue
        lista.append(row[0])

print(determinar_porcentajes_clase("I hated the poor acting",lista))