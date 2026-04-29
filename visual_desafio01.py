#Author: Raphael Campos Squilaro
#Project: Interface with ViaCep

import customtkinter as ctk
import requests

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

janela = ctk.CTk()
janela.geometry('500x600') # Aumentei um pouco a altura para caber tudo
janela.title("Consulta do ViaCep")

def procurar():
    cep = entry_cep.get()
    button.configure(text="Buscando...", state="disabled")
    janela.update()

    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url)
        dados = resposta.json()

        if "erro" not in dados:
            text_result = f"Rua: {dados['logradouro']}\nBairro: {dados['bairro']}\nCidade: {dados['localidade']} - {dados['uf']}"
            label_res.configure(text=text_result, text_color="white")
            frame_res.configure(border_color="#5400FC")
        else:
            label_res.configure(text="CEP não encontrado!", text_color="#FF5555")
            frame_res.configure(border_color="#FF5555")
    except:
        label_res.configure(text="Erro de conexão!", text_color="#FF5555")
    
    button.configure(text="Procurar", state="normal")

# --- Interface (Tudo usando pack para evitar conflitos) ---

label_title = ctk.CTkLabel(janela, text='VIA CEP', font=('Roboto', 28, 'bold'), text_color="#5400FC")
label_title.pack(pady=20)

input_frame = ctk.CTkFrame(janela, fg_color="transparent")
input_frame.pack(pady=10)

# Mudei de grid para pack para manter a consistência
label_cep = ctk.CTkLabel(input_frame, text='Digite seu CEP:', font=('Roboto', 14, 'bold'))
label_cep.pack(side="left", padx=5)

entry_cep = ctk.CTkEntry(input_frame, width=150, height=40, placeholder_text="00000-000", font=('Roboto', 16), justify='center', border_color="#5400FC")
entry_cep.pack(side="left", padx=5)

button = ctk.CTkButton(janela, text='Procurar', font=('Roboto', 16, 'bold'), height=45, fg_color='#5400FC', hover_color="#3A00B0", command=procurar)
button.pack(pady=20, padx=50, fill="x")

# Frame de Resultado
frame_res = ctk.CTkFrame(janela, width=400, height=150, border_width=2, border_color="#2F4F4F")
frame_res.pack(pady=20, padx=20, fill="both", expand=True)
frame_res.pack_propagate(False)

# IMPORTANTE: label_res agora é filho de frame_res
label_res = ctk.CTkLabel(frame_res, text='Os dados aparecerão aqui', font=('Roboto', 16), wraplength=350)
label_res.pack(expand=True)

janela.mainloop()
