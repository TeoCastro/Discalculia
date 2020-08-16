from tkinter import *

tela_inicial = Tk()

def botao_1():
    texto1['text']= entrada.get()



    
tela_inicial.title('Janela 1')
#Posição da janela    
tela_inicial.geometry('1300x600+50+10')

#Criando botâo
botao = Button(tela_inicial, text = 'clique aqui!!', bg = 'yellow', command=botao_1)  

#Criando Entrada
entrada = Entry(tela_inicial)

# criando os Label
texto = Label(tela_inicial,  text='oi', width= 40, justify=LEFT, bg="red")
texto1 = Label(tela_inicial, text='oi', width= 15, justify=LEFT, bg="yellow")
texto2 = Label(tela_inicial, text='oi', width=20, justify=LEFT, bg="pink")
texto3 = Label(tela_inicial, text='oi', width=20, justify=LEFT, bg="blue")
texto4 = Label(tela_inicial, text='oi', width=20, justify=LEFT, bg="gray")
texto5 = Label(tela_inicial, text='oi', width=20, justify=LEFT, bg="brown")
texto6 = Label(tela_inicial, text='oi', width=20, justify=LEFT, bg="beige")

#colocando Label na tela
texto.pack(side=LEFT, fill=BOTH, expand=1)
texto1.pack(side=LEFT, fill=BOTH, expand=1)
texto2.pack(side=LEFT, fill=BOTH, expand=1)
texto3.pack(side=LEFT, fill=BOTH, expand=1)
texto4.pack(side=LEFT, fill=BOTH, expand=1)
texto5.pack(side=LEFT, fill=BOTH, expand=1)
texto6.pack(side=LEFT, fill=BOTH, expand=1) 

#colocando Label na tela
botao.pack(side=LEFT, fill=BOTH, expand=1 )

#colocando Entry na tela
entrada.pack()

  


#foca o cursor na entrada
entrada.focus()

tela_inicial.mainloop()