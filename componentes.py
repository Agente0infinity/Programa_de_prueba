from constantes import Colores
import tkinter as tk
from tkinter import ttk

class Boton(tk.Button):
    def __init__(self,master=None,texto=None,evento=None,**kwargs):
        valores = {
        
        "bg":Colores["frame_botones"],
        "fg":Colores["texto"],
        "font":("arial",10)
        }
        final_config={**valores, **kwargs}

        super().__init__(master, **final_config)

class Boton_estandar(Boton):
    def __init__(self, master=None,texto=None,evento=None, **kwargs):
        tamaño= {
        "text": texto,
        "command": evento,
        "padx":4,
        "pady":5,
        "width":20,
        "height":20
    
        }
        config={**tamaño,**kwargs}
        super().__init__(master,**config)

class Boton_grande(Boton):
    def __init__(self, master=None,texto=None,evento=None, **kwargs):
        tamaño= {
        "text": texto,
        "command": evento,
        "padx":6,
        "pady":7,
        "width":200,
        "height":50,
        
        }
        config={**tamaño,**kwargs}
        super().__init__(master,**config)



class Etiqueta(tk.Label):
    def __init__(self, master=None, **kwargs):
        valores = {
        "bg":Colores["frame_botones"],
        "fg":Colores["texto"],
        "font":("arial",12)
        }
        final_config={**valores, **kwargs}
        super().__init__(master, **final_config)

class Texto(tk.Text):
    def __init__(self, master=None, **kwargs):
        valores= {
        "fg":Colores["texto"],
        "font":("arial",12)
        }
        config={**valores, **kwargs}
        super().__init__(master,**config)
    
class Contenedor_Columna(tk.Frame):
    def __init__(self, master=None):
        self.contenedor=self

        super().__init__(master)
    def empaquetar_componente(self,frame,relativo):
        frame.pack(in_=self,fill=relativo)

class Contenedor_fila(tk.Frame):
    def __init__(self, master=None):
        self.contenedor=self
        super().__init__(master)
    def empaquetar_componente(self,frame,relativo):
        
        frame.pack(in_=self,side="left",fill=relativo)

class Entrada(tk.Entry):
    def __init__(self, master=None, placeholder_text="", **kwargs):
        valores = {
            "bg": Colores["Frame_inputs"],
            "fg": Colores["texto"],
            "font": ("arial", 12)
        }
        
        final_config = {**valores, **kwargs}
        super().__init__(master, **final_config)
        
        
        self.placeholder = placeholder_text
        self.placeholder_color = Colores["texto"]
        self.default_fg = final_config.get("fg", "black")



import tkinter as tk

class deslizador_vertical(tk.Canvas):
    
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        
        
        self.configure(highlightthickness=0) 
        
       
        self.frame_interno = tk.Frame(self)
        self.create_window((0, 0), window=self.frame_interno, anchor="nw")
        
       
        self.scrollbar = tk.Scrollbar(master, orient="vertical", command=self.yview)
        self.configure(yscrollcommand=self.scrollbar.set)
        
        
        self.frame_interno.bind("<Configure>", self._actualizar_scroll)
    
    def _actualizar_scroll(self):
       
        self.configure(scrollregion=self.bbox("all"))
    
    def agregar_boton(self, texto, comando=None):

        boton = tk.Button(self.frame_interno, text=texto, command=comando)
        boton.pack(fill="x", pady=2)  
    