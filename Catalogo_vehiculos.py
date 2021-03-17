# Realizar el ejercicio aquí
#Import de la función randint de la librería random
from random import randint
#Creación clase Vehiculo con atributos color y ruedas
class Vehiculo:
    color = ""
    ruedas = 0
    
    #Constructor de la clase Vehiculo
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas
    #Se sobreescribe el método String para mostrar la información del vehículo   
    def __str__(self):
        return "Color: {}\nRuedas: {}\n".format(self.color,self.ruedas)
    
#Se crea clase Coche que hereda de Vehiculo.     
class Coche(Vehiculo):
    
    #Se crea el constructor de la clase con atributos de velocidad y cilindrada más los que hereda de la clase Vehículo
    #He puesto por defecto que las ruedas sean 4.
    def __init__(self, velocidad, cilindrada, coche_color, coche_ruedas=4):
        super().__init__(coche_color, coche_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    #Sobreescribe el método String heredando el método __str__ de la clase padre(Vehículo).
    def __str__(self):
        return super().__str__()+"Velocidad: {}Km/h\nCilindrada: {}cc\n".format(self.velocidad,self.cilindrada)

#Se crea la clase Bicicleta con su constructor y sobreescribiendo el método String()
class Bicicleta(Vehiculo):
    
    def __init__(self,tipo, bici_color, bici_ruedas=2):
        super().__init__(bici_color, bici_ruedas)
        self.tipo = tipo
        
    def __str__(self):
        if self.tipo == True:
            tipo = "Deportiva"
        elif self.tipo == False:
            tipo = "Urbana"
        else:
            tipo = "Tipo de Bici no válido"
        return super().__str__()+"Tipo: {}\n".format(tipo)
    
#Se crea la clase Camioneta con su constructor y sobreescribiendo el método String()    
class Camioneta(Coche):
    
    def __init__(self, carga, camioneta_velocidad, camioneta_cilindrada, camioneta_color, camioneta_ruedas=4):
        super().__init__(camioneta_velocidad, camioneta_cilindrada, camioneta_color, camioneta_ruedas)
        self.carga = carga
    
    def __str__(self):
        return super().__str__()+"Carga: {}Kg\n".format(self.carga)
    
#Se crea la clase Motocicleta con su constructor y sobreescribiendo el método String()    
class Motocicleta(Bicicleta):
    
    def __init__(self, velocidad, cilindrada, moto_tipo, moto_color, moto_ruedas=2):
        super().__init__(moto_tipo, moto_color, moto_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
        return super().__str__()+"Velocidad: {}Km/h\nCilindrada: {}cc\n".format(self.velocidad, self.cilindrada)

#Creé esta función para validar la entrada del tipo de objeto que se seleccionará
def validacion_tipo_vehiculos(tipo_vehiculos):
    tipo_tratado = tipo_vehiculos.lower().capitalize()
    return tipo_tratado

#Creación de la función filtrar() donde se le pasan como parámetros una lista de objetos y el tipo de vehículo que hace referencia al objeto
def filtrar(lista_vehiculos, tipo_vehiculos):
    lista_filtrada = []
    tipo_v=validacion_tipo_vehiculos(tipo_vehiculos) #Se llama a la función validacion_tipo_vehiculos() para evitar posibles errores de tipeo 
    print(tipo_v)
    for i in lista_vehiculos:  #Se itera en la lista de objetos y según la selección del usuario, guardará en una lista filtrada los objetos seleccionados
        tipo_vehiculo = type(i).__name__
        if tipo_vehiculo == tipo_v:
            lista_filtrada.append(i)
    return lista_filtrada  #la función devuelve la lista filtrada. 


#Como ejemplo, he creado unas listas con los atributos de las clases para facilitar la creación de los objetos. 
colores = ["Amarillo","Rojo","Azul","Blanco","Negro","Verde","Lila"]
maxc= len(colores) -1
cilindrada = [1100,2100,1600,800]
maxcil = len(cilindrada)-1
tipo = [True,False]
velocidad = [100,80,120,60,220]
maxv = len(velocidad)-1
carga = [20,25,30,40,45]
maxcar= len(carga)-1    
a=b=c=d=0  #contadores de los diferentes vehíchulos inicializados a cero 
lista_vehiculos = []
#He usado la función range() y la función randint() para generar de 1 a 5 vehículos aleatoriamente 
#Como se puede observar en cada una de las iteraciones, he usado la función randint() para seleccionar entre una de las 
#listas de los atributos aleatoriamente.
#En el print() se mostrará la cantidad de vehículos creados por clase, esto para comprobar que la cantidad de vehículos creados
#es igual a la cantidad de vehículos filtrados. 
for i in range(randint(1,5)):
    a += 1
    lista_vehiculos.append(Coche(velocidad[randint(0,maxv)],cilindrada[randint(0,maxcil)],colores[randint(0,maxc)]))
print("Se han creado {} Coches".format(a))
for j in range(randint(1,3)):
    b += 1
    lista_vehiculos.append(Camioneta(carga[randint(0,maxcar)],velocidad[randint(0,maxv)],cilindrada[randint(0,maxcil)],colores[randint(0,maxc)]))
print("Se han creado {} Camionetas".format(b))
for k in range(randint(1,5)):
    c += 1
    lista_vehiculos.append(Bicicleta(tipo[randint(0,1)],colores[randint(0,maxc)]))
print("Se han creado {} Bicicletas".format(c))
for l in range(randint(1,3)):
    d += 1
    lista_vehiculos.append(Motocicleta(velocidad[randint(0,maxv)],cilindrada[randint(0,maxcil)],tipo[randint(0,1)],colores[randint(0,maxc)]))
print("Se han creado {} Motocicletas".format(d))

#Fuentes para mejorar la visibilidad de los resultados 
amarillo="\033[1;43m"
rojo="\033[1;41m"
azul="\033[1;44m"
verde="\033[1;42m"
cian = "\033[1;46m"
blank = '\033[0;m'

#Se crea el programa de consulta para comprobar el funcionamiento del programa 
while True:
    print(cian+"¿Qué vehículos deseas consultar?"+blank+"\n-Coche\n-Camioneta\n-Bicileta\nMotocicleta\n\nPRESIONE Q PARA SALIR")
    opcion= input ("Escriba una de las opciones exactamente igual a como se muestra en las opciones: ")
    opcion_v = validacion_tipo_vehiculos(opcion)
    if opcion_v == "Coche":
        lista_coches = filtrar(lista_vehiculos,"coche")
        print(amarillo+"CATÁLOGO DE COCHES"+blank)
        for i in lista_coches:
            print(i)
    elif opcion_v == "Camioneta":
        lista_camioneta = filtrar(lista_vehiculos,"camioneta")
        print(rojo+"CATÁLOGO DE CAMIONETAS"+blank)
        for i in lista_camioneta:
            print(i)
    elif opcion_v == "Motocicleta":
        lista_Motocicleta = filtrar(lista_vehiculos,"Motocicleta")
        print(azul+"CATÁLOGO DE MOTOCICLETAS"+blank)
        for i in lista_Motocicleta:
            print(i)
    elif opcion_v == "Bicicleta":
        lista_bicicleta = filtrar(lista_vehiculos,"bicicleta")
        print(verde+"CATÁLOGO DE BICICLETAS"+blank)
        for i in lista_bicicleta:
            print(i)
    elif opcion_v == "Q" or opcion_v=="q":
        print(cian+"GRACIAS POR CONSULTAR EL CATÁLOGO, HASTA LUEGO!"+blank)
        break
    else:
        print(rojo+"Ha escrito mal el comando, las opciones disponibles son 'coche','camioneta','motocicleta','bicicleta' o 'q' \n POR FAVOR INTÉNTELO DE NUEVO"+blank)
        
