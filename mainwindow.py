# This Python file uses the following encoding: utf-8
import sys
import requests
import json

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_main import Ui_MainWindow

# Importamos el administrador de rutas
from routes import RouteManager
from helpers import url_api

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Inicializo el administrador de rutas
        self.route_manager = RouteManager()


        # Agregamos funcionalidad a mi botón
        # self.ui.boton_registro.clicked.connect(self.dirigir_a_registro)
        # Agregamos funcionalidad al inicio de sesión
        self.ui.boton_prueba.clicked.connect(self.iniciar_sesion)

    # Este método va a ejecutar el proceso para inicar sesión
    def iniciar_sesion(self):

        # Ruta de mi API
        url = url_api + '/usuarios/login'

        # Información de los inputs
        email = self.ui.input_email.text()
        password = self.ui.input_pass.text()

        # La información que vamos a enviar a la API
        info_a_enviar = {
            'email': email,
            'password': password
        }

        # Creamos una variable para la respuesta del servidor
        response = requests.post(url, data=info_a_enviar)

        print('Se obtuvo una respuesta del servidor: ')

        respuesta_decodificada = response.content.decode('utf-8')

        respuesta_decodificada = json.loads(respuesta_decodificada)

        print(respuesta_decodificada)

        if 'Error' in respuesta_decodificada:
            print('El correo o contraseña no coinciden')
            self.ui.texto_error.setText('El correo o contraseña no coinciden :(')

        elif 'Token' in respuesta_decodificada:
            print('Sesión iniciada correctamente')
            # Se redirige al usuario a la ventana principal
            token = respuesta_decodificada['Token']

            self.route_manager.mandar_a_principal(self, token)

        else:
            print('Error en el servidor')
            self.ui.texto_error.setText('Error interno del servidor :(')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    # -----------------------------------
    # -----------------------------------
    widget.show()
    sys.exit(app.exec())
