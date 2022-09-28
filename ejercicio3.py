
class vehiculo():
    def __init__(self, marca, ruedas, color, enMarcha):
        self.marca = marca
        self.ruedas = ruedas
        self.color = color
        self.enMarcha = enMarcha

    def arrancar(self):
        self.enMarcha = True 
         
    def TipoVehiculo(self):
        if self.ruedas == 4:
            print("Es un Auto")
        if self.ruedas == 2:
            print("Es una Moto")
        else:
            print("Tipo de Vehiuclo no identificado")

    def mostrar(self):
        print(self.marca)
        print(self.ruedas)
        print(self.enMarcha)
        print(self.color)


carro1 = vehiculo("Volkswagen", 4, "blanco", False)

carro1.arrancar()
carro1.TipoVehiculo()
carro1.mostrar()


# Comisión: 1 Tup 1
# Grupo: 3
# Integrantes: Leandro Flores, Lisandro Adagio, Tomas Garcia
# -Legajo: 50973
# -Legajo: 50651
# -Legajo: 50592