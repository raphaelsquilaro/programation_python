# Author: Raphael Campos Squilaro
# Project Name: FP - Visual Interface Example

from tkinter import *

def calcular():
    nome = entry_nome.get()
    peso = float(entry_peso.get())
    altura = float(entry_altura.get())
    imc = peso / (altura**2)
    label_res.configure(text=f'{nome}, seu IMC é de {round(imc)}')

window = Tk()
window.title('Calculdora de IMC')
window.configure(padx=20, pady=20)
window.resizable(False, False)

label_title = Label(window, text='Calculadora de IMC', font='Roboto 20 bold', fg='#2F4F4F')
label_title.grid(column=0, row=0, columnspan=2, pady=(0,20))

label_nome = Label(window, text='Digite seu nome: ', font='Roboto 16 bold', fg='#2F4F4F')
label_nome.grid(column=0, row=1, sticky='w')

entry_nome = Entry(window, width=20, font='Roboto 16', fg='#2F4F4F', justify='center')
entry_nome.grid(column=1, row=1)

label_peso = Label(window, text='Digite seu peso (kg): ', font='Roboto 16 bold', fg='#2F4F4F')
label_peso.grid(column=0, row=2, sticky='w')

entry_peso = Entry(window, width=20, font='Roboto 16', fg='#2F4F4F', justify='center')
entry_peso.grid(column=1, row=2)

label_altura = Label(window, text='Digite sua altura (m): ', font='Roboto 16 bold', fg='#2F4F4F')
label_altura.grid(column=0, row=3, sticky='w')

entry_altura = Entry(window, width=20, font='Roboto 16', fg='#2F4F4F', justify='center')
entry_altura.grid(column=1, row=3)

button = Button(window, text='Calcular', font='Roboto 16 bold', fg='white', bg='#2F4F4F', overrelief='ridge', command=calcular)
button.grid(column=0, row=4, columnspan=2, sticky='we', pady=(10,10))

label_res = Label(window, text='', font='Roboto 16 bold', fg='#2F4F4F')
label_res.grid(column=0, row=5, sticky='w', columnspan=2)

window.mainloop()