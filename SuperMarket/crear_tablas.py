import sqlite3
from crear_bd import crear_conexion 

def crear_tabla(conexion, consulta):
    cursor= conexion.cursor()
    cursor.execute(consulta)
    conexion.commit()
    
    

sql_crear_usuario_tabla= """CREATE TABLE IF NOT EXISTS users(
                            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT(30)  NULL,
                            password TEXT);"""
                            
sql_crear_tarjeta_tabla= """CREATE TABLE IF NOT EXISTS tarjetacredito(
                            numero BIGINT PRIMARY KEY,
                            banco TEXT,
                            titular TEXT,
                            fechaCaducidad TEXT,
                            id_usuario INTEGER,
                            FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
                            );"""


sql_crear_producto_tabla = """CREATE TABLE IF NOT EXISTS products(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre TEXT  NULL,
                            precio FLOAT  NULL,
                            stock INTEGER  NULL
                            ); """
                            
sql_crear_detalle_tabla = """CREATE TABLE IF NOT EXISTS detalle_venta(
                            id_detalle INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre_producto TEXT  NULL,
                            precio FLOAT  NULL,
                            cantidad INTEGER  NULL,
                            subtotal FLOAT  NULL
                            ); """
sql_crear_Carrito= """CREATE TABLE IF NOT EXISTS carrito(
                            nombre TEXT  NULL,
                            precio FLOAT  NULL                            
                            ); """                         
                              
conexion = crear_conexion("Supermarket.db")

# crear_tabla(conexion, sql_crear_usuario_tabla)
# crear_tabla(conexion, sql_crear_tarjeta_tabla)
# crear_tabla(conexion, sql_crear_producto_tabla)
# crear_tabla(conexion, sql_crear_detalle_tabla)
#crear_tabla(conexion, sql_crear_Carrito)