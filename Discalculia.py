from tkinter import *
from tkinter.ttk import *



tela_inicial = Tk()

def botao_1():
    texto1['text']= entrada.get()
    texto2['text']= combo.get()



    
tela_inicial.title('Janela 1')
#Posição da janela    
tela_inicial.geometry('1300x600+50+10')

#Criando botâo
botao = Button(tela_inicial, text = 'clique aqui!!', command=botao_1)  

#Criando Entrada
entrada = Entry(tela_inicial)

#Criando a combobox
combo = Combobox(tela_inicial)
combo['values'] = ('oi', 'adeus', 'beijos', 'tchau', 'olá')
combo.current(0)


# criando os Label
texto = Label(tela_inicial,  text='oi', width= 20)
texto1 = Label(tela_inicial, text='oi', width= 15)
texto2 = Label(tela_inicial, text='oi', width=20)
texto3 = Label(tela_inicial, text='oi', width=20)
texto4 = Label(tela_inicial, text='oi', width=20)
texto5 = Label(tela_inicial, text='oi', width=20)
texto6 = Label(tela_inicial, text='oi', width=20)

#colocando Label na tela
texto.pack(side=TOP, fill=BOTH)
texto1.pack(side=LEFT, fill=BOTH)
texto2.pack(side=LEFT, fill=BOTH)
texto3.pack(side=LEFT, fill=BOTH)
texto4.pack(side=LEFT, fill=BOTH)
texto5.pack(side=LEFT, fill=BOTH)
texto6.pack(side=LEFT, fill=BOTH) 

#colocando Label na tela
botao.pack()

#colocando Entry na tela
entrada.pack()

#colocando cobobox na tela
combo.pack()

  


#foca o cursor na entrada
entrada.focus()

tela_inicial.mainloop()