class Facturador:

    def __init__ (self):
        self.numFactura = 0
        self.fecha = ''
        self.cliente = ''
        self.listaItem = []
        self.total = 0

    def crearFactura (self, numFactura, fecha, cliente):
        self.numFactura = numFactura
        self.fecha = fecha
        self.cliente = cliente
        self.listaItem = []
        self.total = 0

    def agregarItem(self, nomProd, precioUnitario, cantidad):
        self.listaItem += [[nomProd, precioUnitario, cantidad]]

    def verTotal(self):
        subtotal = 0
        impuesto = 0
        mensaje = 'Subtotal: '

        for x in self.listaItem:
            print(self.listaItem)
            subtotal += x[1] * x[2]

        impuesto = int(subtotal * 0.13)
        self.total = subtotal + impuesto

        mensaje += str(subtotal) + ', Impuesto: ' + str(impuesto) + ', Total: ' + str(self.total)
        return mensaje
        
    def cerrarFactura(self):
        return 'Total pagado es de ' + str(self.total) + ' colones'

facturador = Facturador()
#print(facturador.verTotal())


