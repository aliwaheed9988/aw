import requests

id = 1
response = requests.get(f'https://fakestoreapi.com/products/{id}')
print(response.json())