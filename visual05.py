#Author: Raphael Campos Squilaro
#Project: visual of consultation of CNPJ

import requests
import customtkinter as ctk

# Configuration of the visual
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#Creating the window
window = ctk.CTk()
window.geometry("600x550")
window.title("Consultando CNPJ")

#Creating the button to consult the CNPJ
def consultar_cnpj():
    cnpj = cnpj_entry.get()
    url = f"https://api.opencnpj.org/{cnpj}"
    response = requests.get(url)
    data = response.json()
    result_text = f"CNPJ: {data['cnpj']}\nRazão social: {data['razao_social']}\nNome fantasia: {data['nome_fantasia']}\nSituação cadastral: {data['situacao_cadastral']}\nData da situação cadastral: {data['data_situacao_cadastral']}\nData de início de atividade: {data['data_inicio_atividade']}\nCNAE principal: {data['cnae_principal']}\nCNAE secundários: {data['cnaes_secundarios']}\nNatureza jurídica: {data['natureza_juridica']}\n"
    result_box.delete("1.0", "end")
    result_box.insert("end", result_text)

#Add the title in window
title = ctk.CTkLabel(window, text="Consultando CNPJ", text_color="#D60031")
title.pack(pady=20)

#Creating the entry for CNPJ
cnpj_entry = ctk.CTkEntry(window, placeholder_text="Insira o CNPJ que deseja consultar")
cnpj_entry.pack(pady=20)

#Creating the button to consult the CNPJ
consult_button = ctk.CTkButton(window, text="CONSULTAR", command= consultar_cnpj)
consult_button.pack(pady=20)

#Creating the label to show the result
result_label = ctk.CTkLabel(window, text="")
result_label.pack(pady=20)

#Creating the result box to show the result
result_box = ctk.CTkTextbox(window, width=500, height=200)
result_box.pack(pady=20)

window.mainloop()