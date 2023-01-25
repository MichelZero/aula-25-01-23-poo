#
# autores:
# michel

# data: 25/01/2023

# importa a classe Tk
#
from tkinter import *

janela1 = Tk() # iniciar a janela
# inicio 
janela1.title("meu app")

#janela1["bg"] = "blue"
#janela1["background"] = "green"

# botão
# bt1 = Button(janela1, width=2, text="ok")
# bt1.place(x=50, y=40)

# rotulo 
# lb1 = Label(janela1, text="olá")
# lb1["bg"] = "red"
# lb1.place(x=60, y=100)

#LxA+E+T (larguraXaltura+esqueda do vídeo+top do vídeo)
#janela1.geometry("200x100+100+100")
janela1.geometry("200x200")
janela1.mainloop() # criamos a janela e ela fica em um loop infinito 
#janela1.close()