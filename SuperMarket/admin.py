
import tkinter as tk
import sqlite3

conn = sqlite3.connect('Supermarket.db')
cursor = conn.cursor()

window = tk.Tk()
window.geometry("400x300+0+0") 
window.title("Administrar")

name_label = tk.Label(window, text="Nombre:")
name_entry = tk.Entry(window)

price_label = tk.Label(window, text="Precio:")
price_entry = tk.Entry(window)

#Crea una función que se ejecute cuando se haga clic en un botón para guardar los cambios.

def save_changes():
    name = name_entry.get()
    price = price_entry.get()
    
    cursor.execute("UPDATE products SET nombre, precio, ", (name, price, ))
    conn.commit()

#Crea un botón y configúralo para que llame a la función save_changes cuando se haga clic en él:
button = tk.Button(window, text="Guardar cambios", command=save_changes)


name_label.pack()
name_entry.pack()
price_label.pack()
price_entry.pack()

button.pack()

window.mainloop()
