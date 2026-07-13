# ============================================================
# INTEGRANTES
# ============================================================
# - ALVAREZ YAGUAL KAREN
# - MACIAS VILLAMAR MARCOS
# - PINO LOOR EMILY
# - RODRIGUEZ CRESPIN DIDDIER
# - VASQUEZ CHILA VALERIA
# ============================================================
#CLASE HIJA: ViajePrivado

from clases.servicio_transporte import ServicioTransporte
class ViajePrivado(ServicioTransporte):
    """
    Clase que representa un viaje privado
    Hereda de ServicioTransporte y aplica Polimorfismo
    """

    def __init__(
            self,
            codigo:str,
            nombre_pasajero:str,
            fecha:str,
            distancia_km:float,
            costo_km:float
    ):
        """
        Constructor de ViajePrivado
        """

        super().__init__(codigo,
                         nombre_pasajero,
                         fecha)

        self.distancia_km = distancia_km
        self.costo_km = costo_km

    #ENCAPSULAMIENTOS
    @property
    def distancia_km(self):
        return self.__distancia_km

    @distancia_km.setter
    def distancia_km(self,nueva_distancia):
        if nueva_distancia <= 0:
            raise ValueError(
                "La distancia debe ser mayor a 0"
            )
        self.__distancia_km = nueva_distancia
    #-----------------------------------------------------------------
    @property
    def costo_km(self):
        return self.__costo_km

    @costo_km.setter
    def costo_km(self, nuevo_costo):
        if nuevo_costo < 0:
            raise ValueError(
                "El costo no puede ser negativo"
            )
        self.__costo_km=nuevo_costo

    #POLIMORFISMO
    def calcular_tarifa(self):
        return self.__distancia_km * self.__costo_km

    def mostrar_datos(self):
        print("\n ------VIAJE PRIVADO------")
        print(super().__str__())
        print(f"Distancia: {self.__distancia_km} km")
        print(f"Costo por km: ${self.__costo_km}")
        print(f"Tarifa: ${self.calcular_tarifa(): .2f}")

    #STR
    def __str__(self):
        return (
            f"{super().__str__()} | "
            f"Distancia: {self.__distancia_km} km"
        )