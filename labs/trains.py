# Program that prints the data for all trains in Ireland to the console
# Author: Clare Tubridy

import requests
import csv
from xml.dom.minidom import parseString

url = 'http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML'
page = requests.get(url)
doc = parseString(page.content)

# To check it works
#print(doc.toprettyxml())

# To store the xml in a file
with open('trainxml.xml', 'w') as xmlfp:
    doc.writexml(xmlfp)

obj_train_position_nodes = doc.getElementsByTagName('objTrainPositions')
for obj_train_position_nodes in obj_train_position_nodes:
    traincodenode = obj_train_position_nodes.getElementsByTagName('TrainCode').item(0)
    traincode = traincodenode.firstChild.nodeValue.strip()
    #print(traincode)

