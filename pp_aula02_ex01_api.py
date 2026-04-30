#Author: Raphael Campos Squilaro
#Project: learning more of APIs - testing the OpenCNPJAPI

import requests

cnpj = "05061448000139"
url = f"https://api.opencnpj.org/{cnpj}"
response = requests.get(url)

data = response.json()

print(f"CNPJ: {data['cnpj']}")
print("Razão social: " , data['razao_social'])
print(f"Nome fantasia: {data['nome_fantasia']}")
print(f"Situacao cadastral: {data['situacao_cadastral']}")
print(f"Data da situação cadastral: {data['data_situacao_cadastral']}")
print(f"Data de inicio de atividade: {data['data_inicio_atividade']}")
print(f"CNAE principal: {data['cnae_principal']}")
print(f"CNAE secundários: {data['cnaes_secundarios']}")
print(f"Natureza jurídica: {data['natureza_juridica']}")