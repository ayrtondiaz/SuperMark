import sqlite3
from crear_bd import crear_conexion 



def crear_producto(conexion, producto):
    sql="INSERT INTO products(nombre,precio,stock) VALUES(?,?,?)"
    cursor= conexion.cursor()
    cursor.execute(sql,producto)
    conexion.commit()

productos = [
        ['Leche', 200.0, 1000],
        ['Azucar',250.5, 500],
        ['Harina',120.5, 200],
        ['Aceite', 300.5, 560],
        ['Arroz', 220.5, 350],
        ['Yogurt',190.8, 270],
        ['Fideo',  230.0, 400]
]
conexion= crear_conexion(".//Supermarket.db")
for p in productos:
    crear_producto(conexion, p)




def crear_usuario(conexion):
    nomb=input('ingrese nombre de Usuario: ')
    contra=input('ingrese contraseña: ')
    sql_usuario= f"INSERT INTO users(username, password) VALUES('{nomb}','{contra}');"
    cursor= conexion.cursor()
    cursor.execute(sql_usuario)
    conexion.commit()

def crear_tarjeta(conexion):
    numero= int(input('ingrese numero de tarjeta'))
    banco= input('ingrese nombre del banco: ')
    sql_tarjeta= f"INSERT INTO tarjetacredito(numero, banco, titular, fechaCaducidad, id_usuario) VALUES({numero}, '{banco}', 'ayrton', '09-27', 1)"
    cursor= conexion.cursor()
    cursor.execute(sql_tarjeta)
    conexion.commit()

conexion= crear_conexion(".//Supermarket.db")

crear_usuario(conexion)
crear_tarjeta(conexion)