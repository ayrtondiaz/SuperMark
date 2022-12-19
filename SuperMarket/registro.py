from tkinter import *
from tkinter import messagebox

import sqlite3

def register_user():
  # Obtiene el nombre de usuario y la contraseña ingresados por el usuario
  username = username_entry.get()
  password = password_entry.get()

  # Conecta a la base de datos
  conn = sqlite3.connect('Supermarket.db')
  cursor = conn.cursor()

  try:
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
  except sqlite3.Error as e:
    # Muestra un mensaje de error si la consulta falla
    messagebox.showerror("Error", "El nombre de usuario ya existe")
    return

  # Muestra un mensaje de éxito al usuario
  messagebox.showinfo("Registro exitoso", "El usuario ha sido registrado con éxito")

  # Cierra la conexión a la base de datos
  conn.close()

# Crea la ventana principal de la aplicación
root = Tk()
root.geometry("400x300+0+0")
root.title("Registro de usuario")

# Crea los campos de entrada para el nombre de usuario y la contraseña
username_label = Label(root, text="Nombre de usuario:")
username_entry = Entry(root)
password_label = Label(root, text="Contraseña:")
password_entry = Entry(root, show="*")

# Crea el botón de registro y lo configura para llamar a la función de registro cuando se haga clic
register_button = Button(root, text="Registrar", command=register_user, cursor="hand2")

# Empaqueta los widgets en la ventana principal
username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack()
register_button.pack()

# Ejecuta el bucle principal de la aplicación
root.mainloop()


