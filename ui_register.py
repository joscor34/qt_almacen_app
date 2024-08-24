# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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

class Ui_RegisterWindow(object):
    def setupUi(self, RegisterWindow):
        if not RegisterWindow.objectName():
            RegisterWindow.setObjectName(u"RegisterWindow")
        RegisterWindow.resize(481, 600)
        self.centralwidget = QWidget(RegisterWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 60, 161, 71))
        self.label.setStyleSheet(u"font: 700 20pt \"Segoe UI\";")
        self.captura_username = QLineEdit(self.centralwidget)
        self.captura_username.setObjectName(u"captura_username")
        self.captura_username.setGeometry(QRect(130, 160, 221, 28))
        self.captura_mail = QLineEdit(self.centralwidget)
        self.captura_mail.setObjectName(u"captura_mail")
        self.captura_mail.setGeometry(QRect(130, 230, 221, 28))
        self.captura_pass = QLineEdit(self.centralwidget)
        self.captura_pass.setObjectName(u"captura_pass")
        self.captura_pass.setGeometry(QRect(130, 300, 221, 28))
        self.captura_pass.setEchoMode(QLineEdit.Password)
        self.crear_cuenta = QPushButton(self.centralwidget)
        self.crear_cuenta.setObjectName(u"crear_cuenta")
        self.crear_cuenta.setGeometry(QRect(170, 410, 131, 29))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 140, 161, 20))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(130, 210, 111, 20))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(130, 280, 81, 20))
        self.alerta_error = QLabel(self.centralwidget)
        self.alerta_error.setObjectName(u"alerta_error")
        self.alerta_error.setGeometry(QRect(130, 350, 221, 20))
        self.alerta_error.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 0, 0)\n"
"}")
        RegisterWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(RegisterWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 481, 25))
        RegisterWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(RegisterWindow)
        self.statusbar.setObjectName(u"statusbar")
        RegisterWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RegisterWindow)

        QMetaObject.connectSlotsByName(RegisterWindow)
    # setupUi

    def retranslateUi(self, RegisterWindow):
        RegisterWindow.setWindowTitle(QCoreApplication.translate("RegisterWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("RegisterWindow", u"Registrate", None))
        self.captura_username.setPlaceholderText("")
        self.crear_cuenta.setText(QCoreApplication.translate("RegisterWindow", u"Crear cuenta", None))
        self.label_2.setText(QCoreApplication.translate("RegisterWindow", u"Nombre de usuario", None))
        self.label_3.setText(QCoreApplication.translate("RegisterWindow", u"Correo", None))
        self.label_4.setText(QCoreApplication.translate("RegisterWindow", u"Contrase\u00f1a", None))
        self.alerta_error.setText("")
    # retranslateUi

