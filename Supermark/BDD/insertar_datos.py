import sqlite3
from BDD.crear_bd  import crear_conexion 



def crear_datos(conexion,consulta):
    cursor= conexion.cursor()
    cursor.execute(consulta)
    conexion.commit()

def crear_producto(conexion, producto):
    sql="INSERT INTO producto(nombre,marca,precio,stock) VALUES(?,?,?,?)"
    cursor= conexion.cursor()
    cursor.execute(sql,producto)
    conexion.commit()

productos = [
        ['Leche', 'Cosalta', 200.0, 1000],
        ['Azucar', 'Ledesma',250.5, 500],
        ['Harina', 'Cañuelas',120.5, 200],
        ['Aceite', 'Cocinero', 300.5, 560],
        ['Arroz', '10 Minutos', 220.5, 350],
        ['Yogurt', 'Serenisima',190.8, 270],
        ['Fideo', 'Matarazzo',  230.0, 400]
    ]
conexion= crear_conexion(".//BDD//Supermarket.db")
for p in productos:
    crear_producto(conexion, p)


#crear usuario
# nomb=input('ingrese nombre: ')
# ape=input('ingrese apellido: ')
# sql_usuario= f"INSERT INTO usuario(nombre,apellido, email,dni,contrasenia) VALUES('{nomb}','{ape}','ejemplo@gmail.com',42152154, 'ejemplo1234');"

# #crear tarjeta de credito
# numero= int(input('ingrese numero de tarjeta'))
# banco= input('ingrese nombre del banco: ')
# sql_tarjeta= f"INSERT INTO tarjetacredito(numero, banco, titular, fechaCaducidad, id_usuario) VALUES({numero}, '{banco}', 'antonella', '09-27', 1)"

#conexion= crear_conexion("cm7\Supermark\BDD\Supermarket.db")
#crear_datos(conexion,sql_tarjeta)
