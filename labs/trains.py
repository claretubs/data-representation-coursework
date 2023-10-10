# Program that prints the data for all trains in Ireland to the console
# Author: Clare Tubridy

import requests
import csv
from xml.dom.minidom import parseString

retrieveTags=['TrainStatus',
            'TrainLatitude',
            'TrainLongitude',
            'TrainCode',
            'TrainDate',
            'PublicMessage',
            'Direction'
            ]

url = 'http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML'
page = requests.get(url)
doc = parseString(page.content)


# To store the xml in a file
with open('trainxml.xml', 'w') as xmlfp:
   doc.writexml(xmlfp)

with open('week02_train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    obj_train_position_nodes = doc.getElementsByTagName('objTrainPositions')
    for obj_train_position_nodes in obj_train_position_nodes:
        #traincodenode = obj_train_position_nodes.getElementsByTagName('TrainCode').item(0)
        #traincode = traincodenode.firstChild.nodeValue.strip()
        
        # To get all values
        data_list = []
        for retrieveTag in retrieveTags:
            datanode = obj_train_position_nodes.getElementsByTagName(retrieveTag).item(0)
            data_list.append(datanode.firstChild.nodeValue.strip())

        train_writer.writerow(data_list)

