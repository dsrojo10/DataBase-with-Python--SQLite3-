'''Base de Datos con SQLite3 en Python'''

import sqlite3
from estudiantes import Estudiante
import estudiantesDB

conn = sqlite3.connect('universidad.db') # Connection to SQLite *como no hay ninguna con ese nombre se crea.
c = conn.cursor() # Cursor para hacer queries

# Crear una tabla       
c.execute("""CREATE TABLE IF NOT EXISTS estudiantes(
    matricula TEXT PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    promedio REAL)""")

"""Insertar un estudiante a la tabla de FORMA DIRECTA"""
# c.execute("INSERT INTO estudiantes VALUES ('111','Roberto','Cruz', 9.5)")

# Insertar un estudiante a la tabla CON VARIABLES

# Objetos Estudiante de la clase estudiantes
est_1 = Estudiante('222', 'Adriana', 'Cruz', 9.5)
est_2 = Estudiante('333', 'Fabian', 'Romero', 9.0)
est_3 = Estudiante('444', 'Alejandro', 'Cruz', 7.5)
est_4 = Estudiante('555', 'Karen', 'Barrera', 7.5)

#forma 1
# c.execute("INSERT INTO estudiantes VALUES (?, ?, ?, ?)", 
#         (est_1.matricula, est_1.nombre, est_1.apellido, est_1.promedio))

#forma 2
# c.execute("INSERT INTO estudiantes VALUES (:matricula, :nombre, :apellido, :promedio)", {
#     'matricula': est_2.matricula, 'nombre': est_2.nombre, 'apellido': est_2.apellido, 'promedio': est_2.promedio})

#forma 3
# c.execute("INSERT INTO estudiantes (matricula, nombre, apellido) VALUES (?,?,?)",
#     (est_3.matricula, est_3.nombre, est_3.apellido)) # Ya que valor de promedio no es restringido podemos dejarlo vacio 

#forma 4 (varios estudiantes a la misma vez)
many_students = [
    (est_1.matricula, est_1.nombre, est_1.apellido, est_1.promedio),
    (est_2.matricula, est_2.nombre, est_2.apellido, est_2.promedio),
    (est_3.matricula, est_3.nombre, est_3.apellido, est_3.promedio),
    (est_4.matricula, est_4.nombre, est_4.apellido, est_4.promedio)
]
# c.executemany("INSERT INTO estudiantes VALUES (?,?,?,?)", many_students)


# Seleccionar todos los estudiantes de la tabla
# c.execute("SELECT * FROM estudiantes")
# estudiantes = c.fetchall() # Almacenar la tabla en una variable.
# # estudiantes = c.fetchmany(3) # Nos retorna solo 3
# print(estudiantes)

# Seleccionar estudiantes por datos en especifico

# # Por matricula
# c.execute("SELECT * FROM estudiantes WHERE matricula=?", ('444',))
# estudiantes = c.fetchone()
# print(estudiantes)

# # Por apellido
# c.execute("SELECT * FROM estudiantes WHERE apellido=?", ('Cruz',))
# estudiantes = c.fetchall()
# print(estudiantes)

########### FORMA MAS SENCILLA ################################
def insertar_estudiantes(estudiante):
    c.execute("INSERT INTO estudiantes VALUES (?,?,?,?)",
    (estudiante.matricula, estudiante.nombre, estudiante.apellido, estudiante.promedio))
    conn.commit()

# est_5 = Estudiante('666', 'Roberto', 'Barrera', 7.5)
# insertar_estudiantes(est_5)
# c.execute("SELECT * FROM estudiantes")
# print(c.fetchall())

## uso de funciones creadas

estudiantesDB.select_all()



# Para guardar los cambios
conn.commit() 
# Cerrar la conexion a la BD 
conn.close()