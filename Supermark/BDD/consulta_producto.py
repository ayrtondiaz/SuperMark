import sqlite3

# from crear_bd import crear_conexion


def select_producto(conexion):
    cursor= conexion.cursor()
    cursor.execute("SELECT id_producto, nombre, marca, precio FROM producto ")
    filas = cursor.fetchall()
    return filas

def select_producto_by_id(conexion,consulta):
    cursor= conexion.cursor()
    cursor.execute(consulta)
    fila= cursor.fetchall()
    return fila
