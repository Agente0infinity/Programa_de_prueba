from constantes import Colores
import tkinter as tk
from logica import recorrer_rutas, calcular_IVA,agregar_boleta,probar
import os

class Boton(tk.Button):
    def __init__(self,master=None,**kwargs):
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


class emergente(tk.Toplevel):
    def __init__(self,master=None,archivo=None):
        self.archivo=archivo
        super().__init__(master)
        self.geometry("360x360")
        self.configure(bg=Colores["fondo"])
    def organizar(self):
        Titulo=Etiqueta(self)
        Titulo.config(text="Operar sobre libro")
        Titulo.pack(self)
        principal=Contenedor_fila(self)
        principal.configure(bg=Colores["Frame_beta"])
        iva=Boton_estandar(principal,"calcular IVA",lambda archivo:calcular_IVA(archivo))
        boleta=Boton_estandar(principal,"agregar boleta",lambda archivo:agregar_boleta(archivo))
        principal.empaquetar_componente(iva,None)
        principal.empaquetar_componente(boleta,None)

class DeslizadorVertical(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        valores = {
            "bg": Colores["frame_botones"],
            "highlightthickness": 0
        }
        final_config = {**valores, **kwargs}
        super().__init__(master, **final_config)
        

        self.frame_interno = tk.Frame(self, bg=Colores["frame_botones"])
        self.create_window((0, 0), window=self.frame_interno, anchor="nw")
    
        self.scrollbar = tk.Scrollbar(master, orient="vertical", command=self.yview)
        self.configure(yscrollcommand=self.scrollbar.set)
        
        
        self.scrollbar.pack(side="right", fill="y")
        self.pack(side="left", fill="both", expand=True)
        
        
        self.frame_interno.bind("<Configure>", lambda e: self.configure(scrollregion=self.bbox("all")))
        self.bind("<Configure>", lambda e: self.itemconfig(1, width=e.width))
        self.bind_all("<MouseWheel>", lambda e: self.yview_scroll(int(-1*(e.delta/120)), "units"))
    
    def agregar_boton(self, texto, comando):
        boton = Boton_grande(
            self.frame_interno, 
            text=texto, 
            command=comando,
            height=5
        )
        boton.pack(fill="x", padx=5, pady=2)
        return boton
    
    def generar_botones(self):
        for ruta in recorrer_rutas():
            nombre_boton = os.path.basename(ruta)
            funcion=lambda r=ruta: probar(r)
            self.agregar_boton(nombre_boton,funcion)