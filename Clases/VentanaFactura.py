import tkinter
import tkinter.ttk

fuenteTitulo="Helvetica 20"
fuenteEtiqueta="Helvetica 15"
fuenteBoton="Helvetica 10"
fuenteTexto="Helvetica 20"

class VentanaFactura:
    def __init__(self):
        self.ventanaFactura=tkinter.Tk()
        self.ventanaFactura.geometry("322x600+0+0")
        self.ventanaFactura.title("KIBU Programa de Ventas")
    
    def crearWidgetsVentanaFactura(self):
        self.etiquetaTitulo=tkinter.Label(self.ventanaFactura, text="Factura", bg="green", font=fuenteTitulo)# titulo del programa / bg se ocupa para color
        self.etiquetaCreditos=tkinter.Label(self.ventanaFactura, text="Arminda Olivera, 2020")
        self.etiquetaNombre=tkinter.Label(self.ventanaFactura, text="Nombre: Sara Bolivar", font=fuenteEtiqueta)
        self.etiquetaNit=tkinter.Label(self.ventanaFactura, text="NIT: 25882632", font=fuenteEtiqueta)
        self.etiquetaTotal=tkinter.Label(self.ventanaFactura, text="Total: 45 Bolivianos", font=fuenteEtiqueta)
        self.etiquetaEfectivo= tkinter.Label(self.ventanaFactura, text="Efectivo: 50 Bolivianos", font=fuenteEtiqueta)
        self.etiquetaCambio=tkinter.Label(self.ventanaFactura, text="Cambio: 5 Bolivianos", font=fuenteEtiqueta)
        self.etiquetaTituloListaProductos=tkinter.Label(self.ventanaFactura, text="Lista de Productos", bg="green", font=fuenteEtiqueta)
        self.etiquetaDetalleListaProductos=tkinter.Label(self.ventanaFactura, text="Cantidad \t Producto\t Precio \tTotal", bg="gray", font=fuenteEtiqueta)
        self.etiquetaListaProductos=tkinter.Label(self.ventanaFactura, text="pan\t5\t0.5\t2.5", font=fuenteEtiqueta)
        self.separadorHorizontal1=tkinter.Label(self.ventanaFactura, text=" ", font=fuenteEtiqueta)
        self.separadorHorizontal2=tkinter.Label(self.ventanaFactura, text=" ", font=fuenteEtiqueta)

    def crearVentanaFactura(self):
        self.etiquetaTitulo.grid(row=0, column=0, columnspan=2) # fill es para expandir en el eje x, si lleva fill debe tener true
        self.separadorHorizontal1.grid(row=1, columnspan=2)
        self.etiquetaNombre.grid(row=2, column=0)
        self.etiquetaNit.grid(row=3, column=0)
        self.separadorHorizontal2.grid(row=4, column=0, columnspan=2)
        self.etiquetaTituloListaProductos.grid(row=5, column=0, columnspan=2)
        self.etiquetaDetalleListaProductos.grid(row=6, column=0, columnspan=2)
        self.etiquetaListaProductos.grid(row=7, column=0, columnspan=2)
        self.etiquetaTotal.grid(row=8,column=0, columnspan=2)
        self.etiquetaEfectivo.grid(row=9, column=0, columnspan=2)
        self.etiquetaCambio.grid(row=12, columnspan=2)
