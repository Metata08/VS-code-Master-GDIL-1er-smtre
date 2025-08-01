import requests

url = "https://icp-o2ac17c.gamma.site"

response = requests.get(url,auth=('admin','admin'))

# Afficher les en-têtes HTTP
print("En-têtes HTTP:", response.headers)

# Afficher le contenu si nécessaire
print("Contenu:", response.text)

