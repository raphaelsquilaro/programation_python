#Author: Raphael Campos Squilaro
#Project: visual of consultation of CPF

import requests
import customtkinter as ctk

# Configuration of the visual
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#Creating the window
window = ctk.CTk()
window.geometry("600x550")
window.title("Consultando CPF")

#Creating the button to consult the CPF
def consultar_cpf():
    cpf = cpf_entry.get()
    url = f'https://api.cpfhub.io/cpf/{cpf}'
    headers = {
        'x-api-key': 'ad43d4c69f4844d689de7fb683999a40ca086505b068f5f7bc695e9b39e76fca',
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    result_text = f"CPF: {data['data']['cpf']}\nNome: {data['data']['name']}\nData de nascimento: {data['data']['birthDate']}\nSexo: {data['data']['gender']}"
    result_box.delete("1.0", "end")
    result_box.insert("end", result_text)

#Add the title in window
title = ctk.CTkLabel(window, text="Consultando CPF")
title.pack(pady=20)

#Creating the entry for CPF
cpf_entry = ctk.CTkEntry(window, placeholder_text="Insira o CPF que deseja consultar")
cpf_entry.pack(pady=20)

#Creating the button to consult the CPF
consult_button = ctk.CTkButton(window, text="CONSULTAR", command= consultar_cpf)
consult_button.pack(pady=20)

#Creating the label to show the result
result_label = ctk.CTkLabel(window, text="")
result_label.pack(pady=20)

#Creating the result box to show the result
result_box = ctk.CTkTextbox(window, width=500, height=200)
result_box.pack(pady=20)

window.mainloop()