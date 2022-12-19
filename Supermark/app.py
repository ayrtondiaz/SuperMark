import tkinter 

from tkinter import ttk, Button, Frame, messagebox, Tk
from login import Login
from registro import CrearCuenta

class App(Frame):
    
    def __init__(self, root):
        super().__init__(root)
        self.root=root
        self.grid()
        self.crear_widgets()
        
        
    def crear_widgets(self):
        self.button= Button(self)
        self.button["text"] = "Login"
        self.button["command"] = self.abrir_login 
        self.button.grid(padx=50, pady=15)
        
        self.button1= Button(self)
        self.button1["text"] = "Registro"
        self.button1["command"] = self.abrir_registro 
        self.button1.grid(padx=50, pady=15)
        
        
    def abrir_login(self):
        Login(self.root)
        
    
    def abrir_registro(self):
       CrearCuenta(self.root)
        

root=Tk()
app= App(root)
app.mainloop()