# This Python file uses the following encoding: utf-8
import sys
import requests
import json


# Importamos las herramienta para renderizar las aplicaciones
from PySide6.QtWidgets import QApplication, QMainWindow

# Importamos todo el apartado gráfico del archivo "register.ui"
from ui_register import Ui_RegisterWindow

from routes import RouteManager

from helpers import url_api

# Creamos una clase que contrendrá la ventana que vamos a dibujar
class RegisterWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Este atributo contendrá todo el apartado gráfico
        self.ui = Ui_RegisterWindow()
        # Lo inicializamos el apartado gráfico
        self.ui.setupUi(self)

        # Se inicializa el manejador de rutas
        self.route_manager = RouteManager()
        # Le decimos al código que capture, correo, usuario y contraseña
        # Capturamo si el botón fue presionado
        self.ui.crear_cuenta.clicked.connect(self.capturar_info)

        # Esta función se va a encargar de verificar que mi información este correcta


# --------------------------------------------------------------------------

    def capturar_info(self):
        username = self.ui.captura_username.text()
        mail = self.ui.captura_mail.text()
        password = self.ui.captura_pass.text()

        if len(username) == 0 or len(password) == 0 or len(mail) == 0:
            print("Faltan agregar campos")

            self.ui.alerta_error.setText('Faltan completar campos')
            return 1

        elif "@" not in mail or "." not in mail:
            print("El correo no es valido")

            self.ui.alerta_error.setText("Ingresa un correo válido")
            return 1

        print(f'''
            Correo: {mail}
            User: {username}
            Password: {password}
        ''')

        self.crear_usuario(username, mail, password)



    def crear_usuario(self, username, correo, password):

        # La url de mi API
        url = url_api + '/usuarios/registro'

        informacion_user = {
            'username': username,
            'email': correo,
            'password': password
        }

        print('Se esta creando un nuevo usuario')

        # Respuesta de mi servidor
        response = requests.post(url, data=informacion_user)

        print('Se obtuvo una respuesta del servidor: ')

        respuesta_decodificada = response.content.decode('utf-8')

        respuesta_decodificada = json.loads(respuesta_decodificada)

        print(respuesta_decodificada)

        # El usuario esta duplicado
        if 'Error' in respuesta_decodificada:
            print('Usuario Duplicado')
            self.ui.alerta_error.setText("Ese correo ya está registrado")
            return 1

        # El usuario se creo correctamente
        elif 'Nuevo usuario' in respuesta_decodificada:
            print('Se creo un nuevo usuario')

            # Mandamos al usuario a login y cerramos la ventana acutal
            self.route_manager.mandar_a_login(self)


        # Hubo un error con el servidor
        else:
            print('Error interno')
            self.ui.alerta_error.setText("Error interno")
            return 1



        # Es un método mágico -> Verifica si el archivo se esta ejecutando de raíz
if __name__ == '__main__':
    # Inicializamos la aplicación (Ventana)
    app = QApplication(sys.argv)
    # Creamos un objeto de tipo RegisterWindow
    widget = RegisterWindow()
    # Este método hará que mi objeto se muestre
    widget.show()

    # Para poder cerrar la ventana
    sys.exit(app.exec())







