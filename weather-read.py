from pprint import pprint

import requests

r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID=103203a3c4ec1f2b9ddca89b33a3e5b')

print(r.json())
