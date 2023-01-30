from urllib.parse import urlencode, unquote, quote_plus
from urllib.request import urlopen, Request

import io
import json
import requests
import pandas as pd

serviceKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJYLUFwcC1SYXRlLUxpbWl0IjoiMjAwMDA6MTAiLCJhY2NvdW50X2lkIjoiNDg2NjQ0ODIzIiwiYXV0aF9pZCI6IjQiLCJleHAiOjE3MzY4MTM0MTYsImlhdCI6MTY3Mzc0MTQxNiwibmJmIjoxNjczNzQxNDE2LCJzZXJ2aWNlX2lkIjoiNDMwMDExMzk3IiwidG9rZW5fdHlwZSI6IkFjY2Vzc1Rva2VuIn0.FN0ZQrkhRJ7TpSU04AIo5dpvQwoQZvsu2mVjK25lrtw'
serviceKeyDecoded = unquote(serviceKey, 'UTF-8')

def apiCall(count : int , date : str, cursor = None):
    # api query param 
    url = 'https://public.api.nexon.com/openapi/maplestory/v1/cube-use-results'
    returntype = 'json'
    # count = '10'
    # date = '2022-01-15'
    # cursor = ''

    queryParams = '?' + urlencode({quote_plus('ServiceKey') : serviceKeyDecoded, quote_plus('returnType') : returntype ,
    quote_plus('count') : count , quote_plus('date') : date , quote_plus('cursor') : cursor})

    request = Request(url + queryParams + "&_type=json")
    request.get_method = lambda:'GET'
    response_body = urlopen(request).read()

    getJson = json.loads(response_body)["response"]["body"]
    retItems = {}
    i = 0

    #make dict datas
    for item in getJson["items"]["item"]:
        item = dict(item.items())
        retItems['item'] = json.dumps(item, ensure_ascii=False)        

    print(f'2::{retItems}')

    return retItems 
