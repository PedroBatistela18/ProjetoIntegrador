from tkinter import *
from tkinter import ttk


# cores

co0 = '#ffffff' #branca / white
co1 = '#444466' #preta / black
co2 = '#4065a1' #azul / blue

janela = Tk()
janela.title('')
janela.geometry('335x275')
janela.configure(bg=co0)

#----------Dividindo a janela em duas partes---------

frame_cima = Frame(janela, width=335, height=50,bg=co0, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0,column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=335, height=180,bg=co0, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1,column=0, sticky=NSEW)

#----------Configurando frame cima-------------------

app_nome = Label(frame_cima, text='Calculadora de IMC', width=23, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 16 bold'), bg=co0, fg=co1)
app_nome.place(x=18, y=0)

app_linha = Label(frame_cima, text='', width=1000, height=3, padx=0, relief='flat', anchor='center', font=('Ivy 1'), bg=co2, fg=co1)
app_linha.place(x=0, y=35)

#----------Função calcular----------------------------------

def calcular():

    peso = float(e_peso.get())
    altura = float(e_altura.get())

    imc = peso / altura**2

    resultado = imc

    if resultado < 18.5:
        l_resultado_texto['text'] = 'O seu IMC é: Abaixo do peso'

    elif resultado >= 18.5 and resultado < 25: 
        l_resultado_texto['text'] = 'O seu IMC é: Normal'

    elif resultado >= 25 and resultado <30:
        l_resultado_texto['text'] = 'O seu IMC é: Sobrepeso'

    elif resultado >=30 and resultado <35: 
        l_resultado_texto['text'] = 'O seu IMC é: Obesidade grau I' 

    elif resultado >=35 and resultado <40: 
        l_resultado_texto['text'] ='O seu IMC é: Obesidade grau II'

    elif resultado >=40:
               
        l_resultado_texto['text'] = 'O seu IMC é: Obesidade grau III'

    
    l_resultado['text'] = "{:.{}f}".format(resultado, 2)
    
    
#----------Configurando frame baixo------------------

l_peso = Label(frame_baixo, text='Insira seu peso', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 12 bold'), bg=co0, fg=co1)
l_peso.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3)
e_peso = Entry(frame_baixo, width=5, relief='solid', font=('Ivy 12 bold'), justify='center')
e_peso.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3)

l_altura = Label(frame_baixo, text='Insira sua altura', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 12 bold'), bg=co0, fg=co1)
l_altura.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)
e_altura = Entry(frame_baixo, width=5, relief='solid', font=('Ivy 12 bold'), justify='center')
e_altura.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)

l_resultado = Label(frame_baixo, text='---', width=5, height=1, padx=6, pady=12, relief='flat', anchor='center', font=('Ivy 24 bold'), bg=co2, fg=co0)
l_resultado.place(x=205, y=13)

l_resultado_texto = Label(frame_baixo, text='', width=37, height=1, padx=0, pady=11, relief='flat', anchor='center', font=('Ivy 11 bold'), bg=co0, fg=co1)
l_resultado_texto.place(x=0, y=100)

b_calcular = Button(frame_baixo, command=calcular, text='Calcular', width=39, height=3,overrelief=SOLID, relief='raised', anchor='center', font=('Ivy 10 bold'), bg=co2, fg=co0)
b_calcular.grid(row=4, column=0, sticky=NSEW, pady=70, padx=6, columnspan=30)


janela.mainloop()
