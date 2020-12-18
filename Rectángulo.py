class Rectangulo:
    def __init__(self, altura, ancho):
        self.altura = altura
        self.ancho = ancho 
    
    def calcularArea(self):
        resultado = self.ancho * self.altura
        return resultado
    
    def calcularPerimetro(self):
        resultado = self.altura + self.altura + self.ancho + self.ancho
        return resultado