from tkinter import *
from tkinter import messagebox
import sqlite3

def login():
  # Obtiene el nombre de usuario y la contraseña ingresados por el usuario
  username = username_entry.get()
  password = password_entry.get()

  # Conecta a la base de datos
  conn = sqlite3.connect('Supermarket.db')
  cursor = conn.cursor()

  # Verifica si el nombre de usuario y la contraseña coinciden con una fila de la tabla de usuarios
  cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
  row = cursor.fetchone()

  # Si se encontró una fila, el inicio de sesión es correcto
  if row:
    messagebox.showinfo("Inicio de sesión correcto", "Bienvenido al sistema, {}".format(username))
    login_window.destroy()
  else:
    messagebox.showerror("Error", "El nombre de usuario o la contraseña son incorrectos")

  # Cierra la conexión a la base de datos
  conn.close()

# Crea la ventana emergente de inicio de sesión
login_window = Tk()
login_window.geometry("400x300+0+0")
login_window.title("Inicio de sesión")

# Crea los campos de entrada para el nombre de usuario y la contraseña
username_label = Label(login_window, text="Nombre de usuario")
username_entry = Entry(login_window)
password_label = Label(login_window, text="Contraseña")
password_entry = Entry(login_window, show="*")

# Crea el botón de inicio de sesión y lo configura para llamar a la función login() cuando se haga clic
login_button = Button(login_window, text="Iniciar sesión", command=login, cursor="hand2")

# Coloca los widgets en la ventana de inicio de sesión
username_label.grid(row=0, column=0)
username_entry.grid(row=0, column=1)
password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1)
login_button.grid(row=2, column=1)

# Muestra la ventana emergente
login_window.mainloop()

