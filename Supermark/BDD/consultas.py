import sqlite3
from crear_bd import crear_conexion 

def crear_usuario(conexion):
    nomb=input('ingrese nombre de Usuario: ')
    ape=input('ingrese apellido: ')
    sql_usuario= f"INSERT INTO usuario(nombre,apellido, email,dni,contrasenia) VALUES('{nomb}','{ape}','ejemplo@gmail.com',42152154, 'ejemplo1234');"
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

conexion= crear_conexion(".//BDD//Supermarket.db")

crear_usuario(conexion)
crear_tarjeta(conexion)