from Adafruit_BMP.BMP085 import BMP085
sensor = BMP085().read_temperature()

From elasticsearch import Elasticsearch
Es = Elasticsearch( ['<ip>'])  # AWS ELK Server IP:   35.163.69.146
Doc = {
'author': ’<your_name>',
'temp': temp,
'timestamp': datetime.now()
}
 
print es.index(index="iot", doc_type='bmp180', body=doc)
