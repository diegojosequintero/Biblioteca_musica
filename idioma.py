class Idioma:
    def __init__(self,nombre):
        self.__nombre= nombre
        
        
    def getNombre(self):
        return self.__nombre

    def setNombre(self,nombre):
        self.__nombre = nombre
    
    def __str__(self):
        return self.getNombre().lower().capitalize()
    
        
