class pizza:
    mediana = 0.1
    grande = 0.15
    piedra = 0.05
    molde = 0.03
    parrilla = 0.04

    def __init__(self, nombre, ingredientes, tipo, precio_base):
        self.nombre = nombre
        self.ingrediente = ingredientes
        self.tipo = tipo
        self.precio_base = precio_base

    def calcular_precio(self):
