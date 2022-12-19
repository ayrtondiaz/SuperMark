import tkinter as tk
import sqlite3
import tkinter.ttk as ttk

conn = sqlite3.connect('Supermarket.db')
cursor = conn.cursor()

#Ejecuta una consulta SQL para obtener la lista de elementos que deseas mostrar al usuario:
cursor.execute("SELECT * FROM products")
items = cursor.fetchall()

#Crea una ventana y un widget de lista para mostrar los elementos:
window = tk.Tk()
listbox = tk.Listbox(window)
window.geometry("400x300+0+0")
window.title("Productos")

#Itera sobre la lista de elementos y agrégalos al widget de lista
for item in items:
    listbox.insert(tk.END, item)


listbox.pack()

#Crea una función que se encargue de añadir los productos seleccionados al carrito de compras.
def add_to_cart():
    selected_indices = listbox.curselection()
    for index in selected_indices:
        item = items[index]
        # Añade el elemento al carrito de compras
        cursor.execute("INSERT INTO carrito (nombre, precio) VALUES (?, ?)", item)
        conn.commit()


button = ttk.Button(window, text="Añadir al carrito", command=add_to_cart)

button.pack()

window.mainloop()


