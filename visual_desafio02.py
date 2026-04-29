#Author: Raphael Campos Squilaro
#Project: interface with simple and compound interest

import customtkinter as ctk

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

def calcular(tipo):
    try:
        c = float(capital.get())
        i = int(taxa.get()) / 100
        t = float(tempo.get())
        
        if tipo == 'simples':
            juros = c * i * t
            montante = c + juros
            label_resultado.configure(text=f'Juros: R$ {juros:.2f}\nTotal: R$ {montante:.2f}', text_color="white")
        else:
            montante = c * (1 + i) ** t
            juros = montante - c
            label_resultado.configure(text=f'Juros: R$ {juros:.2f}\nTotal: R$ {montante:.2f}', text_color="white")
    except ValueError:
        label_resultado.configure(text="Erro: Insira apenas números!", text_color="red")


janela = ctk.CTk()
janela.geometry('500x600')
janela.title('Calculadora de Juros')

titulo = ctk.CTkLabel(janela, text="Calculadora de Juros")

capital = ctk.CTkEntry(janela, placeholder_text="Insira um capital inicial")
capital.pack(pady=20)

taxa = ctk.CTkEntry(janela, placeholder_text="Insira uma taxa")
taxa.pack(pady=20)

tempo = ctk.CTkEntry(janela, placeholder_text="Insira um tempo")
tempo.pack(pady=20)

btn_simples = ctk.CTkButton(janela, text="Juros Simples" , command=lambda: calcular('simples'))
btn_simples.pack(pady=10)

btn_composto = ctk.CTkButton(janela, text="Juros Compostos" , command=lambda: calcular('composto'))
btn_composto.pack(pady=10)

label_resultado = ctk.CTkLabel(janela, text='')
label_resultado.pack(pady=20)

janela.mainloop()