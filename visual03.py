# Author: Raphael Campos Squilaro
# Project Name: FP - Visual Interface Example

import customtkinter as ctk
from pytubefix import YouTube

#config visuais
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')


#função baixar
def baixar():
    link_youtube = link.get()
    yt = YouTube(link_youtube)
    yt.streams.first().download()
    status.configure(text='Download concluido')

#criando a janela 
janela = ctk.CTk()
janela.geometry('600x400')
janela.title('Downloader de videos do Youtube')

janela.iconbitmap("yt.ico")

titulo = ctk.CTkLabel(janela, text="Downloader de videos do Youtube")
titulo.pack(pady=20)

link = ctk.CTkEntry(janela, placeholder_text="Insira o link desejado")
link.pack(pady= 20)

download = ctk.CTkButton(janela, text="Download", command=baixar)
download.pack(pady=20)

status = ctk.CTkLabel(janela, text='')
status.pack(pady=20)

#loop para gerar a janela
janela.mainloop()