# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("instituto.db")

#La conexion no es persistente, la base de datos es persistente
# Crear tabla de carreras
#INTERGER, TEXT, DATE... son tipos de datos
#
conn.execute(
    """
    CREATE TABLE CARRERAS(id INTEGER PRIMARY KEY, nombre TEXT NOT NULL, duracion INTEGER NOT NULL);
    """
)

# Insertar datos de carreras
conn.execute(
    """
    INSERT INTO CARRERAS (nombre, duracion) VALUES ('Ingeniería en Informática', 5)
    """
)
conn.execute(
    """
    INSERT INTO CARRERAS (nombre, duracion) VALUES ('Licenciatura en Administración', 4)
    """
)

# Consultar datos
print("\nCARRERAS:")
cursor = conn.execute("SELECT * FROM CARRERAS")
for row in cursor:
    print(row)

# CARRERAS:
# (1, 'Ingeniería en Informática', 5)
# (2, 'Licenciatura en Administración', 4)

# Crear tablas de estudiantes
conn.execute(
    """
    CREATE TABLE ESTUDIANTES(id INTEGER PRIMARY KEY,nombre TEXT NOT NULL,apellido TEXT NOT NULL,fecha_nacimiento DATE NOT NULL);
    """
)

# Insertar datos de estudiantes
conn.execute(
    """
    INSERT INTO ESTUDIANTES (nombre, apellido, fecha_nacimiento) VALUES ('Juan', 'Perez', '2000-05-15')
    """
)
conn.execute(
    """
    INSERT INTO ESTUDIANTES (nombre, apellido, fecha_nacimiento) VALUES ('María', 'Lopez', '1999-08-20')
    """
)

# Consultar datos de estudiantes
print("\nESTUDIANTES:")
cursor = conn.execute("SELECT * FROM ESTUDIANTES")
for row in cursor:
    print(row)

# ESTUDIANTES:
# (1, 'Juan', 'Perez', '2000-05-15')
# (2, 'María', 'Lopez', '1999-08-20')

# Crear tabla de matriculación
conn.execute(
    """
    CREATE TABLE MATRICULAS(id INTEGER PRIMARY KEY,estudiante_id INTEGER NOT NULL,carrera_id INTEGER NOT NULL,
    fecha DATE NOT NULL, 
    FOREIGN KEY (estudiante_id) REFERENCES ESTUDIANTES(id),
    FOREIGN KEY (carrera_id) REFERENCES CARRERAS(id));
    """
)

# Insertar datos de matriculación
conn.execute(
    """
    INSERT INTO MATRICULAS (estudiante_id, carrera_id, fecha) 
    VALUES (1, 1, '2024-01-15')
    """
)
conn.execute(
    """
    INSERT INTO MATRICULAS (estudiante_id, carrera_id, fecha) 
    VALUES (2, 2, '2024-01-20')
    """
)

conn.execute(
    """
    INSERT INTO MATRICULAS (estudiante_id, carrera_id, fecha)
    VALUES (1, 2, '2024-01-25')
    """
)

# Consultar datos de matriculación
print("\nMATRICULAS:")
cursor = conn.execute(
    """
    SELECT ESTUDIANTES.nombre, ESTUDIANTES.apellido, CARRERAS.nombre, MATRICULAS.fecha 
    FROM MATRICULAS
    JOIN ESTUDIANTES ON MATRICULAS.estudiante_id = ESTUDIANTES.id 
    JOIN CARRERAS ON MATRICULAS.carrera_id = CARRERAS.id
    """
)
for row in cursor:
    print(row)

# MATRICULACION:
# ('Juan', 'Perez', 'Ingeniería en Informática', '2024-01-15')
# ('María', 'Lopez', 'Licenciatura en Administración', '2024-01-20')
# ('Juan', 'Perez', 'Licenciatura en Administración', '2024-01-25')    

# Eliminar una fila de la tabla de matriculación
conn.execute(
    """
    DELETE FROM MATRICULAS
    WHERE id = 3
    """
)

# Listar datos de matriculación
print("\nMATRICULAS:")
cursor = conn.execute(
    "SELECT * FROM MATRICULAS"
)

for row in cursor:
    print(row)

# MATRICULACION:
# (1, 1, 1, '2024-01-15')
# (2, 2, 2, '2024-01-20')

# Actualizar una fila de la tabla de matriculación
conn.execute(
    """
    UPDATE MATRICULAS
    SET fecha = '2024-01-30'
    WHERE id = 2
    """
)
# Listar datos de matriculación
print("\nMATRICULAS:")
cursor = conn.execute(
    "SELECT * FROM MATRICULAS"
)
for row in cursor:
    print(row)
    
# MATRICULACION:
# (1, 1, 1, '2024-01-15')
# (2, 2, 2, '2024-01-30')

# Cerrar conexión
conn.close()