import requests
import urllib.parse
from htmlconfig import config as cfg

target_URL = 'https://en.wikipedia.org'

api_key = cfg["htmltopdfkey"]
api_url = 'https://api.html2pdf.app/v1/generate'

params = {'url': target_URL, 'api_key': api_key}
parsedparams = urllib.parse.urlencode(params)
request_url = api_url + '?' + parsedparams

response = requests.get(request_url)
print(response.status_code)

result = response.content
with open('document.pdf', 'wb') as handler:
    handler.write(result)