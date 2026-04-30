#Author: Raphael Campos Squilaro
#Project: visual of consultation of CPF and CNPJ

import requests
import customtkinter as ctk

# Configuration of the visual
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#Creating the window
window = ctk.CTk()
window.geometry("600x550")
window.title("Consultando CPF ou CNPJ")

tipo_consulta = ctk.StringVar(value="CPF")

#Creating the button to consult the CPF or CNPJ
def escolha_consulta():
    escolha = tipo_consulta.get()
    documento = entry_doc.get()

    if not documento:
        result_box.delete("1.0", "end")
        result_box.insert("end", "Por favor, digite um CPF ou CNPJ válido.")
        return
    
    if escolha == "CPF":
        consultar_cpf(documento)
    elif escolha == "CNPJ":
        consultar_cnpj(documento)

#Creating the button to consult the CPF
def consultar_cpf(cpf):
    url = f'https://api.cpfhub.io/cpf/{cpf}'
    headers = {
        'x-api-key': 'SUA_CHAVE_DE_API_AQUI',
        'Accept': 'application/json'
    }
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        result_text = f"CPF: {data['data']['cpf']}\nNome: {data['data']['name']}\nData de nascimento: {data['data']['birthDate']}\nSexo: {data['data']['gender']}"
    except Exception:
        result_text = "Erro ao consultar o CPF. Verifique se o CPF é válido e tente novamente."

    result_box.delete("1.0", "end")
    result_box.insert("end", result_text)
    
    
#Creating the button to consult the CNPJ
def consultar_cnpj(cnpj):
    url = f"https://api.opencnpj.org/{cnpj}"
    try:
        response = requests.get(url)
        data = response.json()
        result_text = f"CNPJ: {data['cnpj']}\nRazão social: {data['razao_social']}\nNome fantasia: {data['nome_fantasia']}\nSituação cadastral: {data['situacao_cadastral']}\nData da situação cadastral: {data['data_situacao_cadastral']}\nData de início de atividade: {data['data_inicio_atividade']}\nCNAE principal: {data['cnae_principal']}\nCNAE secundários: {data['cnaes_secundarios']}\nNatureza jurídica: {data['natureza_juridica']}\n"
    except Exception:
        result_text = "Erro ao consultar o CNPJ. Verifique se o CNPJ é válido e tente novamente."
    
    result_box.delete("1.0", "end")
    result_box.insert("end", result_text)

def limpar_campos():
    entry_doc.delete(0, "end")
    result_box.delete("1.0", "end")

#Add the title in window
title = ctk.CTkLabel(window, text="Consultando CPF ou CNPJ", font=("Arial", 20, "bold"))
title.pack(pady=20)

frame_radio = ctk.CTkFrame(window, fg_color="transparent")
frame_radio.pack(pady=10)

rb_cpf = ctk.CTkRadioButton(frame_radio, text="CPF", variable=tipo_consulta, value="CPF", command=limpar_campos)
rb_cpf.pack(side="left", padx=10)

rb_cnpj = ctk.CTkRadioButton(frame_radio, text="CNPJ", variable=tipo_consulta, value="CNPJ", command=limpar_campos)
rb_cnpj.pack(side="left", padx=10)

entry_doc = ctk.CTkEntry(window, placeholder_text="Digite o CPF ou CNPJ aqui", width=300)
entry_doc.pack(pady=20)

btn_consultar = ctk.CTkButton(window, text="Consultar", command=escolha_consulta)
btn_consultar.pack(pady=10)

result_box = ctk.CTkTextbox(window, width=500, height=200)
result_box.pack(pady=20)

window.mainloop()
