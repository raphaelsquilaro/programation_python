#Author: Raphael Campos Squilaro
#Project: learning more of APIs - testing the cpfhub API

import requests

cpf = '48263463874'
url = f'https://api.cpfhub.io/cpf/{cpf}'
headers = {
    'x-api-key': 'SUA_CHAVE_DE_API_AQUI',
    'Accept': 'application/json'
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
