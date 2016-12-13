from Adafruit_BMP.BMP085 import BMP085
from elasticsearch import Elasticsearch
from datetime import datetime

temp = BMP085().read_temperature()

es = Elasticsearch( ['<ip>'])  # AWS ELK Server IP:   35.163.69.146
doc = {
    'author': ’<your_name>',
    'temp': temp,
    'timestamp': datetime.now()
}
 
print es.index(index="iot", doc_type='bmp180', body=doc)
