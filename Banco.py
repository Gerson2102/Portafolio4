class Cuenta:
    total_cuentas = 0
    def __init__(self, saldo_inicial):
        Cuenta.total_cuentas += 1
        self.saldo_inicial = saldo_inicial
        self.monto_total_debitos = 0
        self.monto_total_creditos = 0
        self.saldo_actual = saldo_inicial

    def mostrar_total_cuentas(self):
        print("Total de cuentas en el sistema: ", Cuenta.total_cuentas)

    def cuenta(self, saldo_inicial):
        print("El saldo inicial de la cuenta es: ", self.saldo_inicial)
#Debito = sacar
#Credito = depositar
    def depositar(self, monto):
        if monto >= 0:
            self.monto_total_creditos += monto
            self.saldo_actual += monto
        else:
            return "Error, el monto ingresado no puede ser una cantidad negativa"

    def retirar(self, monto):
        if monto > 0 and monto <= self.saldo_actual:
            self.monto_total_debitos -= monto
            self.saldo_actual -= monto
        else:
            return "Error, usted no posee esa cantidad en su cuenta"

    def determinar_estado_cuenta(self):
        print("Su saldo actual es: ", self.saldo_actual)
        print("Su monto total de debitos: ", self.monto_total_debitos)
        print("Su monto total de creditos: ", self.monto_total_creditos)
        print("Su saldo inicial es: ", self.saldo_inicial)