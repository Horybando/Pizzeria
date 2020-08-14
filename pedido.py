import datetime

class Pedido:
    def __init__(self, id_pedido, cliente, fecha_hora, hora_salida, detalle_pedido = [], total = 0):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.fecha_hora = fecha_hora
        self.hora_salida = hora_salida
        self.detalle_pedido = detalle_pedido
        self.total = total

    def calcular_precio_total(self):

    def pedidos_por_periodo(self, fecha_ini, fecha_fin):

    def agregar_detalle_pedido(self):


