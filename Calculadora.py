class Calculadora:
    def __init__(self, operador_1, operador_2):
        self.operador_1 = operador_1
        self.operador_2 = operador_2

    def sumar(self):
        return self.operador_1 + self.operador_2
    
    def restar(self):
        return self.operador_1 - self.operador_2

    def multiplicar(self):
        return self.operador_1 * self.operador_2

    def dividir(self):
        return self.operador_1 / self.operador_2

    def potencia(self):
        return self.operador_1 ** self.operador_2
