from sqlite3 import *
def crearConexion():
    conn = connect("./base_datos/tecnologico.db")
    conn.commit()
    conn.close()

def crearTablaAlumno():
    conn = connect("./base_datos/tecnologico.db")
    cursor = conn.cursor()
    sentencia="""
        CREATE TABLE IF NOT EXISTS Alumnos(ID INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT(250),edad INTEGER
        )
    """
    cursor.execute(sentencia)
    conn.commit()
    conn.close()
def crearTablaCurso():
    conn = connect("./base_datos/tecnologico.db")
    cursor = conn.cursor()
    sentencia="""
        CREATE TABLE IF NOT EXISTS Cursos(id INTIGER PRIMARY KEY AUTOINCREMET, 
          nombre TEXT(250),
          id_alumno INTIGER,
          FOREIGN KEY(id_alumno) REFERENCES Alumnos(id)
        )
    """
    cursor.execute(sentencia)
    conn.commit()
    conn.close()

def insertAlumno(nombre,edad):
    conn = connect("./base_datos/tecnologico.db")
    cursor = conn.cursor()
    sentencia=f"INSERT INTO Alumnos(nombre,edad) VALUES('{nombre}',{edad})"
    cursor.execute(sentencia)
    conn.commit()
    conn.close()

def insertAlumnos(lista):
    conn=connect("./base_datos/tecnologico.db")
    cursor=conn.cursor()
    sentencia=f"INSERT INTO Alumnos(nombre,edad) VALUES(?,?)"
    cursor.executemany(sentencia,lista)
    conn.commit()
    conn.close()

def eliminarAlumno(id):
    conn = connect("./base_datos/tecnologico.db")
    cursor = conn.cursor()
    sentencia = f"DELETE FROM Alumnos WHERE id={id}"
    cursor.execute(sentencia)
    conn.commit()
    conn.close()

def actualizarAlumno(id,nombre,edad):
    conn = connect("./base_datos/tecnologico.db")
    cursor = conn.cursor()
    sentencia = f"UPDATE Alumnos SET nombre='{nombre}',edad={edad} WHERE id={id}"
    cursor.execute(sentencia)
    conn.commit()
    conn.close()


if __name__=="__main__":
    # crearConexion()
    # crearTablaAlumno()
    # crearTablaCurso()
    # insertAlumno('jory',20)
    # insertAlumno('chinita',18)
    # alum=[
    #     ('jory',50),
    #     ('china',60),
    #     ('criss',20),
    #     ('nadine',10),
    #     ('jhony',20),
    #     ('viuda',40),
    # ]
    # insertAlumnos(alum)
    eliminarAlumno(5)
    # actualizarAlumno(3,'nando',33)



