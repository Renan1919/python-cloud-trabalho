import requests

# URL da API pública do GitHub
url = "https://api.github.com/repos/python/cpython"

# Fazendo a requisição HTTP - envia um requisicao get
resp = requests.get(url)

# Convertendo resposta para JSON (dicionário Python) -
data = resp.json()

# Exibindo alguns campos
print("Repositório:", data["name"])
print("Descrição:", data["description"])
print("Número de estrelas:", data["stargazers_count"]) #data["stargazers_count"  acessa o numero de estrela do repositorio