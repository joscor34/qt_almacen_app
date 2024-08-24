# Este contendrá funciones que se estarán ejecutando muy seguido en el código
# methods - helpers - extensions - manejadores - Auxiliares - Aux

import jwt
import os # Crear un archivo en nuestro proyecto
import datetime # Determinar si mi token sigue vigente

token_file_path = 'token.txt' # Archivo donde se va a almacenar el token

url_api = 'https://7cfa-189-193-83-55.ngrok-free.app'


def delete_token():
    # Abrimos el archivo que queremos reescribir
    with open(token_file_path, 'w') as file:
        # Borrar el contenido
        file.write('') # <- Reescribe el documento con un string vacío

def save_token(token):
    # Abrimos el archivo donde se va a almacenar el token en modo de escritura
    with open(token_file_path, 'w') as file:
        # Se escribe lo que contenga token
        file.write(token)


def load_token():
    # Determinamos si el archivo token.txt existe
    if os.path.exists(token_file_path):
        # Abrimos el archivo txt en modo de lectura
        with open(token_file_path, 'r') as file:
            # Se lee lo que contenga el archivo
            return file.read()
    else:
        # Que archivo con el token no existe
        return None


def token_is_valid(token):

    # Obtengo el payload del token
    info_token = decode_token(token)
    # Obtenemos el tiempo de expiración
    expiration = datetime.datetime.fromtimestamp(info_token['exp'])


    # Token válido - True

    # Tokén expirado - False

    return expiration > datetime.datetime.now()



# Función para descriptar el payload del token
def decode_token(token):
    payload = jwt.decode(token, options={'verify_signature': False})

    return payload

def obtener_usuario_token(token):
    # Obtenemos la información del payload del token
    info_user = decode_token(token)

    # Retornamos el nombre
    return  info_user['sub']
