import requests
import time
key = '3JJSPLBPQM79FD9Q'

temperature = 19.2
radon = 35
tvoc = 212
co2 = 525

params = {'api_key':key, 'field1':temperature, 'field2':radon, 'field3':co2, 'field4':tvoc}

try:
    results = requests.post('https://api.thingspeak.com/update', params=params)
    print(results)
except Exception as e:
    print(e)

