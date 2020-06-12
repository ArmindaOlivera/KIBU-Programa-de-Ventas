import tkinter
import tkinter.ttk

fuenteTitulo="Helvetica 20"
fuenteEtiqueta="Helvetica 15"
fuenteBoton="Helvetica 10"
fuenteTexto="Helvetica 20"

ventanaFactura=tkinter.Tk()
ventanaFactura.geometry("700x600")
ventanaFactura.title("KIBU Programa de Ventas")

class Producto:
    def __init__(self,nombre, precio):
        self.nombre = nombre
        self.precio = precio

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

etiquetaTitulo=tkinter.Label(ventanaFactura, text="KIBU Programa de Ventas", bg="green", font=fuenteTitulo)# titulo del programa / bg se ocupa para color
etiquetaCreditos=tkinter.Label(ventanaFactura, text="Arminda Olivera, 2020")
etiquetaNombre=tkinter.Label(ventanaFactura, text="Nombre", font=fuenteEtiqueta)
etiquetaNit=tkinter.Label(ventanaFactura, text="NIT", font=fuenteEtiqueta)
etiquetaEfectivo= tkinter.Label(ventanaFactura, text="Efectivo", font=fuenteEtiqueta)

separadorVertical = tkinter.ttk.Separator(ventanaFactura, orient="vertical")

botonImprimirFactura=tkinter.Button(ventanaFactura, text="Imprimir Factura", padx=15, pady=10, font=fuenteBoton, borderwidth=5) # , command=
listaBotonesProducto = []
for producto in listaProductos:
    listaBotonesProducto.append(tkinter.Button(ventanaFactura, text=producto.nombre, width=10, height=5, font=fuenteBoton,borderwidth=5)) # , command=

fila = 1
columna = 3
for botonProducto in listaBotonesProducto:
    botonProducto.grid(row=fila, column=columna)
    if columna < 5:
        columna+=1
    else:
        fila+=1
        columna = 3

cajaTextoNombre=tkinter.Entry(ventanaFactura,font=fuenteTexto)
cajaTextoNit=tkinter.Entry(ventanaFactura,font=fuenteTexto)
cajaTextoEfectivo=tkinter.Entry(ventanaFactura,font=fuenteTexto)

etiquetaTitulo.grid(row=0, column=0, columnspan=5)
etiquetaNombre.grid(row=1, column=0)
cajaTextoNombre.grid(row=1, column=1)
etiquetaNit.grid(row=2, column=0)
cajaTextoNit.grid(row=2, column=1)
etiquetaEfectivo.grid(row=3, column=0)
cajaTextoEfectivo.grid(row=3, column=1)
botonImprimirFactura.grid(row=4,column=0, columnspan=2)
separadorVertical.grid(column=2, row=1, rowspan=10, sticky='ns')

#photo=PhotoImage(file="Y:\\Proyectos\\KIBU-Programa-de-Ventas\\Prueba-Concepto\\Imagenes\\pan2.png")
#botonProducto=tkinter.Button(ventanaFactura, text="Pan", image=photo, padx=25, pady=25,font=fuenteBoton) # , command=
#botonProducto.grid(row=0, column=2)

ventanaFactura.mainloop()

#etiquetaFactura["text"]=factura
#nombre=textoNombre.get()
#def imprimirFactura ():
# titulo del programa / bg se ocupa para color

