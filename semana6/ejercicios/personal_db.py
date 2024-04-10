import sqlite3

conn = sqlite3.connect("personal.db")

try:
    conn.execute(
        """
        CREATE TABLE DEPARTAMENTOS(id INTEGER PRIMARY KEY, nombre TEXT NOT NULL, fecha_creacion TEXT NOT NULL);
        """
    )
except sqlite3.OperationalError:
    print("La tabla DEPARTAMENTOS ya exite")

'''conn.execute(
    """
    INSERT INTO DEPARTAMENTOS(nombre, fecha_creacion)VALUES('Ventas', '10-04-2020')
    """
)
conn.execute(
    """
    INSERT INTO DEPARTAMENTOS(nombre, fecha_creacion)VALUES('Marketing', '11-04-2020')
    """
)
'''


try:
    conn.execute(
        """
        CREATE TABLE CARGOS(id INTEGER PRIMARY KEY, nombre TEXT NOT NULL, nivel TEXT NOT NULL, fecha_creacion TEXT NOT NULL);
        """
    )
except sqlite3.OperationalError:
    print("La tabla CARGOS ya exite")

'''conn.execute(
    """
    INSERT INTO CARGOS(nombre, nivel, fecha_creacion)VALUES('Gerente de Ventas', 'Senior', '10-04-2020')
    """
)
conn.execute(
    """
    INSERT INTO CARGOS(nombre, nivel, fecha_creacion)VALUES('Analisis de Marketing', 'Junior', '11-04-2020')
    """
)
conn.execute(
    """
    INSERT INTO CARGOS(nombre, nivel, fecha_creacion)VALUES('Representante de Ventas', 'Junior', '12-04-2020')
    """
)
'''

try:
    conn.execute(
        """
        CREATE TABLE EMPLEADOS(id INTEGER PRIMARY KEY, departamento_id INTEGER NOT NULL, cargo_id INTEGER NOT NULL, nombres TEXT NOT NULL, apellido_paterno TEXT NOT NULL, apellido_materno TEXT NOT NULL, fecha_contratacion DATE NOT NULL, fecha_creacion DATE NOT NULL,
        FOREIGN KEY (departamento_id) REFERENCES DEPARTAMENTOS(id),
        FOREIGN KEY (cargo_id) REFERENCES CARGOS(id));
        """
    )
except sqlite3.OperationalError:
    print("La tabla EMPLEADOS ya exite")


'''conn.execute(
    """
    INSERT INTO EMPLEADOS(nombres, apellido_paterno, apellido_materno, fecha_contratacion, departamento_id, cargo_id, fecha_creacion)VALUES('Juan', 'Gonzales', 'Perez', '15-05-2023', 1, 1,'10-04-2020')
    """
)
conn.execute(
    """
    INSERT INTO EMPLEADOS(nombres, apellido_paterno, apellido_materno, fecha_contratacion, departamento_id, cargo_id, fecha_creacion)VALUES('Maria', 'Lopez', 'Martinez', '20-06-2023', 2, 2,'11-04-2020')
    """
)
'''

try:
    conn.execute(
        """
        CREATE TABLE SALARIOS(id INTEGER PRIMARY KEY, empleado_id INTEGER NOT NULL,
        salario REAL NOT NULL, fecha_inicio DATE NOT NULL, fecha_fin DATE NOT NULL, fecha_creacion TEXT NOT NULL,
        FOREIGN KEY (empleado_id) REFERENCES EMPLEADOS(id));
        """
    )
except sqlite3.OperationalError:
    print("La tabla SALARIOS ya exite")
    
'''conn.execute(
    """
    INSERT INTO SALARIOS(empleado_id, salario, fecha_inicio, fecha_fin, fecha_creacion)
    VALUES(1, '3000.0', '01-04-2024', '30-04-2025', '10-04-2020')
    """
)
conn.execute(
    """
    INSERT INTO SALARIOS(empleado_id, salario, fecha_inicio, fecha_fin, fecha_creacion)
    VALUES(2, '3500.0', '01-07-2023', '30-04-2024', '11-04-2020')
    """
)'''


'''conn.execute(
    """
    DELETE FROM EMPLEADOS
    WHERE id = 1
    """
)'''
conn.commit()
conn.close()