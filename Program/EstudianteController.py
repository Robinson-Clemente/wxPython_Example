from Estudiante import Estudiante
from Database import agregarEstudiante
from Database import actualizarEstudiante
from Database import consultarEstudiante
from Database import eliminarEstudiante
from Database import getList



def addEstudiante(nombre,nota1,nota2,nota3):
    estudiante = Estudiante(nombre,nota1,nota2,nota3)
    agregarEstudiante(estudiante)

def generarEstudiante(nombre,nota1,nota2,nota3):
    estudiante = Estudiante(nombre,nota1,nota2,nota3)
    return estudiante

def ModifyEstudiante(indice,estudiante):
    actualizarEstudiante(indice,estudiante)

def consultarUno(indice):
    lista = consultarEstudiante(indice)

    if lista==None:
        return None
    else:     
        nombre = lista[1]
        nota1 =  lista[2]
        nota2 =  lista[3]
        nota3 =  lista[4]    
        estudiante = Estudiante(nombre,nota1,nota2,nota3)
        return estudiante

    
    
    return estudiante

def deleteEstudiante(indice):
    eliminarEstudiante(indice)       

def getLista():
    lista = getList()
    return lista



            



