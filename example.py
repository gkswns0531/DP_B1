import requests
import json

rsep = requests.post('https://94d2-34-91-64-8.ngrok.io/',
    {"input_sentence":"환자분 어디가 아프신강요"})

rsep.json()