import os


def leer_archivo(nombre_archivo):
    with open(nombre_archivo) as archivo:
        contenido = archivo.read()
    return contenido


if __name__ == "__main__":
    # os.chdir(os.path.dirname(__file__))  # change working dir
    print __file__
    print os.path.dirname(__file__)
    try:
        clave_admin = leer_archivo("admin.txt")
        clave_ingresada = input()

        if clave_ingresada == clave_admin:
            flag = leer_archivo("bandera.txt")
            print flag
        else:
            print "ERROR! Clave incorrecta. Este servidor es muy seguro."
    except Exception as e:
        print e.message
