# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'transporte.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDoubleSpinBox,
    QFormLayout, QFrame, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpinBox, QStackedWidget,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(786, 568)
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblregistro = QLabel(self.centralwidget)
        self.lblregistro.setObjectName(u"lblregistro")
        self.lblregistro.setGeometry(QRect(170, 0, 471, 41))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setItalic(False)
        self.lblregistro.setFont(font1)
        self.gbpasajero = QGroupBox(self.centralwidget)
        self.gbpasajero.setObjectName(u"gbpasajero")
        self.gbpasajero.setGeometry(QRect(20, 50, 331, 301))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.gbpasajero.setFont(font2)
        self.gbpasajero.setStyleSheet(u"QGroupBox{\n"
"    border: 2px solid #BFD7EA;\n"
"    border-radius:10px;\n"
"    margin-top:12px;\n"
"    font-weight:bold;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"    subcontrol-origin: margin;\n"
"    left:10px;\n"
"    padding:0 5px;\n"
"}")
        self.formLayout_2 = QFormLayout(self.gbpasajero)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lblnombre = QLabel(self.gbpasajero)
        self.lblnombre.setObjectName(u"lblnombre")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.lblnombre.setFont(font3)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.lblnombre)

        self.txtnombre = QLineEdit(self.gbpasajero)
        self.txtnombre.setObjectName(u"txtnombre")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(False)
        self.txtnombre.setFont(font4)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtnombre)

        self.lblapellido = QLabel(self.gbpasajero)
        self.lblapellido.setObjectName(u"lblapellido")
        self.lblapellido.setFont(font3)

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lblapellido)

        self.txtapellido = QLineEdit(self.gbpasajero)
        self.txtapellido.setObjectName(u"txtapellido")
        self.txtapellido.setFont(font4)

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.FieldRole, self.txtapellido)

        self.lblcedula = QLabel(self.gbpasajero)
        self.lblcedula.setObjectName(u"lblcedula")
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(12)
        font5.setBold(True)
        self.lblcedula.setFont(font5)

        self.formLayout_2.setWidget(5, QFormLayout.ItemRole.SpanningRole, self.lblcedula)

        self.txtcedula = QLineEdit(self.gbpasajero)
        self.txtcedula.setObjectName(u"txtcedula")
        self.txtcedula.setFont(font4)

        self.formLayout_2.setWidget(6, QFormLayout.ItemRole.FieldRole, self.txtcedula)

        self.lblemail = QLabel(self.gbpasajero)
        self.lblemail.setObjectName(u"lblemail")
        self.lblemail.setFont(font3)

        self.formLayout_2.setWidget(8, QFormLayout.ItemRole.FieldRole, self.lblemail)

        self.txtemail = QLineEdit(self.gbpasajero)
        self.txtemail.setObjectName(u"txtemail")
        self.txtemail.setFont(font4)

        self.formLayout_2.setWidget(9, QFormLayout.ItemRole.FieldRole, self.txtemail)

        self.gbservicio = QGroupBox(self.centralwidget)
        self.gbservicio.setObjectName(u"gbservicio")
        self.gbservicio.setGeometry(QRect(360, 50, 391, 171))
        self.gbservicio.setFont(font2)
        self.gbservicio.setStyleSheet(u"QGroupBox{\n"
"    border: 2px solid #BFD7EA;\n"
"    border-radius:10px;\n"
"    margin-top:12px;\n"
"    font-weight:bold;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"    subcontrol-origin: margin;\n"
"    left:10px;\n"
"    padding:0 5px;\n"
"}\n"
"")
        self.formLayout = QFormLayout(self.gbservicio)
        self.formLayout.setObjectName(u"formLayout")
        self.lblcodigo = QLabel(self.gbservicio)
        self.lblcodigo.setObjectName(u"lblcodigo")
        self.lblcodigo.setFont(font5)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblcodigo)

        self.lblfecha = QLabel(self.gbservicio)
        self.lblfecha.setObjectName(u"lblfecha")
        self.lblfecha.setFont(font5)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lblfecha)

        self.txtcodigo = QLineEdit(self.gbservicio)
        self.txtcodigo.setObjectName(u"txtcodigo")
        self.txtcodigo.setFont(font4)
        self.txtcodigo.setReadOnly(False)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.txtcodigo)

        self.dtfecha = QDateEdit(self.gbservicio)
        self.dtfecha.setObjectName(u"dtfecha")
        self.dtfecha.setFont(font4)
        self.dtfecha.setCalendarPopup(True)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.dtfecha)

        self.lbltipoviaje = QLabel(self.gbservicio)
        self.lbltipoviaje.setObjectName(u"lbltipoviaje")
        self.lbltipoviaje.setFont(font5)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lbltipoviaje)

        self.cmbtipoviaje = QComboBox(self.gbservicio)
        self.cmbtipoviaje.addItem("")
        self.cmbtipoviaje.addItem("")
        self.cmbtipoviaje.setObjectName(u"cmbtipoviaje")
        self.cmbtipoviaje.setFont(font4)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.cmbtipoviaje)

        self.lbltexto1 = QLabel(self.gbservicio)
        self.lbltexto1.setObjectName(u"lbltexto1")
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(8)
        self.lbltexto1.setFont(font6)
        self.lbltexto1.setWordWrap(True)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.lbltexto1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(360, 220, 391, 131))
        self.groupBox.setStyleSheet(u"QGroupBox{\n"
"    border: 2px solid #BFD7EA;\n"
"    border-radius:10px;\n"
"    margin-top:12px;\n"
"    font-weight:bold;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"    subcontrol-origin: margin;\n"
"    left:10px;\n"
"    padding:0 5px;\n"
"}\n"
"")
        self.swviajes = QStackedWidget(self.groupBox)
        self.swviajes.setObjectName(u"swviajes")
        self.swviajes.setGeometry(QRect(10, 20, 371, 101))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.lbldistancia = QLabel(self.page)
        self.lbldistancia.setObjectName(u"lbldistancia")
        self.lbldistancia.setGeometry(QRect(10, 30, 121, 21))
        self.lbldistancia.setFont(font5)
        self.lblcosto = QLabel(self.page)
        self.lblcosto.setObjectName(u"lblcosto")
        self.lblcosto.setGeometry(QRect(10, 70, 131, 31))
        self.lblcosto.setFont(font5)
        self.dsbdistancia = QDoubleSpinBox(self.page)
        self.dsbdistancia.setObjectName(u"dsbdistancia")
        self.dsbdistancia.setGeometry(QRect(140, 30, 101, 31))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(12)
        self.dsbdistancia.setFont(font7)
        self.dsbcosto = QDoubleSpinBox(self.page)
        self.dsbcosto.setObjectName(u"dsbcosto")
        self.dsbcosto.setGeometry(QRect(140, 70, 101, 31))
        self.dsbcosto.setFont(font7)
        self.lblprivado = QLabel(self.page)
        self.lblprivado.setObjectName(u"lblprivado")
        self.lblprivado.setGeometry(QRect(150, 0, 131, 21))
        font8 = QFont()
        font8.setFamilies([u"Segoe UI"])
        font8.setPointSize(12)
        font8.setBold(True)
        font8.setUnderline(False)
        self.lblprivado.setFont(font8)
        self.swviajes.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.lblestaciones = QLabel(self.page_2)
        self.lblestaciones.setObjectName(u"lblestaciones")
        self.lblestaciones.setGeometry(QRect(10, 30, 131, 71))
        self.lblestaciones.setFont(font5)
        self.sbestaciones = QSpinBox(self.page_2)
        self.sbestaciones.setObjectName(u"sbestaciones")
        self.sbestaciones.setGeometry(QRect(140, 40, 111, 31))
        self.sbestaciones.setFont(font7)
        self.lblurbano = QLabel(self.page_2)
        self.lblurbano.setObjectName(u"lblurbano")
        self.lblurbano.setGeometry(QRect(150, 0, 141, 31))
        self.lblurbano.setFont(font5)
        self.swviajes.addWidget(self.page_2)
        self.gbresultado = QGroupBox(self.centralwidget)
        self.gbresultado.setObjectName(u"gbresultado")
        self.gbresultado.setGeometry(QRect(20, 360, 331, 141))
        self.gbresultado.setFont(font2)
        self.gbresultado.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid #A8D5BA;\n"
"    border-radius: 10px;\n"
"    margin-top: 12px;\n"
"    font-weight: bold;\n"
"   \n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 5px;\n"
"}")
        self.fmtarifa = QFrame(self.gbresultado)
        self.fmtarifa.setObjectName(u"fmtarifa")
        self.fmtarifa.setGeometry(QRect(100, 30, 120, 41))
        font9 = QFont()
        font9.setPointSize(15)
        self.fmtarifa.setFont(font9)
        self.fmtarifa.setFrameShape(QFrame.StyledPanel)
        self.fmtarifa.setFrameShadow(QFrame.Raised)
        self.lbltarifa = QLabel(self.fmtarifa)
        self.lbltarifa.setObjectName(u"lbltarifa")
        self.lbltarifa.setGeometry(QRect(20, 0, 81, 41))
        font10 = QFont()
        font10.setBold(True)
        self.lbltarifa.setFont(font10)
        self.lbltarifa.setStyleSheet(u"color:#2E7D32;\n"
"font-size:26px;\n"
"font-weight:bold;")
        self.lblviaje = QLabel(self.gbresultado)
        self.lblviaje.setObjectName(u"lblviaje")
        self.lblviaje.setGeometry(QRect(10, 80, 151, 21))
        font11 = QFont()
        font11.setPointSize(11)
        font11.setBold(False)
        self.lblviaje.setFont(font11)
        self.lblviaje.setStyleSheet(u"")
        self.lbltexto2 = QLabel(self.gbresultado)
        self.lbltexto2.setObjectName(u"lbltexto2")
        self.lbltexto2.setGeometry(QRect(30, 100, 291, 41))
        font12 = QFont()
        font12.setPointSize(11)
        font12.setBold(True)
        self.lbltexto2.setFont(font12)
        self.lbltexto2.setStyleSheet(u"")
        self.gbacciones = QGroupBox(self.centralwidget)
        self.gbacciones.setObjectName(u"gbacciones")
        self.gbacciones.setGeometry(QRect(360, 360, 391, 141))
        self.gbacciones.setFont(font2)
        self.gbacciones.setStyleSheet(u"QGroupBox{\n"
"    border: 2px solid #BFD7EA;\n"
"    border-radius:10px;\n"
"    margin-top:12px;\n"
"    font-weight:bold;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"    subcontrol-origin: margin;\n"
"    left:10px;\n"
"    padding:0 5px;\n"
"}\n"
"")
        self.gridLayout = QGridLayout(self.gbacciones)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btneliminar = QPushButton(self.gbacciones)
        self.btneliminar.setObjectName(u"btneliminar")
        self.btneliminar.setFont(font)
        self.btneliminar.setStyleSheet(u"")

        self.gridLayout.addWidget(self.btneliminar, 1, 0, 1, 1)

        self.btnregistrar = QPushButton(self.gbacciones)
        self.btnregistrar.setObjectName(u"btnregistrar")
        self.btnregistrar.setFont(font)
        self.btnregistrar.setStyleSheet(u"")

        self.gridLayout.addWidget(self.btnregistrar, 0, 0, 1, 1)

        self.btnactualizar = QPushButton(self.gbacciones)
        self.btnactualizar.setObjectName(u"btnactualizar")
        self.btnactualizar.setFont(font)

        self.gridLayout.addWidget(self.btnactualizar, 1, 1, 1, 1)

        self.btnmostrar = QPushButton(self.gbacciones)
        self.btnmostrar.setObjectName(u"btnmostrar")
        self.btnmostrar.setFont(font)
        self.btnmostrar.setStyleSheet(u"")

        self.gridLayout.addWidget(self.btnmostrar, 0, 1, 1, 1)

        self.btnlimpiar = QPushButton(self.gbacciones)
        self.btnlimpiar.setObjectName(u"btnlimpiar")
        self.btnlimpiar.setFont(font)

        self.gridLayout.addWidget(self.btnlimpiar, 2, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 786, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.swviajes.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lblregistro.setText(QCoreApplication.translate("MainWindow", u"SISTEMA DE GESTION DE TRANSPORTE", None))
        self.gbpasajero.setTitle(QCoreApplication.translate("MainWindow", u"DATOS DEL PASAJERO", None))
        self.lblnombre.setText(QCoreApplication.translate("MainWindow", u"Nombres:", None))
        self.lblapellido.setText(QCoreApplication.translate("MainWindow", u"Apellidos:", None))
        self.lblcedula.setText(QCoreApplication.translate("MainWindow", u"C\u00e9dula:", None))
        self.lblemail.setText(QCoreApplication.translate("MainWindow", u"Email: ", None))
        self.gbservicio.setTitle(QCoreApplication.translate("MainWindow", u"DATOS DEL SERVICIO", None))
        self.lblcodigo.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo: ", None))
        self.lblfecha.setText(QCoreApplication.translate("MainWindow", u"Fecha:", None))
        self.lbltipoviaje.setText(QCoreApplication.translate("MainWindow", u"Tipo de Viaje:", None))
        self.cmbtipoviaje.setItemText(0, QCoreApplication.translate("MainWindow", u"Viaje Privado", None))
        self.cmbtipoviaje.setItemText(1, QCoreApplication.translate("MainWindow", u"Viaje Urbano", None))

        self.lbltexto1.setText(QCoreApplication.translate("MainWindow", u"\u24d8Seleccione el tipo de viaje para habilitar los campos correspondientes.", None))
        self.groupBox.setTitle("")
        self.lbldistancia.setText(QCoreApplication.translate("MainWindow", u"Distancia (Km):", None))
        self.lblcosto.setText(QCoreApplication.translate("MainWindow", u"Costo por Km:", None))
        self.lblprivado.setText(QCoreApplication.translate("MainWindow", u"VIAJE PRIVADO", None))
        self.lblestaciones.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Cantidad de</p><p>estaciones:</p><p><br/></p></body></html>", None))
        self.lblurbano.setText(QCoreApplication.translate("MainWindow", u"VIAJE URBANO", None))
        self.gbresultado.setTitle(QCoreApplication.translate("MainWindow", u"TARIFA", None))
        self.lbltarifa.setText(QCoreApplication.translate("MainWindow", u"$0.00 ", None))
        self.lblviaje.setText(QCoreApplication.translate("MainWindow", u"Viaje:  Ninguno", None))
        self.lbltexto2.setText(QCoreApplication.translate("MainWindow", u"Se calcular\u00e1 al registrar el servicio. ", None))
        self.gbacciones.setTitle(QCoreApplication.translate("MainWindow", u"ACCIONES", None))
        self.btneliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.btnregistrar.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.btnactualizar.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.btnmostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.btnlimpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
    # retranslateUi

