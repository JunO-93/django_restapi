from urllib.parse import urlencode, unquote, quote_plus
from urllib.request import urlopen, Request

import io
import json
import requests
import pandas as pd

def apiCall(count : int , date : str, cursor = ''):
    
    serviceKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJYLUFwcC1SYXRlLUxpbWl0IjoiMjAwMDA6MTAiLCJhY2NvdW50X2lkIjoiNDg2NjQ0ODIzIiwiYXV0aF9pZCI6IjQiLCJleHAiOjE3MzY4MTM0MTYsImlhdCI6MTY3Mzc0MTQxNiwibmJmIjoxNjczNzQxNDE2LCJzZXJ2aWNlX2lkIjoiNDMwMDExMzk3IiwidG9rZW5fdHlwZSI6IkFjY2Vzc1Rva2VuIn0.FN0ZQrkhRJ7TpSU04AIo5dpvQwoQZvsu2mVjK25lrtw'
    serviceKeyDecoded = unquote(serviceKey, 'UTF-8')

    url = f'https://public.api.nexon.com/openapi/maplestory/v1/cube-use-results?count={count}&date={date}&cursor={cursor}'  
    headers = {
        'Content-Type': 'application/json',
        'charset': 'UTF-8',
        'Accept': '*/*',
        'authorization' : serviceKey,
    }
    
    try:
        response = requests.get(url, headers = headers)        
        contents = response.text
    except Exception as e:
        print(e)    
    return contents