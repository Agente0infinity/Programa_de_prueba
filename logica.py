import os

def Hola():

    print("hola")

def recorrer_rutas():
    lista_rutas=[]
    carpeta="libros"
    for nombre_archivo in os.listdir(carpeta):
        if nombre_archivo.endswith(".txt"):
            ruta_completa = os.path.join(carpeta, nombre_archivo)
            lista_rutas.append(ruta_completa)
    print(lista_rutas)
    return lista_rutas

def abrir_archivo(ruta):

    with open(ruta,"r") as libro:
        for linea in libro:
            print(linea)






