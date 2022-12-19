from tkinter import Tk, font
import cmp as cmp


class App():
    def __init__(self, titulo="SuperMarket UI"):
        self.__root = Tk()
        self._defaultFont = font.nametofont('TkDefaultFont')
        self._defaultFont.configure(family="Arial", size=15)
        self.preferredSize(800, 800)
        self.root.title(titulo)
        self.cliente = {}
        cmp.menuBar(self)
        cmp.moduloUsuario(self)
        cmp.moduloProducto(self)
        cmp.moduloCarrito()
        cmp.moduloOperaciones(self)


    @property
    def root(self) -> Tk:
        return self.__root


    def preferredSize(self, w: int, h: int):
        sw = self.__root.winfo_screenwidth()
        sh = self.__root.winfo_screenheight()
        self.__root.geometry('%dx%d+%d+%d' % (w, h, (sw-w)/2, (sh-h)/2))


    def iniciar(self):
        self.root.mainloop()


app = App()
app.iniciar()
