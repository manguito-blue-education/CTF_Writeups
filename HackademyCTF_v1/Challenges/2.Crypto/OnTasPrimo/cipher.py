import sys
import base64
from itertools import cycle


def leer_llave(filename, default_key=None):
    if default_key is not None:
        return default_key

    try:
        with open(filename) as fp:
            key = fp.read().strip()
        return key

    except FileNotFoundError:
        print(f"El archivo {filename} no existe, y no hay una llave por defecto.")
        return None


def cifrar(data, encode_output=False, decode_input=False):
    llave = leer_llave("key.txt")
    if llave is None:
        return ""

    print("Llave Usada:", llave)

    if decode_input:
        data = base64.b64decode(data).decode()

    # important: cycle because key might be shorter than data
    texto_cifrado = "".join(chr(ord(x) ^ ord(y)) for (x, y) in zip(data, cycle(llave)))

    if encode_output:
        return base64.b64encode(texto_cifrado.encode()).decode()

    return texto_cifrado


if __name__ == "__main__":
    print("Bienvenido al cifrador perfecto")
    texto = input("Ingresa lo que quieras cifrar: ")
    texto_cifrado = cifrar(texto, encode_output=True)
    print(f"Tu texto: {texto}\nTu texto cifrado: {texto_cifrado}")
