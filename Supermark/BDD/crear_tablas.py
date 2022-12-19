import sqlite3
from BDD.crear_bd import crear_conexion 

def crear_tabla(conexion, consulta):
    cursor= conexion.cursor()
    cursor.execute(consulta)
    conexion.commit()
    
    

sql_crear_usuario_tabla= """CREATE TABLE IF NOT EXISTS usuario(
                            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre TEXT(30) NOT NULL,
                            apellido TEXT(30),
                            email TEXT,
                            dni INTEGER,
                            contrasenia TEXT);"""
                            
sql_crear_tarjeta_tabla= """CREATE TABLE IF NOT EXISTS tarjetacredito(
                            numero BIGINT PRIMARY KEY,
                            banco TEXT,
                            titular TEXT,
                            fechaCaducidad TEXT,
                            id_usuario INTEGER,
                            FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
                            );"""


sql_crear_producto_tabla = """CREATE TABLE IF NOT EXISTS producto(
                            id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre TEXT NOT NULL,
                            marca TEXT NOT NULL,
                            precio FLOAT NOT NULL,
                            stock INTEGER NOT NULL
                            ); """
                            
sql_crear_detalle_tabla = """CREATE TABLE IF NOT EXISTS detalle_venta(
                            id_detalle INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre_producto TEXT NOT NULL,
                            precio FLOAT NOT NULL,
                            cantidad INTEGER NOT NULL,
                            subtotal FLOAT NOT NULL
                            ); """                         
                              
conexion = crear_conexion(".//BDD//Supermarket.db")
crear_tabla(conexion, sql_crear_usuario_tabla)
crear_tabla(conexion, sql_crear_tarjeta_tabla)
crear_tabla(conexion, sql_crear_producto_tabla)
crear_tabla(conexion, sql_crear_detalle_tabla)