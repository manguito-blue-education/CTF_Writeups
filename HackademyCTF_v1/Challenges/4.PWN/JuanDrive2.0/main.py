# TODO: quitar el archivo bandera.txt del mismo folder del main.py
import os
from random import randint


def es_un_bot(operacion, resultado):
    try:
        resultado_evaluacion = eval(operacion)
        return resultado_evaluacion != resultado
    except:
        return True


if __name__ == "__main__":

    usuario = input("Ingresa tu nombre de usuario: ")
    num_bot = randint(1, 100)
    print(f"{'*'*20}\nRevisión de bot\n{'*'*20}")
    print(f"Eres humano {usuario}?")
    print(f"Ingresa una operación que dé como resultado {num_bot}")
    print("Por ejemplo: si el numero es '10', la operación podría ser '8+2'")
    print("No pongas las comillas")
    operacion = input(f"Operación: ")
    if es_un_bot(operacion, num_bot):
        print("Lo siento, sólo los humanos son permitidos")
    else:
        # TODO registrar al usuario
        print(
            f"Gracias por el interés {usuario}! Te notificaremos cuando el servicio esté disponible"
        )
