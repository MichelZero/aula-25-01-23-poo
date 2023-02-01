from tkinter import *

def btClick(): #função que será chamada quando o botão for clicado
  #print("POO2")
  if lb1['text'] == "POO":
    lb1['text'] = "outra coisa"
  elif lb1['text'] == "outra coisa":
    lb1['text'] = "POO"

#inicio
janela1 = Tk() # iniciar a janela

janela1.title("meu app")  #titulo da janela
janela1['bg'] = "green" #cor de fundo da janela

#LxA
janela1.geometry('200x200') #largura x altura
#janela1.geometry('100x100+100+100')

bt1 = Button(janela1, text = "OK", width=4, command=btClick) #cria o botão e chama a função btClick quando o botão for clicado
bt1.place(x=70, y=30)

lb1 = Label(janela1, text = "POO" )
lb1.place(x=70, y=75)
lb1['bg'] = "green"

#fim
janela1.mainloop()