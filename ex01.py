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

janela1["bg"] = "blue"
# janela1["bg"] = "#0f0"
#janela1["background"] = "green"

# botão
bt1 = Button(janela1, width=2, text="ok")
bt1.place(x=50, y=40)

# rotulo 
lb1 = Label(janela1, text="olá")
lb1["bg"] = "red"
lb1.place(x=60, y=100)

#LxA+E+T (larguraXaltura+esquerda do vídeo+top do vídeo)
janela1.geometry("400x200+100+100")
# janela1.geometry("200x200")
janela1.mainloop() # criamos a janela e ela fica em um loop infinito 
janela1.close()

##########################################################
#GUI Graphical User Interface
#widget  são componentes (janelas, botões, rotulo de texto, etc )
#container um componente que tem outros componentes dentro deles, ex janelas
#MDI  múltiplo documentos interface
#SDI single documento interface
#toplevel windows é uma janela independente e que normalmente esta sendo exibido sob as demais

#child-parent  é a relação entre um widget e seu container