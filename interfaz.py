import tkinter as tk
from componentes import Boton_grande,Contenedor_fila,Contenedor_Columna,Etiqueta,Entrada,DeslizadorVertical
from logica import recorrer_rutas
from constantes import Colores

class Interfaz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculador de IVA")
        self.geometry("720x480")
        self.configure(bg=Colores["fondo"])
        self.instanciar()
        self.resizable(False,False)
        
  

    def instanciar(self):
    
        titulo = Etiqueta(self, text="Calculador de IVA")
        titulo.pack(fill="x", pady=10)
    

        creador_libro = Contenedor_fila(self)
        creador_libro.configure(bg=Colores["Frame_beta"])
        creador_libro.pack(expand=True, fill="both", padx=20, pady=20)
    
        Submit = Boton_grande(creador_libro, "Crear Libro", recorrer_rutas)
        Submit.configure(
            height=2,  
            width=20   
        )
        campo_nombre = Entrada(creador_libro, placeholder_text="Ingrese su nombre")
        campo_nombre.configure(
            width=30, 
        )

        columna_libros=Contenedor_Columna(creador_libro)
        columna_libros.configure(width="240",bg=Colores["Frame_omega"])
        creador_libro.empaquetar_componente(campo_nombre,None)
        creador_libro.empaquetar_componente(Submit,None)
        creador_libro.empaquetar_componente(columna_libros,"y")
        dinamico=DeslizadorVertical(columna_libros)
        dinamico.configure(bg=Colores["Frame_omega"])
        columna_libros.empaquetar_componente(dinamico,"both")
        dinamico.generar_botones()
    
    