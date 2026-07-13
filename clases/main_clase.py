# ============================================================
# INTEGRANTES
# ============================================================
# - ALVAREZ YAGUAL KAREN
# - MACIAS VILLAMAR MARCOS
# - PINO LOOR EMILY
# - RODRIGUEZ CRESPIN DIDDIER
# - VASQUEZ CHILA VALERIA
# ============================================================
from viaje_urbano import ViajeUrbano
from viaje_privado import ViajePrivado
from clases.gestor_transporte import GestorTransporte
from pasajero import Pasajero
# ==================================================
# PROGRAMA PRINCIPAL
# ==================================================

try:
    # CREACION DE OBJETOS
    pasajero1 = Pasajero(
        "0102030405",
        "Carlos Perez"
    )

    pasajero2 = Pasajero(
        "0911223344",
        "Maria Lopez"
    )
    pasajero3= Pasajero(
        "0712345678",
        "Juan Torres"
    )
    pasajero4 = Pasajero(
        "0856789012",
        "Ana Ruiz"
    )
    #CREACION DE OBJETOS SERVICIO
    urbano1 = ViajeUrbano(
        "U001",
        pasajero1.nombre,
        "16/05/2026",
        5
    )

    urbano2 = ViajeUrbano(
        "U002",
        pasajero2.nombre,
        "17/05/2026",
        3
    )
    privado1 = ViajePrivado(
        "P001",
        pasajero3.nombre,
        "18/05/2026",
        10,
        2
    )

    privado2 = ViajePrivado(
        "P002",
        pasajero4.nombre,
        "19/05/2026",
        20,
        1.5
    )

    # LISTA DE OBJETOS DE LA SUPERCLASE
    lista_servicios = [
        urbano1,
        urbano2,
        privado1,
        privado2
    ]

    # CREACION DEL GESTOR
    gestor = GestorTransporte()

    # MOSTRAR PASAJEROS
    print("\n===== PASAJEROS =====")
    pasajero1.mostrar_datos()
    pasajero2.mostrar_datos()
    pasajero3.mostrar_datos()
    pasajero4.mostrar_datos()

    # METODOS POLIMORFICOS
    gestor.mostrar_servicios(
        lista_servicios
    )

    total = gestor.calcular_total_tarifas(
        lista_servicios
    )

    print("\n" + "=" * 35)
    print(f"TOTAL DE TARIFAS: ${total:.2f}")
    print("=" * 35)

    print("\n===== OBJETOS =====")

    for servicio in lista_servicios:
        print(servicio)

    #MANEJO DE ERRORES
except ValueError as error:
    print(f"ERROR DE VALIDACION: {error}")
except Exception as error:
    print(f"ERROR INESPERADO: {error}")