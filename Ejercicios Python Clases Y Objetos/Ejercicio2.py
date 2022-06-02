"""Ejemplo extraido desde el libro Python para todos de Raul Gonzalez Duque"""


class Coche:
    def __init__(self, gasolina):
        self.gasolina = gasolina
        print ("Tenemos", gasolina, "litros")

    def arrancar(self):
        if self.gasolina > 0:
            print ("Arranca")
        else:
            print ("No arranca")

    def conducir(self):
        if self.gasolina > 0:
            self.gasolina -= 1
            print ("Quedan"), self.gasolina, "litros"
        else:
            print ("No se mueve")


mi_coche = Coche(4)
mi_coche.arrancar()
mi_coche.conducir()
mi_coche.conducir()
mi_coche.conducir()
mi_coche.conducir()
mi_coche.arrancar()
print (mi_coche.gasolina)
