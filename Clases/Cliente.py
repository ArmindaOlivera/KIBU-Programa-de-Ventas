class Cliente:
    def __init__(self, nombre, nit):
        self.nombre = nombre
        self.nit = nit

    def guardarCliente(self):
        print("Guardar Cliente")