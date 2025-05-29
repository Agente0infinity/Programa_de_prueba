import os

def recorrer_rutas():
    lista_rutas=[]
    carpeta="libros"
    for nombre_archivo in os.listdir(carpeta):
        if nombre_archivo.endswith(".txt"):
            ruta_completa = os.path.join(carpeta, nombre_archivo)
            lista_rutas.append(ruta_completa)
    print(lista_rutas)
    return lista_rutas
def calcular_IVA():

    pass

def agregar_boleta():

    pass

def probar(libro):
    with open(libro,"r") as libro:
        libro.readlines()








