class Cliente:
    def __init__(self, nombre, nit):
        self.nombre = nombre
        self.nit = nit

    def guardarCliente(self):
        print("Guardar Cliente")


class Producto:
    def __init__(self,nombre, precio):
        self.nombre = nombre
        self.precio = precio
        print(nombre, precio)


class Venta:
    def __init__(self, nombre, nit):
        self.cliente = Cliente(nombre, nit)
        self.productos = []
        self.efectivo = 0
        self.totalCompra = 0
        self.cambio = 0

    def registrarVenta (self, producto, cantidad):
        self.productos.append((producto, cantidad))
        self.totalCompra += producto.precio * cantidad

    def guardarVenta (self):
        print("Guardar Venta")

    def aprobarVenta (self, efectivo):
        self.cliente.guardarCliente()
        self.guardarVenta()
        self.efectivo = efectivo
        self.cambio = efectivo - self.totalCompra

    def imprimirFactura (self):
        print("Nombre: ", self.cliente.nombre)
        print("NIT: ", self.cliente.nit)
        print("Cantidad\tProducto\tPrecio\t\tTotal")
        for producto in self.productos:
            print(str(producto[1]) + "\t\t" + producto[0].nombre + "\t\t" +(str(producto[0].precio)) + "\t\t" + str(producto[0].precio * producto[1]))
        print("Total compra",self.totalCompra)
        print("Efectivo",self.efectivo)
        print("Cambio:", self.cambio)
        
        
pan = Producto("pan", 0.50)
leche = Producto("leche", 6.50)
huevo = Producto("huevo", 0.50) 

venta1 = Venta("Erick", 374745)
venta1.registrarVenta(pan, 5)
venta1.registrarVenta(huevo, 12)
venta1.registrarVenta(leche, 1)
venta1.aprobarVenta(100)
venta1.imprimirFactura()























