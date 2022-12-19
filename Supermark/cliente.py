import tkinter as tk
from tkinter import ttk, Button, Frame, messagebox, Tk, Toplevel
from BDD.crear_bd import crear_conexion
from BDD.consulta_producto import select_producto, select_producto_by_id
from BDD.insertar_datos import crear_datos
class Cliente(Toplevel):
    def __init__(self,root):
        super().__init__(root)
        self.root=root
        self.geometry("500x300")
        
        self.nb= ttk.Notebook(self)
        
        self.p1= ttk.Frame(self.nb)  #crear pestañas
        self.crear_tabla()
        self.nb.add(self.p1, text= "Ver productos") #añadir pestaña
        
        
        self.p2= ttk.Frame(self.nb)
        self.crear_compra()
        self.nb.add(self.p2, text= "Realizar Compra")
        
        self.p3= ttk.Frame(self.nb)
        self.nb.add(self.p3, text= "Carrito")
        self.nb.pack(fill="both", expand="yes")
    
    
    def crear_tabla(self):
        columns = ('id_producto', 'nombre', 'marca', 'precio')

        self.tree = ttk.Treeview(self.p1, columns=columns, show='headings')
        self.tree.grid(row=1, column=1, sticky=(tk.N, tk.S, tk.E, tk.W))

        # definimos los encabezados
        self.tree.heading('id_producto', text='ID')
        self.tree.heading('nombre', text='Nombre')
        self.tree.heading('marca', text='Marca')
        self.tree.heading('precio', text='Precio')
        # para ejecutar un callback cuando se haga click en un item
        #self.tree.bind('<<TreeviewSelect>>', self.item_seleccionado)

        # agregar barra de scroll
        scrollbar = ttk.Scrollbar(self.p1, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=2, sticky=(tk.N, tk.S))
        
        conexion = crear_conexion("Supermark\BDD\Supermarket.db")
        filas= select_producto(conexion)
        # agregar datos al treeview
        for fila in filas:
            self.tree.insert('', tk.END, values=fila)

    def crear_compra(self):
        ttk.Label(self.p2, text="Ingresa los datos del producto").grid(row=0, column=0)
        ttk.Label(self.p2, text="Ingresa id: ").grid(row=1, column=0)
        ttk.Label(self.p2, text="Ingresa cantidad: ").grid(row=2, column=0)
        
        self.entry_id = tk.IntVar()
        
        ttk.Entry(self.p2, textvariable=self.entry_id).grid(row=1, column=1)
        
        self.entry_cant = tk.IntVar()
        
        ttk.Entry(self.p2, textvariable=self.entry_cant).grid(row=2, column=1)
        
        ttk.Button(self.p2, text="Comprar", command=self.buscar_producto).grid(row=3, column=1)
        
        
    def buscar_producto(self):
        ruta = "Supermark\BDD\Supermarket.db"
        conexion = crear_conexion(ruta)
        consulta= f"SELECT * FROM producto WHERE id_producto = {self.entry_id.get()}"
        fila= select_producto_by_id(conexion, consulta) #[(1,leche,cosalta,200,1000)]
        if len(fila) == 0:
            messagebox.showerror(message="no hay resultados")
        else:
            if fila[0][4]>= self.entry_cant.get():
                resp=messagebox.askquestion(message=f"{fila[0][1]} -- {fila[0][2]} -- ${fila[0][3]}")
                if resp == "yes":
                    consulta = f"INSERT INTO detalle_venta(nombre_producto,precio, cantidad, subtotal) VALUES('{fila[0][1]}',{fila[0][3]},{self.entry_cant.get()}, {fila[0][3] * self.entry_cant.get()})"
                    crear_datos(conexion, consulta)
            else:
                messagebox.showerror(message="Cantidad insuficiente")