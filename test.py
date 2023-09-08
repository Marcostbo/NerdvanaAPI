import requests

apiKey = 'AIzaSyCjUd6JnP2aKy2AsQJVvWYsgdBIo0MnWQk'
cxId = '82e41cc0cbab7438c'

query = 'God of War'

url = f'https://www.googleapis.com/customsearch/v1?q={query}&cx{cxId}&key={apiKey}&safe=high'

a = requests.get(url)
