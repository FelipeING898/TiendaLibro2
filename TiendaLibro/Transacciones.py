im

class Transacciones:
    TIPO = {
        1:'venta',
        2:'abastecimiento'
    }

    def __init__(self, tipo, cantidad, fecha):
        
        self.__tipo = self.TIPO['1'] if tipo == 1 else self.TIPO['2']
        self.__cantidad = cantidad
        self.__fecha = fecha

    def getTipo(self):
        return self.__tipo
    
    def getCantidad(self):
        return self.__cantidad
    
    def getFecha(fecha):
        return self.__fecha