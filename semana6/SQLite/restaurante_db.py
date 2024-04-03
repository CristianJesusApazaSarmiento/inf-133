import sqlite3

conn = sqlite3.connect("restaurante.db")

#Crear tabla de platos
'''conn.execute(
    """
    CREATE TABLE PLATOS(id INTEGER PRIMARY KEY, nombre TEXT NOT NULL, precio REAL NOT NULL, categoria TEXT NOT NULL);
    """
)'''
#Insertar datos de la tabla platos
conn.execute(
    """
    INSERT INTO PLATOS(nombre, precio, categoria) VALUES ('Pizza','10.99','Italiana')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS(nombre, precio, categoria) VALUES ('Hamburguesa','8.99','Americana')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS(nombre, precio, categoria) VALUES ('Sushi','12.99','Japonesa')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS(nombre, precio, categoria) VALUES ('Ensalada','6.99','Vegetariana')
    """
)
# Consultar datos de Platos
print("\nPLATOS:")
cursor = conn.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)



#Crear tabla de mesas
conn.execute(
    """
    CREATE TABLE MESAS(id INTEGER PRIMARY KEY, numero INTEGER NOT NULL);
    """
)
#Insertar datos de la tabla mesas
conn.execute(
    """
    INSERT INTO MESAS(numero)VALUES('1')
    """
)
conn.execute(
    """
    INSERT INTO MESAS(numero)VALUES('2')
    """
)
conn.execute(
    """
    INSERT INTO MESAS(numero)VALUES('3')
    """
)
conn.execute(
    """
    INSERT INTO MESAS(numero)VALUES('4')
    """
)
# Consultar datos de MEsas
print("\nMESAS:")
cursor = conn.execute("SELECT * FROM MESAS")
for row in cursor:
    print(row)


#Crear tabla de Pedidos
conn.execute(
    """
    CREATE TABLE PEDIDOS(id INTEGER PRIMARY KEY, plato_id INTEGER NOT NULL, mesa_id INTEGER NOT NULL, 
    cantidad INTEGER NOT NULL, fecha DATE NOT NULL,
    FOREIGN KEY(plato_id)REFERENCES PLATOS(id),
    FOREIGN KEY(mesa_id)REFERENCES MESAS(id)
    );
    """
)
#Insertar datos de la tabla pedidos
conn.execute(
    """
    INSERT INTO PEDIDOS(plato_id, mesa_id, cantidad, fecha)VALUES('1','2','2','2024-04-01')
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS(plato_id, mesa_id, cantidad, fecha)VALUES('2','3','1','2024-04-01')
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS(plato_id, mesa_id, cantidad, fecha)VALUES('3','1','3','2024-04-02')
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS(plato_id, mesa_id, cantidad, fecha)VALUES('4','4','1','2024-04-02')
    """
)
# Consultar datos de Pedidos
print("\nPEDIDOS:")
cursor = conn.execute("SELECT * FROM PEDIDOS")
for row in cursor:
    print(row)
    
#Actualiza el precio del plato con id 2 (hamburguesa) a 9.99
conn.execute(
    """
    UPDATE PLATOS
    SET precio = '9.99'
    WHERE id = 2
    """
)
print("\nActualiza el precio del plato con id 2 (hamburguesa) a 9.99")
cursor = conn.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)
    
#Cambia la categoria del plato con id 3 (sushi) a "Fusion" 
conn.execute(
    """
    UPDATE PLATOS
    SET categoria = 'Fusion'
    WHERE id = 3
    """
)
print("\nCambia la categoria del plato con id 3 (sushi) a Fusion")
cursor = conn.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)
    
#Elimina el plato con id 4 (Ensalada) de la tabla de platos
conn.execute(
    """
    DELETE FROM PLATOS
    WHERE id = 4
    """
)
print("\nElimina el plato con id 4 (Ensalada) de la tabla de platos")
cursor = conn.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)
    
#Elimina el pedido con id 3
conn.execute(
    """
    DELETE FROM PEDIDOS
    WHERE id = 3
    """
)
print("\nElimina el pedido con id 3")
cursor = conn.execute("SELECT * FROM PEDIDOS")
for row in cursor:
    print(row)