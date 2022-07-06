# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QCommandLinkButton, QFrame,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class View(object):
    def setupUi(self, Ventana):
        if not Ventana.objectName():
            Ventana.setObjectName(u"Ventana")
        Ventana.setWindowModality(Qt.NonModal)
        Ventana.setEnabled(True)
        Ventana.resize(500, 300)
        Ventana.setMinimumSize(QSize(400, 200))
        Ventana.setMaximumSize(QSize(500, 300))
        Ventana.setSizeIncrement(QSize(0, 0))
        Ventana.setBaseSize(QSize(0, 0))
        Ventana.setWindowOpacity(1.000000000000000)
        Ventana.setLayoutDirection(Qt.LeftToRight)
        Ventana.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        Ventana.setProperty("setFixedSize", QSize(1, 1))
        self.descargar = QPushButton(Ventana)
        self.descargar.setObjectName(u"descargar")
        self.descargar.setGeometry(QRect(10, 240, 481, 24))
        self.descargar.setStyleSheet(u"background-color: rgb(212, 212, 212);\n"
"color: rgb(0, 0, 0);")
        self.salir = QPushButton(Ventana)
        self.salir.setObjectName(u"salir")
        self.salir.setGeometry(QRect(10, 270, 481, 24))
        self.salir.setStyleSheet(u"background-color: rgb(212, 212, 212);\n"
"color: rgb(0, 0, 0);")
        self.title = QLabel(Ventana)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(10, 10, 481, 31))
        font = QFont()
        font.setFamilies([u"Nirmala UI"])
        font.setPointSize(16)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_link = QLabel(Ventana)
        self.label_link.setObjectName(u"label_link")
        self.label_link.setGeometry(QRect(40, 60, 401, 21))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        self.label_link.setFont(font1)
        self.label_link.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_link.setAlignment(Qt.AlignCenter)
        self.link = QLineEdit(Ventana)
        self.link.setObjectName(u"link")
        self.link.setGeometry(QRect(42, 100, 401, 24))
        self.link.setStyleSheet(u"background-color: rgb(255, 170, 255);")
        self.seleccion = QComboBox(Ventana)
        self.seleccion.addItem("")
        self.seleccion.addItem("")
        self.seleccion.addItem("")
        self.seleccion.addItem("")
        self.seleccion.setObjectName(u"seleccion")
        self.seleccion.setEnabled(False)
        self.seleccion.setGeometry(QRect(320, 170, 171, 24))
        self.seleccion.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(193, 193, 193);")
        self.comentario = QLabel(Ventana)
        self.comentario.setObjectName(u"comentario")
        self.comentario.setGeometry(QRect(10, 210, 481, 21))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(10)
        self.comentario.setFont(font2)
        self.comentario.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.comentario.setFrameShadow(QFrame.Plain)
        self.comentario.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.comentario_2 = QLabel(Ventana)
        self.comentario_2.setObjectName(u"comentario_2")
        self.comentario_2.setGeometry(QRect(10, 130, 481, 21))
        self.comentario_2.setFont(font1)
        self.comentario_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.comentario_2.setFrameShadow(QFrame.Plain)
        self.comentario_2.setAlignment(Qt.AlignCenter)
        self.buscar = QCommandLinkButton(Ventana)
        self.buscar.setObjectName(u"buscar")
        self.buscar.setGeometry(QRect(450, 90, 31, 31))
        self.buscar.setCursor(QCursor(Qt.PointingHandCursor))
        self.buscar.setMouseTracking(False)
        self.buscar.setFocusPolicy(Qt.StrongFocus)
        self.buscar.setLayoutDirection(Qt.LeftToRight)
        self.buscar.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(199, 199, 199);")
        self.buscar.setIconSize(QSize(20, 20))
        self.buscar.setAutoRepeatDelay(100)
        self.comentario_3 = QLabel(Ventana)
        self.comentario_3.setObjectName(u"comentario_3")
        self.comentario_3.setEnabled(True)
        self.comentario_3.setGeometry(QRect(120, 170, 191, 21))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(9)
        self.comentario_3.setFont(font3)
        self.comentario_3.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.comentario_3.setFrameShadow(QFrame.Plain)
        self.comentario_3.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Ventana)

        QMetaObject.connectSlotsByName(Ventana)
    # setupUi

    def retranslateUi(self, Ventana):
        Ventana.setWindowTitle(QCoreApplication.translate("Ventana", u"Ventana", None))
        self.descargar.setText(QCoreApplication.translate("Ventana", u"Descargar", None))
        self.salir.setText(QCoreApplication.translate("Ventana", u"Salir", None))
        self.title.setText(QCoreApplication.translate("Ventana", u"Descargar Videos de Youtube", None))
        self.label_link.setText(QCoreApplication.translate("Ventana", u"Ingrese el link del video", None))
        self.seleccion.setItemText(0, "")
        self.seleccion.setItemText(1, QCoreApplication.translate("Ventana", u"Descargar mejor calidad", None))
        self.seleccion.setItemText(2, QCoreApplication.translate("Ventana", u"Descargar menor calidad", None))
        self.seleccion.setItemText(3, QCoreApplication.translate("Ventana", u"Descargar MP3", None))

        self.buscar.setText("")
        self.comentario_3.setText(QCoreApplication.translate("Ventana", u"Secelccione el tipo de descargar", None))
    # retranslateUi

