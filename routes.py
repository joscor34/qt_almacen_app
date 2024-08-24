from helpers import decode_token, save_token, load_token, token_is_valid, obtener_usuario_token


# Este archivo se va a encargar de manejar las redirecciones

# Esta clase administra las ventanas
class RouteManager:

    # En su método constructor cree un nuevo atributo
    # Que va a contener la ventana que quiera abrir
    def __init__(self):
        # Va a estar vacío
        self.current_window = None



    def director_de_inicio(self):
        token_actual = load_token()
        if token_actual != '' and token_is_valid(token_actual):
            # Obtenemos el usuario del token en el archivo
            self.nombre_usuario = obtener_usuario_token(token_actual)
            self.mandar_a_principal(token=token_actual)
            print('Existe un token')

        else:
            print('no hay token - El token expiró')
            self.mandar_a_login()


    # Mandar al usuario a la vista login
    def mandar_a_login(self, ventana_anterior=None):
        from mainwindow import MainWindow  # Importación diferida
        print(ventana_anterior)
        if ventana_anterior:
            # La ventana actual se conviernte en MainWindow
            self.current_window = MainWindow()
            # Mostramos la ventana actual
            self.current_window.show()

            # Se cierra la anterior
            ventana_anterior.close()
        else:
            self.current_window = MainWindow()
            # Mostramos la ventana actual
            self.current_window.show()


    # Mandar al usuario a la vista registro
    def mandar_a_registro(self, ventana_anterior):
        from register import RegisterWindow  # Importación diferida
        self.current_window = RegisterWindow()
        self.current_window.show()

        # Se cierra la ventana actual
        ventana_anterior.close()

    # Mandar al usuario a la vista principal
    def mandar_a_principal(self, ventana_anterior=None, token=None):
        from principal import PrincipalWindow  # Importación diferida



        if ventana_anterior:
            save_token(token)

            #------------------------------------------------------

            info_user = decode_token(token)

            nombre_usuario = info_user['sub'] # Subject (a quien le pertenece el token)

            self.current_window = PrincipalWindow(nombre_usuario=nombre_usuario)
            self.current_window.show()

            # Se cierra la ventana actual
            ventana_anterior.close()

        else:
            info_user = decode_token(token)

            nombre_usuario = info_user['sub'] # Subject (a quien le pertenece el token)
            self.current_window = PrincipalWindow(nombre_usuario=nombre_usuario)
            # Mostramos la ventana actual
            self.current_window.show()



