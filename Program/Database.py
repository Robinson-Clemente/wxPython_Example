import sqlite3


#conexion = sqlite3.connect('estudiante.db')
#cursor = conexion.cursor()
#cursor.execute(""" CREATE TABLE Estudiantes(id integer PRIMARY KEY AUTOINCREMENT
#,nombre text,nota1 integer, nota2 integer, nota3 integer)""")



def agregarEstudiante(estudiante):
    conexion = sqlite3.connect('estudiante.db')
    cursor = conexion.cursor()
    cursor.execute(""" INSERT INTO Estudiantes(nombre,nota1,nota2,nota3) VALUES(?,?,?,?) """, (estudiante.nombre
    ,estudiante.nota1,estudiante.nota2,estudiante.nota3))   
    
    conexion.commit()
    conexion.close()

def eliminarEstudiante(indice):
    conexion = sqlite3.connect('estudiante.db')
    cursor = conexion.cursor()

    cursor.execute(""" DELETE FROM Estudiantes WHERE id=(?) """, (indice,))

    conexion.commit()
    conexion.close()

def actualizarEstudiante(indice,estudiante):
    conexion = sqlite3.connect('estudiante.db')
    cursor = conexion.cursor()

    cursor.execute(""" UPDATE Estudiantes SET nombre=(?),nota1=(?),
    nota2=(?),nota3=(?) WHERE id=(?) """, (estudiante.nombre,
    estudiante.nota1,estudiante.nota2,estudiante.nota3,indice))
    
    conexion.commit()
    conexion.close() 


def consultarEstudiante(indice):

    conexion = sqlite3.connect('estudiante.db')
    cursor = conexion.cursor()

    
    cursor.execute(""" SELECT * FROM Estudiantes WHERE id=(?) """, (indice,))
    estudiante = cursor.fetchone()

   
    conexion.close() 

    return estudiante


def getList():
    conexion = sqlite3.connect('estudiante.db')
    cursor = conexion.cursor()

    cursor.execute(""" SELECT * FROM Estudiantes """)  
    lista = cursor.fetchall()  
    conexion.close() 
     
    return lista 





