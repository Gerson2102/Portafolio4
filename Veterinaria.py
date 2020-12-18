class Veterinaria:
    contador_perros = 0
    contador_gatos = 0
    contador_aves = 0
    def __init__(self, tipo, peso):
        self.tipo = tipo
        self.peso = peso
        if self.tipo == 'Perro':
            Veterinaria.contador_perros += 1
        elif self.tipo == "Gato":
            Veterinaria.contador_gatos += 1
        elif self.tipo == 'Ave':
            Veterinaria.contador_aves += 1
    def verTotalPerros(self):
        print("Cantidad total de perros: ", Veterinaria.contador_perros)

    def verTotalGatos(self):
        print("Cantidad total de gatos: ", Veterinaria.contador_gatos)

    def verTotalAves(self):
        print("Cantidad total de avaes: ", Veterinaria.contador_aves)

    def mostrarDatos(self):
        print("Datos del sistema: \n")
        print('Tipo: ', self.tipo)
        print('Peso: ', self.peso)
        