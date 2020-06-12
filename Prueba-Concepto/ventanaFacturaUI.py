import tkinter
from tkinter import PhotoImage

fuenteTitulo="Helvetica 20"
fuenteEtiqueta="Helvetica 15"
fuenteBoton="Helvetica 15"
fuenteTexto="Helvetica 20"

ventanaFactura=tkinter.Tk()
ventanaFactura.geometry("322x600")
ventanaFactura.title("KIBU Programa de Ventas")

#Lado Izquierdo(Factura)
etiquetaTitulo=tkinter.Label(ventanaFactura, text="KIBU Programa de Ventas", bg="green", font=fuenteTitulo)# titulo del programa / bg se ocupa para color
etiquetaCreditos=tkinter.Label(ventanaFactura, text="Arminda Olivera, 2020")
etiquetaNombre=tkinter.Label(ventanaFactura, text="Nombre: Sara Bolivar", font=fuenteEtiqueta)
etiquetaNit=tkinter.Label(ventanaFactura, text="NIT: 25882632", font=fuenteEtiqueta)
etiquetaTotal=tkinter.Label(ventanaFactura, text="Total: 45 Bolivianos", font=fuenteEtiqueta)
etiquetaEfectivo= tkinter.Label(ventanaFactura, text="Efectivo: 50 Bolivianos", font=fuenteEtiqueta)
etiquetaCambio=tkinter.Label(ventanaFactura, text="Cambio: 5 Bolivianos", font=fuenteEtiqueta)


etiquetaTituloListaProductos=tkinter.Label(ventanaFactura, text="Lista de Productos", bg="green", font=fuenteEtiqueta)
etiquetaDetalleListaProductos=tkinter.Label(ventanaFactura, text="Cantidad \t Producto\t Precio \tTotal", bg="gray", font=fuenteEtiqueta)
etiquetaListaProductos=tkinter.Label(ventanaFactura, text="pan\t5\t0.5\t2.5", font=fuenteEtiqueta)


SeparadorHorizontal1=tkinter.Label(ventanaFactura, text=" ", font=fuenteEtiqueta)
SeparadorHorizontal2=tkinter.Label(ventanaFactura, text=" ", font=fuenteEtiqueta)

cajaTextoNombre=tkinter.Entry(ventanaFactura,font=fuenteTexto)
cajaTextoNit=tkinter.Entry(ventanaFactura,font=fuenteTexto)
cajaTextoEfectivo=tkinter.Entry(ventanaFactura,font=fuenteTexto)

etiquetaTitulo.grid(row=0, column=0, columnspan=2) # fill es para expandir en el eje x, si lleva fill debe tener true
SeparadorHorizontal1.grid(row=1, columnspan=2)
etiquetaNombre.grid(row=2, column=0)
etiquetaNit.grid(row=3, column=0)
SeparadorHorizontal2.grid(row=4, column=0, columnspan=2)
etiquetaTituloListaProductos.grid(row=5, column=0, columnspan=2)
etiquetaDetalleListaProductos.grid(row=6, column=0, columnspan=2)
etiquetaListaProductos.grid(row=7, column=0, columnspan=2)
etiquetaTotal.grid(row=8,column=0, columnspan=2)
etiquetaEfectivo.grid(row=9, column=0, columnspan=2)
etiquetaCambio.grid(row=12, columnspan=2)

#Lado Derecho (Productos)
#photo=PhotoImage(file="Y:\\Proyectos\\KIBU-Programa-de-Ventas\\Prueba-Concepto\\Imagenes\\pan2.png")
#botonProducto=tkinter.Button(ventanaFactura, text="Pan", image=photo, padx=25, pady=25,font=fuenteBoton) # , command=
#botonProducto.grid(row=0, column=2)

ventanaFactura.mainloop()

#etiquetaFactura["text"]=factura
#nombre=textoNombre.get()
#def imprimirFactura ():

