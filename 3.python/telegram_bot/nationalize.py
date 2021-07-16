import requests

name = 'rimi'

url = f'https://api.nationalize.io/?name={name}'
response = requests.get(url).json()
a = response['country']
b = a[0]

print(b['country_id'])
