# Get private data from GitHub
# Clare Tubridy

import requests
import json
from config import config as cfg

filename = "repos-private.json"
url = "https://api.github.com/repos/claretubs/privateone"
apiKey = cfg["apiKey"]

response = requests.get(url, auth =("token", apiKey))
print(response.status_code)

with open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)