from VentanaProductos import VentanaProductos
from VentanaFactura import VentanaFactura

class Main:
    def __init__(self):
        factura = VentanaFactura()
        productos = VentanaProductos()
        factura.crearWidgetsVentanaFactura()
        productos.crearWidgetsVentanaProductos()
        factura.crearVentanaFactura()
        productos.crearVentanaProductos()
        factura.ventanaFactura.mainloop()
        productos.ventanaProducto.mainloop()

main = Main()
