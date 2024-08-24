# This Python file uses the following encoding: utf-8
import sys
from helpers import load_token, obtener_usuario_token, token_is_valid, url_api, delete_token
from routes import RouteManager

import requests # La librería que nos va a permitir manejar la API
import json # Convierte Strings a diccionarios

# Importamos las herramienta para renderizar las aplicaciones
from PySide6.QtWidgets import QApplication, QMainWindow

# Importamos todo el apartado gráfico del archivo "register.ui"
from ui_principal import Ui_PrincipalWindow

# ----------------------------------------------------------------------

# Creamos una clase que contrendrá la ventana que vamos a dibujar
class PrincipalWindow(QMainWindow):
    def __init__(self, nombre_usuario='1', parent=None):
        super().__init__(parent)

        # Inicializo mi administrador de rutas
        self.route_manager = RouteManager()

        # Le creamos una atributo a mi clase llamada "correo_usuario"
        self.nombre_usuario = nombre_usuario

        # Ejecutamos la función que va a cargar el token
        token_actual = load_token()



        # Este atributo contendrá todo el apartado gráfico
        self.ui = Ui_PrincipalWindow()
        # Lo inicializamos el apartado gráfico
        self.ui.setupUi(self)
        # Le decimos a la etiqueta que sobreescriba su contenido con el correo del usuario

        self.ui.mostrar_correo.setText(f'Bienvenido: {self.nombre_usuario}')
        self.ui.boton_buscar.clicked.connect(self.buscar)

        # Control de los checkBox
        # Cuando mi app inicie, el recuadro del ID vendrá seleccionado por defecto
        self.ui.check_id.setChecked(True)


        self.ui.check_id.toggled.connect(self.check_id_presionado)
        self.ui.check_name.toggled.connect(self.check_name_presionado)

        # Control del cerrado de sesión
        self.ui.boton_cerrar.clicked.connect(self.cerrar_sesion)


# ------------ Primero configuramos la ventana y después sacamos al usuario -----------


    # Este método nos ayudará a cerrar mi sesión actual
    def cerrar_sesion(self):
        print("Cerrando sesión")
        # Borrar el token existente
        delete_token()
        print('Token eliminado correctamente')
        # Mandamos al usuario a pantalla del login
        self.route_manager.mandar_a_login(self)


    def check_name_presionado(self, checked):
        # Primer paso es verificar si mi checbox esta activado
        # Segundo es verificar el el otro checkbox (id) esta presionado
        if checked and self.ui.check_id.isChecked():
            # Se desactiva el checkbox del ID
            self.ui.check_id.setChecked(False)


    def check_id_presionado(self, checked):
        # Primer paso es verificar si mi checbox esta activado
        # Segundo es verificar el el otro checkbox (name) esta presionado
        if checked and self.ui.check_name.isChecked():
            # Se desactiva el checkbox del Name
            self.ui.check_name.setChecked(False)








    # Nos va a ayudar a buscar un producto através de la API
    def buscar_producto_id(self):
        id_producto = self.ui.buscador.text()

        # Url al la cual se hará la petición
        url = f"{url_api}/objetos_almacen?id={id_producto}"

        token_actual = load_token()

        headers = {"Authorization": f"Bearer {token_actual}"}

        response = requests.get(url, headers=headers)

        print(response.content.decode('utf-8'))

        respuesta_json = json.loads(response.content.decode('utf-8'))

        print(type(respuesta_json))

        if "message" in respuesta_json:
            self.ui.nombre_producto.setText('No se encontró ningún producto :(')
            self.ui.cantidad_producto.setText('')


        elif "Cantidad" in respuesta_json:
            self.ui.nombre_producto.setText(f'Nombre: {respuesta_json["Nombre"]}')
            self.ui.cantidad_producto.setText(f'Cantidad: {respuesta_json["Cantidad"]}')


    # Nos va a ayudar a buscar un producto por su nombre en la API
    def buscar_producto_nombre(self):

        nombre_producto = self.ui.buscador.text()

        # Url para buscar producto por nombre
        url = f"{url_api}/objetos_almacen?nombre={nombre_producto}"


        token_actual = load_token()

        headers = {"Authorization": f"Bearer {token_actual}"}

        response = requests.get(url, headers=headers)

        print(response.content.decode('utf-8'))

        respuesta_json = json.loads(response.content.decode('utf-8'))

        print(type(respuesta_json))

    # Comparar qué checkbox está activado
    def buscar(self):
        if self.ui.check_id.isChecked():
            # Buscar un producto por su id
            self.buscar_producto_id()

        elif self.ui.check_name.isChecked():
            # Busca un producto por su nombre
            self.buscar_producto_nombre()
# ----------------------------------------------------------------------






# Es un método mágico -> Verifica si el archivo se esta ejecutando de raíz
if __name__ == '__main__':
    # Inicializamos la aplicación (Ventana)
    app = QApplication(sys.argv)
    # Creamos un objeto de tipo RegisterWindow
    router = RouteManager()
    router.director_de_inicio()
    # Para poder cerrar la ventana
    sys.exit(app.exec())



