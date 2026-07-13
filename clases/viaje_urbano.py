# ============================================================
# INTEGRANTES
# ============================================================
# - ALVAREZ YAGUAL KAREN
# - MACIAS VILLAMAR MARCOS
# - PINO LOOR EMILY
# - RODRIGUEZ CRESPIN DIDDIER
# - VASQUEZ CHILA VALERIA
# ============================================================
#CLASE HIJA: ViajeUrbano

from clases.servicio_transporte import ServicioTransporte
class ViajeUrbano(ServicioTransporte):
    """
    Clase que representa un viaje urbano.
    Hereda de ServicioTransporte y aplica Polimorfismo
    """
    def __init__(
            self,
            codigo: str,
            nombre_pasajero: str,
            fecha:str,
            cantidad_estaciones:int
    ):
        """
        Constructor de Viaje Urbano
        """
        super().__init__(codigo,
                         nombre_pasajero,
                         fecha)
        self.cantidad_estaciones=cantidad_estaciones

    #ENCAPSULAMIENTO
    @property
    def cantidad_estaciones(self):
        return self.__cantidad_estaciones

    @cantidad_estaciones.setter
    def cantidad_estaciones(self, nueva_cantidad):
        if nueva_cantidad<=0:
            raise ValueError(
                "La cantidad de estaciones debe ser mayor a 0"
            )
        self.__cantidad_estaciones = nueva_cantidad

    #POLIMORFISMO
    def calcular_tarifa(self):
        #Tarifa fija para viaje urbano
        return 0.50

    def mostrar_datos(self):
        print("\n ------VIAJE URBANO------")
        print(super().__str__())
        print(
            f"Cantidad de estaciones: "
            f"{self.cantidad_estaciones}"
        )
        print (f"Tarifa: ${self.calcular_tarifa():.2f}")

    #STR
    def __str__(self):
        return (
            f"{super().__str__()} | "
            f"Estaciones: {self.cantidad_estaciones}"
        )
