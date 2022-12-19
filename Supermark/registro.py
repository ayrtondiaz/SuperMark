import tkinter
from tkinter import ttk, Frame, Button, Tk, Toplevel, messagebox
from BDD.crear_bd import crear_conexion
 
class CrearCuenta (Toplevel):
   def _init_(self, root):
       super (0._init_(root)
      self.root=root
      self.grid()
      self.crear_widgets


def crear_widgets(self):
   ttk.Label(self, text= "Nombre") .grid(row=0, column=0)
   ttk.Label(self, text= "Apellido").grid(row=1, column=0)
   ttk.Label(self, text= "Email").grid(row-2, column=0)
   ttk.Label(self, text=" "DNI").grid(row=3, columna=0)
   ttk.Label(self, text= "Contrasenia").grid(row-4, column=0)
   self.entry_nombre= tkinter.StringVar(
   ttk.Entry(self, textvariable=self.entry_nombre).grid(row=0, column=1)
   self.entry_apellido= tkinter.StringVar
   ttk.Entry(self, textvariable=self.entry_apellido).grid(row=1, column=1)
   self.entry_email= tkinter.StringVar
   ttk.Entry(self, textvariable=self.entry_email).grid(row=2, column=1)
   self.entry_dni= tkinter.IntVar
   ttk.Entry(self, textvariable=self.entry_dni).grid(row=3, column=1)
   self.entry_pass= tkinter.StringVar()
   ttk.Entry(self, textvariable=self.entry_pass).grid(row=4, column=1)


self.button_confirmar= Button(self,text="Confirmar", command=self.crear_usuario).grid(row=5, column1)