

class Estudiante():

    def __init__(self,nombre,nota1,nota2,nota3):        
        self.__nombre = nombre
        self.__nota1 = nota1
        self.__nota2= nota2
        self.__nota3 = nota3

    
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    @property
    def nota1(self):
        return self.__nota1

    @nota1.setter
    def nota1(self,nota1):
        self.__nota1 = nota1

    @property
    def nota2(self):
        return self.__nota2

    @nota2.setter
    def nota2(self,nota2):
        self.__nota2 = nota2

    @property
    def nota3(self):
        return self.__nota3

    @nota3.setter
    def nota3(self,nota3):
        self.__nota3 = nota3               