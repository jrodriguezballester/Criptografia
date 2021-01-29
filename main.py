import argparse
import os
import sys

from cryptography.fernet import Fernet


def crear_clave():
    return Fernet.generate_key()


def save_key(key):
    try:
        file = open('fichero.txt', 'bw')
        file.write(key)
        file.close()
    except:
        return False
    return True


def exists_file():
    # print('existe:', os.path.isfile('fichero.txt'))
    return os.path.isfile('fichero.txt')


def get_key():
    try:
        file = open('fichero.txt', 'br')
        my_key = file.readline()
        file.close()
    except:
        return None
    return my_key


def encriptar(mensaje, f):
    token = f.encrypt(mensaje.encode())
    # print('el mensaje:::', f.decrypt(token).decode())
    return token


def desencriptar(token, f):
    mensaje = f.decrypt(token).decode()
    return mensaje


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('-d', '--desencrip', help='Mensaje a decodificar')
    parser.add_argument('-e', '--encrip', help='codificar mensaje')

    args = parser.parse_args()

    # Para ambos opciones Controlar que exista fichero con clave
    if not exists_file():
        # print('no existe')
        clave = crear_clave()
        print(' inicio')
        almacenada = save_key(clave)
        if not almacenada:
            print('ERROR, no se ha guardado la clave')
            sys.exit(0)

    # Recoger clave del fichero

    key = get_key()

    if key is not None:
        # print('key', key)

        f = Fernet(key)

        # Actuar en funcion del argumento
        # Encriptar
        if args.encrip:
            print('el mensaje es: ', args.encrip)
            mensaje = args.encrip
            token = encriptar(mensaje, f)
            print('el token: ', token)

        # Desencriptar
        if args.desencrip:
            print('token: ', args.desencrip)
            token = args.desencrip.encode()
            mensaje = desencriptar(token, f)
            print('el mensaje:', mensaje)

    else:
        print('No se ha podido leer la clave para codificar')
