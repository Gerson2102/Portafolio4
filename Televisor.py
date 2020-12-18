class Televisor:
    canal_actual = 0
    volumen_actual = 0
    def __init__(self, marca):
        self.marca = marca

    def mostrar(self):
        return self.marca

    def tipo(self):
        return "Televisor"

    def canal_up(self):
        Televisor.canal_actual += 1
        return "El canal actual es el: ", Televisor.canal_actual

    def canal_down(self):
        Televisor.canal_actual -= 1
        return "El canal actual es el: ", Televisor.canal_actual

    def volumen_up(self):
        Televisor.volumen_actual += 1
        return "El volumen actual es: ", Televisor.volumen_actual

    def volumen_down(self):
        Televisor.volumen_actual -= 1
        return "El volumen actual es: ", Televisor.volumen_actual

    def establecer_canal(self, canal):
        if isinstance(canal, int) and (canal >= 0):
            if canal <= 999:
                Televisor.canal_actual = canal
                return "El canal actual es el: ", Televisor.canal_actual
            else:
                return "Error, este televisor posee un rango máximo de 999 canales"
        else:
            return "Error, el elemento ingresado debe ser un número positivo"