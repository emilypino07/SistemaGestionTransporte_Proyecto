# ============================================================
# INTEGRANTES
# ============================================================
# - ALVAREZ YAGUAL KAREN
# - MACIAS VILLAMAR MARCOS
# - PINO LOOR EMILY
# - RODRIGUEZ CRESPIN DIDDIER
# - VASQUEZ CHILA VALERIA
# ============================================================
#CLASE GESTOR DE TRANSPORTE

class GestorTransporte:
    """
       Clase encargada de gestionar los servicios
       de transporte.
       """

    # METODO POLIMORFICO 1
    def mostrar_servicios(self, lista_servicios):
        print("\n" + "=" * 40)
        print("      DATOS DE SERVICIOS")
        print("=" * 40)

        if not lista_servicios:
            print("No hay servicios registrados.")
            return

        for servicio in lista_servicios:
            servicio.mostrar_datos()


    # METODO POLIMORFICO 2
    def calcular_total_tarifas(self,
                               lista_servicios):

        if not lista_servicios:
            print("No hay servicios registrados.")
            return 0


        total = 0
        for servicio in lista_servicios:
            total += servicio.calcular_tarifa()
        return total

    #METODO PARA MOSTRAR DATOS
    def mostrar_total(self, lista_servicios):
        total = self.calcular_total_tarifas(lista_servicios)
        print(f"\nTotal de tarifas: ${total:.2f}")