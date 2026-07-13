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
import sys
from PySide6.QtWidgets import (
QApplication,
    QMainWindow,
    QMessageBox
)
from GUI.transporte import Ui_MainWindow
from clases.pasajero import Pasajero
from clases.viaje_privado import ViajePrivado
from clases.viaje_urbano import ViajeUrbano
from conexion import conectar_bd
from PySide6.QtCore import QDate
#----------------------------------------------------------
# Inicialización de la ventana
#----------------------------------------------------------
class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #Botón mostrar
        self.ui.btnmostrar.clicked.connect(
            self.mostrar_servicio
        )
        # Mostrar Viaje Privado al iniciar
        self.ui.swviajes.setCurrentIndex(0)
        # Eventos
        self.ui.cmbtipoviaje.currentIndexChanged.connect(
            self.cambiar_tipo_viaje
        )
        #Botón limpiar
        self.ui.btnlimpiar.clicked.connect(
            self.limpiar_campos
        )
        #Botón registrar
        self.ui.btnregistrar.clicked.connect(
            self.registrar_servicio
        )
        #Botón actualizar
        self.ui.btnactualizar.clicked.connect(
            self.actualizar_servicio
        )
        #Botón eliminar
        self.ui.btneliminar.clicked.connect(
            self.eliminar_servicio
        )
        # Estado inicial del resumen
        self.ui.lbltarifa.setText("$0.00")
        self.ui.lblviaje.setText("Sin seleccionar")
        self.ui.lbltexto2.setText("Esperando registro...")
        #Generar codigo automaticamente
        self.generar_codigo()
    # -------------------------------------------------
    # Cambia la interfaz según el tipo de viaje seleccionado
    def cambiar_tipo_viaje(self):

        indice = self.ui.cmbtipoviaje.currentIndex()

        self.ui.swviajes.setCurrentIndex(indice)
    # -------------------------------------------------
    # Genera automaticamente el codigo del servicio
    def generar_codigo(self):
        try:
            conexion = conectar_bd()
            cursor = conexion.cursor()
            cursor.execute("SELECT MAX(Idservicio) FROM Servicios")
            ultimo = cursor.fetchone()[0]
            conexion.close()
            if ultimo is None:
                nuevo_codigo = "TR001"
            else:
                nuevo_codigo = f"TR{ultimo + 1:03d}"
            self.ui.txtcodigo.setText(nuevo_codigo)
        except Exception:
            # Inicia la numeración desde TR001
            self.ui.txtcodigo.setText("TR001")
    #--------------------------------------------------------------------------
    # Limpia todos los campos de la interfaz
    def limpiar_campos(self):
        self.ui.txtcedula.clear()
        self.ui.txtnombre.clear()
        self.ui.txtapellido.clear()
        self.ui.txtemail.clear()
        self.ui.dsbdistancia.setValue(0)
        self.ui.dsbcosto.setValue(0)
        self.ui.sbestaciones.setValue(0)
        self.ui.cmbtipoviaje.setCurrentIndex(0)
        self.ui.lbltarifa.setText("$0.00")
        self.ui.lblviaje.setText("Sin seleccionar")
        self.ui.lbltexto2.setText("Esperando registro...")
        self.generar_codigo()
    # ------------------------------------------------------------------------
    # Registra un nuevo servicio en la base de datos
    def registrar_servicio(self):
        try:
                # Datos pasajer
                cedula = self.ui.txtcedula.text()
                nombre = self.ui.txtnombre.text()
                apellido = self.ui.txtapellido.text()
                email = self.ui.txtemail.text()
                pasajero = Pasajero(
                    cedula,
                    nombre,
                    apellido,
                    email
                )
                # Datos servicio
                codigo = self.ui.txtcodigo.text()
                fecha = self.ui.dtfecha.date().toString(
                    "yyyy-MM-dd"
                )
                nombre_completo = (
                    f"{pasajero.nombre} "
                    f"{pasajero.apellido}"
                )
                # Viaje privado
                if self.ui.cmbtipoviaje.currentIndex() == 0:
                    distancia = self.ui.dsbdistancia.value()
                    costo = self.ui.dsbcosto.value()
                    servicio = ViajePrivado(
                        codigo,
                        nombre_completo,
                        fecha,
                        distancia,
                        costo
                    )
                    tipo = "Privado"
                # Viaje urbano
                else:
                    estaciones = self.ui.sbestaciones.value()
                    servicio = ViajeUrbano(
                        codigo,
                        nombre_completo,
                        fecha,
                        estaciones
                    )
                    tipo = "Urbano"
                tarifa = servicio.calcular_tarifa()
                self.ui.lbltarifa.setText(f"${tarifa:.2f}")
                self.ui.lblviaje.setText(tipo)
                self.ui.lbltexto2.setText("✔ Servicio registrado correctamente")
                # Guardar en SQL
                conexion = conectar_bd()
                cursor = conexion.cursor()
                if tipo == "Privado":
                    distancia_bd = distancia
                    costo_bd = costo
                    estaciones_bd = None
                else:
                    distancia_bd = None
                    costo_bd = None
                    estaciones_bd = estaciones
                cursor.execute("""
                INSERT INTO Servicios
                (
                codigo,
                cedula,
                nombre,
                apellido,
                email,
                tipo,
                fecha,
                distancia,
                costo_km,
                estaciones,
                tarifa
                )

                VALUES
                (?,?,?,?,?,?,?,?,?,?,?)
                """,
                (
                        codigo,
                        cedula,
                        nombre,
                        apellido,
                        email,
                        tipo,
                        fecha,
                        distancia_bd,
                        costo_bd,
                        estaciones_bd,
                        tarifa
                ))
                conexion.commit()
                conexion.close()
                QMessageBox.information(
                    self,
                    "Éxito",
                    "El servicio fue registrado correctamente"
                )
                self.limpiar_campos()
        except Exception as error:
            QMessageBox.critical(
                self,
                "Error inesperado",
                str(error)
            )
    #----------------------------------------------------------------------------
    # Consulta un servicio mediante su código
    def mostrar_servicio(self):
        codigo = self.ui.txtcodigo.text().strip()
        if codigo == "":
            QMessageBox.warning(
                self,
                "Código vacío",
                "Ingrese un código para buscar el servicio."
            )
            return
        if not codigo.startswith("TR"):
            QMessageBox.warning(
                self,
                "Código incorrecto",
                "Ingrese un código válido. Ejemplo: TR001."
            )
            return
        try:
            conexion = conectar_bd()
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT
                    cedula,
                    nombre,
                    apellido,
                    email,
                    tipo,
                    fecha,
                    distancia,
                    costo_km,
                    estaciones,
                    tarifa
                FROM Servicios
                WHERE codigo = ?
            """, (codigo,))
            registro = cursor.fetchone()
            conexion.close()
            if registro:
                cedula, nombre, apellido, email, tipo, fecha, distancia, costo, estaciones, tarifa = registro
                self.ui.txtcedula.setText(str(cedula))
                self.ui.txtnombre.setText(nombre)
                self.ui.txtapellido.setText(apellido)
                self.ui.txtemail.setText(email)
                fecha_qt = QDate.fromString(fecha, "yyyy-MM-dd")
                self.ui.dtfecha.setDate(fecha_qt)
                self.ui.lbltarifa.setText(f"${tarifa:.2f}")
                self.ui.lblviaje.setText(tipo)
                self.ui.lbltexto2.setText("Servicio encontrado.")
                if tipo == "Privado":
                    self.ui.cmbtipoviaje.setCurrentIndex(0)
                    self.ui.dsbdistancia.setValue(float(distancia))
                    self.ui.dsbcosto.setValue(float(costo))
                    # Limpiar datos del viaje urbano
                    self.ui.sbestaciones.setValue(0)
                else:
                    self.ui.cmbtipoviaje.setCurrentIndex(1)
                    self.ui.sbestaciones.setValue(int(estaciones))
                    # Limpiar datos del viaje privado
                    self.ui.dsbdistancia.setValue(0)
                    self.ui.dsbcosto.setValue(0)
                QMessageBox.information(
                    self,
                    "Consulta",
                    "Servicio encontrado correctamente."
                )
            else:
                QMessageBox.information(
                    self,
                    "Sin resultados",
                    "No existe un servicio con ese código."
                )
        except Exception as error:
            QMessageBox.critical(
                self,
                "Error",
                str(error)
            )
    # -------------------------------------------------------------------------------
    # Actualiza un servicio existente
    def actualizar_servicio(self):
        try:
            codigo = self.ui.txtcodigo.text().strip()
            if codigo == "":
                QMessageBox.warning(
                    self,
                    "Código",
                    "No existe un código para actualizar."
                )
                return
            cedula = self.ui.txtcedula.text()
            nombre = self.ui.txtnombre.text()
            apellido = self.ui.txtapellido.text()
            email = self.ui.txtemail.text()
            fecha = self.ui.dtfecha.date().toString(
                "yyyy-MM-dd"
            )
            if self.ui.cmbtipoviaje.currentIndex() == 0:
                tipo = "Privado"
                distancia = self.ui.dsbdistancia.value()
                costo = self.ui.dsbcosto.value()
                estaciones = 0
                tarifa = distancia * costo
            else:
                tipo = "Urbano"
                estaciones = self.ui.sbestaciones.value()
                distancia = 0
                costo = 0
                tarifa = estaciones * 0.35
            conexion = conectar_bd()
            cursor = conexion.cursor()
            cursor.execute("""
            UPDATE Servicios
            SET
                cedula=?,
                nombre=?,
                apellido=?,
                email=?,
                tipo=?,
                fecha=?,
                distancia=?,
                costo_km=?,
                estaciones=?,
                tarifa=?
            WHERE codigo=?
            """,
            (
                cedula,
                nombre,
                apellido,
                email,
                tipo,
                fecha,
                distancia,
                costo,
                estaciones,
                tarifa,
                codigo
            ))
            conexion.commit()
            conexion.close()
            self.ui.lbltarifa.setText(f"${tarifa:.2f}")
            self.ui.lblviaje.setText(tipo)
            self.ui.lbltexto2.setText("Servicio actualizado.")
            QMessageBox.information(
                self,
                "Actualizado",
                "Servicio actualizado correctamente."
            )
        except Exception as error:
            QMessageBox.critical(
                self,
                "Error",
                str(error)
            )
    # ---------------------------------------------------------------
    # Elimina un servicio en la base de datos
    def eliminar_servicio(self):
        codigo = self.ui.txtcodigo.text().strip()
        if codigo == "":
            QMessageBox.warning(
                self,
                "Código",
                "Ingrese un código para eliminar."
            )
            return
        respuesta = QMessageBox.question(
            self,
            "Confirmar",
            f"¿Está seguro de eliminar el servicio {codigo}?",
            QMessageBox.Yes | QMessageBox.No
        )
        if respuesta == QMessageBox.No:
            return
        try:
            conexion = conectar_bd()
            cursor = conexion.cursor()
            cursor.execute(
                "DELETE FROM Servicios WHERE codigo = ?",
                (codigo,)
            )
            conexion.commit()
            filas = cursor.rowcount
            conexion.close()
            if filas > 0:
                QMessageBox.information(
                    self,
                    "Eliminado",
                    "Servicio eliminado correctamente."
                )
                self.limpiar_campos()
            else:
                QMessageBox.information(
                    self,
                    "Sin resultados",
                    "No existe un servicio con ese código."
                )
        except Exception as error:
            QMessageBox.critical(
                self,
                "Error",
                str(error)
            )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())