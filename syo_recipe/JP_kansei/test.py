import requests
import json
from pprint import pprint

# url = "https://recipt2food.herokuapp.com/post"
url = "http://0.0.0.0:5000/post"
payload = {"1" : "とれたて人参", "2" : "ごぼう"}
r = requests.post(url, payload)

print(r.text)