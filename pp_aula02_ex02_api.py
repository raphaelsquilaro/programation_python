#Author: Raphael Campos Squilaro
#Project: learning more of APIs - testing the cpfhub API

import requests

cpf = '48263463874'
url = f'https://api.cpfhub.io/cpf/{cpf}'
headers = {
    'x-api-key': 'ad43d4c69f4844d689de7fb683999a40ca086505b068f5f7bc695e9b39e76fca',
    'Accept': 'application/json'
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)