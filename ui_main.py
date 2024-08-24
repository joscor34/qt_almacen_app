# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(793, 685)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.boton_prueba = QPushButton(self.centralwidget)
        self.boton_prueba.setObjectName(u"boton_prueba")
        self.boton_prueba.setGeometry(QRect(250, 240, 281, 61))
        self.boton_prueba.setStyleSheet(u"QPushButton {\n"
"    background-color: #3dccab;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 15px 32px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"    cursor: pointer;\n"
"    border-radius: 25px; /* Bordes bastante redondeados */\n"
"    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Sombra de fondo */\n"
"    transition: background-color 0.3s; /* Transici\u00f3n suave para el efecto hover */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #35b197; /* Color oscurecido */\n"
"}")
        self.input_email = QLineEdit(self.centralwidget)
        self.input_email.setObjectName(u"input_email")
        self.input_email.setGeometry(QRect(250, 150, 281, 28))
        self.texto_error = QLabel(self.centralwidget)
        self.texto_error.setObjectName(u"texto_error")
        self.texto_error.setGeometry(QRect(250, 340, 231, 61))
        self.texto_error.setStyleSheet(u"QLabel {\n"
"	font: 12pt \"Sitka Banner\";\n"
"	color: rgb(255,0,0)\n"
"	\n"
"}")
        self.input_pass = QLineEdit(self.centralwidget)
        self.input_pass.setObjectName(u"input_pass")
        self.input_pass.setEnabled(True)
        self.input_pass.setGeometry(QRect(250, 190, 281, 28))
        font = QFont()
        font.setPointSize(9)
        self.input_pass.setFont(font)
        self.input_pass.setEchoMode(QLineEdit.Password)
        self.input_pass.setCursorPosition(0)
        self.input_pass.setDragEnabled(False)
        self.input_pass.setReadOnly(False)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(250, 110, 171, 20))
        self.label.setStyleSheet(u"")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 480, 131, 20))
        self.boton_registro = QPushButton(self.centralwidget)
        self.boton_registro.setObjectName(u"boton_registro")
        self.boton_registro.setGeometry(QRect(380, 470, 101, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 793, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.boton_prueba.setText(QCoreApplication.translate("MainWindow", u"Inicar sesi\u00f3n", None))
        self.input_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingresa tu correo", None))
        self.texto_error.setText("")
        self.input_pass.setText("")
        self.input_pass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingresa tu contrase\u00f1a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Inicio de sesi\u00f3n", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u00bfNo tienes cuenta?", None))
        self.boton_registro.setText(QCoreApplication.translate("MainWindow", u"\u00a1Registrate!", None))
    # retranslateUi

