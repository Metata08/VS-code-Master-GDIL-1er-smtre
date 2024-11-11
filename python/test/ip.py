import requests

url = "http://foad.ugb.sn/login/index.php"

response = requests.get(url,auth=('admin','admin'))

# Afficher les en-têtes HTTP
print("En-têtes HTTP:", response.headers)

# Afficher le contenu si nécessaire
print("Contenu:", response.text)

