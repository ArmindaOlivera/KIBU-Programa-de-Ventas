import tkinter
import tkinter.ttk

from Producto import Producto

fuenteTitulo="Helvetica 20"
fuenteEtiqueta="Helvetica 15"
fuenteBoton="Helvetica 10"
fuenteTexto="Helvetica 20"

listaProductos = [Producto("PAN\nMOLDE\nFIBRA", 24.50), 
Producto("LECHE\nDESLAC", 6.70), 
Producto("TE\nPARIS\nC/CANELA", 9.80), 
Producto("PASTA\nDON\nVITTORIO", 3.50 ),
Producto("GEL\nDE\nMANOS\nSANIT", 9),
Producto("PURE\nDE\nPAPAS", 13.90),
Producto("AVENA\nINSTANT", 9.90),
Producto("QUINUA", 6.70),
Producto("TOALLA\nHUM.\nPEQUENIN", 26),
Producto("ROCKLETS", 4),
Producto("SARDINA", 10.80),
Producto("ATUN\nNOERTE\nLOMITOS", 13.70),
Producto("SALCHICHA\n1 KG", 28.70),
Producto("CHULETA\nDE\nLOMO\n1 KG", 30.70),
Producto("ARINA\n1 KG", 26.70)]

class VentanaProductos:
    def __init__(self):
        self.ventanaProducto=tkinter.Tk()
        self.ventanaProducto.geometry("700x600+340+0")
        self.ventanaProducto.title("KIBU Programa de Ventas")
    
    def crearWidgetsVentanaProductos(self):
        self.etiquetaTitulo=tkinter.Label(self.ventanaProducto, text="KIBU Programa de Ventas", bg="green", font=fuenteTitulo)# titulo del programa / bg se ocupa para color
        self.etiquetaCreditos=tkinter.Label(self.ventanaProducto, text="Arminda Olivera, 2020")
        self.etiquetaNombre=tkinter.Label(self.ventanaProducto, text="Nombre", font=fuenteEtiqueta)
        self.etiquetaNit=tkinter.Label(self.ventanaProducto, text="NIT", font=fuenteEtiqueta)
        self.etiquetaEfectivo= tkinter.Label(self.ventanaProducto, text="Efectivo", font=fuenteEtiqueta)
        self.separadorVertical = tkinter.ttk.Separator(self.ventanaProducto, orient="vertical")
        self.botonImprimirFactura=tkinter.Button(self.ventanaProducto, text="Imprimir Factura", font=fuenteBoton, borderwidth=5)
        self.cajaTextoNombre=tkinter.Entry(self.ventanaProducto,font=fuenteTexto)
        self.cajaTextoNit=tkinter.Entry(self.ventanaProducto,font=fuenteTexto)
        self.cajaTextoEfectivo=tkinter.Entry(self.ventanaProducto,font=fuenteTexto)
        self.listaBotonesProducto = []
        for producto in listaProductos:
            self.listaBotonesProducto.append(tkinter.Button(self.ventanaProducto, text=producto.nombre, width=10, height=5, font=fuenteBoton,borderwidth=5))

    def crearVentanaProductos(self):
        fila = 1
        columna = 3
        self.etiquetaTitulo.grid(row=0, column=0, columnspan=5)
        self.etiquetaNombre.grid(row=1, column=0)
        self.cajaTextoNombre.grid(row=1, column=1)
        self.etiquetaNit.grid(row=2, column=0)
        self.cajaTextoNit.grid(row=2, column=1)
        self.etiquetaEfectivo.grid(row=3, column=0)
        self.cajaTextoEfectivo.grid(row=3, column=1)
        self.botonImprimirFactura.grid(row=4,column=0, columnspan=2)
        self.separadorVertical.grid(column=2, row=1, rowspan=10, sticky='ns')
        for botonProducto in self.listaBotonesProducto:
            botonProducto.grid(row=fila, column=columna)
            if columna < 5:
                columna+=1
            else:
                fila+=1
                columna = 3
