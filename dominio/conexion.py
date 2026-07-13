# PROYECTO SEGUNDO PARCIAL - SISTEMA GESTIÓN DE TRANSPORTE
# ASIGNATURA: PROGRAMACIÓN ORIENTADA A OBJETOS
# JORNADA : MATUTINA
# GRUPO 5
# ============================================================
# INTEGRANTES
# ============================================================
# - ALVAREZ YAGUAL KAREN
# - MACIAS VILLAMAR MARCOS
# - PINO LOOR EMILY
# - RODRIGUEZ CRESPIN DIDDIER
# - VASQUEZ CHILA VALERIA
# ============================================================
# Conexión con la base de datos
import pyodbc
# Establece la conexión con SQL
def conectar_bd():
    conexion = pyodbc.connect(
        "DRIVER={SQL Server};"
        "SERVER=.\\SQLPINOEMILY;"
        "DATABASE=ServicioTransporte;"
        "Trusted_Connection=yes;"
    )
    return conexion