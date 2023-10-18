# Program that retrieves the dataset for the "exchequer account (historical series)" from CSO
# It also stores it in a file called "cso.json"
# Auhtor: Clare Tubridy

import requests
import json

url_beginning = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/'
url_end = '/JSON-stat/2.0/en'

def get_all_as_file(dataset):
    with open('cso.json', 'wt') as fp:
        print(json.dumps(get_all(dataset)), file=fp)

def get_all(dataset):
    url = url_beginning + dataset + url_end
    resonse = requests.get(url)
    return resonse.json()

if __name__ == '__main__':
    get_all_as_file('FIQ02')
